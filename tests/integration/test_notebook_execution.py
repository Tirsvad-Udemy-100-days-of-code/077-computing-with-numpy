from pathlib import Path

from computing_with_numpy.application.lesson import all_steps
from computing_with_numpy.infrastructure.notebook import (
    build_executed_notebook,
    build_notebook,
    write_notebook,
)

ROOT = Path(__file__).resolve().parents[2]


def test_execute_notebook_gives_every_step_stdout_and_no_error() -> None:
    executed = build_executed_notebook(ROOT)
    for cell in executed.cells:
        if "slug" not in cell.metadata:
            continue
        kinds = [output.output_type for output in cell.outputs]
        stdout = "".join(o.text for o in cell.outputs if o.output_type == "stream")
        assert "error" not in kinds, cell.metadata["slug"]
        assert stdout.strip(), cell.metadata["slug"]


def test_write_notebook_creates_ipynb_file(tmp_path: Path) -> None:
    target = write_notebook(build_notebook(all_steps()), tmp_path / "n" / "a.ipynb")
    assert target.read_text(encoding="utf-8").startswith("{")
