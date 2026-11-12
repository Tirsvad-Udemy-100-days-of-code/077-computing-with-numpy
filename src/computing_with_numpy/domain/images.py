"""Lecture part 4: images as ndarrays (grayscale, flip, rotate, invert)."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

IMAGE_HEIGHT = 768
IMAGE_WIDTH = 1024
CHANNELS = 3
MAX_PIXEL = 255
# Luminance weights of red, green and blue (ITU-R BT.709) for grayscale.
GREY_VALUES = [0.2126, 0.7152, 0.0722]

SKY_TOP = (30, 90, 200)
SKY_BOTTOM = (170, 210, 250)
HORIZON_ROW = 480
GRASS = (40, 150, 60)
SOIL = (120, 80, 40)
SOIL_ROW = 640
SUN_CENTER = (150, 800)
SUN_RADIUS = 80
SUN_COLOR = (255, 220, 40)
HOUSE_ROWS = (330, HORIZON_ROW)
HOUSE_COLUMNS = (150, 330)
HOUSE_COLOR = (190, 40, 40)
ROOF_COLOR = (60, 30, 20)
TREE_TRUNK_ROWS = (380, HORIZON_ROW)
TREE_TRUNK_COLUMNS = (500, 530)
TREE_TRUNK_COLOR = (90, 55, 25)
TREE_CENTER = (330, 515)
TREE_RADIUS = 70
TREE_COLOR = (10, 90, 30)


@dataclass(frozen=True, slots=True)
class ImageDescription:
    """The facts the lecture prints about an image."""

    dtype: str
    shape: tuple[int, ...]
    ndim: int
    width: int
    height: int


def _blend(
    top: tuple[int, int, int], bottom: tuple[int, int, int]
) -> NDArray[np.uint8]:
    """Return a vertical gradient from ``top`` to ``bottom`` for the sky rows."""
    weight = np.linspace(0.0, 1.0, HORIZON_ROW)[:, None, None]
    gradient = (1 - weight) * np.array(top) + weight * np.array(bottom)
    return np.broadcast_to(gradient, (HORIZON_ROW, IMAGE_WIDTH, CHANNELS)).astype(
        np.uint8
    )


def load_face_image() -> NDArray[np.uint8]:
    """Return the lesson picture, a generated (768, 1024, 3) ``uint8`` scene.

    It stands in for the lecture's raccoon picture (ADR-0001): a sky gradient,
    a sun, a house, a tree and ground bands, so no part is symmetric and a flip,
    a rotation and an inversion each look different.
    """
    img = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH, CHANNELS), dtype=np.uint8)
    img[:HORIZON_ROW] = _blend(SKY_TOP, SKY_BOTTOM)
    img[HORIZON_ROW:SOIL_ROW] = GRASS
    img[SOIL_ROW:] = SOIL
    rows, columns = np.ogrid[:IMAGE_HEIGHT, :IMAGE_WIDTH]
    sun = (rows - SUN_CENTER[0]) ** 2 + (columns - SUN_CENTER[1]) ** 2 <= SUN_RADIUS**2
    img[sun] = SUN_COLOR
    img[HOUSE_ROWS[0] : HOUSE_ROWS[1], HOUSE_COLUMNS[0] : HOUSE_COLUMNS[1]] = (
        HOUSE_COLOR
    )
    roof = (
        (rows >= HOUSE_ROWS[0] - 90)
        & (rows < HOUSE_ROWS[0])
        & (columns - HOUSE_COLUMNS[0] >= HOUSE_ROWS[0] - rows)
        & (HOUSE_COLUMNS[1] - columns >= HOUSE_ROWS[0] - rows)
    )
    img[roof] = ROOF_COLOR
    img[
        TREE_TRUNK_ROWS[0] : TREE_TRUNK_ROWS[1],
        TREE_TRUNK_COLUMNS[0] : TREE_TRUNK_COLUMNS[1],
    ] = TREE_TRUNK_COLOR
    crown = (rows - TREE_CENTER[0]) ** 2 + (columns - TREE_CENTER[1]) ** 2 <= (
        TREE_RADIUS**2
    )
    img[crown] = TREE_COLOR
    return img


def describe_image(img: NDArray[np.uint8]) -> ImageDescription:
    """Return the dtype, shape, number of dimensions and resolution of ``img``."""
    height, width = img.shape[:2]
    return ImageDescription(
        dtype=str(img.dtype),
        shape=img.shape,
        ndim=img.ndim,
        width=width,
        height=height,
    )


def to_grayscale(img: NDArray[np.uint8]) -> NDArray[np.float64]:
    """Return a 2-D grayscale of ``img`` with values from 0 to 1.

    The sRGB values are divided by 255, then the matrix product with the grey
    values weighs red, green and blue into one channel.
    """
    gray: NDArray[np.float64] = (img / MAX_PIXEL) @ np.array(GREY_VALUES)
    return gray


def flip_image(img: NDArray[np.generic]) -> NDArray[np.generic]:
    """Return ``img`` turned upside down with ``np.flip``."""
    return np.flip(img)


def rotate_image(img: NDArray[np.generic]) -> NDArray[np.generic]:
    """Return ``img`` rotated 90 degrees with ``np.rot90``."""
    return np.rot90(img)


def invert_image(img: NDArray[np.uint8]) -> NDArray[np.uint8]:
    """Return ``255 - img``, the solarized (inverted) picture."""
    return MAX_PIXEL - img
