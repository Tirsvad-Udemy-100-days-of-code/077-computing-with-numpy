from pathlib import Path

import numpy as np

from computing_with_numpy.infrastructure.screenshots import (
    render_text_screenshot,
    save_array_screenshot,
)

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def test_render_text_screenshot_writes_png(tmp_path: Path) -> None:
    target = render_text_screenshot(
        "Title", ("line one", "line two"), tmp_path / "a.png"
    )
    assert target.read_bytes().startswith(PNG_SIGNATURE)


def test_save_array_screenshot_writes_png(tmp_path: Path) -> None:
    image = np.zeros((4, 4, 3))
    target = save_array_screenshot(image, "Black", tmp_path / "b.png")
    assert target.read_bytes().startswith(PNG_SIGNATURE)
