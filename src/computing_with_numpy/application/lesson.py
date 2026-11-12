"""The lesson: every step in lecture order and where its notebook lives."""

from __future__ import annotations

from computing_with_numpy.application.lesson_step import LessonStep
from computing_with_numpy.application.steps_basics import basics_steps
from computing_with_numpy.application.steps_generating import generating_steps
from computing_with_numpy.application.steps_images import images_steps
from computing_with_numpy.application.steps_linear_algebra import linear_algebra_steps
from computing_with_numpy.application.steps_setup import setup_steps

NOTEBOOK_PATH = "notebooks/computing_with_numpy.ipynb"


def all_steps() -> list[LessonStep]:
    """Return every lesson step in lecture order."""
    return [
        *setup_steps(),
        *basics_steps(),
        *generating_steps(),
        *linear_algebra_steps(),
        *images_steps(),
    ]
