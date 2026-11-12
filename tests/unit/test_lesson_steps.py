from computing_with_numpy import __version__
from computing_with_numpy.application.lesson import all_steps


def test_package_has_version() -> None:
    assert __version__ == "0.1.0"


def test_all_steps_start_with_setup() -> None:
    assert all_steps()[0].slug == "00-setup"


def test_all_steps_include_the_three_basics_steps() -> None:
    slugs = [step.slug for step in all_steps()]
    assert slugs[1:4] == ["01-vector", "02-matrix", "03-mystery-array"]


def test_all_steps_include_the_eight_challenge_steps() -> None:
    slugs = [step.slug for step in all_steps()]
    assert slugs[4:12] == [
        "04-arange",
        "05-slicing",
        "06-reverse",
        "07-nonzero",
        "08-random",
        "09-linspace-x",
        "10-linspace-plot",
        "11-noise-image",
    ]


def test_all_steps_include_the_four_linear_algebra_steps() -> None:
    slugs = [step.slug for step in all_steps()]
    assert slugs[12:16] == [
        "12-vector-math",
        "13-lists-vs-arrays",
        "14-broadcasting",
        "15-matrix-product",
    ]


def test_all_steps_end_with_the_seven_image_steps() -> None:
    slugs = [step.slug for step in all_steps()]
    assert slugs[16:] == [
        "16-image-info",
        "17-image-show",
        "18-grayscale",
        "19-flip-gray",
        "20-rotate",
        "21-invert",
        "22-own-image",
    ]


def test_challenge_steps_are_titled_by_number() -> None:
    titles = [step.title for step in all_steps()[4:12]]
    assert all(
        title.startswith(f"Challenge {number}:")
        for number, title in enumerate(titles, start=1)
    )


def test_all_steps_have_unique_slugs() -> None:
    slugs = [step.slug for step in all_steps()]
    assert len(slugs) == len(set(slugs))


def test_all_steps_have_nonempty_code() -> None:
    assert all(step.code.strip() for step in all_steps())
