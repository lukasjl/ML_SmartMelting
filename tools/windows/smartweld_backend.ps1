param(
    [Parameter(Mandatory=$true)]
    [string]$InputJson,
    [Parameter(Mandatory=$true)]
    [string]$OutputJson,
    [string]$MatlabExe = "matlab.exe",
    [string]$MatlabFunction = "smartweld_batch_entry"
)

$ErrorActionPreference = "Stop"
$inputFull = (Resolve-Path $InputJson).Path
$outputFull = [System.IO.Path]::GetFullPath($OutputJson)
$workDir = Split-Path -Parent $outputFull

if (-not (Test-Path $workDir)) {
    New-Item -ItemType Directory -Path $workDir | Out-Null
}

$mfiles = Join-Path $env:USERPROFILE "SmartWeld\Mfiles"
if (-not (Test-Path $mfiles)) {
    throw "SmartWeld M-files not found at $mfiles. Run bootstrap_smartweld.ps1 first."
}

$inventory = Join-Path $mfiles "smartweld_source_inventory.txt"
if (-not (Test-Path $inventory)) {
    & $MatlabExe -batch "addpath(genpath('$($mfiles.Replace("'","''"))')); inspect_smartweld"
    if ($LASTEXITCODE -ne 0) { throw "MATLAB source inventory failed." }
}

$env:SMARTWELD_INPUT_JSON = $inputFull
$env:SMARTWELD_OUTPUT_JSON = $outputFull

$escapedMfiles = $mfiles.Replace("'", "''")
$escapedFunction = $MatlabFunction.Replace("'", "''")
$cmd = "addpath(genpath('$escapedMfiles')); feval('$escapedFunction'); exit"

& $MatlabExe -batch $cmd
if ($LASTEXITCODE -ne 0) {
    throw "MATLAB SmartWeld backend failed with exit code $LASTEXITCODE."
}
if (-not (Test-Path $outputFull)) {
    throw "MATLAB completed but did not create output JSON: $outputFull"
}
Write-Host "SmartWeld output: $outputFull"
