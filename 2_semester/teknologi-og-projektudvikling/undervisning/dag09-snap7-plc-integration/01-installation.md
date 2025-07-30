<!-- File: dag09-snap7/01-installation.md -->

# 01 – snap7‑Installation & Smoke‑test

> *Første opgave på Dag 09 – Python ⇄ Siemens S7*

## 🎯 Formål

At installere **python‑snap7** i et isoleret miljø på både Windows **og** Linux, bekræfte at modulet kan importeres, samt udføre en hurtig “smoke‑test”, der forbinder til en S7‑PLC og læser ét byte for at verificere netværksadgang.

---

## 📂 Forudsætninger

| Krav              | Windows 11 / 10                   | Ubuntu 22.04 LTS         |
| ----------------- | --------------------------------- | ------------------------ |
| Python            | 3.9 – 3.12 (x64)                  | 3.9 – 3.12               |
| Compiler          | **Visual C++ Build Tools** (MSVC) | `build-essential`        |
| snap7 lib         | DLL følger med pip‑pakken         | `libsnap7-dev` (valgfri) |
| Admin‑rettigheder | Kun til VC‑installation           | Kun til `apt`            |

---

## 🔧 Trin for trin

### 1. Opret og aktiver virtuel env

```bash
# vælg mappe dag09-snap7/
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

### 2. Installér python‑snap7 (pip)

```bash
python -m pip install --upgrade pip
pip install python-snap7
```

Dette henter **prékompilerede binærfiler** (DLL/so) for dit OS.

### 3. Verificér import

```bash
python - << "PY"
import snap7, platform, sys
print("snap7 version:", snap7.__version__)
print("OS:", platform.system(), platform.release())
print("Python:", sys.version)
PY
```

Output skal vise snap7‑versionen uden Tracebacks.

### 4. Smoke‑test mod PLC

> **Tip:** Brug samme IP, rack & slot som i TIA Portal (fx `192.168.0.1`, rack 0, slot 1 for S7‑1200).

```python
# save as smoke_test.py
import snap7
from snap7.util import get_int
from snap7.snap7types import S7AreaDB

IP   = "192.168.0.1"
RACK = 0
SLOT = 1
DB   = 1
BYTES = 2  # læs 2 bytes

client = snap7.client.Client()
client.connect(IP, RACK, SLOT)

raw = client.read_area(S7AreaDB, DB, 0, BYTES)
print("DB1.DBB0‑1 as INT:", get_int(raw, 0))

client.disconnect()
```

Kør:

```bash
python smoke_test.py
```

Hvis scriptet printer en heltalsværdi **uden** fejl, er forbindelsen OK.

---

## 🛠️ Fejlfinding

| Fejlmeddelelse                             | Løsning                                                              |
| ------------------------------------------ | -------------------------------------------------------------------- |
| `OSError: [WinError 193]`                  | Sørg for at Python‑bitness (x64) matcher snap7‑DLL (x64).            |
| `ImportError: DLL load failed`             | Installér **Visual C++ Redistributable** (x64) og genstart terminal. |
| `ConnectError: CLI cannot connect`         | Tjek IP, subnet, firewall; ping PLC; bekræft rack/slot.              |
| `SystemError: missing libsnap7.so` (Linux) | `sudo apt install libsnap7-dev` eller reinstallér pip‑pakke.         |

---

## ✅ Afleveringskrav

* Skærmdump eller terminal‑output som viser succesfuld `import snap7` **og** værdien fra smoke‑test.
* Føj filen `smoke_test.py` til repoet (`src/`‑mappen).
* Opdater `.env.example` med `PLC_IP`, `RACK`, `SLOT` – **ingen** reelle credentials i repo.

*Done?* Commit & push:

```bash
git add src/smoke_test.py 01-installation.md .env.example
git commit -m "Dag09: Opgave 01 – snap7 installation og smoke‑test"
git push
```

---

*Tip:* Hvis du vil prøve en **Docker‑løsning**, findes en officielt vedligeholdt `snap7`‑container på Docker Hub – men den dækker ikke Windows‑drivere.
