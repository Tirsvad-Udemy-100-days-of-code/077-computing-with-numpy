from pathlib import Path

import numpy as np

from computing_with_numpy.domain.generating import (
    linspace_x,
    linspace_y,
    noise_image,
)
from computing_with_numpy.infrastructure.screenshots import (
    plot_line,
    render_text_screenshot,
    save_array_screenshot,
    save_noise_image,
)

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def test_render_text_screenshot_writes_png(tmp_path: Path) -> None:
    target = render_text_screenshot(
        "Title", ("line one", "line two"), tmp_path / "a.png"
    )
    assert target.read_bytes().startswith(PNG_SIGNATURE)


def test_plot_line_writes_png(tmp_path: Path) -> None:
    target = plot_line(linspace_x(), linspace_y(), tmp_path / "sub" / "line.png")
    assert target == tmp_path / "sub" / "line.png"
    assert target.read_bytes().startswith(PNG_SIGNATURE)


def test_save_noise_image_writes_png(tmp_path: Path) -> None:
    target = save_noise_image(noise_image(1), tmp_path / "noise.png")
    assert target.read_bytes().startswith(PNG_SIGNATURE)


def test_save_array_screenshot_writes_png(tmp_path: Path) -> None:
    image = np.zeros((4, 4, 3))
    target = save_array_screenshot(image, "Black", tmp_path / "b.png")
    assert target.read_bytes().startswith(PNG_SIGNATURE)
