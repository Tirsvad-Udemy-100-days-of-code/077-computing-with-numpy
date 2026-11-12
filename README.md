# 🚀 077 Computing with NumPy

Day 77 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp": NumPy ndarrays, slicing, generated arrays, broadcasting, matrix multiplication and images as arrays. Every challenge is a tested function with the assignment's name, for coursists who want to compare solutions and for visitors browsing the repository.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [Lecture steps](#-lecture-steps)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

| Part | What it is for |
| --- | --- |
| `src/computing_with_numpy/domain/` | The NumPy computations of each challenge, with the assignment's function names |
| `src/computing_with_numpy/application/` | The lecture steps and their output |
| `src/computing_with_numpy/infrastructure/` | Charts, image files and screenshots (Agg backend, no window) |
| `src/computing_with_numpy/presentation/` | The command line |
| `tests/` | One test per challenge result stated in the lecture |
| `notebooks/` | The Jupyter notebook that walks through the lecture |
| `docs/` | Project documents, screenshots (`docs/images/`) and the wiki (`docs/wiki/`) |
| `scripts/` | Screenshot generator and the opengrep check |

## 📋 Requirements

- Python 3.13 or newer (`python --version`).
- Runtime libraries, installed by `pip`: NumPy, Matplotlib and Pillow, the minimum the lecture needs.
- Development tools, only for tests and the notebook: pytest, ruff, mypy, JupyterLab.

## 🛠️ Setup

Create and use a local `.venv`, upgrade `pip`, then install the project in editable mode.

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Without the development tools, install `python -m pip install -e .` instead.

![Setup: Python and NumPy](docs/images/00-setup.png)

## ▶️ Run

```bash
python -m computing_with_numpy
jupyter lab notebooks/computing_with_numpy.ipynb
python scripts/make_screenshots.py
```

The first command prints every lecture step; the last one rewrites the screenshots in `docs/images/`. Charts are saved to files, so no window opens.

## 🧪 Tests

```bash
python -m pytest
ruff check .
ruff format --check .
mypy src
```

Run the static scan with opengrep before every push (`~\.opengrep\cli\latest\opengrep.exe` on Windows):

```bash
bash scripts/check-opengrep.sh
```

```powershell
.\scripts\check-opengrep.ps1
```

## 🖼️ Lecture steps

The setup step is shown above. Each later milestone adds its steps, their functions and a screenshot here.

## 📄 License

GNU Affero General Public License v3, see [LICENSE](./LICENSE).

## 🔗 Links

- [Repository][repository]
- [Wiki][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
