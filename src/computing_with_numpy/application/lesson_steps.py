"""Lesson steps shown by the command line and captured as screenshots."""

from __future__ import annotations

import platform
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class LessonStep:
    """One lecture step: a slug for file names, a title and its output lines."""

    slug: str
    title: str
    lines: tuple[str, ...]


def setup_step() -> LessonStep:
    """Describe the environment the lesson runs in."""
    return LessonStep(
        slug="00-setup",
        title="Setup: Python and NumPy",
        lines=(
            "$ python -m venv .venv",
            "$ python -m pip install --upgrade pip",
            '$ python -m pip install -e ".[dev]"',
            f"Python {platform.python_version()}",
            f"NumPy {np.__version__}",
        ),
    )


def all_steps() -> list[LessonStep]:
    """Return every lesson step in lecture order."""
    return [setup_step()]
