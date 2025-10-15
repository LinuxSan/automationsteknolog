<!-- File: dag09-snap7/05-dashboard.md -->

# 05 – Mini‑Dashboard (CLI eller Web)

*Del af **Dag 09 – Python ⇄ Siemens S7 med snap7***

---

## 📘 Introduktion

Efter at have læst, logget og skrevet PLC‑data mangler vi ét sidste trin for at få en komplet DevOps‑pipeline: **real‑time visualisering**. Et hurtigt dashboard gør det muligt for operatør eller underviser at følge procesværdierne i øjeblikket, spotte afvigelser og demonstrere, at din Python‑stack kan levere *live* indsigt.

---

## 🎯 Formål

Når opgaven er gennemført, kan du:

1. læse flere PLC‑variabler i en kontinuerlig løkke,
2. vise dem med lav latenstid (< 2 s) i terminal eller browser, og
3. parametrisere både PLC‑forbindelse og UI fra miljøvariabler.

---

### 🧑‍🏫 Teori – fra rå polling til elegant, responsivt dashboard

En live-visualisering af PLC-data skal både være **hurtig** og **stabil**.
Det virker måske simpelt at smide en `while True`-løkke og tegne tal på skærmen, men uden omtanke ender du hurtigt med hakkende grafer, CPU-spikes eller endda en PLC, der nægter flere forbindelser. Lad os derfor dykke lidt dybere ned i de fem nøglebegreber:

| Begreb                  | Hvad betyder det i praksis?                                                                                                                                                                                          | Venlig tommelfingerregel / “best practice”                                                                                                                         |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Polling-frekvens**    | Hver læsecyklus belaster både PLC-CPU og netværk. En billig laboratorie-S7-1200 kan uden problemer håndtere 5–10 TCP-pakker i sekundet, men rammer du > 10 Hz, stiger risikoen for timeouts og tabte pakker hurtigt. | Start i **1 Hz**: ét read-kald pr. sekund. Sæt kun op til **5 Hz** på signaler, som *virkelig* har brug for høj opløsning (f.eks. vibrationsmåling).               |
| **UI-latens**           | En operatør tolererer typisk 1-2 s forsinkelse mellem fysisk hændelse og visning. Latensen er summen af PLC-scan-tid, netværk, din read-løkke og selve rendering-tiden i UI-biblioteket.                             | Hold “løkke-tid + netværk” under **dobbelt periodetid**. Ved 1 Hz polling bør grafen altså aldrig være mere end \~2 s bagefter virkeligheden.                      |
| **Thread vs. Async**    | Snap7-kald er **blokkerende** – de pauser Python-fortolkeren, mens TCP-pakken flyver frem og tilbage. I Streamlit (eller andre event-drevne frameworks) kan blokering fryse hele UI’et.                              | Kør PLC-polling i **baggrundstråd** (klassisk `threading.Thread`) eller brug **async-IO** (`asyncio.to_thread()` i Py 3.12), så UI-loopet aldrig blokeres.         |
| **Terminal-TUI**        | Rich og Textual kan tegne farverige tabeller og plots direkte i terminalen – perfekt, når SSH er eneste adgang. De opdaterer skærmbufferen ved hvert “tick”.                                                         | Brug `Live(refresh_per_second=...)` til at begrænse refresh; **2–5 fps** er rigeligt til tal og enkle bar-grafer.                                                  |
| **Ressource-oprydning** | Hver `cli.connect()` åbner en TCP-session i PLC-en; glemmer du `disconnect()`, kan du hurtigt løbe tør for forbindelser (S7-1200 tillader kun 8 samtidige). Det samme gælder for threads, filehandles osv.           | Pak langkørende kode i `try/except` + `finally`, eller brug context-managers (`with`-blokke), så forbindelser *altid* lukkes – også ved `Ctrl+C` eller Exceptions. |

---

#### Eksempel: minimal, men robust loop i en baggrundstråd

```python
import threading, time, queue, snap7
from snap7.snap7types import S7AreaDB
from snap7.util import get_real

def plc_poll(data_q, stop_evt, ip="192.168.0.1", db=1, period=1.0):
    cli = snap7.client.Client(); cli.connect(ip, 0, 1)
    try:
        while not stop_evt.is_set():
            t0 = time.perf_counter()
            raw = cli.read_area(S7AreaDB, db, 4, 4)      # DBD4
            lvl = round(get_real(raw, 0), 1)
            data_q.put(("level", lvl))
            dt = time.perf_counter() - t0
            time.sleep(max(0, period - dt))
    finally:
        cli.disconnect()

data_q  = queue.Queue()
stop_evt = threading.Event()
thread   = threading.Thread(target=plc_poll, args=(data_q, stop_evt))
thread.start()

try:
    while True:                               # UI-loop (Rich, Streamlit, …)
        sig, val = data_q.get()
        print(f"{sig}: {val:5.1f} %")
except KeyboardInterrupt:
    stop_evt.set()
    thread.join()
```

* **Polling-frekvens** styres af `period`.
* **Latens** er max `period` + UI-render.
* PLC-kald kører i baggrundstråd ➜ UI fryser ikke.
* `finally`-blokken sørger for **ressource-oprydning**.

---

#### Hvorfor ikke bare skrue helt op for hastigheden?

1. **PLC-scan-tid**: En simpel 1212C-CPU bruger \~2 ms pr. 1 kB TCP-payload. Ved 20 Hz udgør det pludselig 40 % af CPU-tiden.
2. **Netværksstøj**: Flere klienter (HMI, SCADA, logger) giver flere pakker; hurtig polling fra *én* klient kan stjæle båndbredde fra de andre.
3. **GUI-render**: Selv Streamlit har en intern throttling; spammer du den, vil den alligevel droppe frames.

