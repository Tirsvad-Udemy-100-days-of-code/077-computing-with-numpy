# Image source for the raccoon lesson

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [MIL-005] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after RC-014 (Go) | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The lecture opens the raccoon picture with `scipy.misc.face()`. That function was removed from SciPy; its replacement, `scipy.datasets.face()`, downloads the file on first use and needs two more libraries (SciPy and Pooch). The lecture zip with the picture is a signed link and S01 has not given permission to download it. S03 wants no runtime dependencies beyond what the lecture needs ([BC-001] Constraints), and the picture's licence is not ours to redistribute.

Options considered:

1. Use `scipy.datasets.face()`: adds two runtime dependencies and a network download, which breaks offline runs and tests.
2. Commit the lecture's picture: needs the download and has an unclear licence.
3. Generate a deterministic stand-in picture of the same size (768 rows, 1024 columns, 3 colour channels, unsigned 8-bit) with NumPy, and let the reader load any picture of their own with Pillow.

## Decision

Use option 3: `load_face_image()` returns a generated 768 x 1024 x 3 `uint8` picture, so every lecture step runs offline with no extra dependency, and `load_image(path)` opens a reader's own 3-channel file with Pillow. The README shows how to swap in the real raccoon picture.

## Consequences

**Positive:**

- No download, no extra runtime dependency, no licence question, identical behaviour on every machine.
- Tests are deterministic and the shape (768, 1024, 3) matches the lecture's answers.

**Negative:**

- The screenshots show a generated scene, not the raccoon of the lecture.
- A coursist who wants the original picture has to load it themselves.

## Affected Artifacts

- [BC-001] — keeps the runtime dependencies to the lecture's needs and resolves the image-source risk
- [MIL-005] — task 1 is this decision; the image tasks use the stand-in

---

[BC-001]: ../business-case.md
[MIL-005]: ../milestones/mil-005-images-as-ndarrays.md
