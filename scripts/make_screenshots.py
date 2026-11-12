"""Write one PNG per lesson step into docs/images (no window is opened)."""

from __future__ import annotations

from pathlib import Path

from computing_with_numpy.application.lesson_steps import all_steps
from computing_with_numpy.infrastructure.screenshots import render_text_screenshot

IMAGES = Path(__file__).resolve().parents[1] / "docs" / "images"


def main() -> None:
    """Render every step's output as a screenshot."""
    for step in all_steps():
        render_text_screenshot(step.title, step.lines, IMAGES / f"{step.slug}.png")


if __name__ == "__main__":
    main()
