"""Print every lesson step; ``python -m computing_with_numpy`` runs it."""

from __future__ import annotations

import sys

from computing_with_numpy.application.lesson import NOTEBOOK_PATH, all_steps


def main() -> int:
    """Write each lesson step to standard output and return the exit code."""
    for step in all_steps():
        sys.stdout.write(f"== {step.title} ==\n")
        sys.stdout.write(f"{step.explanation}\n\n")
        sys.stdout.write(f"{step.code}\n\n")
    sys.stdout.write(f"Run the steps in the notebook: {NOTEBOOK_PATH}\n")
    return 0
