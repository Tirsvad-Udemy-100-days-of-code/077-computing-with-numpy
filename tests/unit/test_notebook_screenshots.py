import base64
from pathlib import Path
from typing import Any

import nbformat

from computing_with_numpy.infrastructure.notebook_screenshots import (
    cell_screenshot_lines,
    write_cell_screenshots,
)

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def _cell(source: str, outputs: list[dict[str, Any]]) -> dict[str, Any]:
    return {"source": source, "outputs": outputs}


def _stream(text: str) -> dict[str, Any]:
    return {"output_type": "stream", "name": "stdout", "text": text}


def _notebook_with(outputs: list[dict[str, Any]]) -> Any:
    notebook = nbformat.v4.new_notebook()
    notebook.cells.append(nbformat.v4.new_markdown_cell("## A title\n\ntext"))
    cell = nbformat.v4.new_code_cell("print(1)")
    cell.metadata["slug"] = "09-fake"
    cell.outputs = outputs
    notebook.cells.append(cell)
    return notebook


def test_cell_screenshot_lines_prefix_code_and_append_stdout() -> None:
    cell = _cell("a = 1\nprint(a)", [_stream("1\n")])
    assert cell_screenshot_lines(cell) == (">>> a = 1", "... print(a)", "1")


def test_write_cell_screenshots_renders_text_cell(tmp_path: Path) -> None:
    notebook = _notebook_with([_stream("1\n")])
    written = write_cell_screenshots(notebook, tmp_path)
    assert written == [tmp_path / "09-fake.png"]
    assert written[0].read_bytes().startswith(PNG_SIGNATURE)


def test_write_cell_screenshots_saves_display_png_directly(tmp_path: Path) -> None:
    payload = PNG_SIGNATURE + b"figure"
    output = {
        "output_type": "display_data",
        "data": {"image/png": base64.b64encode(payload).decode()},
        "metadata": {},
    }
    write_cell_screenshots(_notebook_with([output]), tmp_path)
    assert (tmp_path / "09-fake.png").read_bytes() == payload


def test_write_cell_screenshots_skips_cells_without_slug(tmp_path: Path) -> None:
    notebook = nbformat.v4.new_notebook()
    notebook.cells.append(nbformat.v4.new_code_cell("%matplotlib inline"))
    assert write_cell_screenshots(notebook, tmp_path) == []
