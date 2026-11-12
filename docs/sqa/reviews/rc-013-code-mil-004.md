# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [QC-PY-001], [MIL-004] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [baf70b4] |

---

## Artifact Under Review

- Instance reviewed: the code added at milestone MIL-004 ([MIL-004], tasks 1 to 4): `src/computing_with_numpy/domain/linear_algebra.py`, `application/steps_linear_algebra.py`, `application/lesson.py`, `tests/unit/test_linear_algebra.py` and `tests/unit/test_lesson_steps.py`
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

Tool evidence (run in `.venv`): `python -m pytest -q` 61 passed, 1 warning; `ruff check .` clean; `ruff format --check .` clean (55 files); `mypy src tests scripts` clean (strict, 30 files); `bash scripts/check-opengrep.sh` -> opengrep: no findings.

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `linear_algebra`, `steps_linear_algebra`, `create_vector_v1`, `matrix_product`, `VECTOR_1`, `MATRIX_A1`; ruff `N` passes. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names mirror the lecture (`add_vectors`, `scale_array`, `matrix_product`, `a1`, `b1`, `v1`, `v2`); `a` and `b` in `matrix_product` are tiny scopes and the maths' own names. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check .` -> All checks passed; `ruff format --check .` -> 55 files already formatted. One `# type: ignore[operator]` in `multiply_lists`, on the line that deliberately multiplies two lists; its docstring explains the purpose (the lecture's "error!", raises `TypeError`). Optional: add a short comment on the ignore line saying so. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All functions in the reviewed files and tests are annotated; ruff `ANN` passes. `multiply_lists -> object` is deliberate: the function always raises. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `try`/`except` in Python code; the `except TypeError as error` is inside the lesson-code string, prints the error and is the lecture's demonstration. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No defaults; ruff `B` passes; the module-level lists `VECTOR_1` etc. are copied by `np.array` and are not shared defaults. |
| 7 | Files, locks and connections are managed with context managers | N-A | No files, locks or connections in the reviewed code. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public function and module has a docstring; ruff `D` passes. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` or logging in Python code (only in lesson-code strings run in the notebook); no secrets. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists. Functions trace to the tasks of [MIL-004]: task 1 `add_vectors`, `multiply_vectors`, `add_lists` (plus `multiply_lists` for the lecture's list error); task 2 `scale_array`; task 3 `matrix_product`; the `create_*` functions supply the lecture's data. The Deliverable already names `domain.linear_algebra`. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `pytest -q` -> 61 passed, 1 warning (zmq Proactor event-loop on Windows, harmless). `tests/unit/test_linear_algebra.py` has 10 tests: sums [6, 6, 5, 10], products [8, 5, 6, 21], list concatenation, `TypeError` on list product, scaling in 1D and 2D, shape (4, 3), `@` equals `np.matmul`, c12 = 25, c33 = 28. `test_lesson_steps.py` checks the four new slugs in order and unique slugs; `test_notebook_execution` runs every step with no error. Names state behaviour; no network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | (Optional) `mypy src tests scripts` -> Success: no issues found in 30 source files (strict); no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | (Optional) No new dependency in MIL-004; only numpy. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The lecture's data is defined once as module constants (`VECTOR_1`, `VECTOR_2`, `MATRIX_2D`, `MATRIX_A1`, `MATRIX_B1`) and wrapped by the `create_*` functions; the step code and the tests use those functions or constants, not copies of the numbers. `add_vectors`/`add_lists` look alike but express different knowledge (element-wise versus concatenation), the point of the lesson. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain/linear_algebra.py` imports only numpy; `steps_linear_algebra.py` imports only `lesson_step`; `lesson.py` imports the four step modules at top level. No cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One module per lecture part; the part was added by a new `steps_linear_algebra.py` and one entry in `all_steps()`; small pure functions; no inheritance. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure, in `snake_case`, and imports between the layers point inward | Pass | `domain/linear_algebra.py`, `application/steps_linear_algebra.py`, `application/lesson.py`, `tests/unit/test_linear_algebra.py`; `tests/e2e` not needed yet. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Python files are snake_case; images `12-vector-math.png` to `15-matrix-product.png` use letters, digits and `-`. |

## Overall Verdict

Go — every criterion is Pass or N-A, and pytest, ruff, mypy strict and opengrep are green. No blocking finding; one optional suggestion (comment the `# type: ignore[operator]` line in `multiply_lists`).

Milestone Go/No-Go table of [MIL-004], row by row: 1 `add_vectors` gives [6, 6, 5, 10], `multiply_vectors` gives [8, 5, 6, 21], and a test asserts that adding the two lists gives the 8-element concatenation: Go (`test_add_vectors_adds_element_by_element`, `test_multiply_vectors_multiplies_element_by_element`, `test_add_lists_concatenates` pass); 2 scalar broadcasting for 1D and 2D arrays: Go (`test_scale_array_doubles_a_vector`, `test_scale_array_doubles_a_2d_array` pass); 3 `matrix_product(a1, b1)` has shape (4, 3) with c12 = 25 and c33 = 28, and `@` and `np.matmul` agree: Go (four tests pass; the executed notebook prints [[19 25 18], [5 8 5], [34 22 28], [71 65 62]], (4, 3) and True); 4 screenshots for every step in the README: Go (`docs/images/12-vector-math.png` to `15-matrix-product.png` exist, all four are referenced in `README.md` lines 153 to 159). The images are the real notebook output: the executed `notebooks/computing_with_numpy.ipynb` holds the same stdout for cells 12 to 15 (checked: [6 6 5 10] and [8 5 6 21]; the list concatenation and the `TypeError` message; the scaled arrays; the matrix product), and the screenshots 13 and 15 show the cell code followed by that output. All four milestone criteria are Go.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Optional: add a short comment on the `# type: ignore[operator]` line of `multiply_lists` saying the list product is deliberate (criterion 3) | S01 | 2026-11-17 |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[MIL-004]: ../../milestones/mil-004-broadcasting-matmul.md
[baf70b4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/commit/baf70b41a5da2da8a0ff4e934994102b9138545e
