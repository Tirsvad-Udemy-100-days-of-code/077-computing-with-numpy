# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [QC-WF-001], [QC-YML-001], [MIL-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Delta re-review of the failed criteria: Go | pending |

---

## Artifact Under Review

- Instance reviewed: `.gitea/workflows/tests.yml` ([MIL-001], task 5)
- Checklist used: [QC-WF-001] (`QC-WF-001`) and [QC-YML-001] (`QC-YML-001`)
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

Evidence (delta re-review 2026-11-12): `actionlint` 1.7.12 -> no findings, exit 0; `yamllint` 1.38.0 -> exit 0; PyYAML 6.0.3 safe load with duplicate-key check -> OK (initial review).

### QC-WF-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | Delta re-review: the YAML checklist rows 3 and 11 now pass. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | `.gitea/workflows/tests.yml` only; no `.github/` directory exists. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | `name: tests`, `on: push, pull_request`, `jobs: tests` (safe load). Filtering is judged in criterion 16. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | Header now has purpose, `Implements: MIL-001 task 5`, triggers, `Inputs: none`, secrets, outside changes, verified-on. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | Job `Python 3.13`, 7 uniquely named steps. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | `actionlint .gitea/workflows/tests.yml` -> no findings, exit 0; actionlint 1.7.12. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | Workflow-level `permissions: contents: read` applies to the only job. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch | Pass | `actions/checkout@11bd7190...` (v4.2.2) and `actions/setup-python@0b93645e...` (v5.3.0), both full SHAs. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | No secrets used. |
| 10 | Untrusted text is never interpolated into a `run:` script; it is passed through `env:` | Pass | No `${{ }}` in any `run:`; `github.ref` appears only in `concurrency.group`. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch does not check out or execute that code | N-A | Only `push` and `pull_request`; no `pull_request_target` or `workflow_run`. |
| 12 | A workflow that changes state outside the repository is started by hand or by a protected branch, and a manual run defaults to a dry run | N-A | Changes nothing outside the runner. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | Pass | (Optional) Read-only built-in token; no personal token. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | `runs-on: ubuntu-latest`, `timeout-minutes: 15`. |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`) | Pass | `group: tests-${{ github.ref }}`, `cancel-in-progress: true`. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | `push` limited to `branches: [main]`; `pull_request` kept, so a branch push is not run twice. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | `pip==26.3` pinned in the workflow; `pip install -c constraints.txt` pins numpy, matplotlib, pillow, pytest, ruff, mypy and yamllint to exact versions; Python 3.13. |
| 18 | A dependency cache is used where the install is slow enough to matter | Pass | (Optional) `cache: pip` in `actions/setup-python`. |
| 19 | A failing step names the tool, the file and the reason in its log | Pass | (Optional) ruff, mypy and pytest each print file and reason; steps are named per tool. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file that the step calls with one command | Pass | Longest `run:` block is 2 lines. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action | N-A | One workflow, no reuse. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | Header records `Gitea 28.3.0`. The act_runner version is not exposed by the host (accepted by S01). Re-confirm on the first CI run. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches | N-A | (Optional) Not a reusable workflow. |
| 24 | A static test of the repository's workflows exists and runs on every pull request | Fail | (Optional) No static workflow test in `tests/`; deferred (accepted); actionlint and yamllint run by hand and yamllint runs in CI. |

### QC-YML-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | PyYAML 6.0.3 `SafeLoader` with a duplicate-key check -> parsed; top-level keys name, on, permissions, concurrency, jobs; no duplicates. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | `file` -> ASCII text; 0 CR; no trailing spaces; last byte is a single LF. |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | `.yamllint` committed (extends default; line-length 100, `truthy` and `document-start` set in the config, no `disable` comments); `yamllint 1.38.0 .gitea .yamllint` -> exit 0; also run as a CI step. |
| 4 | A scalar that YAML would coerce to another type is quoted | Pass | `python-version: "3.13"` is quoted. Key `on` is unquoted as Actions expects (PyYAML reads it as `true`; actionlint accepts it). |
| 5 | Only safe, plain types are used: no language-specific tags | Pass | No `!!` tags. |
| 6 | No secret is written in the file | Pass | No credentials present. |
| 7 | Embedded program text in a value is at most five lines | Pass | Longest `run:` block is 2 lines. |
| 8 | A block of keys or values repeated in the file or across files is defined once | Pass | No repetition. |
| 9 | Anchors, aliases and merge keys are used only where the consuming tool is known to support them | N-A | None used. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | Pass | (Optional) actionlint 1.7.12 validates the workflow schema, no findings. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | Header states purpose, the tool (Gitea Actions) and the milestone it implements (`MIL-001 task 5`). |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file | Pass | `runs-on`, `timeout-minutes`, `cancel-in-progress`, `python-version`: kebab-case as Actions requires. |
| 13 | Multi-line strings use a block scalar and state the chomping indicator where the trailing newline matters | Pass | (Optional) `run: |` blocks; the trailing newline does not matter. |
| 14 | The file name is lowercase kebab-case with one extension style used throughout the repository | Pass | (Optional) `tests.yml`; only `.yml` in the repository. |
| 15 | A change is exercised by a check that runs without the real target | Pass | (Optional) actionlint runs without a runner (run manually here). |

## Overall Verdict

Go — the delta re-review finds all six Mandatory failures (QC-WF-001 4, 16, 17, 22; QC-YML-001 3, 11) fixed, and actionlint and yamllint are clean. The only open item is QC-WF-001 24 (Optional, deferred, accepted), which does not block. The act_runner version is not recorded because the host does not expose it.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Optional: add a static workflow test to `tests/` (QC-WF-001 24) | S01 | later milestone |
| Confirm the header's Gitea version on the first green CI run | S01 | first CI run |

---

[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[MIL-001]: ../../milestones/mil-001-project-setup.md
