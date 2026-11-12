# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [ea0c2d7] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001] to [MIL-006] | - |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | tasks | [RC-003] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001] | tasks | [RC-004] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001] | tasks | [RC-005] |
| [MIL-004] | MIL | en | it | [BC-001], [PP-001] | tasks | [RC-006] |
| [MIL-005] | MIL | en | it | [BC-001], [PP-001] | tasks | [RC-007] |
| [MIL-006] | MIL | en | it | [BC-001], [PP-001] | tasks | [RC-008] |
| `src/`, `tests/`, `scripts/` (MIL-001) | Python code | - | - | [MIL-001] | - | [RC-009] |
| `.gitea/workflows/tests.yml` | Workflow | - | - | [MIL-001] | - | [RC-010] |
| `src/`, `tests/`, `scripts/` (MIL-002) | Python code | - | - | [MIL-002] | - | [RC-011] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | - | - | - | Gap (code not written yet) |
| CN-002 | - | - | - | Gap (code not written yet) |
| CN-003 | - | - | - | Gap (code not written yet) |
| CN-004 | - | - | - | Gap (code not written yet) |
| CN-005 | - | - | - | Gap (code not written yet) |
| CN-006 | - | - | - | Gap (code not written yet) |
| CN-007 | - | - | - | Gap (code not written yet) |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | - | None found | - | Closed | - |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[RC-001]: reviews/rc-001-business-case.md
[RC-002]: reviews/rc-002-stakeholder-analysis.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[RC-003]: reviews/rc-003-mil-001.md
[MIL-002]: ../milestones/mil-002-ndarray-basics.md
[RC-004]: reviews/rc-004-mil-002.md
[MIL-003]: ../milestones/mil-003-generating-ndarrays.md
[RC-005]: reviews/rc-005-mil-003.md
[MIL-004]: ../milestones/mil-004-broadcasting-matmul.md
[RC-006]: reviews/rc-006-mil-004.md
[MIL-005]: ../milestones/mil-005-images-as-ndarrays.md
[RC-007]: reviews/rc-007-mil-005.md
[MIL-006]: ../milestones/mil-006-wiki-and-release.md
[RC-008]: reviews/rc-008-mil-006.md
[ea0c2d7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/commit/ea0c2d7ed4eb1e98937384a8d8b5bf386f457529
[RC-009]: reviews/rc-009-code-mil-001.md
[RC-010]: reviews/rc-010-workflow-mil-001.md
[RC-011]: reviews/rc-011-code-mil-002.md
