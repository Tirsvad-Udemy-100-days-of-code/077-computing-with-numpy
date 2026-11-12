"""Lecture part 1: NumPy's ndarray in one, two and more dimensions."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


@dataclass(frozen=True)
class ArrayDescription:
    """What the lecture asks of an array: dimensions and the length of each axis."""

    ndim: int
    shape: tuple[int, ...]


def create_vector() -> NDArray[np.float64]:
    """Return the lecture's 1-dimensional array (a "vector")."""
    return np.array([1.1, 9.2, 8.1, 4.7])


def create_matrix() -> NDArray[np.int64]:
    """Return the lecture's 2-dimensional array (a "matrix"): 2 rows, 4 columns."""
    return np.array([[1, 2, 3, 9], [5, 6, 7, 8]])


def describe_array(array: NDArray[np.generic]) -> ArrayDescription:
    """Return the number of dimensions and the shape of ``array``."""
    return ArrayDescription(ndim=array.ndim, shape=array.shape)


def vector_element(vector: NDArray[np.float64], index: int) -> float:
    """Return the element at ``index``, as in ``my_array[2]``."""
    return float(vector[index])


def matrix_element(matrix: NDArray[np.int64], row: int, column: int) -> int:
    """Return one value, as in ``array_2d[1, 2]`` (3rd value of the 2nd row)."""
    return int(matrix[row, column])


def matrix_row(matrix: NDArray[np.int64], row: int) -> NDArray[np.int64]:
    """Return an entire row, as in ``array_2d[0, :]``."""
    return matrix[row, :]


def mystery_array() -> NDArray[np.int64]:
    """Return the lecture's 3-dimensional "mystery" array of shape (3, 2, 4)."""
    return np.array(
        [
            [[0, 1, 2, 3], [4, 5, 6, 7]],
            [[7, 86, 6, 98], [5, 1, 0, 4]],
            [[5, 36, 32, 48], [97, 0, 27, 18]],
        ]
    )


def mystery_value_18(array: NDArray[np.int64]) -> int:
    """Return the value 18: index 2 on axis 0, 1 on axis 1, 3 on axis 2."""
    return int(array[2, 1, 3])


def mystery_last_row_vector(array: NDArray[np.int64]) -> NDArray[np.int64]:
    """Return the vector [97, 0, 27, 18]: ``mystery_array[2, 1, :]``."""
    return array[2, 1, :]


def mystery_first_elements_matrix(array: NDArray[np.int64]) -> NDArray[np.int64]:
    """Return the (3, 2) matrix of first elements on axis 2: ``array[:, :, 0]``."""
    return array[:, :, 0]
