"""Read and write picture files with Pillow."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from numpy.typing import ArrayLike, NDArray
from PIL import Image

from computing_with_numpy.infrastructure.screenshots import save_array_screenshot

GRAY_TITLE = "Grayscale image"


def load_image(path: Path) -> NDArray[np.uint8]:
    """Open a picture file as a (height, width, 3) ``uint8`` array."""
    with Image.open(path) as picture:
        return np.asarray(picture.convert("RGB"), dtype=np.uint8)


def save_image(img: NDArray[np.uint8], path: Path) -> Path:
    """Write a (height, width, 3) array to ``path``; the suffix picks the format."""
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(img, mode="RGB").save(path)
    return path


def save_gray_image(img_gray: ArrayLike, path: Path) -> Path:
    """Save a 2-D grayscale array rendered with the ``gray`` colour map."""
    return save_array_screenshot(img_gray, GRAY_TITLE, path, cmap="gray")
