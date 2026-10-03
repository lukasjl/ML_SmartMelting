"""Data structures for SmartWeld-generated ML records."""

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class SmartWeldRecord:
    """One provenance-aware SmartWeld simulation record."""

    run_id: str
    inputs: Dict[str, Any]
    outputs: Any
    units: Dict[str, str] = field(default_factory=dict)
    generator_version: str = "0.1.0"
    smartweld_version: Optional[str] = None
    model_id: Optional[str] = None
    seed: Optional[int] = None
    status: str = "unknown"
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "run_id": self.run_id,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "units": self.units,
            "generator_version": self.generator_version,
            "smartweld_version": self.smartweld_version,
            "model_id": self.model_id,
            "seed": self.seed,
            "status": self.status,
            "metadata": self.metadata,
        }
