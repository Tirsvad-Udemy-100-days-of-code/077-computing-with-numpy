**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

Requirements: Python 3.13 or newer. Runtime libraries: NumPy, Matplotlib and Pillow.

Create and use a local `.venv` (Windows PowerShell):

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

Run the lesson, the tests and the notebook:

```bash
python -m computing_with_numpy
python -m pytest
jupyter lab notebooks/computing_with_numpy.ipynb
```

Run the static scan before you push (Windows PowerShell, then Linux and macOS):

```powershell
.\scripts\check-opengrep.ps1
```

```bash
bash scripts/check-opengrep.sh
```

![Setup: Python and NumPy](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/00-setup.png)

## What you gain

- A repeatable set-up: one virtual environment per project, so libraries never clash.
- A package installed in editable mode, so your edits take effect at once.
- Tests that prove each answer of the lecture.
