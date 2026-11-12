# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [QC-PY-001], [MIL-005], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [64a7682] |

---

## Artifact Under Review

- Instance reviewed: the code added at milestone MIL-005, tasks 2 to 5 ([MIL-005]; task 1 is [ADR-0001]): `src/computing_with_numpy/domain/images.py`, `infrastructure/images.py`, `application/steps_images.py`, `application/lesson.py`, `tests/unit/test_images.py`, `tests/integration/test_image_files.py` and `tests/unit/test_lesson_steps.py`
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

Tool evidence (run in `.venv`): `python -m pytest -q` 77 passed, 1 warning; `ruff check .` clean; `ruff format --check .` clean (63 files); `mypy src tests scripts` clean (strict, 35 files); `bash scripts/check-opengrep.sh` -> opengrep: no findings.

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `images`, `steps_images`, `load_face_image`, `ImageDescription`, `GREY_VALUES`, `HORIZON_ROW`; ruff `N` passes. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | `img`, `img_gray`, `to_grayscale`, `rotate_image` follow the lecture's names; `GREY_VALUES` carries a comment naming the BT.709 weights. No single-letter names. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check .` -> All checks passed; `ruff format --check .` -> 63 files already formatted; no `noqa` or `type: ignore` in the reviewed files. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All functions in the reviewed source and tests are annotated (including the test helper `_tiny() -> NDArray[np.uint8]`); ruff `ANN` passes. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `try`/`except` or `raise` in the reviewed Python files. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No defaults; ruff `B` passes. The module-level list `GREY_VALUES` is read only (wrapped in `np.array`). |
| 7 | Files, locks and connections are managed with context managers | Pass | `load_image` opens the file with `with Image.open(path) as picture`; the lesson code of step 22 uses `with tempfile.TemporaryDirectory()`; `save_image` uses `Image.save(path)`, which closes its file. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public module, class and function has a docstring; ruff `D` passes. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` or logging in Python code (only in lesson-code strings run in the notebook); no secrets. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists. Functions trace to the tasks of [MIL-005]: task 2 `load_face_image`, `load_image`, `describe_image`; task 3 `to_grayscale` and `save_gray_image`; task 4 `flip_image`, `rotate_image`, `invert_image`; the generated scene follows [ADR-0001]. Deviation to record: task 3 names `show_gray`, the code has `save_gray_image` in `infrastructure/images.py` (it saves, it does not show), and `save_image` is added for the own-image step. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `pytest -q` -> 77 passed, 1 warning (zmq Proactor event-loop on Windows, harmless). `tests/unit/test_images.py` (12 tests): uint8, shape (768, 1024, 3), 3 dims, deterministic scene, `ImageDescription`, grayscale 2D in 0 to 1, equals `np.matmul(img / 255, GREY_VALUES)`, white pixel is 1.0, flip, rotate and invert on tiny arrays and the full picture, double inversion is identity. `tests/integration/test_image_files.py`: generated JPEG round-trip with shape and dtype, grayscale file converted to 3 channels, gray PNG written. `test_lesson_steps.py` checks slugs 16 to 22 in order; `test_notebook_execution` runs every step with no error. Suggestion, not a Fail: `test_figure_screenshots.py` still lists only slugs 10 and 11, so the figure cells 17 to 21 are not asserted to display a PNG (checked by hand below). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | (Optional) `mypy src tests scripts` -> Success: no issues found in 35 source files (strict); no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | (Optional) Pillow (declared runtime dependency, `pillow==13.0.0` in `constraints.txt`) is now imported by `infrastructure/images.py`, so it is used; no new dependency. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Image size, channels, `MAX_PIXEL` and `GREY_VALUES` are single constants used by the scene, `to_grayscale` and `invert_image`; the scene colours and positions are named constants; `save_gray_image` reuses `save_array_screenshot`; the step code reuses `IMPORT_PLT`, `IMPORT_FACE`, `IMPORT_GRAY`. The tests repeat `255` and the shape (768, 1024, 3) as expected values, which is intended. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain/images.py` imports only numpy and stdlib; `infrastructure/images.py` imports Pillow, numpy and the sibling `screenshots`; `steps_images.py` imports only `lesson_step`; `lesson.py` imports the five step modules at top level. No cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | File I/O (Pillow) lives in infrastructure and the pure array operations in domain; the part was added by a new step module and one entry in `all_steps()`; no inheritance. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure, in `snake_case`, and imports between the layers point inward | Pass | `domain/images.py`, `infrastructure/images.py`, `application/steps_images.py`, `application/lesson.py`; `tests/unit/test_images.py`, `tests/integration/test_image_files.py`; `tests/e2e` not needed yet. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Python files are snake_case; images `16-image-info.png` to `22-own-image.png` use letters, digits and `-`. |

