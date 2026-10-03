$ErrorActionPreference = "Stop"

param(
    [string]$InstallRoot = "$env:USERPROFILE\SmartWeld"
)

$url = "https://sourceforge.net/projects/smartweld/files/Smartweld_Mfiles_12Mar2012.zip/download"
$sha256 = "46714ca97f740e1430e17f0265d97e7b5a909f790ac60df91cf8d157a8fb6008"

New-Item -ItemType Directory -Force -Path $InstallRoot | Out-Null
$zip = Join-Path $InstallRoot "Smartweld_Mfiles_12Mar2012.zip"
Invoke-WebRequest -Uri $url -OutFile $zip

$actual = (Get-FileHash -Algorithm SHA256 $zip).Hash.ToLower()
if ($actual -ne $sha256) {
    throw "SHA-256 mismatch. Expected $sha256, got $actual"
}

$src = Join-Path $InstallRoot "Mfiles"
if (Test-Path $src) { Remove-Item -Recurse -Force $src }
New-Item -ItemType Directory -Force -Path $src | Out-Null
Expand-Archive -Path $zip -DestinationPath $src -Force

Write-Host "SmartWeld M-files installed at: $src"
