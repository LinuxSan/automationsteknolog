# 🍎 Installation af nyeste Python-version i VS Code på macOS

Denne guide hjælper dig med at installere den nyeste version af Python og integrere den korrekt i Visual Studio Code på macOS.

---

## 🧰 Forudsætninger

* macOS 11 eller nyere
* Visual Studio Code er installeret
* Terminal-adgang (Cmd + Space → "Terminal")

---

## 1️⃣ Installer Homebrew (hvis nødvendigt)

Homebrew er den anbefalede pakkehåndtering til macOS:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Test om det virker:

```bash
brew --version
```

---

## 2️⃣ Installer nyeste Python med Homebrew

```bash
brew install python@3.12
```

Bekræft installationen:

```bash
python3 --version
```

Du bør se fx: `Python 3.12.x`

---

## 3️⃣ (Valgfrit) Tilføj Python 3.12 som default alias

```bash
echo 'alias python=python3' >> ~/.zshrc
source ~/.zshrc
```

---

## 4️⃣ Installer VS Code Python Extension

1. Start Visual Studio Code
2. Gå til Extensions-panelet (🔌)
3. Søg efter **Python** og vælg den fra Microsoft
4. Klik **Install**
5. (Valgfrit) Installer også **Pylance** for avanceret kodehjælp

---

## 5️⃣ Vælg Python-fortolker i VS Code

1. Åbn en `.py`-fil eller opret en ny
2. Klik på Python-versionen i statuslinjen nederst i vinduet
3. Vælg den nyinstallerede `Python 3.12` fra Homebrew

   * Hvis den ikke vises, tryk `Cmd + Shift + P` → "Python: Select Interpreter"

---

## 6️⃣ Test din installation

Opret en fil `test.py` med:

```python
import sys
print("Din Python-version:", sys.version)
```

Kør filen i terminalen eller med **Run Python File in Terminal** i VS Code

---

## ✅ Klar til brug!

Du har nu installeret og konfigureret den nyeste version af Python til brug i VS Code på macOS.

> Du kan nu installere biblioteker med `pip3 install pandas matplotlib snap7`

Spørg underviser ved problemer med installation eller opsætning.