## Overall Verdict

Go — every criterion is Pass or N-A, and pytest, ruff, mypy strict and opengrep are green. No blocking finding. Two optional suggestions: extend `FIGURE_SLUGS` in `tests/integration/test_figure_screenshots.py` with `17-image-show`, `18-grayscale`, `19-flip-gray`, `20-rotate`, `21-invert` so every figure cell is asserted to display a PNG, and record the `show_gray` to `save_gray_image` naming deviation in the milestone.

Milestone Go/No-Go table of [MIL-005], row by row: 1 the test image has dtype uint8, 3 dimensions, 3 channels and shape (768, 1024, 3): Go (`test_face_image_is_uint8_with_three_channels` passes; the notebook cell 16 prints `uint8`, `(768, 1024, 3)`, `3`, `1024 x 768`); 2 `to_grayscale` divides by 255 and applies [0.2126, 0.7152, 0.0722] with `@`, giving a 2D result between 0 and 1: Go (source line `(img / MAX_PIXEL) @ np.array(GREY_VALUES)`; tests for shape (768, 1024), range 0 to 1 and equality with the matmul pass); 3 `flip_image`, `rotate_image` (rot90) and `invert_image` (255 - img) give the expected shapes and values: Go (tests on tiny arrays and the full picture pass, rotated shape (1024, 768, 3), double inversion is identity); 4 `load_image(path)` opens a 3-channel file with Pillow with a generated JPEG: Go (`test_load_image_reads_a_generated_jpeg_with_three_channels` passes); 5 the image source decision is recorded in ADR-0001, accepted: Go (`docs/adr/adr-0001-image-source.md` exists, its Version History row has status `Accepted`). Images 16 to 22 exist in `docs/images/` and `README.md` lines 174 to 186 reference all seven. They are the real notebook output: the executed `notebooks/computing_with_numpy.ipynb` holds the same stdout for cells 16 and 22 (text screenshots), and for cells 17 to 21 the PNG displayed by the cell is byte-identical to `docs/images/17` to `21-*.png` (checked); the rotated picture `20-rotate.png` was viewed and shows the scene turned a quarter turn (1024 rows by 768 columns). All five milestone criteria are Go.

Observation outside this record's scope: the Version History of ADR-0001 now has a single row with status `Accepted` and the change `Initial version`, whereas [RC-014] reviewed it as `Proposed`; QC-ADR-001 criterion 8 asks for a new row for a status change rather than rewriting the earlier one. Add the `Proposed` row back, or record the acceptance as a new row, when the ADR is next touched.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Optional: add the slugs `17-image-show` to `21-invert` to `FIGURE_SLUGS` in `tests/integration/test_figure_screenshots.py` | S01 | 2026-11-18 |
| Optional: record in [MIL-005] that `show_gray` is implemented as `save_gray_image` | S01 | 2026-11-18 |
| ADR-0001: keep the `Proposed` row and add the `Accepted` row as a new Version History row (QC-ADR-001 criterion 8) | S01 | 2026-11-18 |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[MIL-005]: ../../milestones/mil-005-images-as-ndarrays.md
[ADR-0001]: ../../adr/adr-0001-image-source.md
[RC-014]: ./rc-014-adr-0001.md
[64a7682]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/commit/64a7682c30eed7cd1111ed72b9e8ccde7d7b69a1
