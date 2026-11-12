# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-001 |
| CrossReference | [BC-001], [QC-BC-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [ea0c2d7] |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Full re-review after rework of BC-001: earlier No-Go findings resolved, verdict Go-with-conditions | [ea0c2d7] |

---

## Artifact Under Review

- Instance reviewed: [BC-001]
- Checklist used: [QC-BC-001] (`QC-BC-001`), together with [QC-LANG-001] (the Business Case is written in the PO language)
- Scope: full re-review after rework (the first review gave No-Go; see Action Items)
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: S01 (person, confirmed criteria 3, 5 and 9 in chat on 2026-11-12)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | ROI/Cost-Benefit analysis is quantitative, or where qualitative, is explicitly justified | Pass | "About 20 hours of S01 review time and AI effort, no licence cost" (cost quantified); benefits qualitative and justified: "qualitative, justified because the project is a learning and portfolio exercise". |
| 2 | Risks are identified with documented impact and mitigation | Pass | Five rows in `## Risks`, each with Impact and Mitigation (e.g. "Chart windows block automated tests" / "Tests hang" / "Tests save charts to files instead of opening windows"). |
| 3 | Success criteria are measurable, stating explicit targets rather than vague aspirations | Pass | Six rows with Target and Measure, e.g. "100 % of the lecture challenges have a function", "0 error-severity findings before each push", "at least 5 topics". |
| 4 | Scope explicitly separates In Scope vs Out of Scope | Pass | `### In Scope` and `### Out of Scope` both present and populated. |
| 5 | Stakeholders are cross-referenced to Stakeholder Analysis IDs rather than re-described inline | Pass | Metadata `CrossReference` = `[SA-001]`; link definition `[SA-001]: ./stakeholder-analysis.md`; table header "Stakeholder ID ([SA-001])" with S01 to S03 (matching SA-001) and only a one-line interest each. |
| 6 | Methodology and quality-standard foundation are stated explicitly (e.g. ISO/IEC 25010, Larman) | Pass | Optional. "ISO/IEC 25010:2023 ... Functional suitability, Maintainability, Interaction Capability and Flexibility" now uses the 2023 names; SSDF and ISO/IEC 25002 named. |
| 7 | Assumptions and constraints are explicit and clearly distinguished from one another | Pass | Separate `## Assumptions` and `## Constraints` sections with distinct content (installed Python, existing repository vs. folder separation, dependency limit, duration 2026-11-12 to 2026-11-18). |
| 8 | Document supports executive decision-making with a clear, unambiguous recommendation | Pass | "Proceed — the scope is small, the lecture is fully specified and every outcome can be checked by a test or a document review." |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language` = `en`, `Domain` = `it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the domain list of `docs/artifact-registry.md`. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English; "raccoon" is now spelled correctly. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Registry gives BC "IT Executive English". Commands, file names and tool names are gone: "A current Python version with an isolated local environment", "A local static security scan before each push", "Test run exit code 0". Residual named items (Jupyter, Gitea, NumPy) are product names, not implementation detail. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | `N-A` is not allowed for this criterion. The project has no Domain Dictionary instance to check against. Proposal only: terms are consistent ("coursists" throughout, ndarray, milestone, pull request). S01 as a person to confirm. Confirmed by S01 in chat on 2026-11-12: text is English; IT-domain terms are used correctly; no Domain Dictionary is kept for this small project. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | All English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | Only `docs/business-case.md` exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First version; no previous accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | `N-A` is not allowed. The reviewer is an AI stand-in (not independent). Proposal: IT terms used correctly. S01 to confirm with ID and date. Confirmed by S01 in chat on 2026-11-12: text is English; IT-domain terms are used correctly; no Domain Dictionary is kept for this small project. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Optional. SQA, QC, ISO/IEC and SSDF are now spelled out at first use. Residual: README, PyPI, AI are established terms left unexpanded; acceptable. |

## Overall Verdict

Go — no criterion fails except the Optional ones fixed or recorded; QC-LANG-001 criteria 3, 5 and 9 are confirmed by S01 as a person on 2026-11-12. The reviewed artifact is Accepted.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Resolved: first review gave No-Go (QC-BC-001 #5 missing SA-001 cross-reference, QC-LANG-001 #4 implementation detail in executive register); fixed in the reworked BC-001 | S01 | 2026-11-12 |
| Resolved: Optional findings QC-BC-001 #6 (2023 characteristic names), QC-LANG-001 #10 (acronyms), "racoon" typo | S01 | 2026-11-12 |
| Done: QC-LANG-001 #3, #5 and #9 confirmed by S01 in chat on 2026-11-12 | S01 | 2026-11-13 |
| Noted, non-blocking: S03 keeps the PO-given name "GitHub viewers"; the BC says repository visitors | S01 | 2026-11-13 |

---

[BC-001]: ../../business-case.md
[QC-BC-001]: ../../../framework/qc/artifacts/qc-business-case.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[ea0c2d7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/commit/ea0c2d7ed4eb1e98937384a8d8b5bf386f457529
