"""Parameter-space sampling utilities.

Ranges are supplied by the user or validated configuration; no default
physical ranges are invented here.
"""

from typing import Dict, List, Tuple
import random


def random_samples(
    ranges: Dict[str, Tuple[float, float]],
    n: int,
    seed: int = 0,
) -> List[Dict[str, float]]:
    """Generate reproducible uniform samples within configured bounds."""
    if n < 1:
        raise ValueError("n must be positive")
    rng = random.Random(seed)
    for name, (lo, hi) in ranges.items():
        if lo >= hi:
            raise ValueError(f"Invalid range for {name}: {lo} >= {hi}")
    return [
        {name: rng.uniform(lo, hi) for name, (lo, hi) in ranges.items()}
        for _ in range(n)
    ]
