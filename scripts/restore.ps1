param([string]$Udid = '')
$ErrorActionPreference = 'Stop'
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$VenvPython = Join-Path $ProjectRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $VenvPython)) { throw 'Run scripts\setup.ps1 first.' }
Write-Host 'First press ENTER in the active location session. Then run this restore script.'
$Arguments = @((Join-Path $ProjectRoot 'src\iphone_location.py'), 'restore')
if ($Udid) { $Arguments += @('--udid', $Udid) }
& $VenvPython @Arguments
exit $LASTEXITCODE
