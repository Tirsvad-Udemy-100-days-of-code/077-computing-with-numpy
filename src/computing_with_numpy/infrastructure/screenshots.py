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
LINE_TITLE = "linspace: y against x"
NOISE_TITLE = "Noise image (128 x 128 x 3)"
FIGURE_SIZE = (6.0, 4.5)
FIGURE_DPI = 100


def _new_figure(
    size: tuple[float, float] = FIGURE_SIZE, facecolor: str | None = None
) -> Figure:
    """Return an Agg-backed figure, so no window is ever opened."""
    figure = Figure(figsize=size, dpi=FIGURE_DPI, facecolor=facecolor)
    FigureCanvasAgg(figure)
    return figure


def _save_figure(figure: Figure, path: Path, facecolor: str | None = None) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    if facecolor is None:
        figure.savefig(path)
    else:
        figure.savefig(path, facecolor=facecolor)
    return path


def render_text_screenshot(title: str, lines: tuple[str, ...], path: Path) -> Path:
    """Draw a terminal-like screenshot of ``lines`` under ``title`` into ``path``."""
    height = max(MIN_HEIGHT, LINE_HEIGHT * (len(lines) + 2))
    longest = max([len(title), *(len(line) for line in lines)])
    width = max(MIN_WIDTH, longest * CHAR_WIDTH + 2 * MARGIN)
    figure = _new_figure((width, height), facecolor=BACKGROUND)
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
    return _save_figure(figure, path, facecolor=BACKGROUND)


def save_array_screenshot(
    array: ArrayLike, title: str, path: Path, *, cmap: str | None = None
) -> Path:
    """Draw an image-like array with ``imshow`` into ``path``."""
    figure = _new_figure()
    axes = figure.add_subplot(1, 1, 1)
    axes.imshow(array, cmap=cmap)
    axes.set_title(title)
    axes.set_axis_off()
    return _save_figure(figure, path)


def plot_line(x: ArrayLike, y: ArrayLike, path: Path) -> Path:
    """Save a line chart of ``y`` against ``x`` as a PNG and return ``path``."""
    figure = _new_figure()
    axes = figure.add_subplot(1, 1, 1)
    axes.plot(x, y)
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    axes.set_title(LINE_TITLE)
    return _save_figure(figure, path)


def save_noise_image(image: ArrayLike, path: Path) -> Path:
    """Save an RGB noise image rendered with ``imshow`` as a PNG; return ``path``."""
    return save_array_screenshot(image, NOISE_TITLE, path)
