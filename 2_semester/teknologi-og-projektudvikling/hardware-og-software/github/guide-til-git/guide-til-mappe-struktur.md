# 📁 Studerendes standard mappestruktur – Teknologi og Projektudvikling

Denne struktur er den officielle, obligatoriske mappestruktur for studerende på faget *Teknologi og Projektudvikling*. Alle grupper skal følge den, så underviser kan give feedback, vurdere dokumentation og følge med i arbejdet.

---

## 📦 Obligatorisk mappestruktur

```plaintext
📂 gruppe-xx-projekt/
├── 📁 docs/                  # Teknisk dokumentation
│   ├── kravspecifikation.md
│   ├── signalbeskrivelse.md
│   ├── testplan.md
│   └── blokdiagram.drawio
│
├── 📁 data/                  # Sensor-data (CSV), evt. dummy data
│   ├── raw.csv
│   └── cleaned.csv
│
├── 📁 esp32/                 # .ino-filer til ESP32 kode (Arduino IDE)
│   └── main.ino
│
├── 📁 python/                # Python scripts og notebooks
│   ├── reader.py
│   ├── analyse.ipynb
│   └── plot.py
│
├── 📁 tests/                 # Testkørsler, mock scripts
│   └── dummy_serial.py
│
├── README.md                # Kort opsummering af projektet (1. side!)
├── .gitignore               # Udelad fx .csv, .pyc, .vscode osv.
```

---

## 🧠 Noter og regler

* Brug **gruppe-xx-projekt** som mappenavn (fx `gruppe-07-projekt`)
* Der må **ikke ændres i mappestrukturen** uden tilladelse
* **README.md** skal være opdateret og forklare projektets formål, arkitektur og status
* `.gitignore` skal anvendes korrekt
* Alle scripts skal placeres i relevante mapper – ingen rod i roden!

---

## 🧪 Eksempel på .gitignore

```gitignore
# Python
__pycache__/
*.pyc

# Arduino
*.elf
*.hex

# Data
*.csv
*.json

# IDE/OS
.vscode/
.DS_Store
Thumbs.db
```

---

## 🔍 Husk

* Projektet afleveres som GitHub-repository (privat eller public)
* Den struktur her bruges til vurdering – projekter uden denne struktur får ikke fuld vurdering
* Underviser skal kunne finde og åbne:

  * ESP32 kode
  * Python-analyse
  * Datagrundlag
  * Dokumentation (Markdown og diagrammer)

> Enhver afvigelse skal begrundes og godkendes.

# ❓ Hvad er .gitignore?

`.gitignore` er en tekstfil, som du placerer i roden af dit Git-projekt for at fortælle Git, hvilke filer og mapper det **ikke** skal holde styr på (altså ignorere).

Dette er nyttigt for at undgå at inkludere:

* Midlertidige filer genereret af dit operativsystem eller din editor (fx `.DS_Store`, `Thumbs.db`, `.vscode/`)
* Store filer og datafiler (fx `.csv`, `.zip`, `.log`), der ikke skal versionsstyres
* Lokale build-filer eller cache-filer (fx `__pycache__/`, `*.pyc`)

---

## 🧰 Hvordan virker det?

Når Git ser en fil i `.gitignore`, ignorerer den filen **fra og med næste gang**, hvis den ikke allerede er tracket.

### Eksempel på .gitignore:

```gitignore
# Python cache-filer
__pycache__/
*.pyc

# VS Code mappe
.vscode/

# Data og logs
*.csv
*.json
*.log

# Operativsystem-filer
.DS_Store
Thumbs.db
```

---

## 📌 Bemærk:

* `.gitignore` virker kun på filer, der **ikke allerede er tracket** af Git. Har du fx allerede committed en `.csv`, skal du fjerne den først:

```bash
git rm --cached fil.csv
```

* `.gitignore` kan opdateres løbende i et projekt
* Du kan have flere `.gitignore`-filer i undermapper, hvis du vil ignorere mapper lokalt

---

## ✅ Fordele ved at bruge .gitignore

* Din Git-historik bliver ryddelig og hurtigere
* Du undgår utilsigtet at dele følsomme eller unødvendige filer
* Det bliver nemmere for andre at clone og arbejde med dit projekt

> Brug `.gitignore` sammen med god mappestruktur og `README.md` for at gøre dit projekt professionelt og samarbejdsklart.
