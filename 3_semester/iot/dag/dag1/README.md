# 📄 Modul 01 – Introduktion til Node‑RED og flow‑struktur

## 🎯 Formål

Dette første modul giver dig et solidt fundament i Node‑RED som visuelt programmerings‑ og dataintegrationsværktøj til industrielle opgaver. Du lærer centrale begreber som **node**, **flow**, `msg.payload`, runtime og *deploy*‑cyklussen og får hænderne på de vigtigste standardnoder.

---

## 📁 Modulstruktur

```
01-intro/
├── 01-installation-node-red/
│   ├── README.md   # installationsguide (lokal & Docker)
│   └── install_checklist.md
├── 02-foerste-flow/
│   ├── README.md   # inject → debug (”Hello flow”)
│   └── first_flow.json
├── 03-node-red-begreber/
│   ├── README.md   # msg, payload, topic, flow, context
│   └── cheat_sheet.pdf
└── 04-standardnoder/
    ├── 01-inject.md    # timestamp, string, repeat
    ├── 02-debug.md     # debug‑pane & levels
    ├── 03-function.md  # custom JS, msg‑objekt
    ├── 04-change.md    # set, move, delete
    ├── 05-switch.md    # routing på payload/topic
    ├── 06-delay.md     # rate‑limit & queue
    └── 07-template.md  # HTML & mustache‐output
```

> *Hver undermappe fungerer som mini‑workshop med kort teori, trinvise øvelser og færdige flow‑filer.*

---

## ⏲️  Tidsplan (3 × 45 min)

| Klokkeslæt      | Aktivitet          | Indhold                                                             |
| --------------- | ------------------ | ------------------------------------------------------------------- |
| **0:00 – 0:10** | Intro & målsætning | Kursusramme, repo‑struktur, forventninger                           |
| **0:10 – 0:35** | Teori ①            | Node‑RED‑arkitektur, noder, wires, deploy → live‑demo               |
| **0:35 – 1:00** | Teori ②            | `msg.payload`, topic, flow‑context, standardnoder (inject, debug)   |
| **1:00 – 2:30** | Hands‑on A         | *01-installation-node-red* → installér, kør editor, tag screenshot  |
| **2:30 – 2:50** | Hands‑on B         | *02-foerste-flow* → importér `first_flow.json`, udvid med ui\_gauge |
| **2:50 – 3:00** | Opsamling          | Git commit & push, Q\&A, preview af Dag 02 (MQTT)                   |

---

## ✅ Læringsudbytte

Efter Modul 01 kan du

* installere og starte Node‑RED lokalt eller med Docker,
* forklare forskellen på node, wire og flow,
* bygge og deploye et simpelt *inject → debug*‑flow,
* bruge **ui\_gauge** og **ui\_chart** til at visualisere en dummy‑værdi,
* gemme og importere flows (.json) og committe til Git.

---

## 🔧 Forudsætninger

* Laptop med **Docker Desktop** eller **Node.js ≥ 18** installeret.
* Git‑klient og GitHub‑konto (SSH‑nøgle sat op).
* Browser (Chrome/Edge/Firefox) til Node‑RED‑editoren.

---

## 🏋️‍♀️ Opgaver & afleveringer

1. **Installation Check** – udfyld `install_checklist.md` og commit.
2. **Hello Flow** – importer `first_flow.json`, udvid med *ui\_gauge*, tag screenshot `hello_dashboard.png` og commit.
3. **Forklar begreber** – i `03-node-red-begreber/README.md` beskriv med maks 100 ord forskellen mellem `msg.payload` og `msg.topic`.
4. *(Stretch)* Tilføj en **delay‑node** der publicerer tidspunkter hvert 2 s og vis graf i *ui\_chart*.

Aflevering sker som pull‑request til branch `day01_<navn>`.

---

## 💡 Videre arbejde

Når du er færdig med alle mini‑workshops i `01-intro/`, fortsæt til `dag02_mqtt_telemetri/README.md`, hvor du kobler Node‑RED op mod en MQTT‑broker og ESP32‑sensoren.

Happy hacking! 🚀
