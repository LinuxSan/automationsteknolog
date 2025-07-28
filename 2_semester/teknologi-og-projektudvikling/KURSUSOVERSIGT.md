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
│   ├── dag06_sanity-timestamp.md
│   ├── dag07_miniprojekt-1.md
│   ├── dag08_python-databehandling.md
│   ├── dag09_snap7-plc.md
│   ├── dag10_dokumentation-test.md
│   ├── dag11_miniprojekt-2.md
│   └── dag12_praesentation.md
```

## 📅 Kursusforløb med fokusområder

| Dag | Emne                          | Hovedtema                                          |
| --- | ----------------------------- | -------------------------------------------------- |
| 1   | GitHub + Python intro         | Kursusintro, versionsstyring, Python-basics        |
| 2   | Python + CSV + Pandas intro   | Dataimport og analyse                              |
| 3   | ESP32 intro                   | Sensoropsætning og seriel dataudgang               |
| 4   | Python + pyserial             | Modtagelse og lagring af seriel data               |
| 5   | Pandas visualisering          | Glidende gennemsnit og plots                       |
| 6   | Sanity checks + tidsstempling | Datavalidering, grænseværdier, fejlhåndtering, tid |
| 7   | Mini-projekt 1                | Simpelt system fra sensor til CSV                  |
| 8   | Python databehandling         | Rensning og strukturering af ESP32-data            |
| 9   | Snap7 + PLC-integration       | Data fra S7-PLC via Python                         |
| 10  | Dokumentation og test         | Blokdiagram, testlog, kravopfyldelse               |
| 11  | Mini-projekt 2                | Fuldt system og dokumentation                      |
| 12  | Præsentation og evaluering    | Formidling og peer feedback                        |

Forstået – her er den justerede version med "studerende" i stedet for "elever":

---

### 📆 Dag-for-dag beskrivelse

**🛠️ Dag 1 – GitHub + Python intro**
Kursusstart med fokus på versionsstyring og samarbejde. De studerende opretter deres første GitHub-repository, lærer at bruge GitHub CLI og skriver simple Python-programmer for at få grundlæggende styr på syntaks, variabler og kontrolstrukturer.

**📊 Dag 2 – Python + CSV + Pandas intro**
Introduktion til databehandling i Python. De studerende lærer at læse og skrive CSV-filer, og bruger `pandas` til at analysere datasæt med funktioner som `read_csv()`, `head()` og `describe()`.

**📡 Dag 3 – ESP32 intro**
Fokus på hardware: sensorvalg, forbindelser og brug af `analogRead()`. ESP32 programmeres med Arduino IDE og sender data ud via seriel kommunikation, som vises i Serial Monitor.

**🔌 Dag 4 – Python + pyserial**
ESP32 kobles sammen med Python via `pyserial`. De studerende opsætter et script, der læser data i realtid, gemmer det i CSV-filer og forbereder det til videre analyse.

**📈 Dag 5 – Pandas visualisering**
Python-data visualiseres med `matplotlib`. Fokus på filtrering, glidende gennemsnit og hvordan man præsenterer målinger i overskuelige grafer.

**🧠 Dag 6 – Sanity checks + tidsstempling**
Validering af måledata med Python. De studerende implementerer grænseværdier, outlier-filtrering og fejlhåndtering. `datetime` bruges til at tidsstemple data for at sikre sporbarhed.

**🔧 Dag 7 – Mini-projekt 1**
Grupperne anvender de første seks dages viden til at opbygge et simpelt system fra sensor til CSV og visualisering – med fokus på struktur og klar dokumentation.

**🧹 Dag 8 – Python databehandling**
Fokus på dataoprensning: fjernelse af fejlmålinger, brug af rullende gennemsnit og eksport af færdige datasæt. Data gøres klar til præsentation og dokumentation.

**🏭 Dag 9 – Snap7 + PLC-integration**
Python forbindes til en Siemens S7 PLC via Snap7. De studerende læser én variabel fra en datablock og visualiserer data, som alternativ til ESP32-input.

**🗂️ Dag 10 – Dokumentation og tests**
Fokus på projektafslutning: signalbeskrivelser, blokdiagrammer og testlogs. Grupperne arbejder i `docs/` og bruger deres GitHub-repo som afleveringsplatform.

**🔬 Dag 11 – Mini-projekt 2**
Grupperne laver en samlet løsning: sensor- eller PLC-input → Python-analyse → dokumentation. GitHub-strukturen færdiggøres og kvalitetssikres.

**🎤 Dag 12 – Fremlæggelse og evaluering**
Mundtlig præsentation af projekterne. Hver gruppe fremlægger deres løsning, modtager feedback og evalueres på funktion, dokumentation og refleksion.

## 🧰 Brugte teknologier

* **Python**: `pandas`, `matplotlib`, `pyserial`, `snap7`, `datetime`
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
