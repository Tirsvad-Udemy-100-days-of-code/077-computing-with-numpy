from computing_with_numpy import __version__
from computing_with_numpy.application.lesson_steps import all_steps, setup_step


def test_package_has_version() -> None:
    assert __version__ == "0.1.0"


def test_setup_step_names_python_and_numpy() -> None:
    text = "\n".join(setup_step().lines)
    assert "Python 3." in text
    assert "NumPy" in text


def test_all_steps_start_with_setup() -> None:
    assert all_steps()[0].slug == "00-setup"
