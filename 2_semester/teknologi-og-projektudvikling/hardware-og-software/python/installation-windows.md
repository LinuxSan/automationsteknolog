# 🪟 Installation af nyeste Python-version i VS Code på Windows

Denne guide hjælper dig med at installere den nyeste version af Python og konfigurere det i Visual Studio Code på Windows.

---

## 🧰 Forudsætninger

* Du har allerede installeret Visual Studio Code
* Du har administratorrettigheder på din Windows-PC

---

## 1️⃣ Download og installer Python

1. Gå til den officielle side:
   👉 [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Klik på **Download Python 3.x.x** under "Latest"
3. Kør den downloadede installationsfil
4. **VIGTIGT!** Sæt flueben i:

   * ✅ "Add Python 3.x to PATH"
5. Klik på **Install Now**
6. Når installationen er færdig, klik på **Close**

---

## 2️⃣ Bekræft installationen

Åbn Kommandoprompt (cmd) og skriv:

```cmd
python --version
```

eller

```cmd
py --version
```

Du bør se noget ala `Python 3.12.x`

---

## 3️⃣ Installer Python-udvidelse i VS Code

1. Start Visual Studio Code
2. Gå til Extensions-panelet (venstre menu med 🔌-ikon)
3. Søg efter **Python** og vælg den officielle fra Microsoft
4. Klik på **Install**
5. (Valgfrit) Installer **Pylance**-udvidelsen for bedre IntelliSense

---

## 4️⃣ Vælg korrekt Python-fortolker

1. Åbn en `.py`-fil eller opret en ny
2. Klik på den viste Python-version i statusbaren (nederst til venstre)
3. Vælg den nyinstallerede `Python 3.x` fra listen

   * Hvis den ikke vises, tryk `Ctrl + Shift + P` → skriv: "Python: Select Interpreter"

---

## 5️⃣ Test din installation

1. Opret en fil `test.py` med følgende indhold:

```python
import sys
print("Din Python-version:", sys.version)
```

2. Højreklik på filen og vælg **Run Python File in Terminal**
3. Du bør nu se din Python-version printet i terminalen nederst i VS Code

---

## ✅ Klar til brug!

Python og VS Code er nu klar til brug. Du kan installere ekstra biblioteker via terminalen:

```cmd
pip install pandas matplotlib snap7
```

> Kontakt underviser hvis du har problemer med installationen eller opsætningen.
