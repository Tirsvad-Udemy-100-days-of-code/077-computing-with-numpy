# MIL-001 Project setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the repository foundation (packaging, layout, tooling, documentation baseline, host metadata) is good enough to build the lecture code on.

## Deliverable

A Python 3.13+ project with `pyproject.toml`, `src/` and `tests/` layout, Python `.gitignore`, documented `.venv` setup, README from the framework template, local opengrep check, continuous integration (CI) workflow running the tests, repository description and topics on the host, and a screenshot generator.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m venv .venv`, `python -m pip install --upgrade pip` and `python -m pip install -e .[dev]` succeed on Python 3.13+ | Succeeds | Any error |
| 2 | `python -m pytest` collects and passes at least the smoke test | Exit code 0 with 1 or more tests passed | Exit code other than 0, or no test collected |
| 3 | README follows the framework template and documents setup, run and tests | `check-readme.sh` passes | Check fails |
| 4 | opengrep run on the repository reports no error-severity finding | 0 findings | Any finding |
| 5 | Repository description and at least 5 topics are set on the host | Visible in settings | Missing |
| 6 | The continuous integration (CI) workflow file exists and the screenshot generator writes a PNG file | Both verified by a command | Either missing |
| 7 | `.env` is ignored and never read by project code | `git check-ignore .env` succeeds; no reference in `src/` | Reference found |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway after the baseline |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4 and 6 of [BC-001] | [BC-001] |
| concerns CN-003, CN-004, CN-005, CN-007 of [SA-001] | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — within the six-working-day duration constraint of [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set the description and topics (python, numpy, jupyter, matplotlib, udemy, 100-days-of-code, learning) on the Gitea repository through the host's application programming interface (API) with the repository token from `.env`. The token is read by a one-off command, never printed and never used by project code. | No | |
| 2 | Add pyproject.toml, layout and .gitignore | Create `pyproject.toml` (requires-python >=3.13, runtime dependencies numpy, matplotlib, pillow; dev extras pytest, jupyter, ruff), the `src/computing_with_numpy/` package, `tests/` with a smoke test that imports the package, and a Python `.gitignore` that also ignores `.env` and `.venv`. | No | |
| 3 | Document venv setup and write the README | Write `README.md` from the framework template with `.venv` creation for both Windows PowerShell and Linux/macOS, `python -m pip install --upgrade pip`, install, run and test instructions, and the function-name table for S02. | No | |
| 4 | Add local opengrep check and git hooks | Add `scripts/check-opengrep.ps1`/`.sh` calling `~\.opengrep\cli\latest\opengrep.exe` before push, install the framework git hooks and the plan-gate hook, and document both in the README. | No | |
| 5 | Add CI workflow for tests | Add a Gitea Actions workflow that installs the project on Python 3.13 and runs pytest and ruff, so rule 8 of AGENTS.md has a CI to wait for. | No | |
| 6 | Add screenshot generator | Add `scripts/make_screenshots.py` that renders the printed output and figures of each lecture step to PNG files in `docs/images/` using the Agg backend, so no GUI is driven on the host desktop. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
