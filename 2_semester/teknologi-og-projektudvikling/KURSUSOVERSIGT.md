# 🗂️ KURSUS-OVERSIGT: Teknologi og Projektudvikling (5 ECTS)

## 📌 Kursusstruktur

Dette kursus strækker sig over 12 undervisningsdage og fokuserer på dataanalyse i Python, sensorintegration via ESP32, PLC-kommunikation via Snap7 og dokumentationspraksis med GitHub.

Node-RED indgår ikke i dette forløb for at sikre fokus på kernekompetencer inden for måling, databehandling og systemintegration.

Kursusplanen følger mappestrukturen i projektmappen:

```
📂 teknologi-og-projektudvikling/
├── undervisning/
│   ├── dag01_intro-github-python.md
│   ├── dag02_python-csv-pandas.md
│   ├── dag03_esp32-intro.md
│   ├── dag04_python-serial.md
│   ├── dag05_pandas-visualisering.md
│   ├── dag06_git-dokumentation.md
│   ├── dag07_miniprojekt-1.md
│   ├── dag08_python-databehandling.md
│   ├── dag09_snap7-plc.md
│   ├── dag10_dokumentation-test.md
│   ├── dag11_miniprojekt-2.md
│   └── dag12_praesentation.md
```

## 📅 Kursusforløb med fokusområder

| Dag | Emne                        | Hovedtema                                   |
| --- | --------------------------- | ------------------------------------------- |
| 1   | GitHub + Python intro       | Kursusintro, versionsstyring, Python-basics |
| 2   | Python + CSV + Pandas intro | Dataimport og analyse                       |
| 3   | ESP32 intro                 | Sensoropsætning og seriel dataudgang        |
| 4   | Python + pyserial           | Modtagelse og lagring af seriel data        |
| 5   | Pandas visualisering        | Glidende gennemsnit og plots                |
| 6   | Git og dokumentation        | Struktur, kravspecifikation, signalvej      |
| 7   | Mini-projekt 1              | Simpelt system fra sensor til CSV           |
| 8   | Python databehandling       | Rensning og strukturering af ESP32-data     |
| 9   | Snap7 + PLC-integration     | Data fra S7-PLC via Python                  |
| 10  | Dokumentation og test       | Blokdiagram, testlog, kravopfyldelse        |
| 11  | Mini-projekt 2              | Fuldt system og dokumentation               |
| 12  | Præsentation og evaluering  | Formidling og peer feedback                 |

## 🧰 Brugte teknologier

* **Python**: `pandas`, `matplotlib`, `pyserial`, `snap7`
* **ESP32**: sensorer, `analogRead()`, `Serial.print()`
* **Git/GitHub**: versionsstyring, `README.md`, projektsamarbejde
* **Siemens PLC**: Snap7-integration via Python

## 📋 Dokumentation

Studerende arbejder løbende med:

* Kravspecifikation (`README.md`)
* Signalbeskrivelser og blokdiagrammer (`docs/`)
* Testlog og dokumentation af datakvalitet og fejl
* Versionshistorik via Git

## ✅ Aflevering og evaluering

* Ét GitHub-repository per gruppe
* Indeholder ESP32-kode, Python scripts, CSV-filer og dokumentation
* Mundtlig fremlæggelse i slutningen af kurset (dag 12)

**Vurdering baseres på:**

* Funktionalitet og realiseret løsning
* Kvalitet af dokumentation og datastruktur
* Refleksion og præsentation

---

Denne kursusoversigt supplerer `LEKTIONSPLAN.md` og de daglige undervisningsfiler i `undervisning/`.
