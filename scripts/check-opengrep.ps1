# Runs opengrep on the repository; run it before every push (Windows PowerShell).
# Looks for opengrep on PATH, then in ~\.opengrep\cli\latest.
# Exits non-zero when opengrep reports a finding.
$ErrorActionPreference = 'Stop'

$tool = (Get-Command opengrep -ErrorAction SilentlyContinue).Source
if (-not $tool) {
    $tool = Join-Path $HOME '.opengrep\cli\latest\opengrep.exe'
}
if (-not (Test-Path $tool)) {
    Write-Error 'opengrep not found: install it from https://github.com/opengrep/opengrep'
    exit 2
}

Set-Location (git rev-parse --show-toplevel)
& $tool scan --config auto --error --quiet .
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Output 'opengrep: no findings'
