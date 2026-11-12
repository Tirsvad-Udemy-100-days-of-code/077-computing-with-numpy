# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-017 |
| CrossReference | [QC-PY-001], [MIL-006] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the code added at milestone MIL-006 ([MIL-006], task 4): `src/computing_with_numpy/infrastructure/wiki_check.py`, `scripts/check_wiki.py` and `tests/unit/test_wiki_check.py`
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

Tool evidence (run in `.venv`): `python -m pytest -q` 93 passed, 1 warning; `ruff check .` clean; `ruff format --check .` clean (90 files); `mypy src tests scripts` clean (strict, 38 files); `bash scripts/check-opengrep.sh` -> opengrep: no findings; `python scripts/check_wiki.py` -> exit 0 on the real wiki.

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `wiki_check`, `check_twins`, `_english_pages`, `TRANSLATION_SUFFIXES`, `LANGUAGES_HEADING`; ruff `N` passes. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | `check_language_lines`, `check_step_images`, `check_flat` state purpose. `p`, `s` and `ln` appear only in one-line comprehensions (tiny scopes). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check .` -> All checks passed; `ruff format --check .` -> 90 files already formatted; no `noqa` or `type: ignore` in the reviewed files. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All functions annotated, including the private helpers and all 16 test functions (`-> None`); ruff `ANN` passes. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `try`/`except`; problems are returned as strings, not raised; an unreadable folder raises the standard `OSError` unchanged. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No default arguments; ruff `B` passes; no builtin rebound. |
| 7 | Files, locks and connections are managed with context managers | Pass | Files are read with `Path.read_text(encoding="utf-8")`, which closes the file; no handle is held. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | (Optional) The module, `check_twins`, `check_language_lines`, `check_step_images`, `check_sidebar`, `check_flat`, `check_wiki` and `scripts/check_wiki.py` `main` have docstrings; private helpers (`_stems`, `_read`, ...) have none, as ruff `D` allows. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` or logging; the script writes the problems with `sys.stdout.write`, which is its product output; no secrets. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists. The code traces to task 4 of [MIL-006] (`scripts/check_wiki.py` checks that every Step page references an existing screenshot in each language) and Go/No-Go rows 1 to 3; the checks also cover twins, language lines, sidebar and flatness, as `framework/process/wiki.md` and QC-WIKI-001 require. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `pytest -q` -> 93 passed, 1 warning (zmq Proactor event-loop on Windows, harmless); `tests/unit/test_wiki_check.py` -> 16 passed. It builds fake wikis in `tmp_path` and covers: a good wiki gives no problems, missing folder, missing translation, orphan translation, missing language link, blank lines before the language line, page without image, missing image file, non-Step pages ignored, missing sidebar, unlinked English page, link to a missing page, `Languages` not last (two cases), subfolder, flat wiki. Names state behaviour; no network; the real wiki is checked by running the script (exit 0). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | (Optional) `mypy src tests scripts` -> Success: no issues found in 38 source files (strict); no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | (Optional) Standard library only (`re`, `pathlib`, `sys`); no new dependency. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Language suffixes, special pages, the sidebar name, the `**Languages**` heading, the `Step-` prefix, the images folder and the page suffix are single constants; `_stems`, `_suffix_of`, `_base_name`, `_read` are shared by all checks. The script's `IMAGES = ROOT / "docs" / "images"` and the module's `IMAGES_FOLDER = "docs/images"` name the same folder, but one is the file system path and the other the URL pattern in the page text, so they are not merged; a note, not a Fail. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `infrastructure/wiki_check.py` imports only the standard library; `scripts/check_wiki.py` imports it; no cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One function per rule, each returning a list of problems; `check_wiki` composes them, so a new rule is one new function and one line; no inheritance or `isinstance` chains. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure, in `snake_case`, and imports between the layers point inward | Pass | The file-reading checker is in `infrastructure/`; the script is in `scripts/`; the test is in `tests/unit/` (it uses `tmp_path`; this project keeps such tests in `unit/`, as earlier records accepted). `tests/e2e` not needed. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | `wiki_check.py`, `check_wiki.py`, `test_wiki_check.py` are snake_case. The wiki file names use hyphens and capitals as Gitea page names (wiki rule), not Python files. |

## Overall Verdict

Go — every criterion is Pass or N-A, and pytest, ruff, mypy strict and opengrep are green. No blocking finding and no suggestion that needs action.

Milestone Go/No-Go table of [MIL-006], rows touched by this review: 2 every Step page references at least one screenshot file that exists, checked by `scripts/check_wiki.py`: Go (the script exits 0 on the real wiki; `test_check_step_images_reports_page_without_image` and `test_check_step_images_reports_missing_file` prove it fails when an image is absent); 5 all tests pass and opengrep reports 0 findings: Go (93 passed; opengrep: no findings). Rows 1, 3 and 4 are judged in [RC-016]; row 6 (tag v1.0.0) cannot be verified before the release.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None open | S01 | n/a |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[MIL-006]: ../../milestones/mil-006-wiki-and-release.md
[RC-016]: ./rc-016-wiki-mil-006.md
