import numpy as np
import pytest

from computing_with_numpy.domain.linear_algebra import (
    VECTOR_1,
    VECTOR_2,
    add_lists,
    add_vectors,
    create_array_2d,
    create_matrix_a1,
    create_matrix_b1,
    create_vector_v1,
    create_vector_v2,
    matrix_product,
    multiply_lists,
    multiply_vectors,
    scale_array,
)


def test_add_vectors_adds_element_by_element() -> None:
    result = add_vectors(create_vector_v1(), create_vector_v2())
    assert result.tolist() == [6, 6, 5, 10]


def test_multiply_vectors_multiplies_element_by_element() -> None:
    result = multiply_vectors(create_vector_v1(), create_vector_v2())
    assert result.tolist() == [8, 5, 6, 21]


def test_add_lists_concatenates() -> None:
    assert add_lists(VECTOR_1, VECTOR_2) == [4, 5, 2, 7, 2, 1, 3, 3]


def test_multiply_lists_raises_type_error() -> None:
    with pytest.raises(TypeError):
        multiply_lists(VECTOR_1, VECTOR_2)


def test_scale_array_doubles_a_vector() -> None:
    assert scale_array(create_vector_v1(), 2).tolist() == [8, 10, 4, 14]


def test_scale_array_doubles_a_2d_array() -> None:
    assert scale_array(create_array_2d(), 2).tolist() == [
        [2, 4, 6, 8],
        [10, 12, 14, 16],
    ]


def test_matrix_product_has_shape_4_3() -> None:
    assert matrix_product(create_matrix_a1(), create_matrix_b1()).shape == (4, 3)


def test_matrix_product_matches_np_matmul() -> None:
    a1 = create_matrix_a1()
    b1 = create_matrix_b1()
    assert np.array_equal(matrix_product(a1, b1), np.matmul(a1, b1))


def test_matrix_product_c12_is_25() -> None:
    assert matrix_product(create_matrix_a1(), create_matrix_b1())[0, 1] == 25


def test_matrix_product_c33_is_28() -> None:
    assert matrix_product(create_matrix_a1(), create_matrix_b1())[2, 2] == 28
