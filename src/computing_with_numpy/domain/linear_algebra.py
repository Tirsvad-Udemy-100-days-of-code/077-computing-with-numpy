"""Lecture part 3: vector maths, broadcasting and matrix multiplication."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

VECTOR_1 = [4, 5, 2, 7]
VECTOR_2 = [2, 1, 3, 3]
MATRIX_2D = [[1, 2, 3, 4], [5, 6, 7, 8]]
MATRIX_A1 = [[1, 3], [0, 1], [6, 2], [9, 7]]
MATRIX_B1 = [[4, 1, 3], [5, 8, 5]]


def create_vector_v1() -> NDArray[np.int64]:
    """Return the lecture's first vector, ``[4, 5, 2, 7]``."""
    return np.array(VECTOR_1)


def create_vector_v2() -> NDArray[np.int64]:
    """Return the lecture's second vector, ``[2, 1, 3, 3]``."""
    return np.array(VECTOR_2)


def create_array_2d() -> NDArray[np.int64]:
    """Return the 2 by 4 array ``[[1, 2, 3, 4], [5, 6, 7, 8]]``."""
    return np.array(MATRIX_2D)


def create_matrix_a1() -> NDArray[np.int64]:
    """Return the lecture's 4 by 2 matrix ``a1``."""
    return np.array(MATRIX_A1)


def create_matrix_b1() -> NDArray[np.int64]:
    """Return the lecture's 2 by 3 matrix ``b1``."""
    return np.array(MATRIX_B1)


def add_vectors(v1: NDArray[np.int64], v2: NDArray[np.int64]) -> NDArray[np.int64]:
    """Return the element-wise sum of two vectors."""
    return v1 + v2


def multiply_vectors(v1: NDArray[np.int64], v2: NDArray[np.int64]) -> NDArray[np.int64]:
    """Return the element-wise product of two vectors."""
    return v1 * v2


def add_lists(list1: list[int], list2: list[int]) -> list[int]:
    """Return the two Python lists joined: ``+`` concatenates, it does not add."""
    return list1 + list2


def multiply_lists(list1: list[int], list2: list[int]) -> object:
    """Multiply two Python lists, the lecture's "error!": raises ``TypeError``."""
    return list1 * list2  # type: ignore[operator]


def scale_array(array: NDArray[np.int64], factor: int) -> NDArray[np.int64]:
    """Return ``array`` times ``factor``; the scalar is broadcast to every element."""
    return array * factor


def matrix_product(a: NDArray[np.int64], b: NDArray[np.int64]) -> NDArray[np.int64]:
    """Return the matrix product of ``a`` and ``b`` with the ``@`` operator."""
    return a @ b
