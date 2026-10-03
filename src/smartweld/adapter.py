"""SmartWeld execution/import adapter.

The bundled SmartWeld standalone is a Windows/MATLAB GUI application and has
no documented command-line interface. This adapter therefore supports a
verified external runner plus direct import of verified SmartWeld exports.
"""

from __future__ import annotations

import csv
import json
import os
import subprocess
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Sequence

from .schema import SmartWeldRecord


class SmartWeldExecutionError(RuntimeError):
    """Raised when SmartWeld execution or result parsing fails."""


class SmartWeldAdapter:
    """Adapter for verified SmartWeld results and external SmartWeld runners."""

    def __init__(
        self,
        model_id: str,
        smartweld_version: Optional[str] = None,
        executable: Optional[str] = None,
        runner: Optional[Sequence[str]] = None,
    ):
        self.model_id = model_id
        self.smartweld_version = smartweld_version
        self.executable = executable
        self.runner = list(runner) if runner else None

    def run(
        self,
        inputs: Dict[str, Any],
        run_id: str,
        seed: Optional[int] = None,
        workdir: Optional[str] = None,
        timeout_s: int = 300,
    ) -> SmartWeldRecord:
        """Execute a configured external SmartWeld runner.

        The runner receives SMARTWELD_INPUT_JSON and must write JSON results to
        SMARTWELD_OUTPUT_JSON. SMARTWELD_EXECUTABLE and SMARTWELD_SEED are also
        supplied when configured.
        """
        if not self.runner:
            raise SmartWeldExecutionError(
                "No SmartWeld runner configured. The archived standalone "
                "application is GUI-only; do not assume an undocumented CLI."
            )

        root = Path(workdir or os.getcwd()).resolve()
        root.mkdir(parents=True, exist_ok=True)
        input_path = root / f"{run_id}.input.json"
        output_path = root / f"{run_id}.output.json"
        input_path.write_text(
            json.dumps(inputs, indent=2, ensure_ascii=False), encoding="utf-8"
        )

        env = os.environ.copy()
        env["SMARTWELD_INPUT_JSON"] = str(input_path)
        env["SMARTWELD_OUTPUT_JSON"] = str(output_path)
        if self.executable:
            env["SMARTWELD_EXECUTABLE"] = self.executable
        if seed is not None:
            env["SMARTWELD_SEED"] = str(seed)

        completed = subprocess.run(
            self.runner, cwd=str(root), env=env, capture_output=True,
            text=True, timeout=timeout_s, check=False
        )
        if completed.returncode != 0:
            raise SmartWeldExecutionError(
                f"SmartWeld runner failed with exit code {completed.returncode}: "
                f"{completed.stderr[-2000:]}"
            )
        if not output_path.exists():
            raise SmartWeldExecutionError(
                f"Runner completed but did not create {output_path}"
            )

        outputs = json.loads(output_path.read_text(encoding="utf-8"))
        return self._record(run_id, inputs, outputs, seed, "completed")

    def from_export(
        self,
        path: str,
        run_id: str,
        inputs: Dict[str, Any],
        units: Optional[Dict[str, str]] = None,
    ) -> SmartWeldRecord:
        """Import a verified SmartWeld JSON or CSV result."""
        p = Path(path)
        if p.suffix.lower() == ".csv":
            with p.open(newline="", encoding="utf-8-sig") as fh:
                outputs: Any = list(csv.DictReader(fh))
        else:
            outputs = json.loads(p.read_text(encoding="utf-8"))

        return self._record(
            run_id, inputs, outputs, None, "imported", units=units
        )

    def _record(
        self,
        run_id: str,
        inputs: Mapping[str, Any],
        outputs: Any,
        seed: Optional[int],
        status: str,
        units: Optional[Dict[str, str]] = None,
    ) -> SmartWeldRecord:
        return SmartWeldRecord(
            run_id=run_id,
            inputs=dict(inputs),
            outputs=outputs,
            units=units or {},
            smartweld_version=self.smartweld_version,
            model_id=self.model_id,
            seed=seed,
            status=status,
        )

    @staticmethod
    def write_jsonl(records: Sequence[SmartWeldRecord], path: str) -> None:
        with Path(path).open("w", encoding="utf-8") as fh:
            for record in records:
                fh.write(json.dumps(asdict(record), ensure_ascii=False) + "\n")

    @staticmethod
    def write_csv(records: Sequence[SmartWeldRecord], path: str) -> None:
        """Flatten records while retaining full JSON provenance."""
        fieldnames = [
            "run_id", "status", "model_id", "smartweld_version", "seed",
            "inputs_json", "outputs_json", "units_json"
        ]
        with Path(path).open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=fieldnames)
            writer.writeheader()
            for record in records:
                writer.writerow({
                    "run_id": record.run_id,
                    "status": record.status,
                    "model_id": record.model_id,
                    "smartweld_version": record.smartweld_version,
                    "seed": record.seed,
                    "inputs_json": json.dumps(record.inputs, ensure_ascii=False),
                    "outputs_json": json.dumps(record.outputs, ensure_ascii=False),
                    "units_json": json.dumps(record.units, ensure_ascii=False),
                })
