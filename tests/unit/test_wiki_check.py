"""Tests for the wiki checks, on small fake wikis built in tmp_path."""

from __future__ import annotations

from pathlib import Path

import pytest

from computing_with_numpy.infrastructure.wiki_check import (
    check_flat,
    check_language_lines,
    check_sidebar,
    check_step_images,
    check_twins,
    check_wiki,
)

URL = "https://host/x/raw/branch/main/docs/images/{}.png"
SIDEBAR = (
    "**Wiki**\n\n- [Home](Home)\n- [Step-1](Step-1)\n\n"
    "**Languages**\n\n- English: [Home](Home)\n"
)


def _language_line(base: str, own: str) -> str:
    links = {
        "": f"[English]({base})",
        "-da": f"[Dansk]({base}-da)",
        "-ms": f"[Melayu]({base}-ms)",
    }
    return " · ".join(v for k, v in links.items() if k != own) + "\n\n"


def _good_wiki(tmp_path: Path) -> tuple[Path, Path]:
    wiki = tmp_path / "wiki"
    images = tmp_path / "images"
    wiki.mkdir()
    images.mkdir()
    (images / "a.png").write_bytes(b"png")
    for base in ("Home", "Step-1"):
        for suffix in ("", "-da", "-ms"):
            body = _language_line(base, suffix)
            if base == "Step-1":
                body += f"![x]({URL.format('a')})\n"
            (wiki / f"{base}{suffix}.md").write_text(body, encoding="utf-8")
    (wiki / "_Sidebar.md").write_text(SIDEBAR, encoding="utf-8")
    return wiki, images


def test_check_wiki_accepts_good_wiki(tmp_path: Path) -> None:
    wiki, images = _good_wiki(tmp_path)
    assert check_wiki(wiki, images) == []


def test_check_wiki_reports_missing_folder(tmp_path: Path) -> None:
    assert len(check_wiki(tmp_path / "none", tmp_path)) == 1


def test_check_twins_reports_missing_translation(tmp_path: Path) -> None:
    wiki, _ = _good_wiki(tmp_path)
    (wiki / "Home-ms.md").unlink()
    assert check_twins(wiki) == ["Home-ms.md is missing (twin of Home.md)"]


def test_check_twins_reports_orphan_translation(tmp_path: Path) -> None:
    wiki, _ = _good_wiki(tmp_path)
    (wiki / "Extra-da.md").write_text("x", encoding="utf-8")
    problems = check_twins(wiki)
    assert problems == ["Extra-da.md has no English page Extra.md"]


def test_check_language_lines_reports_missing_link(tmp_path: Path) -> None:
    wiki, _ = _good_wiki(tmp_path)
    (wiki / "Home-da.md").write_text("**Dansk**\n", encoding="utf-8")
    problems = check_language_lines(wiki)
    assert problems == [
        "Home-da.md: language line does not link to Home",
        "Home-da.md: language line does not link to Home-ms",
    ]


def test_check_language_lines_skips_blank_lines_before(tmp_path: Path) -> None:
    wiki, images = _good_wiki(tmp_path)
    page = wiki / "Home.md"
    page.write_text("\n" + page.read_text(encoding="utf-8"), encoding="utf-8")
    assert check_wiki(wiki, images) == []


def test_check_step_images_reports_page_without_image(tmp_path: Path) -> None:
    wiki, images = _good_wiki(tmp_path)
    (wiki / "Step-1-da.md").write_text(
        _language_line("Step-1", "-da"), encoding="utf-8"
    )
    assert check_step_images(wiki, images) == [
        "Step-1-da.md references no image under docs/images"
    ]


def test_check_step_images_reports_missing_file(tmp_path: Path) -> None:
    wiki, images = _good_wiki(tmp_path)
    (images / "a.png").unlink()
    problems = check_step_images(wiki, images)
    assert len(problems) == 3
    assert "image a.png is not in docs/images" in problems[0]


def test_check_step_images_ignores_non_step_pages(tmp_path: Path) -> None:
    wiki, images = _good_wiki(tmp_path)
    assert not any(p.startswith("Home") for p in check_step_images(wiki, images))


def test_check_sidebar_reports_missing_file(tmp_path: Path) -> None:
    wiki, _ = _good_wiki(tmp_path)
    (wiki / "_Sidebar.md").unlink()
    assert check_sidebar(wiki) == ["_Sidebar.md does not exist"]


def test_check_sidebar_reports_unlinked_english_page(tmp_path: Path) -> None:
    wiki, _ = _good_wiki(tmp_path)
    (wiki / "_Sidebar.md").write_text(
        SIDEBAR.replace("- [Step-1](Step-1)\n", ""), encoding="utf-8"
    )
    assert check_sidebar(wiki) == ["_Sidebar.md does not link Step-1"]


def test_check_sidebar_reports_link_to_missing_page(tmp_path: Path) -> None:
    wiki, _ = _good_wiki(tmp_path)
    (wiki / "_Sidebar.md").write_text(
        SIDEBAR.replace("- English", "- [Gone](Gone)\n- English"), encoding="utf-8"
    )
    assert check_sidebar(wiki) == ["_Sidebar.md links Gone, which does not exist"]


@pytest.mark.parametrize(
    "text",
    [
        "**Wiki**\n\n- [Home](Home)\n- [Step-1](Step-1)\n",
        SIDEBAR + "\n**Related**\n\n- [Home](Home)\n",
    ],
)
def test_check_sidebar_reports_languages_not_last(tmp_path: Path, text: str) -> None:
    wiki, _ = _good_wiki(tmp_path)
    (wiki / "_Sidebar.md").write_text(text, encoding="utf-8")
    assert any("Languages" in p for p in check_sidebar(wiki))


def test_check_flat_reports_subfolder(tmp_path: Path) -> None:
    wiki, _ = _good_wiki(tmp_path)
    (wiki / "en").mkdir()
    assert check_flat(wiki) == ["en is a subfolder; the wiki must be flat"]


def test_check_flat_accepts_flat_wiki(tmp_path: Path) -> None:
    wiki, _ = _good_wiki(tmp_path)
    assert check_flat(wiki) == []
