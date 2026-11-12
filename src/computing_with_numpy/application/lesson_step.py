"""The lesson step value object."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LessonStep:
    """One lecture step: file-name slug, title, explanation and notebook code."""

    slug: str
    title: str
    explanation: str
    code: str
