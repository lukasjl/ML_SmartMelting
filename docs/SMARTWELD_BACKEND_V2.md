# SmartWeld backend

## Current implementation

The backend now binds the recovered original SmartWeld OSLW model at the source level.

Verified call path from the official 12 March 2012 M-files:

    app_specific_data
        -> schedulermodels
            -> queryfunc

For OSLW, queryfunc(inputs) accepts three physical inputs in the original program path:

- laser output power [W]
- travel speed [mm/s]
- spot diameter [cm]

The OSLW source returns:

- energy-transfer efficiency
- melting efficiency
- weld width [mm]
- penetration depth [mm]
- penetration sensitivity [mm/W]

The public SmartWeld documentation independently describes OSLW as a continuous-wave laser welding model using laser power/intensity, travel speed, focused spot size and shielding gas, with weld dimensions and efficiency outputs.

## Runtime boundary

Python:
    SmartWeldAdapter
        |
        v
    PowerShell
        |
        v
    MATLAB
        |
        v
    smartweld_batch_entry.m
        |
        +--> app_specific_data.m
        |
        +--> queryfunc.m
        |       |
        |       +--> schedulermodels.m
        |
        +--> JSON result
        |
        v
    SmartWeldRecord

The PowerShell bridge reads the JSON request with PowerShell's JSON parser and exposes the required fields as environment variables. This avoids requiring JSON parsing support from legacy MATLAB.

## Required request fields

    {
      "power_W": 1000,
      "travel_speed_mm_s": 10,
      "spot_diameter_cm": 0.0118,
      "material": "304 stainless",
      "shielding_gas": "argon"
    }

Accepted aliases are documented in smartweld_backend.ps1.

The OSLW source defines four verified lens spot diameters in centimetres:

- 0.0118
- 0.0164
- 0.0225
- 0.0294

Ar/He are the two shielding-gas cases implemented in the recovered OSLW source.

## Windows setup

1. Run tools/windows/bootstrap_smartweld.ps1.
2. Install/use the MATLAB environment compatible with the supplied historical M-files. SmartWeld's public FAQ states that the M-files and Standalone were generated with MATLAB 2010a; Standalone 3.0 requires MCR 7.13.
3. Put the repository on the Windows host.
4. Verify source discovery with:

       matlab -r "addpath(genpath(fullfile(getenv('USERPROFILE'),'SmartWeld','Mfiles'))); inspect_smartweld; exit"

5. Configure SmartWeldAdapter with the PowerShell command produced by smartweld.windows_runner.command().

## Scientific validation gate

The source-level binding is now identified, but a numerical regression test still requires MATLAB/SmartWeld execution on Windows.

Before using the backend for DOE/ML training:

1. run one OSLW case through the original GUI;
2. run the same physical inputs through smartweld_batch_entry;
3. compare all five numerical outputs;
4. record the SmartWeld version and material/gas/spot configuration;
5. only then enable automated DOE generation.

This distinction matters because SmartWeld is a welding model; for the MX-Grande DED project, powder feed, layer height, nozzle standoff and other DED-specific quantities remain outside the verified OSLW input space. SmartWeld should therefore remain a physics prior until DED-side validation is performed.
