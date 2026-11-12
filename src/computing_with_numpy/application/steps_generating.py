"""Steps of lecture part 2: generating and manipulating ndarrays."""

from __future__ import annotations

from computing_with_numpy.application.lesson_step import LessonStep

# Fixed so the notebook output and the screenshots are the same on every run.
NOTEBOOK_SEED = 77


def generating_steps() -> list[LessonStep]:
    """Return the steps for challenges 1 to 8."""
    return [
        LessonStep(
            slug="04-arange",
            title="Challenge 1: arange",
            explanation="`np.arange(10, 30)` makes a vector of the values 10 to 29.",
            code=(
                "from computing_with_numpy.domain.generating import "
                "create_range_vector\n"
                "\n"
                "a = create_range_vector()\n"
                "print(a)"
            ),
        ),
        LessonStep(
            slug="05-slicing",
            title="Challenge 2: slicing",
            explanation=(
                "A slice `start:stop:step` takes part of an axis. A negative start "
                "counts from the end."
            ),
            code=(
                "from computing_with_numpy.domain.generating import (\n"
                "    all_except_first_twelve,\n"
                "    create_range_vector,\n"
                "    every_second,\n"
                "    fourth_to_sixth,\n"
                "    last_three,\n"
                ")\n"
                "\n"
                "a = create_range_vector()\n"
                "print(last_three(a))\n"
                "print(fourth_to_sixth(a))\n"
                "print(all_except_first_twelve(a))\n"
                "print(every_second(a))"
            ),
        ),
        LessonStep(
            slug="06-reverse",
            title="Challenge 3: reverse an array",
            explanation="`a[::-1]` and `np.flip(a)` both reverse a vector.",
            code=(
                "from computing_with_numpy.domain.generating import (\n"
                "    create_range_vector,\n"
                "    reverse_array,\n"
                "    reverse_array_with_flip,\n"
                ")\n"
                "\n"
                "a = create_range_vector()\n"
                "print(reverse_array(a))\n"
                "print(reverse_array_with_flip(a))"
            ),
        ),
        LessonStep(
            slug="07-nonzero",
            title="Challenge 4: nonzero",
            explanation=(
                "`np.nonzero` returns a tuple with the indices of the non-zero "
                "elements, one array per axis."
            ),
            code=(
                "import numpy as np\n"
                "\n"
                "from computing_with_numpy.domain.generating import nonzero_indices\n"
                "\n"
                "print(nonzero_indices(np.array([6, 0, 9, 0, 0, 5, 0])))"
            ),
        ),
        LessonStep(
            slug="08-random",
            title="Challenge 5: random numbers",
            explanation=(
                "A random generator fills an array of shape (3, 3, 3). A seed makes "
                "the numbers repeat."
            ),
            code=(
                "from computing_with_numpy.domain.generating import random_cube\n"
                "\n"
                f"cube = random_cube({NOTEBOOK_SEED})\n"
                "print(cube.shape)\n"
                "print(cube)"
            ),
        ),
        LessonStep(
            slug="09-linspace-x",
            title="Challenge 6: linspace",
            explanation="`np.linspace(0, 100, num=9)` gives 9 evenly spaced values.",
            code=(
                "from computing_with_numpy.domain.generating import linspace_x\n"
                "\n"
                "x = linspace_x()\n"
                "print(x)"
            ),
        ),
        LessonStep(
            slug="10-linspace-plot",
            title="Challenge 7: plot a line",
            explanation=(
                "`linspace_y` gives 9 values from -3 to 3. Matplotlib plots y "
                "against x."
            ),
            code=(
                "import matplotlib.pyplot as plt\n"
                "\n"
                "from computing_with_numpy.domain.generating import "
                "linspace_x, linspace_y\n"
                "\n"
                "x = linspace_x()\n"
                "y = linspace_y()\n"
                "print(y)\n"
                "plt.plot(x, y)\n"
                "plt.show()"
            ),
        ),
        LessonStep(
            slug="11-noise-image",
            title="Challenge 8: a noise image",
            explanation=(
                "Random values of shape (128, 128, 3) are read as the red, green "
                "and blue of a 128 by 128 image."
            ),
            code=(
                "import matplotlib.pyplot as plt\n"
                "\n"
                "from computing_with_numpy.domain.generating import noise_image\n"
                "\n"
                f"noise = noise_image({NOTEBOOK_SEED})\n"
                "print(noise.shape)\n"
                "plt.imshow(noise)\n"
                "plt.show()"
            ),
        ),
    ]