---

#### Konklusion

Ved at ­**balancere polling-frekvens, tråd/asynkronitet og pæn oprydning** får du et dashboard, der både er **responsivt** og **robust** – en fornøjelse at bruge og et godt visitkort til enhver kunde eller underviser.

---

## 🛠️ Kompetencer

Du lærer at:

* bygge en *observer‑loop* som ikke spænder ben for UI‑rendering,
* anvende farvekoder/alarmer på tærskeloverskridelser,
* forklare fordele/ulemper ved TUI vs. Web‑UI i rapportform.

---

## 📂 Forudsætninger

| Krav       | Beskrivelse                                                |
| ---------- | ---------------------------------------------------------- |
| snap7‑read | Koden fra Opgave 02 eller logger‑funktionen fra Opgave 03. |
| Ekstra lib | Vælg én variant: `rich` (CLI) **eller** `streamlit` (Web). |
| Struktur   |                                                            |

````text
└── dag09-snap7/
    ├── src/
    │   ├── dashboard_cli.py   # CLI‑variant
    │   └── dashboard_web.py   # Web‑variant
    └── 05-dashboard.md        # denne fil
```|

---

## 🔧 Trin for trin
> **Vælg én af de to varianter nedenfor.** Du får fuldt point for én fuldt fungerende løsning.

### Variant A – CLI‑Dashboard med Rich
1. **Installér Rich**
   ```bash
   pip install rich
````

2. **Grundskabelon** (`src/dashboard_cli.py`)

   ```python
   import time, os, snap7
   from snap7.util import get_real, get_int, get_bool
   from snap7.snap7types import S7AreaDB
   from rich.live import Live
   from rich.table import Table

   PLC_IP = os.getenv("PLC_IP", "192.168.0.1")
   DB     = int(os.getenv("DB_NUM", 1))
   OFFSETS = {
       "tank_level": ("real", 4),  # DBD4
       "temp":       ("int", 2),   # DBW2
       "pump_on":    ("bool", 0, 0)  # DBX0.0
   }

   cli = snap7.client.Client(); cli.connect(PLC_IP, 0, 1)

   def read_vals():
       raw = cli.read_area(S7AreaDB, DB, 0, 8)
       return {
           "tank_level": round(get_real(raw, 4), 1),
           "temp":       get_int(raw, 2),
           "pump_on":    get_bool(raw, 0, 0)
       }

   with Live(refresh_per_second=2, screen=False) as live:
       try:
           while True:
               vals = read_vals()
               tbl = Table(title="PLC Live Data", expand=True)
               tbl.add_column("Signal"); tbl.add_column("Værdi")
               for k, v in vals.items():
                   tbl.add_row(k, str(v))
               live.update(tbl)
               time.sleep(1)
       except KeyboardInterrupt:
           cli.disconnect()
   ```
3. **Kør**

   ```bash
   PLC_IP=192.168.0.1 python src/dashboard_cli.py
   ```

### Variant B – Web‑Dashboard med Streamlit

1. **Installér Streamlit**

   ```bash
   pip install streamlit
   ```
2. **Grundskabelon** (`src/dashboard_web.py`)

   ```python
   import os, time, snap7, streamlit as st
   from snap7.util import get_real, get_int
   from snap7.snap7types import S7AreaDB

   st.set_page_config(page_title="PLC Live Dashboard", layout="wide")

   PLC_IP = os.getenv("PLC_IP", "192.168.0.1")
   DB     = int(os.getenv("DB_NUM", 1))
   cli = snap7.client.Client(); cli.connect(PLC_IP, 0, 1)

   col1, col2 = st.columns(2)
   chart_lvl = col1.line_chart()
   chart_tmp = col2.line_chart()

   while True:
       raw = cli.read_area(S7AreaDB, DB, 0, 8)
       lvl = round(get_real(raw, 4), 1)
       tmp = get_int(raw, 2)
       chart_lvl.add_rows([lvl])
       chart_tmp.add_rows([tmp])
       col1.metric("Tankniveau (%)", f"{lvl}")
       col2.metric("Temperatur (°C)", f"{tmp}")
       time.sleep(1)
   ```
3. **Kør**

   ```bash
   PLC_IP=192.168.0.1 streamlit run src/dashboard_web.py
   ```

---

## 💾 Aflevering

* `dashboard_cli.py` **eller** `dashboard_web.py` i `src/`.
* `dashboard_notes.md`: variant, polling‑frekvens, evt. alarm­logik.
* Skærmbillede eller kort screen‑capture GIF, der viser live‑opdatering.

---

## ✅ Peer‑review tjekliste

* [ ] Dashboard viser live‑data uden exceptioner (< 2 s latenstid).
* [ ] PLC‑parametre kommer fra environment‑variabler.
* [ ] `KeyboardInterrupt` / Streamlit‑stop lukker PLC‑forbindelsen.
* [ ] Koden er tydeligt opdelt i funktioner og følger PEP 8.
* [ ] README‑uddrag eller note forklarer, hvordan dashboardet startes.

---

### 📌 Ekstra idéer (frivilligt)

* Alarmfarver, når thresholds overskrides.
* Glide­vindue (seneste 5 min) i grafen med `deque(maxlen=300)`.
* `textual`‑TUI for avanceret terminal‑UI.
* Web‑slider til set‑points, der skriver tilbage til PLC.
* WebSockets for push‑opdateringer i stedet for polling.

---

*Tip:* Streamlit er ikke realtids‑kritisk; hvis snap7‑kald blokerer, så pak det i en baggrundstråd eller brug async‑IO fra Python 3.12.\*
