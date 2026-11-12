"""Check a flat, three-language wiki folder against framework/process/wiki.md."""

from __future__ import annotations

import re
from pathlib import Path

ENGLISH = ""
TRANSLATION_SUFFIXES = ("-da", "-ms")
SPECIAL_PAGES = ("_Sidebar", "_Footer")
SIDEBAR = "_Sidebar"
LANGUAGES_HEADING = "**Languages**"
STEP_PREFIX = "Step-"
IMAGES_FOLDER = "docs/images"
PAGE_SUFFIX = ".md"

_LINK = re.compile(r"\]\(([^)\s]+)\)")
_IMAGE_URL = re.compile(r"/" + re.escape(IMAGES_FOLDER) + r"/([\w.-]+\.png)")
_HEADING = re.compile(r"^\*\*[^*]+\*\*\s*$")


def _stems(wiki: Path) -> list[str]:
    """Return the sorted page names (file names without .md) in the folder."""
    return sorted(p.name[: -len(PAGE_SUFFIX)] for p in wiki.glob("*" + PAGE_SUFFIX))


def _suffix_of(stem: str) -> str:
    """Return the language suffix of a page name, or ENGLISH when it has none."""
    for suffix in TRANSLATION_SUFFIXES:
        if stem.endswith(suffix):
            return suffix
    return ENGLISH


def _english_pages(stems: list[str]) -> list[str]:
    return [s for s in stems if _suffix_of(s) == ENGLISH and s not in SPECIAL_PAGES]


def _base_name(stem: str) -> str:
    suffix = _suffix_of(stem)
    return stem[: len(stem) - len(suffix)]


def _read(wiki: Path, stem: str) -> str:
    return (wiki / (stem + PAGE_SUFFIX)).read_text(encoding="utf-8")


def check_twins(wiki: Path) -> list[str]:
    """Every English page has a twin per language and no twin is orphaned."""
    stems = set(_stems(wiki))
    problems: list[str] = []
    for page in _english_pages(sorted(stems)):
        problems.extend(
            f"{page + suffix}.md is missing (twin of {page}.md)"
            for suffix in TRANSLATION_SUFFIXES
            if page + suffix not in stems
        )
    for stem in sorted(stems):
        if _suffix_of(stem) != ENGLISH and _base_name(stem) not in stems:
            problems.append(f"{stem}.md has no English page {_base_name(stem)}.md")
    return problems


def _first_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line
    return ""


def check_language_lines(wiki: Path) -> list[str]:
    """Every page starts with links to the other two languages."""
    problems: list[str] = []
    for stem in _stems(wiki):
        if stem in SPECIAL_PAGES:
            continue
        base = _base_name(stem)
        own = _suffix_of(stem)
        expected = {
            base + suffix
            for suffix in (ENGLISH, *TRANSLATION_SUFFIXES)
            if suffix != own
        }
        found = set(_LINK.findall(_first_line(_read(wiki, stem))))
        problems.extend(
            f"{stem}.md: language line does not link to {target}"
            for target in sorted(expected - found)
        )
    return problems


def check_step_images(wiki: Path, images: Path) -> list[str]:
    """Every Step page references a screenshot and each one exists."""
    problems: list[str] = []
    for stem in _stems(wiki):
        if not stem.startswith(STEP_PREFIX):
            continue
        names = _IMAGE_URL.findall(_read(wiki, stem))
        if not names:
            problems.append(f"{stem}.md references no image under {IMAGES_FOLDER}")
        problems.extend(
            f"{stem}.md: image {name} is not in {IMAGES_FOLDER}"
            for name in sorted(set(names))
            if not (images / name).is_file()
        )
    return problems


def _sidebar_links(text: str) -> list[str]:
    return _LINK.findall(text)


def _languages_is_last(text: str) -> bool:
    headings = [ln.strip() for ln in text.splitlines() if _HEADING.match(ln.strip())]
    return bool(headings) and headings[-1] == LANGUAGES_HEADING


def check_sidebar(wiki: Path) -> list[str]:
    """Check the sidebar lists every English page and ends with Languages."""
    path = wiki / (SIDEBAR + PAGE_SUFFIX)
    if not path.is_file():
        return [f"{SIDEBAR}.md does not exist"]
    text = path.read_text(encoding="utf-8")
    stems = _stems(wiki)
    links = set(_sidebar_links(text))
    problems = [
        f"{SIDEBAR}.md does not link {page}"
        for page in _english_pages(stems)
        if page not in links
    ]
    problems.extend(
        f"{SIDEBAR}.md links {target}, which does not exist"
        for target in sorted(links - set(stems))
    )
    if not _languages_is_last(text):
        problems.append(f"{SIDEBAR}.md must end with the {LANGUAGES_HEADING} section")
    return problems


def check_flat(wiki: Path) -> list[str]:
    """Report any subfolder, because the wiki folder must be flat."""
    return [
        f"{p.name} is a subfolder; the wiki must be flat"
        for p in sorted(wiki.iterdir())
        if p.is_dir()
    ]


def check_wiki(wiki: Path, images: Path) -> list[str]:
    """Run every wiki check and return the problems found."""
    if not wiki.is_dir():
        return [f"wiki folder {wiki} does not exist"]
    return [
        *check_twins(wiki),
        *check_language_lines(wiki),
        *check_step_images(wiki, images),
        *check_sidebar(wiki),
        *check_flat(wiki),
    ]
