"""Render lesson output as PNG screenshots without opening a window."""

from __future__ import annotations

from pathlib import Path

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from numpy.typing import ArrayLike

BACKGROUND = "#1e1e1e"
FOREGROUND = "#d4d4d4"
ACCENT = "#4ec9b0"
LINE_HEIGHT = 0.3
MIN_HEIGHT = 1.4
WIDTH = 9.0


def render_text_screenshot(title: str, lines: tuple[str, ...], path: Path) -> Path:
    """Draw a terminal-like screenshot of ``lines`` under ``title`` into ``path``."""
    height = max(MIN_HEIGHT, LINE_HEIGHT * (len(lines) + 2))
    figure = Figure(figsize=(WIDTH, height), dpi=100, facecolor=BACKGROUND)
    FigureCanvasAgg(figure)
    axes = figure.add_axes((0, 0, 1, 1))
    axes.set_axis_off()
    axes.set_xlim(0, 1)
    axes.set_ylim(0, 1)
    axes.text(
        0.02,
        1 - LINE_HEIGHT / height,
        title,
        color=ACCENT,
        fontsize=11,
        fontweight="bold",
        va="top",
    )
    for index, line in enumerate(lines):
        y_position = 1 - (LINE_HEIGHT * (index + 2)) / height
        axes.text(
            0.02,
            y_position,
            line,
            color=FOREGROUND,
            fontsize=10,
            family="monospace",
            va="top",
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(path, facecolor=BACKGROUND)
    return path


def save_array_screenshot(
    array: ArrayLike, title: str, path: Path, *, cmap: str | None = None
) -> Path:
    """Draw an image-like array with ``imshow`` into ``path``."""
    figure = Figure(figsize=(6, 4.5), dpi=100)
    FigureCanvasAgg(figure)
    axes = figure.add_subplot(1, 1, 1)
    axes.imshow(array, cmap=cmap)
    axes.set_title(title)
    axes.set_axis_off()
    path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(path)
    return path
