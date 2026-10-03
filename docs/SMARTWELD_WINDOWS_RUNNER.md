# SmartWeld Windows runner contract

The archived SmartWeld standalone package contains SmartWeld-1March2012.exe
and the matching MATLAB Compiler Runtime installer. The supplied README states
that SmartWeld is launched as a Windows GUI application and that its
applications write output files into the OutputFiles directory.

The executable inspected in the project environment is a 32-bit Windows PE
binary. Its embedded MATLAB symbol strings include oslw_gui, weld2d_gui,
heat2d_gui and iso25Solver functions. This confirms compiled application
content, but not a supported command-line API.

## Adapter contract

SmartWeldAdapter.run() requires a verified external runner. The runner receives
these environment variables:

- SMARTWELD_INPUT_JSON: JSON input path
- SMARTWELD_OUTPUT_JSON: required JSON output path
- SMARTWELD_EXECUTABLE: SmartWeld executable path, when configured
- SMARTWELD_SEED: optional reproducibility seed

The runner must create SMARTWELD_OUTPUT_JSON.

The runner can later be implemented with MATLAB M-files on Windows or tested
GUI automation. No undocumented SmartWeld CLI syntax is hard-coded.

## Scientific boundary

For InssTek MX-Grande DED, SmartWeld outputs must initially be treated as a
physics-based laser/welding prior. They are not automatically validated DED
predictions. Powder feed rate, layer height, nozzle/standoff and DED geometry
remain separate machine/process variables unless a selected SmartWeld model
explicitly supports them.

Large generated datasets should not be committed to ordinary Git history.
Store reproducible manifests in Git and datasets as release/LFS artifacts.
