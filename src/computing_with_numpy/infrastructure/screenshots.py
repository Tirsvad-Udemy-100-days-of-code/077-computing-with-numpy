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
MIN_WIDTH = 4.0
# Inches per character of 10 pt monospace text (about 6.0 pt) plus headroom.
CHAR_WIDTH = 0.092
MARGIN = 0.25


def render_text_screenshot(title: str, lines: tuple[str, ...], path: Path) -> Path:
    """Draw a terminal-like screenshot of ``lines`` under ``title`` into ``path``."""
    height = max(MIN_HEIGHT, LINE_HEIGHT * (len(lines) + 2))
    longest = max([len(title), *(len(line) for line in lines)])
    width = max(MIN_WIDTH, longest * CHAR_WIDTH + 2 * MARGIN)
    figure = Figure(figsize=(width, height), dpi=100, facecolor=BACKGROUND)
    FigureCanvasAgg(figure)
    axes = figure.add_axes((0, 0, 1, 1))
    axes.set_axis_off()
    axes.set_xlim(0, 1)
    axes.set_ylim(0, 1)
    left = MARGIN / width
    axes.text(
        left,
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
            left,
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
