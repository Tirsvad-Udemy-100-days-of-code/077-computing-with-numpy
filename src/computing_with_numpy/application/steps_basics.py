"""Steps of lecture part 1: NumPy's ndarray."""

from __future__ import annotations

from computing_with_numpy.application.lesson_step import LessonStep


def basics_steps() -> list[LessonStep]:
    """Return the steps for 1D, 2D and N-D arrays."""
    return [
        LessonStep(
            slug="01-vector",
            title="1 dimension: a vector",
            explanation=(
                "An ndarray is homogeneous: every element has the same type. "
                "`shape` and `ndim` describe it; an element is read by index."
            ),
            code=(
                "from computing_with_numpy.domain.ndarray_basics import (\n"
                "    create_vector,\n"
                "    describe_array,\n"
                "    vector_element,\n"
                ")\n"
                "\n"
                "my_array = create_vector()\n"
                "print(my_array)\n"
                "print(describe_array(my_array))\n"
                "print(vector_element(my_array, 2))"
            ),
        ),
        LessonStep(
            slug="02-matrix",
            title="2 dimensions: a matrix",
            explanation=(
                "A 2-dimensional array has two axes: 2 rows and 4 columns. A value "
                "needs one index per axis; `:` takes a whole axis."
            ),
            code=(
                "from computing_with_numpy.domain.ndarray_basics import (\n"
                "    create_matrix,\n"
                "    describe_array,\n"
                "    matrix_element,\n"
                "    matrix_row,\n"
                ")\n"
                "\n"
                "array_2d = create_matrix()\n"
                "print(array_2d)\n"
                "print(describe_array(array_2d))\n"
                "print(matrix_element(array_2d, 1, 2))\n"
                "print(matrix_row(array_2d, 0))"
            ),
        ),
        LessonStep(
            slug="03-mystery-array",
            title="N dimensions: the mystery array challenge",
            explanation=(
                "A tensor has three or more axes. Shape (3, 2, 4) needs three "
                "indices to reach one value; slices fix some axes and keep others."
            ),
            code=(
                "from computing_with_numpy.domain.ndarray_basics import (\n"
                "    describe_array,\n"
                "    mystery_array,\n"
                "    mystery_first_elements_matrix,\n"
                "    mystery_last_row_vector,\n"
                "    mystery_value_18,\n"
                ")\n"
                "\n"
                "mystery = mystery_array()\n"
                "print(describe_array(mystery))\n"
                "print(mystery_value_18(mystery))\n"
                "print(mystery_last_row_vector(mystery))\n"
                "print(mystery_first_elements_matrix(mystery))"
            ),
        ),
    ]
