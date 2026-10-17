param([string]$Preset = 'new-york', [string]$Udid = '')
$ErrorActionPreference = 'Stop'
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$VenvPython = Join-Path $ProjectRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $VenvPython)) { throw 'Run scripts\setup.ps1 first.' }
$Arguments = @((Join-Path $ProjectRoot 'src\iphone_location.py'), 'start', '--preset', $Preset)
if ($Udid) { $Arguments += @('--udid', $Udid) }
& $VenvPython @Arguments
exit $LASTEXITCODE
