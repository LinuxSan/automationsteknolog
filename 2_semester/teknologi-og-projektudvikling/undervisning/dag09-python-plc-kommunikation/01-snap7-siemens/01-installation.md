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