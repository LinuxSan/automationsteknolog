# 📆 LEKTIONSPLAN – Teknologi og Projektudvikling (5 ECTS)

**Uddannelse:** Automationsteknolog
**Semester:** 2. semester
**Varighed:** 12 undervisningsdage
**ECTS:** 5

---

## 📅 Oversigt over lektionsindhold og progression

| Dag | Tema                          | Indhold                                                                     | Output                                 |
| --- | ----------------------------- | --------------------------------------------------------------------------- | -------------------------------------- |
| 1   | GitHub + Python intro         | Introduktion til kurset, opstart af GitHub-repo, basis Python-programmering | README.md, `basis.py`, `.gitignore`    |
| 2   | Python + CSV + Pandas intro   | Læs/skriv CSV, Pandas `read_csv`, `head()`, `describe()`                    | Simpel CSV-analyse                     |
| 3   | ESP32 intro                   | analogRead, Serial output struktur, sensorvalg                              | `sensor.ino`, debug via Serial Monitor |
| 4   | Python + pyserial             | Læs ESP32-seriel data, gem som CSV, vis i `matplotlib`                      | Real-time datalogger i Python          |
| 5   | Pandas visualisering          | `matplotlib`, filtrering, glidende gennemsnit                               | Grafer og renset data                  |
| 6   | Sanity checks + tidsstempling | Validering af måledata, grænseværdier, fejlhåndtering, `datetime`-modulet   | `sanity.py`, `timestamp_logger.py`     |
| 7   | Mini-projekt 1                | Sensor → CSV → visualisering i Python                                       | Projektstruktur og dokumentation       |
| 8   | Python databehandling         | Databehandling af ESP32-målinger i Pandas, visualisering og eksport         | Renset datasæt til dokumentation       |
| 9   | Snap7 + PLC-integration       | Læs én DB-variabel fra S7 PLC i Python                                      | `plc_read.py`, datavisualisering       |
| 10  | Dokumentation og tests        | Blokdiagram, testlog, signalbeskrivelse                                     | `docs/` komplet til projekt            |
| 11  | Mini-projekt 2                | Sensor → Python → Analyse → Dokumentation                                   | Klar GitHub-projektmappe               |
| 12  | Fremlæggelse og evaluering    | Mundtlig præsentation, peer-review og opsamling                             | Projektfeedback                        |

---

## 🧠 Metoder

* Praktiske øvelser og prototyper
* Opgaver i grupper (maks 3 personer)
* Brug af GitHub og Markdown som dokumentationsplatform
* Brug af Python som samlet analyse- og kommunikationsværktøj

## 📂 Ressourcer og værktøjer

* Python (VS Code eller Jupyter)
* ESP32 med sensorer (DHT22, potmeter, etc.)
* Siemens S7 PLC eller simulator (Snap7)
* Git + GitHub til versionsstyring og dokumentation

---

Dette dokument understøtter dag-til-dag planlægning og skal anvendes sammen med `KURSUS-OVERSIGT.md` og mapperne under `undervisning/`.
