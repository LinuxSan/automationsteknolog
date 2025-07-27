
# 🗂️ KURSUS-OVERSIGT: Teknologi og Projektudvikling (5 ECTS)

## 📌 Kursusstruktur

Dette kursus strækker sig over 12 undervisningsdage og kombinerer visuel programmering i Node-RED, dataanalyse i Python, sensorintegration via ESP32 og dokumentationspraksis med GitHub.

Kursusplanen følger mappestrukturen i projektmappen:

```
📂 teknologi-og-projektudvikling/
├── undervisning/
│   ├── dag01_node-red-intro.md
│   ├── dag02_node-red-serial.md
│   ├── dag03_python-intro.md
│   ├── dag04_python-pandas.md
│   ├── dag05_python-serial.md
│   ├── dag06_git-og-dokumentation.md
│   ├── dag07_miniprojekt-1.md
│   ├── dag08_esp32-sensor.md
│   ├── dag09_node-python-plc.md
│   ├── dag10_dokumentation.md
│   ├── dag11_miniprojekt-2.md
│   └── dag12_praesentation.md
```

## 📅 Kursusforløb med fokusområder

| Dag | Emne                            | Hovedtema                          |
| --- | ------------------------------- | ---------------------------------- |
| 1   | Node-RED + GitHub intro         | Flow-forståelse og versionskontrol |
| 2   | Seriel data i Node-RED          | Kommunikation med hardware         |
| 3   | Python intro                    | Grundlæggende programmering        |
| 4   | Pandas og datavisualisering     | Dataanalyse og grafer              |
| 5   | Seriel læsning i Python         | Input fra ESP32                    |
| 6   | Git og dokumentation            | Projekthåndtering og dokumentation |
| 7   | Mini-projekt 1                  | Simpelt system fra sensor til CSV  |
| 8   | ESP32 sensoropsætning           | Hardware og dataoutput             |
| 9   | Node-RED + Python + PLC (Snap7) | Integration til Siemens PLC        |
| 10  | Dokumentation og test           | Signalvej, blokdiagram, testlog    |
| 11  | Mini-projekt 2                  | Fuldt system og dokumentation      |
| 12  | Præsentation og evaluering      | Formidling og peer feedback        |

## 🧰 Brugte teknologier

* **Node-RED**: datastrømme, dashboard, seriel input
* **Python**: `pandas`, `matplotlib`, `pyserial`, `snap7`
* **ESP32**: sensorer, `analogRead()`, `Serial.print()`
* **Git/GitHub**: versionsstyring, `README.md`, projektsamarbejde
* **Siemens PLC**: Snap7-integration via Python

## 📋 Dokumentation

Studerende arbejder løbende med:

* Kravspecifikation (`README.md`)
* Flowdiagrammer og signalbeskrivelser (`docs/`)
* Testlog og dokumentation af fejl/ændringer
* Versionshistorik via Git

## ✅ Aflevering og evaluering

* Et GitHub-repository per gruppe
* Inkluderer Node-RED flows, ESP32-kode, Python scripts og dokumentation
* Afleveres og præsenteres mundtligt i uge 12

**Vurdering baseres på:**

* Funktionalitet og realiseret system
* Dokumentation og versionsstyring
* Præsentation og refleksion

---

Denne kursusoversigt supplerer `LEKTIONSPLAN.md` og de daglige undervisningsfiler i `undervisning/`.
