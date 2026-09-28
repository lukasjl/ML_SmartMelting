"""Adapter boundary between SmartWeld and the ML dataset pipeline.

This module intentionally does not implement or reproduce SmartWeld itself.
The adapter expects an externally available SmartWeld installation/API or an
exported result file and converts verified outputs into ML records.
"""

from pathlib import Path
from typing import Any, Dict, Optional
import json

from .schema import SmartWeldRecord


class SmartWeldAdapter:
    """Minimal interface for integrating an actual SmartWeld installation."""

    def __init__(self, model_id: str, smartweld_version: Optional[str] = None):
        self.model_id = model_id
        self.smartweld_version = smartweld_version

    def run(self, inputs: Dict[str, Any], run_id: str, seed: Optional[int] = None) -> SmartWeldRecord:
        """Run SmartWeld and return a validated record.

        The actual solver call is deliberately left as an integration point.
        It must be implemented against the user's licensed/available SmartWeld
        environment rather than guessed from undocumented interfaces.
        """
        raise NotImplementedError(
            "Connect this adapter to the available SmartWeld installation/API."
        )

    def from_export(
        self,
        path: str,
        run_id: str,
        inputs: Dict[str, Any],
        units: Optional[Dict[str, str]] = None,
    ) -> SmartWeldRecord:
        """Import a verified SmartWeld JSON export."""
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return SmartWeldRecord(
            run_id=run_id,
            inputs=inputs,
            outputs=data,
            units=units or {},
            smartweld_version=self.smartweld_version,
            model_id=self.model_id,
            status="imported",
        )
