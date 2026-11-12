# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Identify the people with an interest in the project, classify them by power and interest (Mendelow grid), and record their concerns so later artifacts can cite stable IDs. Method: stakeholder identification, Power/Interest grid, mapping of concerns to the FURPS+ attributes (Functionality, Usability, Reliability, Performance, Supportability). Objectives are those of [BC-001].

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer, reviewer | Tirsvad | High | High | Manage Closely | A complete, correct and well documented solution to the Day 77 assignment |
| S02 | Udemy coursists | Other participants of the bootcamp | Udemy community | Low | High | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors browsing the repository for ideas | Public | Low | Low | Monitor | A clear repository description, topics and README, and no runtime dependencies beyond what is needed |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews and accepts every artifact; the only person who can change the plan.
- **Keep Informed (S02):** cannot change the project but compare solutions and benefit from clear instructions; informed through README and wiki.
- **Monitor (S03):** casual visitors; served by repository metadata and README, no active communication.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every lecture challenge has a correct, tested solution | Functionality |
| CN-002 | S02 | Function names match the assignment | Usability |
| CN-003 | S02 | I can run the code and tests from the README alone | Usability |
| CN-004 | S03 | The repository description, topics and README explain what it is | Usability |
| CN-005 | S03 | No runtime dependencies beyond the lecture's needs | Supportability |
| CN-006 | S01 | The wiki explains what was gained in each step, in three languages, with screenshots | Functionality |
| CN-007 | S01 | Personal tokens in `.env` are never exposed | Reliability |

## Communication Requirements

| Channel | Frequency | Deliverable type | Phase |
| --- | --- | --- | --- |
| Chat with S01 | Per milestone | Summary of pull requests, `RC-*` verdicts, stand-in decisions | Every milestone |
| README | Per milestone | Setup, run and test instructions, screenshots | MIL-001 to MIL-006 |
| Wiki | Per release | Lecture explanations in en, da, ms | MIL-006 |

## Conflicting Interests and Mitigations

| Conflict | Mitigation |
| --- | --- |
| S03 wants no runtime dependencies; the lecture needs NumPy and Matplotlib | Keep to the minimum the lecture needs; tools for tests, notebook and lint are development dependencies |
| S02 wants the assignment's function names; naming conventions prefer snake_case | Use snake_case names that match the assignment's wording, listed in the README |

## Traceability Analysis

| Concern | Stakeholder | Actor / use case | Business Case objective or element ([BC-001]) |
| --- | --- | --- | --- |
| CN-001 | S01 | Developer and reviewer; plain tasks, no use case | Objectives 1 and 2 |
| CN-002 | S02 | Reader who runs the code | Objective 1 |
| CN-003 | S02 | Reader who runs the code | Objectives 3 and 4 |
| CN-004 | S03 | Reader of repository metadata | Objectives 4 and 6 |
| CN-005 | S03 | Reader of repository metadata | Constraints: runtime dependencies kept to the lecture's needs |
| CN-006 | S01 | Developer and reviewer | Objective 5 |
| CN-007 | S01 | Developer | Risks: personal access tokens leak; Out of Scope: use of the credentials file by project code |

Every concern traces to a Business Case objective, constraint or risk.

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | pending | |

---

[BC-001]: ./business-case.md
