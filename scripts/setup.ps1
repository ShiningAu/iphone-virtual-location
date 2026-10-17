param([string]$Python = 'py')
$ErrorActionPreference = 'Stop'
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$VenvPython = Join-Path $ProjectRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $VenvPython)) {
    & $Python -m venv (Join-Path $ProjectRoot '.venv')
    if ($LASTEXITCODE -ne 0) { throw 'Python 3.12 is recommended. Pass its path using -Python.' }
}
& $VenvPython -m pip install -r (Join-Path $ProjectRoot 'requirements-lock.txt')
if ($LASTEXITCODE -ne 0) { throw 'Dependency installation failed. Check the network and Python version.' }
Write-Host 'Setup complete. Connect and unlock iPhone, then run scripts\start.ps1.'
