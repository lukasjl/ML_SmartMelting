from src.smartweld.sampling import random_samples


def test_random_samples_are_reproducible():
    ranges = {"laser_power": (100.0, 200.0), "scan_speed": (1.0, 2.0)}
    assert random_samples(ranges, 3, seed=42) == random_samples(ranges, 3, seed=42)
