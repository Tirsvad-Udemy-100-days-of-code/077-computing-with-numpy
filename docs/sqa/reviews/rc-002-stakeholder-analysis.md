# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-002 |
| CrossReference | [SA-001], [QC-SA-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [ea0c2d7] |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Full re-review after rework of SA-001: earlier No-Go finding resolved, verdict Go-with-conditions | [ea0c2d7] |

---

## Artifact Under Review

- Instance reviewed: [SA-001]
- Checklist used: [QC-SA-001] (`QC-SA-001`), together with [QC-LANG-001] (the Stakeholder Analysis is written in the PO language)
- Scope: full re-review after rework (the first review gave No-Go; see Action Items)
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: S01 (person, confirmed criteria 3, 5 and 9 in chat on 2026-11-12)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Power/Interest grid is filled for every stakeholder, with no gaps or unclassified entries | Pass | S01 High/High "Manage Closely", S02 Low/High "Keep Informed", S03 Low/Low "Monitor"; consistent with the rationale section. |
| 2 | Each stakeholder is assigned a unique, stable ID (e.g. S01-S11 style) reusable for RACI assignments in other artifacts | Pass | S01, S02, S03, unique; the same IDs are used in [BC-001]. |
| 3 | Roles and organizational context are defined with explicit Power and Interest levels, not just narrative description | Pass | Role/Title, Organization, Power Level, Interest Level filled for all three. Observation: S03 is "GitHub viewers" while [BC-001] publishes to a Gitea host (open action item). |
| 4 | Communication needs (channel, frequency, deliverable type) are mapped to project phases or milestones | Pass | Optional. Channel, Frequency, Deliverable type, Phase: "README ... MIL-001 to MIL-006", "Wiki ... MIL-006"; those milestones exist. |
| 5 | Conflicting stakeholder interests are identified with documented mitigation or resolution strategies | Pass | Two conflicts, each with a mitigation (development-only tools; snake_case names listed in the README). |
| 6 | Stakeholder concerns are explicitly traced to Business Case objectives | Pass | `## Traceability Analysis` is now concern-level: CN-001 to CN-007 each map to BC-001 objectives (e.g. CN-003 "Objectives 3 and 4", CN-006 "Objective 5") or, for CN-005 and CN-007, to a named BC-001 Constraint, Risk and Out of Scope item, all of which exist in the reworked BC-001 ("Runtime dependencies are kept to what the lecture needs", "Personal access tokens leak"). Strictly these two are not objectives; the trace is explicit and accepted. |
| 7 | Primary concerns are expressed in both business language and a recognized quality-attribute mapping (e.g. FURPS+) | Pass | Optional. "Primary Concern (Business Language)" column plus a FURPS+ attribute per concern. |
| 8 | Document is understandable and navigable by non-technical stakeholders reviewing their own entry | Pass | Optional. One row per stakeholder with plain-language concern. Minor: S03's "runtime dependencies" is technical wording. |
| 9 | Every concern has a stable ID (`CN-NNN`) in the concern register, with the stakeholder who raised it; IDs are never renumbered or reused | Pass | CN-001 to CN-007, sequential, unique, each with a Stakeholder; IDs unchanged by the rework. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language` = `en`, `Domain` = `it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Registry gives SA "IT Professional English"; the text is professional (Mendelow grid, FURPS+, development dependencies). |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | `N-A` is not allowed. No Domain Dictionary instance exists to check against. Proposal only: terms are consistent ("coursists", "viewers", "runtime dependencies"). S01 as a person to confirm. Confirmed by S01 in chat on 2026-11-12: text is English; IT-domain terms are used correctly; no Domain Dictionary is kept for this small project. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | All English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | Only `docs/stakeholder-analysis.md` exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First version; no previous accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | `N-A` is not allowed. The reviewer is an AI stand-in (not independent). Proposal: terms used correctly. S01 to confirm with ID and date. Confirmed by S01 in chat on 2026-11-12: text is English; IT-domain terms are used correctly; no Domain Dictionary is kept for this small project. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Optional. FURPS+ is now spelled out (Functionality, Usability, Reliability, Performance, Supportability). Residual: README, `RC-*` and `MIL-NNN` are established terms or framework IDs; acceptable. |

## Overall Verdict

Go — no criterion fails except the Optional ones fixed or recorded; QC-LANG-001 criteria 3, 5 and 9 are confirmed by S01 as a person on 2026-11-12. The reviewed artifact is Accepted.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Resolved: first review gave No-Go (QC-SA-001 #6, concerns not traced to Business Case objectives); fixed by the concern-level Traceability Analysis | S01 | 2026-11-12 |
| Resolved: Optional finding QC-LANG-001 #10 (FURPS+ spelled out) | S01 | 2026-11-12 |
| Done: QC-LANG-001 #3, #5 and #9 confirmed by S01 in chat on 2026-11-12 | S01 | 2026-11-13 |
| Open, non-blocking: S03 "GitHub viewers" against the Gitea host in [BC-001] Objective 6; align the wording | S01 | 2026-11-13 |

---

[SA-001]: ../../stakeholder-analysis.md
[BC-001]: ../../business-case.md
[QC-SA-001]: ../../../framework/qc/artifacts/qc-stakeholder-analysis.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[ea0c2d7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/commit/ea0c2d7ed4eb1e98937384a8d8b5bf386f457529
