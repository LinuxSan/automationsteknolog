# 🍎 Installation af Visual Studio Code på macOS

Denne guide viser, hvordan du installerer Visual Studio Code og konfigurerer det til Python-programmering på en Mac.

---

## 🧰 Forudsætninger

* En Mac med macOS 11 (Big Sur) eller nyere
* Internetforbindelse

---

## 1️⃣ Installer VS Code

1. Gå til den officielle hjemmeside:
   👉 [https://code.visualstudio.com](https://code.visualstudio.com)
2. Klik på **Download for macOS**
3. Åbn den downloadede `.zip`-fil og træk **Visual Studio Code** til din `Programmer`-mappe
4. Start programmet via Launchpad eller Finder

---

## 2️⃣ Tilføj VS Code til din terminal (valgfrit, men anbefales)

1. Åbn VS Code
2. Tryk `Cmd + Shift + P` for at åbne kommando-paletten
3. Skriv og vælg: **Shell Command: Install 'code' command in PATH**
4. Genstart evt. terminalen

Herefter kan du åbne mapper med:

```bash
code .
```

---

## 3️⃣ Installer Python (hvis nødvendigt)

1. Tjek om du allerede har Python installeret:

```bash
python3 --version
```

2. Hvis ikke, download fra:
   👉 [https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/)
3. Kør `.pkg`-installationsfilen og følg anvisningerne

---

## 4️⃣ Installer Python-udvidelsen i VS Code

1. Start VS Code
2. Gå til Extensions (🧩-ikon i venstre sidebar)
3. Søg efter **Python** og vælg udvidelsen fra Microsoft
4. Klik **Install**
5. (Valgfrit) Installer **Pylance** for bedre IntelliSense

---

## 5️⃣ Test din installation

1. Opret en mappe og en ny fil, fx `hello.py`

```bash
mkdir -p ~/projekter/teknologi
cd ~/projekter/teknologi
code hello.py
```

2. Skriv følgende kode:

```python
print("Hej fra macOS og VS Code!")
```

3. Tryk `Cmd + Shift + P` → vælg **Run Python File in Terminal**

Du burde nu se output i terminalen nederst i VS Code.

---

## ✅ Klar til brug!

VS Code og Python er nu installeret og konfigureret på din Mac.

> Overvej også at installere Git og oprette en GitHub-konto hvis du skal arbejde med versionsstyring og samarbejde.

Kontakt underviser ved installationsproblemer.
