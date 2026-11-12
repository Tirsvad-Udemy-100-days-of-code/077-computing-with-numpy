# MIL-006 Wiki and release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the project is complete: wiki in three languages explaining what was gained in each lecture step, final README, and a release.

## Deliverable

`docs/wiki/` with Home, Getting Started (Windows PowerShell and Linux/macOS commands, as separate command blocks), Step 1 ndarrays, Step 2 Generating ndarrays, Step 3 Broadcasting and matmul, Step 4 Images, Summary and the sidebar in English, Danish (`-da`) and Bahasa Malaysia (`-ms`), each with its screenshots; final README; tag v1.0.0.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every English wiki page exists in `-da` and `-ms` with the same page set | `check-languages.sh` passes | Page missing |
| 2 | Every Step page references at least one screenshot file that exists, checked by `scripts/check_wiki.py` | Script exits 0 | Script exits non-zero |
| 3 | `_Sidebar.md` follows `framework/process/wiki.md` | Review Go against QC-WIKI-001 | Review No-Go |
| 4 | README final: setup, run, tests, screenshots, document appendix | `check-readme.sh` passes | Check fails |
| 5 | All tests pass and opengrep reports 0 findings | Green | Red |
| 6 | Tag v1.0.0 exists on the host | `git ls-remote --tags origin v1.0.0` lists it | Tag missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Needs the lecture steps documented |
| MIL-005 | Needs the final lecture step |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4 and 5 of [BC-001] | [BC-001] |
| concerns CN-003, CN-004, CN-006 of [SA-001] | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-19 — within the six-working-day duration constraint of [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write English wiki pages | Write Home, Getting Started (separate Windows PowerShell and Linux/macOS blocks for venv, pip upgrade, install, run, tests and Jupyter), Step 1 to Step 4 pages that explain what was gained in each lecture step with screenshots, a Summary page and `_Sidebar.md`. | No | |
| 2 | Write Danish wiki pages | Translate every English page to Danish as `<Page>-da.md`, with the language line and the same screenshots; code, commands and IDs stay in English. | No | |
| 3 | Write Bahasa Malaysia wiki pages | Translate every English page to Bahasa Malaysia as `<Page>-ms.md`, with the language line and the same screenshots; code, commands and IDs stay in English. | No | |
| 4 | Finalise README and project documents | Add `scripts/check_wiki.py` (every Step page references an existing screenshot in each language), finish the README appendix and the traceability matrix, run all checks (`check-readme.sh`, `check-languages.sh`, tests, ruff, opengrep) and fix findings. | No | |
| 5 | Tag release v1.0.0 | Create the release notes from the milestones and tag v1.0.0 after the last pull request is merged, using the release token only for that call. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
