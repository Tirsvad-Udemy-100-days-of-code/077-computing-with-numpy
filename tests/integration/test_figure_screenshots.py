from pathlib import Path

import pytest
from nbformat import NotebookNode

from computing_with_numpy.infrastructure.notebook import build_executed_notebook
from computing_with_numpy.infrastructure.notebook_screenshots import (
    cell_png,
    write_cell_screenshots,
)

ROOT = Path(__file__).resolve().parents[2]
FIGURE_SLUGS = ("10-linspace-plot", "11-noise-image")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


@pytest.fixture(scope="module")
def executed() -> NotebookNode:
    return build_executed_notebook(ROOT)


def test_figure_cells_display_a_png(executed: NotebookNode) -> None:
    cells = {c.metadata.get("slug"): c for c in executed.cells}
    for slug in FIGURE_SLUGS:
        png = cell_png(cells[slug])
        assert png is not None, slug
        assert png.startswith(PNG_SIGNATURE), slug


def test_figure_screenshots_are_the_cells_figures(
    executed: NotebookNode, tmp_path: Path
) -> None:
    write_cell_screenshots(executed, tmp_path)
    cells = {c.metadata.get("slug"): c for c in executed.cells}
    for slug in FIGURE_SLUGS:
        assert (tmp_path / f"{slug}.png").read_bytes() == cell_png(cells[slug])
