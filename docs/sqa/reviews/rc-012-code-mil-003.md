# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [QC-PY-001], [MIL-003] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [b8e25e0] |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Delta re-review of criterion 14: Go | [b8e25e0] |

---

## Artifact Under Review

- Instance reviewed: the code added at milestone MIL-003 ([MIL-003], tasks 1 to 5): `src/computing_with_numpy/domain/generating.py`, `application/steps_generating.py`, `application/lesson.py`, `infrastructure/screenshots.py` (`plot_line`, `save_noise_image`) and the new and touched tests under `tests/`
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review, then delta re-review of criterion 14 on 2026-11-12 (earlier verdict No-Go)
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

Tool evidence (run in `.venv`, delta re-review 2026-11-12): `python -m pytest -q` 50 passed, 1 warning; `ruff check .` clean; `ruff format --check .` clean (51 files); `mypy src tests scripts` clean (strict, 27 files); `bash scripts/check-opengrep.sh` -> opengrep: no findings.

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `generating`, `steps_generating`, `create_range_vector`, `RANGE_START`, `CUBE_SHAPE`, `NOTEBOOK_SEED`, `LINE_TITLE`; ruff `N` passes. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Function names mirror the lecture challenges (`last_three`, `fourth_to_sixth`, `nonzero_indices`). The parameter `a` in the one-line slicing functions and `x`/`y` in `plot_line` are tiny scopes and the lecture's own names. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check .` -> All checks passed; `ruff format --check .` -> 51 files already formatted; no `noqa`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All functions in `generating.py`, `steps_generating.py`, `screenshots.py` and the new tests are annotated; ruff `ANN` passes. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `try`/`except` or `raise` in the reviewed files. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Defaults are `None` (`seed`) only; ruff `B` passes; no builtin rebound. |
| 7 | Files, locks and connections are managed with context managers | Pass | No handles opened; `Figure.savefig(path)` writes the file; figures are built with `Figure`, not pyplot, so none stay open. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public function in `generating.py`, `steps_generating.py`, `plot_line` and `save_noise_image` has a docstring; ruff `D` passes. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` or logging in Python code (`print(` appears only inside the lesson-code strings run in the notebook); no secrets. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists. Functions trace to the tasks of [MIL-003] (tasks 1 to 4: all named functions exist, plus `reverse_array_with_flip`, which the task text asks for as the `np.flip` variant). Deviation to record in the milestone: the module is `computing_with_numpy.domain.generating`, not `computing_with_numpy.generating` as the Deliverable says. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `pytest -q` -> 50 passed, 1 warning (zmq Proactor event-loop on Windows, harmless). `tests/unit/test_generating.py` covers every domain function with the lecture's values (10 to 29, [27, 28, 29], [13, 14, 15], 22 to 29, every second, reverse and flip, `(array([0, 2, 5]),)`, cube shape and range, seeded repeat, linspace values and bounds, noise shape); `tests/integration/test_screenshots.py` covers `plot_line` and `save_noise_image` (PNG signature); `tests/integration/test_figure_screenshots.py` shows the notebook cells 10 and 11 display a PNG and the screenshot bytes equal the cell figure; `test_lesson_steps.py` covers the eight challenge steps and unique slugs. Names state behaviour; seeds fixed; `tmp_path`; no network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | (Optional) `mypy src tests scripts` -> Success: no issues found in 27 source files (strict). |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | (Optional) No new dependency in MIL-003; matplotlib and numpy are declared and pinned in `constraints.txt`. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Delta re-review 2026-11-12: `FIGURE_SIZE`, `FIGURE_DPI`, `_new_figure()` and `_save_figure()` in `infrastructure/screenshots.py` are used by `render_text_screenshot`, `save_array_screenshot` and `plot_line`; no repeated figure literals remain. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain/generating.py` imports only numpy; `application/steps_generating.py` imports only `lesson_step`; `lesson.py` imports the three step modules at top level; `infrastructure/screenshots.py` imports matplotlib and no project module. No cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One module per lecture part; the new part was added by a new `steps_generating.py` and one line in `all_steps()`; no inheritance or `isinstance` chains. Note: `plot_line` and `save_noise_image` are not called by the notebook or scripts (the notebook shows the figures with pyplot), so they are exercised only by tests; they are required by [MIL-003] tasks 3 and 4. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure, in `snake_case`, and imports between the layers point inward | Pass | `domain/generating.py`, `application/steps_generating.py` and `application/lesson.py`, `infrastructure/screenshots.py`; `tests/unit` and `tests/integration`; `tests/e2e` not needed yet. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | `generating.py`, `steps_generating.py`, `test_generating.py`, `test_figure_screenshots.py` are snake_case; images `04-arange.png` to `11-noise-image.png` use letters, digits and `-`. |

## Overall Verdict

Go — the delta re-review finds criterion 14 fixed (figure format defined once); every criterion is Pass or N-A and pytest, ruff, mypy strict and opengrep are green.

Milestone Go/No-Go table of [MIL-003], row by row: 1 `create_range_vector()` returns 10 to 29: Go (`test_create_range_vector_returns_10_to_29` passes); 2 slicing returns the last 3, the 4th to 6th, all but the first 12 and every second value: Go (four tests pass); 3 `reverse_array` and `nonzero_indices` give the stated results and `random_cube` has shape (3, 3, 3): Go (tests pass, including the flip variant); 4 `linspace_x` and `linspace_y` have size 9 with bounds 0 to 100 and -3 to 3, and the chart and a 128x128x3 noise image are saved without a GUI: Go (linspace tests; `test_plot_line_*` and `test_save_noise_image_*` write PNG files through the Agg canvas; notebook figure cells verified); 5 screenshots for every challenge in the README: Go (`docs/images/04-arange.png` to `11-noise-image.png` exist, all eight are referenced in `README.md` lines 126 to 140). The images are the real notebook output: the executed `notebooks/computing_with_numpy.ipynb` holds the same stdout for cells 04 to 09, and cells 10 and 11 hold a PNG display output; `test_figure_screenshots_are_the_cells_figures` asserts the two figure screenshots are byte-identical to those cell figures, and the text screenshots (checked 05-slicing, 10-linspace-plot) show the cell code with its output. All five milestone criteria are Go. The milestone Deliverable now names `computing_with_numpy.domain.generating`, matching the code.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None open | S01 | n/a |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[MIL-003]: ../../milestones/mil-003-generating-ndarrays.md
[b8e25e0]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/commit/b8e25e06565206dd9fcc052d67826da3d186774e
