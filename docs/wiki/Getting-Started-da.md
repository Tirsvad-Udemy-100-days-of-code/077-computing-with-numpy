[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

Krav: Python 3.13 eller nyere. Biblioteker ved kørsel: NumPy, Matplotlib og Pillow.

Opret og brug et lokalt `.venv` (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux og macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Kør lektionen, testene og notebooken:

```bash
python -m computing_with_numpy
python -m pytest
jupyter lab notebooks/computing_with_numpy.ipynb
```

Kør den statiske scanning, før du pusher (Windows PowerShell, derefter Linux og macOS):

```powershell
.\scripts\check-opengrep.ps1
```

```bash
bash scripts/check-opengrep.sh
```

![Opsætning: Python og NumPy](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/00-setup.png)

## Det får du ud af det

- En gentagelig opsætning: ét virtuelt miljø pr. projekt, så biblioteker aldrig kommer i konflikt.
- En pakke installeret i redigerbar tilstand, så dine ændringer virker med det samme.
- Tests, der beviser hvert svar i lektionen.
