import numpy as np

from computing_with_numpy.domain.ndarray_basics import (
    ArrayDescription,
    create_matrix,
    create_vector,
    describe_array,
    matrix_element,
    matrix_row,
    mystery_array,
    mystery_first_elements_matrix,
    mystery_last_row_vector,
    mystery_value_18,
    vector_element,
)


def test_mystery_array_has_three_dimensions() -> None:
    assert mystery_array().ndim == 3


def test_mystery_array_has_shape_3_2_4() -> None:
    assert mystery_array().shape == (3, 2, 4)


def test_mystery_value_18_returns_18() -> None:
    assert mystery_value_18(mystery_array()) == 18


def test_mystery_last_row_vector_returns_lecture_vector() -> None:
    result = mystery_last_row_vector(mystery_array())
    assert result.tolist() == [97, 0, 27, 18]


def test_mystery_first_elements_matrix_returns_3_by_2_matrix() -> None:
    result = mystery_first_elements_matrix(mystery_array())
    assert result.tolist() == [[0, 4], [7, 5], [5, 97]]


def test_vector_element_2_is_8_1() -> None:
    assert vector_element(create_vector(), 2) == 8.1


def test_matrix_element_row_1_column_2_is_7() -> None:
    assert matrix_element(create_matrix(), 1, 2) == 7


def test_matrix_row_0_returns_first_row() -> None:
    assert matrix_row(create_matrix(), 0).tolist() == [1, 2, 3, 9]


def test_describe_array_for_vector() -> None:
    assert describe_array(create_vector()) == ArrayDescription(1, (4,))


def test_describe_array_for_matrix() -> None:
    assert describe_array(create_matrix()) == ArrayDescription(2, (2, 4))


def test_describe_array_for_mystery_array() -> None:
    assert describe_array(mystery_array()) == ArrayDescription(3, (3, 2, 4))


def test_create_vector_is_float_array() -> None:
    assert create_vector().dtype == np.float64
