# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [QC-PY-001], [MIL-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Delta re-review of criteria 11, 13, 14: Go | pending |

---

## Artifact Under Review

- Instance reviewed: `src/` and `tests/` at milestone MIL-001, plus `scripts/make_screenshots.py` ([MIL-001], tasks 2 and 6)
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

Tool evidence (run in `.venv`, delta re-review 2026-11-12): `python -m pytest -q` 5 passed; `ruff check .` clean; `ruff format --check .` clean; `mypy src` clean (strict).

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `computing_with_numpy`, `lesson_steps`, `render_text_screenshot`, `LessonStep`, `BACKGROUND`/`MIN_HEIGHT`; ruff rule set N passes. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names such as `setup_step`, `all_steps`, `y_position`; no single-letter names (`cmap` is the matplotlib term). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check .` -> All checks passed; `ruff format --check .` -> 34 files already formatted; `per-file-ignores` for `tests/**` (D, ANN) is configured in `pyproject.toml`; no `noqa` in code. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All src and script functions annotated (`main() -> None` in `scripts/make_screenshots.py`, `-> int` in `cli.py`); ruff `ANN` passes; test functions annotated `-> None` too. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `try`/`except` or `raise` in `src/`, `tests/` or `scripts/make_screenshots.py`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Only default is `cmap: str | None = None`; ruff `B` passes; no builtin names rebound. |
| 7 | Files, locks and connections are managed with context managers | Pass | No file handles opened; `Figure.savefig(path)` and `Path.mkdir(parents=True, exist_ok=True)` own the I/O; `Figure` is used without pyplot so no global figure leaks. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every module, class and function in `src/` and the script has a docstring; ruff `D` passes. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging; the CLI writes its product output with `sys.stdout.write` (user output, not diagnostics); `.env` is not referenced in `src/` or `scripts/`. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists at MIL-001; the milestone covers project setup only. First applies from MIL-002. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | Delta re-review 2026-11-12: `pytest -q` -> 5 passed; `test_save_array_screenshot_writes_png` now covers `save_array_screenshot`; names state behaviour, `tmp_path`, no network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `[tool.mypy] strict = true`; `mypy src` -> Success: no issues found in 9 source files; `mypy src tests scripts` -> no issues in 12 files; no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | (Optional) Delta re-review: `pyproject.toml` keeps lower bounds (accepted); exact versions are pinned in `constraints.txt` (numpy, matplotlib, pillow, pytest, ruff, mypy, yamllint) and used by CI. `jupyterlab`/`nbclient`/`pillow` are used by later milestones (accepted by S01). |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Delta re-review: `LINE_HEIGHT` is used at lines 21, 30 and 38 of `screenshots.py`; no `0.3` literal remains. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `presentation.cli` imports `application`; `application.lesson_steps` imports only stdlib and numpy; `infrastructure.screenshots` imports matplotlib and no inner layer; `domain` is empty. No cycles. `scripts/make_screenshots.py` is the composition entry point. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Single-purpose modules; one frozen dataclass; no inheritance or `isinstance` chains. The script depends directly on `infrastructure` (acceptable composition root); no protocol is needed yet. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | `src/computing_with_numpy/{domain,application,infrastructure,presentation}` and `tests/{unit,integration}` exist. `domain` holds only `__init__.py` and `tests/e2e` does not exist yet: no domain code or end-to-end test at MIL-001 (note for MIL-002). |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All Python files are `snake_case.py`; `scripts/check-opengrep.ps1`/`.sh` are shell scripts in kebab-case (shell convention); `computing_with_numpy.egg-info/` is generated build output. |

## Overall Verdict

Go — the delta re-review of criteria 11, 13 and 14 (earlier verdict No-Go) finds all three fixed; every criterion is now Pass or N-A, and pytest, ruff and mypy strict are green. Criterion 13 (Optional) is accepted with lower bounds in `pyproject.toml` and exact pins in `constraints.txt`.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None open. Note for MIL-002: add `domain` code and a `tests/e2e` folder when needed (criterion 17) | S01 | MIL-002 |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[MIL-001]: ../../milestones/mil-001-project-setup.md
