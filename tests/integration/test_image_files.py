from pathlib import Path

import numpy as np
from PIL import Image

from computing_with_numpy.domain.images import load_face_image, to_grayscale
from computing_with_numpy.infrastructure.images import (
    load_image,
    save_gray_image,
    save_image,
)

PNG_SIGNATURE = b"\x89PNG"


def test_load_image_reads_a_generated_jpeg_with_three_channels(tmp_path: Path) -> None:
    path = save_image(load_face_image(), tmp_path / "own.jpg")
    img = load_image(path)
    assert img.shape == (768, 1024, 3)
    assert img.dtype == np.uint8


def test_load_image_converts_a_grayscale_file_to_three_channels(
    tmp_path: Path,
) -> None:
    path = tmp_path / "gray.png"
    Image.fromarray(np.zeros((4, 5), dtype=np.uint8)).save(path)
    assert load_image(path).shape == (4, 5, 3)


def test_save_gray_image_writes_a_png(tmp_path: Path) -> None:
    path = save_gray_image(to_grayscale(load_face_image()), tmp_path / "gray.png")
    assert path.read_bytes().startswith(PNG_SIGNATURE)
