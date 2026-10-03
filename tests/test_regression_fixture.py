"""Structural checks for the historical OSLW regression fixture.

These checks validate the fixture contract only. They do not execute SmartWeld
or establish numerical agreement with the original MATLAB implementation.
"""
import json
from pathlib import Path


FIXTURE = Path(__file__).parents[1] / "data" / "regression" / "smartweld_oslw_regression_case.json"
INPUT_KEYS = {
    "power_W", "travel_speed_mm_s", "spot_diameter_cm", "material", "shielding_gas"
}
OUTPUT_KEYS = {
    "energy_transfer_efficiency", "melting_efficiency", "weld_width_mm",
    "penetration_depth_mm", "penetration_sensitivity_um_per_W",
}


def test_oslw_fixture_has_complete_provenance_and_values():
    case = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert case["run_id"]
    assert INPUT_KEYS <= case["inputs"].keys()
    assert OUTPUT_KEYS == case["expected"].keys()
    assert case["validation"]["source"]
    assert case["validation"]["purpose"]
    assert case["validation"]["note"]


def test_oslw_fixture_values_are_finite_and_physically_bounded():
    case = json.loads(FIXTURE.read_text(encoding="utf-8"))
    values = case["expected"]
    assert all(isinstance(v, (int, float)) for v in values.values())
    assert all(__import__("math").isfinite(v) for v in values.values())
    assert 0 < values["energy_transfer_efficiency"] <= 1
    assert 0 < values["melting_efficiency"] <= 1
    assert values["weld_width_mm"] > 0
    assert values["penetration_depth_mm"] > 0
    assert values["penetration_sensitivity_um_per_W"] > 0
