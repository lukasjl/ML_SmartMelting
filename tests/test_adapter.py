from pathlib import Path
import json

from src.smartweld.adapter import SmartWeldAdapter, SmartWeldExecutionError


def test_import_and_csv_export(tmp_path: Path):
    src = tmp_path / "result.json"
    src.write_text(json.dumps({"melt_pool_width_mm": 1.2, "penetration_mm": 0.4}))
    adapter = SmartWeldAdapter("smartweld-oslw", smartweld_version="3.0")
    record = adapter.from_export(
        str(src),
        run_id="case-001",
        inputs={"power_W": 500, "speed_mm_s": 10},
    )
    assert record.status == "imported"
    out = tmp_path / "records.csv"
    adapter.write_csv([record], str(out))
    assert "case-001" in out.read_text()


def test_run_requires_verified_runner():
    adapter = SmartWeldAdapter("smartweld-oslw")
    try:
        adapter.run({"power_W": 500}, "case-001")
    except SmartWeldExecutionError as exc:
        assert "No SmartWeld runner configured" in str(exc)
    else:
        raise AssertionError("run() must not invent an undocumented SmartWeld CLI")
