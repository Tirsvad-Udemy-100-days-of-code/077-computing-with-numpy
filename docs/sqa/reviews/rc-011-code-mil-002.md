# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [QC-PY-001], [MIL-002] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Delta re-review of criteria 12, 14, 15: Go | pending |

---

## Artifact Under Review

- Instance reviewed: `src/` (domain, application, infrastructure, presentation), `tests/`, and `scripts/make_screenshots.py` at milestone MIL-002 ([MIL-002], tasks 1 to 3: `domain/ndarray_basics.py`, `application/{lesson,lesson_step,steps_setup,steps_basics}.py`, `infrastructure/{notebook,notebook_screenshots,screenshots}.py`, `presentation/cli.py`)
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review, then delta re-review of criteria 12, 14 and 15 on 2026-11-12 (earlier verdict No-Go)
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

Tool evidence (run in `.venv`, delta re-review 2026-11-12): `python -m pytest -q` 28 passed, 1 warning; `ruff check .` clean; `ruff format --check .` clean (46 files); `mypy src tests scripts` clean (strict, 23 files); `bash scripts/check-opengrep.sh` -> opengrep: no findings.

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `ndarray_basics`, `steps_basics`, `build_notebook`, `ArrayDescription`, `LessonStep`, `CELL_TIMEOUT_SECONDS`, `HEADING_PREFIX`; ruff `N` passes. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | `create_vector`, `matrix_row`, `mystery_value_18` mirror the lecture; no single-letter names (`cmap`, `png` are the library terms). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check .` -> All checks passed; `ruff format --check .` -> 46 files already formatted; no `noqa` in the reviewed files. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All functions annotated; ruff `ANN` passes. `build_executed_notebook` returns `NotebookNode` (fixed since the first pass). |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `try`/`except` or `raise` in the reviewed files. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; ruff `B` passes; no builtin rebound. |
| 7 | Files, locks and connections are managed with context managers | Pass | Files are written through `nbformat.write`, `Path.write_bytes`, `Figure.savefig`; the kernel lifecycle is owned by `NotebookClient.execute()`. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | All public modules, classes and functions in the scope have docstrings; ruff `D` passes. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` or logging in Python code (`print(` appears only inside the lesson-code strings run in the notebook, which is the lecture's output); the CLI uses `sys.stdout.write`; no `.env` access. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | The project has no Design Class Diagram. The functions trace to the task list of [MIL-002] (tasks 1 and 2: `create_vector`, `create_matrix`, `describe_array`, the six `mystery_*` names). Deviation to record in the milestone: the module is `computing_with_numpy.domain.ndarray_basics`, not `computing_with_numpy.ndarray_basics` as the Deliverable says. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `pytest -q` -> 28 passed, 1 warning (zmq Proactor event-loop on Windows, from the kernel client, harmless). Tests cover every `ndarray_basics` function, the CLI, notebook build/execute/write, and screenshot helpers (`cell_screenshot_lines`, text and PNG cells, skipped cells); names state behaviour; `tmp_path`; no network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | (Optional) Delta re-review: `mypy src tests scripts` -> Success: no issues found in 23 source files (strict); `build_executed_notebook` now returns `NotebookNode`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | (Optional) Lower bounds in `pyproject.toml`, exact pins in `constraints.txt` (numpy, matplotlib, pillow, pytest, ruff, mypy, yamllint, nbformat 5.11.1, nbclient 0.11.0, ipykernel 7.4.0) as accepted in RC-009. Note: `infrastructure/notebook.py` imports `nbformat` and `nbclient`, which are declared only in the `dev` extra; acceptable while the notebook builder is a development tool, to revisit if the CLI ever imports it. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Delta re-review: `NOTEBOOK_PATH` is defined once (`application/lesson.py`), used by `cli.py` and `scripts/make_screenshots.py`; `build_executed_notebook(working_dir)` lives once in `infrastructure/notebook.py`; `scripts/build_notebook.py` is deleted. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | Delta re-review: `LessonStep` is in `application/lesson_step.py`; `steps_setup.py` and `steps_basics.py` import only it; `application/lesson.py` imports the step modules at top level; no function-local imports remain. No cycle; layer direction unchanged. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Small single-purpose modules; `LessonStep` data is extended by adding a `steps_*` module; no inheritance or `isinstance` chains; `write_cell_screenshots` takes a notebook and a directory. Adding a step module still needs an edit in `all_steps()` (acceptable at this size). |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure, in `snake_case`, and imports between the layers point inward | Pass | `domain/ndarray_basics.py`, `application/`, `infrastructure/`, `presentation/cli.py`; `tests/unit` and `tests/integration` exist; `tests/e2e` not needed yet. Cycle fixed (criterion 15). |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Python files `snake_case.py`; images `00-setup.png` ... `03-mystery-array.png` and `notebooks/computing_with_numpy.ipynb` use letters, digits, `-`, `_`. |

## Overall Verdict

Go — the delta re-review finds criteria 12, 14 and 15 fixed: the import cycle is gone, the notebook path and the build chain are defined once, and mypy strict is clean on `src tests scripts`. Every criterion is Pass or N-A; pytest, ruff, mypy and opengrep are green.

Milestone Go/No-Go table of [MIL-002], judged on this evidence: 1 `mystery_array` ndim 3 and shape (3, 2, 4): Go; 2 indexing returns 18, [97, 0, 27, 18] and [[0, 4], [7, 5], [5, 97]]: Go; 3 each lecture step has a screenshot in the README: Go (`docs/images/00-setup.png` to `03-mystery-array.png` exist and are referenced); 4 ruff and opengrep 0 findings: Go. The milestone Deliverable still names the module `computing_with_numpy.ndarray_basics` while the code is `computing_with_numpy.domain.ndarray_basics`; correct the text when the milestone is closed.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Correct the module name in the Deliverable of [MIL-002] (`domain.ndarray_basics`) | S01 | 2026-11-13 |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[MIL-002]: ../../milestones/mil-002-ndarray-basics.md
