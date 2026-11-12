"""Steps of lecture part 4: images as ndarrays."""

from __future__ import annotations

from computing_with_numpy.application.lesson_step import LessonStep

IMPORT_PLT = "import matplotlib.pyplot as plt\n\n"
IMPORT_FACE = (
    "from computing_with_numpy.domain.images import load_face_image\n\n"
    "img = load_face_image()\n"
)
IMPORT_GRAY = (
    "from computing_with_numpy.domain.images import load_face_image, to_grayscale\n\n"
    "img_gray = to_grayscale(load_face_image())\n"
)


def images_steps() -> list[LessonStep]:
    """Return the steps that treat a picture as an ndarray."""
    return [
        LessonStep(
            slug="16-image-info",
            title="Images are ndarrays",
            explanation=(
                "A picture is a 3-D `uint8` array: rows, columns and the red, "
                "green and blue channels. The generated scene stands in for the "
                "lecture's raccoon (ADR-0001)."
            ),
            code=(
                "from computing_with_numpy.domain.images import (\n"
                "    describe_image,\n"
                "    load_face_image,\n"
                ")\n"
                "\n"
                "img = load_face_image()\n"
                "info = describe_image(img)\n"
                "print(type(img))\n"
                "print(info.dtype)\n"
                "print(info.shape)\n"
                "print(info.ndim)\n"
                "print(f'{info.width} x {info.height}')"
            ),
        ),
        LessonStep(
            slug="17-image-show",
            title="Show the image",
            explanation="`plt.imshow` draws the array as a picture.",
            code=(
                IMPORT_PLT
                + IMPORT_FACE
                + "print(img.shape)\nplt.imshow(img)\nplt.show()"
            ),
        ),
        LessonStep(
            slug="18-grayscale",
            title="Convert the image to grayscale",
            explanation=(
                "Divide the sRGB values by 255, then the matrix product with the "
                "grey values `[0.2126, 0.7152, 0.0722]` gives one channel from 0 "
                "to 1. `cmap='gray'` draws it in grey."
            ),
            code=(
                IMPORT_PLT + IMPORT_GRAY + "print(img_gray.shape)\n"
                "plt.imshow(img_gray, cmap='gray')\n"
                "plt.show()"
            ),
        ),
        LessonStep(
            slug="19-flip-gray",
            title="Flip the grayscale image",
            explanation="`np.flip` turns the grayscale image upside down.",
            code=(
                IMPORT_PLT + "from computing_with_numpy.domain.images import (\n"
                "    flip_image,\n"
                "    load_face_image,\n"
                "    to_grayscale,\n"
                ")\n"
                "\n"
                "img_gray = to_grayscale(load_face_image())\n"
                "flipped = flip_image(img_gray)\n"
                "print(flipped.shape)\n"
                "plt.imshow(flipped, cmap='gray')\n"
                "plt.show()"
            ),
        ),
        LessonStep(
            slug="20-rotate",
            title="Rotate the colour image",
            explanation="`np.rot90` rotates the colour image a quarter turn.",
            code=(
                IMPORT_PLT + "from computing_with_numpy.domain.images import (\n"
                "    load_face_image,\n"
                "    rotate_image,\n"
                ")\n"
                "\n"
                "img = load_face_image()\n"
                "rotated = rotate_image(img)\n"
                "print(rotated.shape)\n"
                "plt.imshow(rotated)\n"
                "plt.show()"
            ),
        ),
        LessonStep(
            slug="21-invert",
            title="Invert (solarize) the colour image",
            explanation="`255 - img` inverts every channel value.",
            code=(
                IMPORT_PLT + "from computing_with_numpy.domain.images import (\n"
                "    invert_image,\n"
                "    load_face_image,\n"
                ")\n"
                "\n"
                "img = load_face_image()\n"
                "inverted = invert_image(img)\n"
                "print(inverted.dtype)\n"
                "plt.imshow(inverted)\n"
                "plt.show()"
            ),
        ),
        LessonStep(
            slug="22-own-image",
            title="Use your own image",
            explanation=(
                "`load_image` opens any 3-channel picture file with Pillow as an "
                "ndarray. The example saves the scene as a temporary JPEG and "
                "opens it again."
            ),
            code=(
                "import tempfile\n"
                "from pathlib import Path\n"
                "\n"
                "from computing_with_numpy.domain.images import load_face_image\n"
                "from computing_with_numpy.infrastructure.images import (\n"
                "    load_image,\n"
                "    save_image,\n"
                ")\n"
                "\n"
                "with tempfile.TemporaryDirectory() as folder:\n"
                "    path = save_image(load_face_image(), Path(folder) / 'own.jpg')\n"
                "    own = load_image(path)\n"
                "print(own.shape)"
            ),
        ),
    ]
