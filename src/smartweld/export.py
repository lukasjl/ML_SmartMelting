"""Dataset export helpers for SmartWeld records."""

import json
from pathlib import Path
from typing import Iterable

from .schema import SmartWeldRecord


def write_jsonl(records: Iterable[SmartWeldRecord], path: str) -> None:
    """Write provenance-aware records as JSON Lines."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record.to_dict(), ensure_ascii=False) + "\n")
