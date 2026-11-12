# MIL-004 Broadcasting and matrix multiplication

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether vector arithmetic, broadcasting with scalars and matrix multiplication are correctly implemented, tested and documented.

## Deliverable

Module `computing_with_numpy.linear_algebra` with vector addition and multiplication, scalar broadcasting and the matrix multiplication challenge, tests, notebook section, README section and screenshots.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `add_vectors` gives [6, 6, 5, 10] and `multiply_vectors` gives [8, 5, 6, 21]; a test asserts that adding the two Python lists gives the 8-element concatenation | Tests pass | Test fails |
| 2 | Scalar broadcasting works for 1D and 2D arrays | Tests pass | Test fails |
| 3 | `matrix_product(a1, b1)` has shape (4, 3) with c12 = 25 and c33 = 28; `@` and `np.matmul` agree | Tests pass | Test fails |
| 4 | Screenshots for every step in README | Images present | Missing image |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Provides the screenshot generator and project layout |
| MIL-003 | Follows the generating challenges in the plan order and reuses their helpers |

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

2026-11-17 — within the six-working-day duration constraint of [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement vector arithmetic and list contrast | Add `add_vectors`, `multiply_vectors`, `add_lists` and tests showing that adding Python lists concatenates them while arrays add element by element. | No | |
| 2 | Implement scalar broadcasting | Add `scale_array` for 1D and 2D arrays, with tests for multiplication by a scalar. | No | |
| 3 | Implement matrix multiplication challenge | Add `matrix_product` with the lecture's a1 (4x2) and b1 (2x3), and tests for c12 = 1*1 + 3*8 = 25 and c33 = 6*3 + 2*5 = 28 using both `@` and `np.matmul`. | No | |
| 4 | Add notebook section and screenshots for linear algebra | Extend the notebook and generate one screenshot per step; reference them from the README. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
