import numpy as np

from computing_with_numpy.domain.generating import (
    all_except_first_twelve,
    create_range_vector,
    every_second,
    fourth_to_sixth,
    last_three,
    linspace_x,
    linspace_y,
    noise_image,
    nonzero_indices,
    random_cube,
    reverse_array,
    reverse_array_with_flip,
)


def test_create_range_vector_returns_10_to_29() -> None:
    assert create_range_vector().tolist() == list(range(10, 30))


def test_last_three_returns_27_28_29() -> None:
    assert last_three(create_range_vector()).tolist() == [27, 28, 29]


def test_fourth_to_sixth_returns_13_14_15() -> None:
    assert fourth_to_sixth(create_range_vector()).tolist() == [13, 14, 15]


def test_all_except_first_twelve_returns_22_to_29() -> None:
    assert all_except_first_twelve(create_range_vector()).tolist() == list(
        range(22, 30)
    )


def test_every_second_returns_10_12_to_28() -> None:
    assert every_second(create_range_vector()).tolist() == list(range(10, 30, 2))


def test_reverse_array_returns_29_down_to_10() -> None:
    assert reverse_array(create_range_vector()).tolist() == list(range(29, 9, -1))


def test_reverse_array_with_flip_matches_slice() -> None:
    a = create_range_vector()
    assert np.array_equal(reverse_array_with_flip(a), reverse_array(a))


def test_nonzero_indices_returns_tuple_with_0_2_5() -> None:
    result = nonzero_indices(np.array([6, 0, 9, 0, 0, 5, 0]))
    assert isinstance(result, tuple)
    assert len(result) == 1
    assert result[0].tolist() == [0, 2, 5]


def test_nonzero_indices_of_all_zero_array_is_empty() -> None:
    assert nonzero_indices(np.zeros(3, dtype=np.int64))[0].size == 0


def test_random_cube_has_shape_3_3_3_and_unit_range() -> None:
    cube = random_cube()
    assert cube.shape == (3, 3, 3)
    assert cube.min() >= 0.0
    assert cube.max() < 1.0


def test_random_cube_repeats_for_the_same_seed() -> None:
    assert np.array_equal(random_cube(1), random_cube(1))


def test_random_cube_differs_for_different_seeds() -> None:
    assert not np.array_equal(random_cube(1), random_cube(2))


def test_linspace_x_has_9_values_from_0_to_100() -> None:
    x = linspace_x()
    assert x.size == 9
    assert x[0] == 0
    assert x[-1] == 100
    assert x.tolist() == [0.0, 12.5, 25.0, 37.5, 50.0, 62.5, 75.0, 87.5, 100.0]


def test_linspace_y_has_9_values_from_minus_3_to_3() -> None:
    y = linspace_y()
    assert y.size == 9
    assert y[0] == -3
    assert y[-1] == 3
    assert y.tolist() == [-3.0, -2.25, -1.5, -0.75, 0.0, 0.75, 1.5, 2.25, 3.0]


def test_noise_image_has_shape_128_128_3() -> None:
    assert noise_image().shape == (128, 128, 3)


def test_noise_image_repeats_for_the_same_seed() -> None:
    assert np.array_equal(noise_image(5), noise_image(5))
