# MIL-003 Generating and manipulating ndarrays

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [ea0c2d7] |

---

## Purpose

Decide whether challenges 1 to 8 (arange, slicing, flip, nonzero, random, linspace, plotting, noise image) are correctly implemented, tested and documented.

## Deliverable

Module `computing_with_numpy.domain.generating` with one function per challenge, tests, notebook section, README section and screenshots, including the line chart and the noise image.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `create_range_vector()` returns the values 10 to 29 | Test passes | Test fails |
| 2 | Slicing functions return the last 3 values, the 4th to 6th values, all but the first 12 and every second value | Tests pass | Test fails |
| 3 | `reverse_array`, `nonzero_indices` return the stated results; `random_cube` has shape (3, 3, 3) | Tests pass | Test fails |
| 4 | `linspace_x` and `linspace_y` have size 9 with the stated bounds; the chart and a 128x128x3 noise image are saved without a GUI | Tests pass and PNG files exist | Test fails |
| 5 | Screenshots for every challenge in README | Images present | Missing image |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Provides the screenshot generator and project layout |
| MIL-002 | Builds on the ndarray basics module |

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

2026-11-16 — within the six-working-day duration constraint of [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement arange and slicing challenges 1 to 3 | Add `create_range_vector`, `last_three`, `fourth_to_sixth`, `all_except_first_twelve`, `every_second` and `reverse_array` (both `[::-1]` and `np.flip`), with tests against the lecture's expected values. | No | |
| 2 | Implement nonzero and random challenges 4 and 5 | Add `nonzero_indices` for [6, 0, 9, 0, 0, 5, 0] (result (array([0, 2, 5]),)) and `random_cube` with a seedable generator so tests are deterministic. | No | |
| 3 | Implement linspace and plotting challenges 6 and 7 | Add `linspace_x` (0 to 100, 9 values), `linspace_y` (-3 to 3, 9 values) and `plot_line` that saves the Matplotlib chart to a file using the Agg backend. | No | |
| 4 | Implement the noise image challenge 8 | Add `noise_image` returning a 128x128x3 array and `save_noise_image` that renders it with `imshow` to a PNG. | No | |
| 5 | Add notebook section and screenshots for challenges 1 to 8 | Extend the notebook and generate one screenshot per challenge; reference them from the README. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[ea0c2d7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/commit/ea0c2d7ed4eb1e98937384a8d8b5bf386f457529
