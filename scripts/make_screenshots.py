"""Execute the notebook, then write one PNG per step into docs/images."""

from __future__ import annotations

from pathlib import Path

from computing_with_numpy.application.lesson import NOTEBOOK_PATH
from computing_with_numpy.infrastructure.notebook import (
    build_executed_notebook,
    write_notebook,
)
from computing_with_numpy.infrastructure.notebook_screenshots import (
    write_cell_screenshots,
)

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "docs" / "images"


def main() -> None:
    """Run the notebook, save it with outputs and render the screenshots."""
    executed = build_executed_notebook(ROOT)
    write_notebook(executed, ROOT / NOTEBOOK_PATH)
    write_cell_screenshots(executed, IMAGES)


if __name__ == "__main__":
    main()
