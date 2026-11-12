# MIL-002 ndarray basics

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [ea0c2d7] |

---

## Purpose

Decide whether the lecture part "NumPy's ndarray" (1D, 2D and N-D arrays, shape, ndim, indexing, mystery array challenge) is correctly implemented, tested and documented.

## Deliverable

Module `computing_with_numpy.ndarray_basics` with the functions for 1D, 2D and N-D arrays and the mystery array challenge, its tests, the notebook section, README section and screenshots.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `mystery_array` has 3 dimensions and shape (3, 2, 4) | Test passes | Test fails |
| 2 | Indexing returns 18, [97, 0, 27, 18] and the (3, 2) matrix [[0, 4], [7, 5], [5, 97]] | Tests pass | Test fails |
| 3 | Each lecture step has a screenshot in README | Images referenced and present | Missing image |
| 4 | Code passes ruff and opengrep | 0 findings | Any finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs the project foundation |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 4 of [BC-001] | [BC-001] |
| concerns CN-001, CN-002 of [SA-001] | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-13 — within the six-working-day duration constraint of [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement 1D and 2D array functions | Add `create_vector`, `create_matrix` and `describe_array` (ndim, shape, rows, columns) with the lecture's arrays, and tests for element access `array_2d[1, 2]` and row access `array_2d[0, :]`. | No | |
| 2 | Implement the mystery array challenge | Add `mystery_array`, `mystery_dimensions`, `mystery_shape`, `mystery_value_18`, `mystery_last_row_vector` and `mystery_first_elements_matrix` with tests for ndim 3, shape (3, 2, 4), the value 18, [97, 0, 27, 18] and the (3, 2) matrix. | No | |
| 3 | Add notebook section and screenshots for ndarray basics | Add the Jupyter notebook section for 1D, 2D and N-D arrays and generate one screenshot per step; reference them from the README. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[ea0c2d7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/commit/ea0c2d7ed4eb1e98937384a8d8b5bf386f457529
