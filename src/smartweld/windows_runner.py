"""Windows runner for the recovered SmartWeld MATLAB backend.

This module only constructs the PowerShell command. MATLAB/SmartWeld must be
installed on the Windows host.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List


def command(script: str | None = None) -> List[str]:
    """Return the PowerShell command used by SmartWeldAdapter.

    The adapter supplies SMARTWELD_INPUT_JSON and SMARTWELD_OUTPUT_JSON.
    """
    if not sys.platform.startswith("win"):
        raise RuntimeError("The SmartWeld MATLAB backend requires Windows.")

    script_path = Path(
        script or Path(__file__).resolve().parents[2] / "tools" / "windows" / "smartweld_backend.ps1"
    )
    return [
        "powershell.exe",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(script_path),
    ]
