# SmartWeld M-files recovery and Windows integration

## Verified

The supplied SmartWeld-1March2012.exe contains an embedded ZIP/CTF payload.
The payload contains compiled MATLAB project resources and filenames including
main.m, mat_file.m, oslw_gui.m, oslw_gui_callbacks.m, oslw_gui_layout.m,
iso25Solver1.m through iso25Solver4.m, isotherms*.m, spotfun*.m and
weld2dfunc*.m.

These embedded files are compiled MATLAB artifacts, not plain-text source.
They cannot safely be used as source code for a new direct API.

The official SourceForge download page identifies Smartweld_Mfiles_12Mar2012.zip
and publishes SHA-256:
46714ca97f740e1430e17f0265d97e7b5a909f790ac60df91cf8d157a8fb6008.

## Windows bootstrap

tools/windows/bootstrap_smartweld.ps1 downloads the exact archive and verifies
its SHA-256 before extraction.

SmartWeld documentation states that the M-files and standalone were generated
with MATLAB 2010a and that the standalone requires matching MCR 7.13.

## Current execution boundary

tools/windows/run_smartweld_matlab.m starts the original Main.m workflow once
the real M-files are installed.

A parameterized ML runner must not be fabricated until the actual source
M-files are available and their function signatures are verified.

## Next verified step

Inspect Main.m, oslw_gui.m, oslw_gui_callbacks.m, material/property functions,
and output-file writers. Then implement a direct function-level adapter and
deterministic DOE runner for MX-Grande parameters.
