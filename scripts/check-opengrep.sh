#!/usr/bin/env bash
# Runs opengrep on the repository; run it before every push.
# Looks for opengrep on PATH, then in ~/.opengrep/cli/latest.
# Exits non-zero when opengrep reports a finding.
set -euo pipefail

if command -v opengrep >/dev/null 2>&1; then
  tool="opengrep"
elif [[ -x "$HOME/.opengrep/cli/latest/opengrep.exe" ]]; then
  tool="$HOME/.opengrep/cli/latest/opengrep.exe"
elif [[ -x "$HOME/.opengrep/cli/latest/opengrep" ]]; then
  tool="$HOME/.opengrep/cli/latest/opengrep"
else
  echo "opengrep not found: install it from https://github.com/opengrep/opengrep" >&2
  exit 2
fi

cd "$(git rev-parse --show-toplevel)"
"$tool" scan --config auto --error --quiet .
echo "opengrep: no findings"
