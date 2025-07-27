# 🐧 Installation af nyeste Python-version i VS Code på Linux (Ubuntu/Debian)

Denne guide viser, hvordan du installerer den nyeste version af Python og konfigurerer den til brug i Visual Studio Code på et Linux-system.

---

## 🧰 Forudsætninger

* Ubuntu/Debian-baseret Linux
* Terminal med sudo-adgang
* Visual Studio Code installeret

---

## 1️⃣ Installer Python 3.12 (eller nyeste) via deadsnakes PPA

```bash
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-distutils -y
```

---

## 2️⃣ Gør Python 3.12 til standard (valgfrit)

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1
```

Tjek version:

```bash
python3 --version
```

---

## 3️⃣ Installer pip og venv

```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12
python3.12 -m ensurepip
python3.12 -m pip install --upgrade pip
```

---

## 4️⃣ Konfigurer VS Code til at bruge ny Python-version

1. Start VS Code
2. Åbn en `.py`-fil eller opret en ny
3. Klik på Python-versionen i statusbaren (nederst)
4. Vælg Python 3.12 fra listen (hvis ikke synlig, tryk `Ctrl + Shift + P` → "Python: Select Interpreter")

---

## 5️⃣ Installer Python Extension i VS Code

1. Gå til Extensions-panelet (🧩)
2. Søg efter **Python** og vælg den fra Microsoft
3. Klik **Install**
4. (Valgfrit) Installer **Pylance** for avanceret funktionalitet

---

## 6️⃣ Test din installation

Opret og kør `test.py`:

```python
import sys
print("Din Python-version:", sys.version)
```

Kør i terminal eller via **Run Python File in Terminal** i VS Code

---

## ✅ Klar til brug!

Du har nu den nyeste version af Python installeret og integreret med VS Code på Linux.

> Du kan nu installere moduler med `python3.12 -m pip install pandas matplotlib` og begynde at analysere data.

Kontakt underviser ved problemer eller spørgsmål.
