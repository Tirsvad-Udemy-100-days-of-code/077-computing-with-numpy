# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [ea0c2d7] |

---

## Executive Summary

Day 77 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" teaches NumPy: ndarrays, slicing, generated arrays, broadcasting, matrix multiplication and images as arrays. The project turns the lecture's Google Colab notebook into a runnable, tested Python repository with the assignment's function names, a Jupyter notebook, a README and a three-language wiki (English, Danish, Bahasa Malaysia), each lecture step illustrated with a screenshot.

## Methodological and Standards Foundation

The project follows the Software Quality Assurance (SQA) and Quality Control (QC) framework used in this repository: planning comes before code, and every document is reviewed against a checklist with a recorded verdict. Product quality follows ISO/IEC 25010:2023 (International Organization for Standardization / International Electrotechnical Commission); the characteristics that matter here are Functional suitability, Maintainability, Interaction Capability and Flexibility. Secure development follows the Secure Software Development Framework (SSDF) practices, and quality measurement follows ISO/IEC 25002.

## Problem Statement

The lecture ships as a Colab notebook with code scattered over prose. A course participant cannot run it locally with one command, cannot test that each challenge gives the stated answer, and other coursists cannot compare solutions without opening the notebook. The belief that would kill the idea: a participant (S01) does not gain more from a structured repository than from the notebook alone.

## Business Opportunity

A small, reproducible repository makes the lecture's solutions readable, runnable and verifiable, and doubles as a portfolio piece (S03). The same layout can be reused for the next lessons of the bootcamp.

## Objectives

1. Implement every challenge of the Day 77 lecture as a function with the assignment's name, in the source folder.
2. Verify each challenge's stated result with an automated test in the tests folder.
3. Provide a Jupyter notebook that walks through the lecture using the same functions.
4. Provide a README with setup, run and test instructions for Windows and Linux/macOS, and one screenshot per lecture step.
5. Provide a wiki in English, Danish and Bahasa Malaysia that explains what was gained in each lecture step, with the same screenshots.
6. Publish the repository with a description and topics on the Gitea host, one pull request per milestone.

## Scope

### In Scope

- Lecture parts: ndarray basics (1D, 2D, N-D), the generating and manipulating challenges 1 to 8, broadcasting, matrix multiplication, images as ndarrays (grayscale, flip, rotate, invert, own image).
- A current Python version with an isolated local environment, a standard project configuration file and a Jupyter notebook.
- README from the framework template; wiki in English, Danish and Bahasa Malaysia.
- A local static security scan before each push.

### Out of Scope

- Other days of the bootcamp.
- Publishing the Udemy lecture material itself beyond the small code and image needed to run the examples.
- Packaging for PyPI.
- Any use of the personal credentials file by the project code; it is never imported, tested or committed.

## Expected Benefits

### Tangible Benefits

- One command runs the tests; every challenge has an executable check.
- A README and wiki that other coursists (S02) and viewers (S03) can follow without the course.

### Intangible Benefits

- Deeper understanding of ndarray indexing, broadcasting and linear algebra.
- A repeatable template for later bootcamp days.

## Strategic Alignment

The project supports S01's goal of completing the bootcamp with documented, reviewable work, and the quality framework's goal of showing a complete plan-first lifecycle on a small project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Challenges implemented | 100 % of the lecture challenges have a function | Count of challenges against functions in the source folder |
| 2 | Tests pass | All automated tests pass on the supported Python version | Test run exit code 0 |
| 3 | Static analysis | 0 error-severity findings before each push | Output of the local security scan |
| 4 | Screenshots | One screenshot per lecture step in README and in each wiki language | Count of images referenced |
| 5 | Wiki languages | 3 languages with the same page set | Page files per language in the wiki folder |
| 6 | Repository metadata | Description and at least 5 topics set | Repository settings on the host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The lecture's raccoon image is no longer bundled with the library the lecture used, and its replacement needs a download | Image milestone cannot run offline | Keep the image with the repository, make the library an optional extra, or use a generated stand-in; decided in the images milestone |
| Chart windows block automated tests | Tests hang | Tests save charts to files instead of opening windows |
| Personal access tokens leak | Credential exposure | The credentials file is ignored by version control, never read by project code and never printed |
| Danish and Malay translations contain errors | Misleading wiki | English is authoritative; translations are reviewed page by page |
| The signed lecture download link expires | Image data missing | Ask S01 for permission to download, otherwise use a generated or bundled image |

## Assumptions

- The Product Owner (S01) is also developer and reviewer; in autonomous mode the AI stands in for S01 as reviewer and records it.
- Python 3.13 or newer is installed; "greater than 3.13" is read as 3.13 or newer.
- The Gitea repository exists and the personal access tokens held outside the repository have the scopes named by their keys.
- The people the project is for (S02, S03) are not contacted during the project.

## Constraints

- Source code, tests and documents live in separate folders.
- Runtime dependencies are kept to what the lecture needs (numerical, charting and image libraries); test, notebook and lint tools are development-only.
- Python 3.13 or newer with an isolated local environment.
- One branch and one pull request per milestone.
- Duration: six working days, 2026-11-12 to 2026-11-19 (the weekend of 2026-11-14 and 2026-11-15 is not used).

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About 20 hours of S01 review time and AI effort, no licence cost | A reusable, tested lecture repository and a three-language wiki; qualitative, justified because the project is a learning and portfolio exercise |

## Stakeholders

| Stakeholder ID ([SA-001]) | Interest in this project |
| --- | --- |
| S01 | Wants a complete, reviewed solution |
| S02 | Wants readable, runnable code with the assignment's function names |
| S03 | Wants a clear repository description, topics and README |

## Recommendation

Proceed — the scope is small, the lecture is fully specified and every outcome can be checked by a test or a document review.

---

[SA-001]: ./stakeholder-analysis.md
[ea0c2d7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/commit/ea0c2d7ed4eb1e98937384a8d8b5bf386f457529
