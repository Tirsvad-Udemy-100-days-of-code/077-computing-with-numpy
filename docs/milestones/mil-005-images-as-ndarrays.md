# MIL-005 Images as ndarrays

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [ea0c2d7] |

---

## Purpose

Decide whether images as ndarrays (type, shape, grayscale, flip, rotate, invert, own image) are correctly implemented, tested and documented, and decide the source of the raccoon image.

## Deliverable

Module `computing_with_numpy.domain.images` with image loading, inspection, grayscale conversion, flip, rotation, inversion and own-image loading, tests, notebook section, README section and screenshots. An architecture decision record (ADR) records the image source decision.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The test image has dtype uint8, 3 dimensions and 3 channels; its shape is (768, 1024, 3) when the lecture image is used | Tests pass | Test fails |
| 2 | `to_grayscale` divides by 255 and applies [0.2126, 0.7152, 0.0722] with `@`; the result is 2D with values between 0 and 1 | Tests pass | Test fails |
| 3 | `flip_image`, `rotate_image` (rot90) and `invert_image` (255 - img) give the expected shapes and values | Tests pass | Test fails |
| 4 | `load_image(path)` opens a 3-channel file with Pillow (PIL) into an ndarray | Test passes with a generated JPEG | Test fails |
| 5 | The image source decision is recorded in ADR-0001 | ADR-0001 accepted | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | Uses broadcasting and matrix multiplication |
| Permission from S01 to download the lecture zip | Without it, the architecture decision record (ADR) chooses another image source |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 4 of [BC-001] | [BC-001] |
| concerns CN-001, CN-002, CN-005 of [SA-001] | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-18 — within the six-working-day duration constraint of [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Decide the raccoon image source in an ADR | Record whether the image comes from the lecture zip kept in the repository, from `scipy.datasets.face` as an optional extra, or from a generated stand-in; consider S03's wish for few runtime dependencies and the licence of the image. | No | |
| 2 | Implement image loading and inspection | Add `load_face_image`, `load_image` (Pillow (PIL) to ndarray) and `describe_image` (type, shape, ndim, resolution) with tests. | No | |
| 3 | Implement grayscale conversion | Add `to_grayscale` using the sRGB division by 255 and the matrix product with the grey values, and `save_gray_image` (the lecture's display step) that saves the result with cmap gray. | No | |
| 4 | Implement flip, rotate and invert | Add `flip_image` (np.flip), `rotate_image` (np.rot90) and `invert_image` (255 - img) with tests on small known arrays and the full image. | No | |
| 5 | Add notebook section and screenshots for images | Extend the notebook and generate one screenshot per step including the grayscale, flipped, rotated and solarized images; reference them from the README. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[ea0c2d7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/commit/ea0c2d7ed4eb1e98937384a8d8b5bf386f457529
