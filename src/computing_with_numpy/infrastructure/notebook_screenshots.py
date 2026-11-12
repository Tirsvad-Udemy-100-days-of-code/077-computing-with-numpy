"""Turn the cells of an executed notebook into screenshots."""

from __future__ import annotations

import base64
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from nbformat import NotebookNode

from computing_with_numpy.infrastructure.screenshots import render_text_screenshot

PROMPT = ">>> "
CONTINUATION = "... "
HEADING_PREFIX = "## "


def cell_stdout(cell: Mapping[str, Any]) -> str:
    """Return the text a code cell wrote to standard output."""
    parts = [
        str(output.get("text", ""))
        for output in cell.get("outputs", [])
        if output.get("output_type") == "stream" and output.get("name") == "stdout"
    ]
    return "".join(parts)


def cell_png(cell: Mapping[str, Any]) -> bytes | None:
    """Return the first PNG image a code cell displayed, if any."""
    for output in cell.get("outputs", []):
        data = output.get("data", {})
        if "image/png" in data:
            return base64.b64decode(data["image/png"])
    return None


def cell_screenshot_lines(cell: Mapping[str, Any]) -> tuple[str, ...]:
    """Return the code (after a ``>>> `` prompt) followed by the cell's output."""
    code_lines = str(cell.get("source", "")).splitlines()
    prompted = [
        (PROMPT if index == 0 else CONTINUATION) + line
        for index, line in enumerate(code_lines)
    ]
    return (*prompted, *cell_stdout(cell).splitlines())


def write_cell_screenshots(notebook: NotebookNode, images_dir: Path) -> list[Path]:
    """Write ``<slug>.png`` for each code cell that has a ``slug`` in its metadata."""
    written: list[Path] = []
    title = ""
    for cell in notebook.cells:
        if cell.cell_type == "markdown":
            first_line = str(cell.source).splitlines()[0] if cell.source else ""
            if first_line.startswith(HEADING_PREFIX):
                title = first_line.removeprefix(HEADING_PREFIX)
            continue
        slug = cell.metadata.get("slug")
        if cell.cell_type != "code" or not slug:
            continue
        target = images_dir / f"{slug}.png"
        png = cell_png(cell)
        if png is None:
            render_text_screenshot(title, cell_screenshot_lines(cell), target)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(png)
        written.append(target)
    return written
