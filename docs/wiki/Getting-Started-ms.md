[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Bermula

Keperluan: Python 3.13 atau lebih baharu. Pustaka runtime: NumPy, Matplotlib dan Pillow.

Cipta dan gunakan `.venv` setempat (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux dan macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Jalankan pelajaran, ujian dan notebook:

```bash
python -m computing_with_numpy
python -m pytest
jupyter lab notebooks/computing_with_numpy.ipynb
```

Jalankan imbasan statik sebelum anda push (Windows PowerShell, kemudian Linux dan macOS):

```powershell
.\scripts\check-opengrep.ps1
```

```bash
bash scripts/check-opengrep.sh
```

![Persediaan: Python dan NumPy](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/00-setup.png)

## Apa yang anda peroleh

- Persediaan yang boleh diulang: satu persekitaran maya bagi setiap projek, supaya pustaka tidak bercanggah.
- Pakej yang dipasang dalam mod editable, supaya suntingan anda berkuat kuasa serta-merta.
- Ujian yang membuktikan setiap jawapan kuliah.
