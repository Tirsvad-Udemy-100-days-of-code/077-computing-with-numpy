from computing_with_numpy import __version__
from computing_with_numpy.application.lesson import all_steps


def test_package_has_version() -> None:
    assert __version__ == "0.1.0"


def test_all_steps_start_with_setup() -> None:
    assert all_steps()[0].slug == "00-setup"


def test_all_steps_include_the_three_basics_steps() -> None:
    slugs = [step.slug for step in all_steps()]
    assert slugs[1:] == ["01-vector", "02-matrix", "03-mystery-array"]


def test_all_steps_have_unique_slugs() -> None:
    slugs = [step.slug for step in all_steps()]
    assert len(slugs) == len(set(slugs))


def test_all_steps_have_nonempty_code() -> None:
    assert all(step.code.strip() for step in all_steps())
