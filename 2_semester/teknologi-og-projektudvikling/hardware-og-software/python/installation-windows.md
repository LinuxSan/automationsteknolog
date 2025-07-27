# 🐍 Installation af nyeste Python-version i Visual Studio Code (Windows/macOS/Linux)

Denne guide hjælper dig med at installere den nyeste version af Python og sikre korrekt integration i Visual Studio Code.

---

## 🧰 Forudsætninger

* Du har allerede installeret VS Code
  (se evt. installationsguide for dit styresystem)
* Internetforbindelse og rettigheder til at installere software

---

## 1️⃣ Download og installer Python

1. Gå til den officielle side:
   👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Klik på **Download Python 3.x.x** (øverste version)
3. Kør installationsfilen
4. **VIGTIGT:** Sæt flueben i:

   * ✅ "Add Python 3.x to PATH"
5. Klik "Install Now"

> macOS: Installer `.pkg`-filen.
> Linux: Brug evt. `sudo apt install python3.11` eller nyeste via source.

---

## 2️⃣ Bekræft installationen

Åbn terminal (eller kommandoprompt på Windows):

```bash
python --version
```

eller

```bash
python3 --version
```

Du skal se den nyeste version f.eks. `Python 3.12.x`

---

## 3️⃣ Opsætning i Visual Studio Code

1. Start VS Code
2. Åbn en `.py`-fil eller opret en ny
3. Klik på **Python-versionen** i øverste højre hjørne af editoren (eller nede i statusbaren)
4. Vælg den Python 3.x-installation du netop har installeret

   * Hvis den ikke vises: Tryk `Ctrl + Shift + P` → "Python: Select Interpreter"

---

## 4️⃣ Installer Python-udvidelse i VS Code

1. Gå til Extensions (🔌-ikon i venstre menu)
2. Søg efter **Python** (Microsoft)
3. Klik **Install**
4. (Valgfrit) Installer også **Pylance** for bedre IntelliSense og ydeevne

---

## 5️⃣ Test det hele virker

1. Opret en fil `test.py`:

```python
import sys
print("Din Python-version:", sys.version)
```

2. Kør filen via højreklik → **Run Python File in Terminal**
3. Du bør se din aktuelle Python-version printet

---

## ✅ Klar til brug!

Du har nu den nyeste Python-version integreret i Visual Studio Code og kan begynde at kode og analysere data uden problemer.

> Tip: Brug `pip install` i terminalen for at installere ekstra biblioteker (f.eks. `pandas`, `matplotlib`, `snap7`)

Kontakt underviser hvis du oplever fejl eller har brug for hjælp til opsætningen.
