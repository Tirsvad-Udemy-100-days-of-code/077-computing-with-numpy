"""Print every lesson step; ``python -m computing_with_numpy`` runs it."""

from __future__ import annotations

import sys

from computing_with_numpy.application.lesson_steps import all_steps


def main() -> int:
    """Write each lesson step to standard output and return the exit code."""
    for step in all_steps():
        sys.stdout.write(f"== {step.title} ==\n")
        for line in step.lines:
            sys.stdout.write(f"{line}\n")
        sys.stdout.write("\n")
    return 0
