"""Build the lesson notebook from the lesson steps and execute it."""

from __future__ import annotations

from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbformat import NotebookNode

from computing_with_numpy.application.lesson import all_steps
from computing_with_numpy.application.lesson_step import LessonStep

TITLE = "# Day 77: Computing with NumPy"
PREAMBLE = "%matplotlib inline"
CELL_TIMEOUT_SECONDS = 120


def build_notebook(steps: list[LessonStep]) -> NotebookNode:
    """Return a notebook with a markdown cell and a code cell per step."""
    notebook = nbformat.v4.new_notebook()
    notebook.cells.append(nbformat.v4.new_markdown_cell(TITLE))
    notebook.cells.append(nbformat.v4.new_code_cell(PREAMBLE))
    for step in steps:
        notebook.cells.append(
            nbformat.v4.new_markdown_cell(f"## {step.title}\n\n{step.explanation}")
        )
        cell = nbformat.v4.new_code_cell(step.code)
        cell.metadata["slug"] = step.slug
        notebook.cells.append(cell)
    return notebook


def execute_notebook(notebook: NotebookNode, working_dir: Path) -> NotebookNode:
    """Run every cell in a kernel started in ``working_dir``; return the result."""
    client = NotebookClient(
        notebook,
        timeout=CELL_TIMEOUT_SECONDS,
        kernel_name="python3",
        resources={"metadata": {"path": str(working_dir)}},
    )
    return client.execute()


def build_executed_notebook(working_dir: Path) -> NotebookNode:
    """Build the lesson notebook from every step and run it in ``working_dir``."""
    return execute_notebook(build_notebook(all_steps()), working_dir)


def write_notebook(notebook: NotebookNode, path: Path) -> Path:
    """Write ``notebook`` as an .ipynb file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(notebook, str(path))
    return path
