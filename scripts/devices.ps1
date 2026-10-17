$ErrorActionPreference = 'Stop'
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$VenvPython = Join-Path $ProjectRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $VenvPython)) { throw 'Run scripts\setup.ps1 first.' }
& $VenvPython (Join-Path $ProjectRoot 'src\iphone_location.py') devices
exit $LASTEXITCODE
