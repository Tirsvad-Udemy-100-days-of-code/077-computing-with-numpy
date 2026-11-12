"""The setup step: which Python and NumPy run the lesson."""

from __future__ import annotations

from computing_with_numpy.application.lesson_step import LessonStep


def setup_steps() -> list[LessonStep]:
    """Return the setup step."""
    return [
        LessonStep(
            slug="00-setup",
            title="Setup: Python and NumPy",
            explanation=(
                "NumPy is imported as `np` by convention. The versions below are "
                "the ones this notebook runs with."
            ),
            code=(
                "import platform\n"
                "import numpy as np\n"
                "\n"
                'print(f"Python {platform.python_version()}")\n'
                'print(f"NumPy {np.__version__}")'
            ),
        )
    ]
