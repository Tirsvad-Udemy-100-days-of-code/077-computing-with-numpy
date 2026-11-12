from computing_with_numpy.application.lesson import all_steps
from computing_with_numpy.infrastructure.notebook import build_notebook


def test_build_notebook_has_a_code_cell_per_step_with_slug() -> None:
    steps = all_steps()
    notebook = build_notebook(steps)
    slugs = [
        cell.metadata["slug"]
        for cell in notebook.cells
        if cell.cell_type == "code" and "slug" in cell.metadata
    ]
    assert slugs == [step.slug for step in steps]


def test_build_notebook_code_cell_holds_step_code() -> None:
    steps = all_steps()
    notebook = build_notebook(steps)
    sources = [c.source for c in notebook.cells if "slug" in c.metadata]
    assert sources == [step.code for step in steps]
