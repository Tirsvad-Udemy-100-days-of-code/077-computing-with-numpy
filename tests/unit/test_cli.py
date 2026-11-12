import pytest

from computing_with_numpy.presentation.cli import main


def test_main_prints_steps_and_notebook_pointer(
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = main()
    output = capsys.readouterr().out
    assert exit_code == 0
    assert "N dimensions: the mystery array challenge" in output
    assert "mystery_value_18" in output
    assert output.rstrip().endswith("notebooks/computing_with_numpy.ipynb")
