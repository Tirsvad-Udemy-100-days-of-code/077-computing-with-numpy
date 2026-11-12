import numpy as np
from numpy.typing import NDArray

from computing_with_numpy.domain.images import (
    GREY_VALUES,
    ImageDescription,
    describe_image,
    flip_image,
    invert_image,
    load_face_image,
    rotate_image,
    to_grayscale,
)


def _tiny() -> NDArray[np.uint8]:
    return np.arange(12, dtype=np.uint8).reshape(2, 2, 3)


def test_face_image_is_uint8_with_three_channels() -> None:
    img = load_face_image()
    assert img.dtype == np.uint8
    assert img.shape == (768, 1024, 3)
    assert img.ndim == 3


def test_face_image_is_deterministic() -> None:
    assert np.array_equal(load_face_image(), load_face_image())


def test_describe_image_reports_type_shape_and_resolution() -> None:
    assert describe_image(load_face_image()) == ImageDescription(
        dtype="uint8", shape=(768, 1024, 3), ndim=3, width=1024, height=768
    )


def test_grayscale_is_2d_with_values_between_zero_and_one() -> None:
    gray = to_grayscale(load_face_image())
    assert gray.shape == (768, 1024)
    assert gray.min() >= 0.0
    assert gray.max() <= 1.0


def test_grayscale_equals_matmul_of_scaled_image() -> None:
    img = load_face_image()
    expected = np.matmul(img / 255, np.array(GREY_VALUES))
    assert np.array_equal(to_grayscale(img), expected)


def test_grayscale_of_white_pixel_is_one() -> None:
    white = np.full((1, 1, 3), 255, dtype=np.uint8)
    assert np.isclose(to_grayscale(white)[0, 0], 1.0)


def test_flip_image_reverses_every_axis_on_tiny_array() -> None:
    assert np.array_equal(flip_image(_tiny()), _tiny()[::-1, ::-1, ::-1])


def test_flip_image_keeps_shape_and_differs_on_full_picture() -> None:
    img = load_face_image()
    flipped = flip_image(img)
    assert flipped.shape == img.shape
    assert not np.array_equal(flipped, img)


def test_rotate_image_turns_tiny_array_a_quarter() -> None:
    rotated = rotate_image(np.array([[1, 2, 3], [4, 5, 6]]))
    assert rotated.tolist() == [[3, 6], [2, 5], [1, 4]]


def test_rotate_image_swaps_height_and_width_of_full_picture() -> None:
    assert rotate_image(load_face_image()).shape == (1024, 768, 3)


def test_invert_image_subtracts_from_255_on_tiny_array() -> None:
    result = invert_image(np.array([[0, 100, 255]], dtype=np.uint8))
    assert result.tolist() == [[255, 155, 0]]
    assert result.dtype == np.uint8


def test_invert_image_twice_is_identity() -> None:
    img = load_face_image()
    assert np.array_equal(invert_image(invert_image(img)), img)
