"""Lecture part 2: generating and manipulating ndarrays."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

RANGE_START = 10
RANGE_STOP = 30
CUBE_SHAPE = (3, 3, 3)
IMAGE_SHAPE = (128, 128, 3)
LINSPACE_POINTS = 9
X_START = 0
X_STOP = 100
Y_START = -3
Y_STOP = 3


def create_range_vector() -> NDArray[np.int64]:
    """Return the vector of the values 10 to 29: ``np.arange(10, 30)``."""
    return np.arange(RANGE_START, RANGE_STOP)


def last_three(a: NDArray[np.int64]) -> NDArray[np.int64]:
    """Return the last three values: ``a[-3:]``."""
    return a[-3:]


def fourth_to_sixth(a: NDArray[np.int64]) -> NDArray[np.int64]:
    """Return the 4th to 6th values: ``a[3:6]``."""
    return a[3:6]


def all_except_first_twelve(a: NDArray[np.int64]) -> NDArray[np.int64]:
    """Return every value but the first twelve: ``a[12:]``."""
    return a[12:]


def every_second(a: NDArray[np.int64]) -> NDArray[np.int64]:
    """Return every second value, starting with the first: ``a[::2]``."""
    return a[::2]


def reverse_array(a: NDArray[np.int64]) -> NDArray[np.int64]:
    """Return ``a`` in reverse order with the slice ``a[::-1]``."""
    return a[::-1]


def reverse_array_with_flip(a: NDArray[np.int64]) -> NDArray[np.int64]:
    """Return ``a`` in reverse order with ``np.flip``."""
    return np.flip(a)


def nonzero_indices(array: NDArray[np.int64]) -> tuple[NDArray[np.intp], ...]:
    """Return the indices of the non-zero elements: ``np.nonzero(array)``."""
    return np.nonzero(array)


def random_cube(seed: int | None = None) -> NDArray[np.float64]:
    """Return random values in an array of shape (3, 3, 3); a seed makes it repeat."""
    return np.random.default_rng(seed).random(CUBE_SHAPE)


def linspace_x() -> NDArray[np.float64]:
    """Return 9 evenly spaced values from 0 to 100."""
    return np.linspace(X_START, X_STOP, num=LINSPACE_POINTS)


def linspace_y() -> NDArray[np.float64]:
    """Return 9 evenly spaced values from -3 to 3."""
    return np.linspace(Y_START, Y_STOP, num=LINSPACE_POINTS)


def noise_image(seed: int | None = None) -> NDArray[np.float64]:
    """Return random RGB noise of shape (128, 128, 3); a seed makes it repeat."""
    return np.random.default_rng(seed).random(IMAGE_SHAPE)
