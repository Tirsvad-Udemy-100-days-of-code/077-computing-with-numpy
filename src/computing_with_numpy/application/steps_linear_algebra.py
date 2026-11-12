"""Steps of lecture part 3: vector maths, broadcasting and matrix products."""

from __future__ import annotations

from computing_with_numpy.application.lesson_step import LessonStep


def linear_algebra_steps() -> list[LessonStep]:
    """Return the steps for vector maths, broadcasting and matrix products."""
    return [
        LessonStep(
            slug="12-vector-math",
            title="Linear algebra with vectors",
            explanation=(
                "Arrays add and multiply element by element: "
                "`[4, 5, 2, 7] + [2, 1, 3, 3]` is `[6, 6, 5, 10]`."
            ),
            code=(
                "from computing_with_numpy.domain.linear_algebra import (\n"
                "    add_vectors,\n"
                "    create_vector_v1,\n"
                "    create_vector_v2,\n"
                "    multiply_vectors,\n"
                ")\n"
                "\n"
                "v1 = create_vector_v1()\n"
                "v2 = create_vector_v2()\n"
                "print(add_vectors(v1, v2))\n"
                "print(multiply_vectors(v1, v2))"
            ),
        ),
        LessonStep(
            slug="13-lists-vs-arrays",
            title="Lists versus arrays",
            explanation=(
                "`+` on two Python lists joins them, and `*` on two lists is an "
                "error. Arrays do the maths."
            ),
            code=(
                "from computing_with_numpy.domain.linear_algebra import (\n"
                "    VECTOR_1,\n"
                "    VECTOR_2,\n"
                "    add_lists,\n"
                "    multiply_lists,\n"
                ")\n"
                "\n"
                "print(add_lists(VECTOR_1, VECTOR_2))\n"
                "try:\n"
                "    multiply_lists(VECTOR_1, VECTOR_2)\n"
                "except TypeError as error:\n"
                "    print(f'TypeError: {error}')"
            ),
        ),
        LessonStep(
            slug="14-broadcasting",
            title="Broadcasting a scalar",
            explanation=(
                "A scalar is broadcast to every element, in one or two dimensions."
            ),
            code=(
                "from computing_with_numpy.domain.linear_algebra import (\n"
                "    create_array_2d,\n"
                "    create_vector_v1,\n"
                "    scale_array,\n"
                ")\n"
                "\n"
                "print(scale_array(create_vector_v1(), 2))\n"
                "print(scale_array(create_array_2d(), 2))"
            ),
        ),
        LessonStep(
            slug="15-matrix-product",
            title="Matrix multiplication challenge",
            explanation=(
                "`a1 @ b1` multiplies a (4, 2) matrix by a (2, 3) matrix and gives "
                "a (4, 3) matrix. `np.matmul` gives the same result."
            ),
            code=(
                "import numpy as np\n"
                "\n"
                "from computing_with_numpy.domain.linear_algebra import (\n"
                "    create_matrix_a1,\n"
                "    create_matrix_b1,\n"
                "    matrix_product,\n"
                ")\n"
                "\n"
                "a1 = create_matrix_a1()\n"
                "b1 = create_matrix_b1()\n"
                "c = matrix_product(a1, b1)\n"
                "print(c)\n"
                "print(c.shape)\n"
                "print(np.array_equal(c, np.matmul(a1, b1)))"
            ),
        ),
    ]
