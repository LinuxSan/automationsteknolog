<!-- File: dag09-snap7/02-plc-read.md -->

# 02 – PLC‑Connect & Read BOOL/INT/REAL

*Del af **Dag 09 – Python ⇄ Siemens S7 med snap7***

---

## 📘 Introduktion

Du har nu `python‑snap7` installeret og verificeret med en simpel smoke‑test. Næste skridt er at **oprette en vedvarende klientforbindelse** til PLC’en og læse flere forskellige datatyper fra en datablock (DB). I Siemens‑verdenen kan én DB indeholde både BOOL‑flag, heltal (INT) og flydende tal (REAL). Ved at hente disse i samme kald får du indblik i **adressemodellen** og lærer at oversætte rå bytes til meningsfulde Python‑værdier.

---

## 🎯 Formål

Efter denne opgave kan du

1. oprette en stabil snap7‑klientforbindelse,
2. læse en *sammenhængende* byte‑blok fra PLC’en,
3. pakke data til **BOOL**, **INT** og **REAL** i Python, og
4. dokumentere hvert offset, så teamet hurtigt kan ændre DB‑layoutet uden at knække koden.

---

### 🧑‍🏫 Teori — PLC-hukommelse, adressering og datatyper

I Siemens-styrede PLC-anlæg fungerer **Data Blocks (DB)** som små, selvstændige “harddiske” i CPU-ens RAM.
Hver DB kan gemme flere hundrede kilobyte procesdata og er opbygget som en lineær **byte-array**:

$$
\text{Adresse   }=\;\underbrace{\text{DB-nummer}}_{\scriptsize \text{identificerer blok}} \;+\;
\underbrace{\text{byte-offset}}_{\scriptsize 0,1,2,\dots}\;+\;
\underbrace{\text{bit-offset}}_{\scriptsize 0\!-\!7\text{ (kun for BOOL)}}
$$

| Begreb              | Detaljeret forklaring                                                                                                                                                    | Typisk notation (TIA Portal)                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| **DB (Data Block)** | Et logisk segment af PLC-RAM der **bevares** gennem omstarter. Bruges til set-punkter, historik eller komplette strukturer (UDT’er).                                     | `DB1`, `DB20`, …                              |
| **Offset**          | Byte-indeks **inden i** en DB. De første fire bytes hedder `DBB0-DBB3`. 16-bit og 32-bit felter må *altid* begynde på et **jævnt** byte-tal for at undgå alignment-fejl. | `DB1.DBB4`                                    |
| **BOOL**            | Enkelt bit (0 / 1). PLC-en pakker otte BOOLs i én byte, så adressen angives som byte + bit.                                                                              | `DB1.DBX0.3` = tredjesidste bit i første byte |
| **INT**             | Signed 16-bit heltal i **big-endian** (MSB først). Gyldigt interval `-32 768 … 32 767`.                                                                                  | `DB1.DBW2` (bytes 2-3)                        |
| **REAL**            | IEEE-754 32-bit floating-point. Valider altid om PLC-projektet bruger **engineering units** (°C, bar) eller rå AD-counts.                                                | `DB1.DBD4` (bytes 4-7)                        |
| **Endianness**      | S7-CPU’er transmitterer multi-byte tal i **big-endian**. På x86-baserede computere er Python derimod **little-endian**, hvilket kræver korrekt byte-swap.                | –                                             |

---

#### Byte-array til Python-typer

`snap7` leverer rå data som `bytearray`. For hver måling henter du et *sammenhængende* udsnit af hukommelsen og oversætter det til Python-typer med helper-funktionerne i **`snap7.util`**:

```python
from snap7.util import get_bool, get_int, get_real
raw = plc.read_area(S7AreaDB, db_number=1, start=0, size=8)

level_ok   = get_bool(raw, 0, 3)   # DBX0.3  → Python bool
pressure   = get_int (raw, 2)      # DBW2    → Python int
temperature = get_real(raw, 4)     # DBD4    → Python float
```

> **Tip 1:** Brug én samlet `read_area()`-kald per cyklus i stedet for flere små – det reducerer bus-trafik og latency.
> **Tip 2:** Sørg for, at Python-siden *kender* præcis samme layout som PLC-siden. Den nemmeste måde er at eksportere en **UDT-CSV** fra TIA Portal og generere en offset-mappe automatisk.

---

#### Alignment- og række­følge­faldgruber

1. **Bit-felter efter 8-, 16- eller 32-bit felter** giver hulrum—TIA **aligner automatisk** til næste bytegrænse, mens din egen håndskrevne offset-tabel måske ikke gør.
2. Siemens **kopierer** komplette DBD/DBW-felter ved `BLKMOV`; overskriv derfor aldrig kun halvdelen af et tal fra Python-siden.
3. Når du skriver (`write_area`) skal du **læse → patche → skrive** for at bevare de omkringliggende bits/bytes.

---

#### Kontrol-tjekliste til fejlsøgning

| Fejl­symptom  | Sandsynlig årsag                     | Hurtig test                                                      |
| ------------- | ------------------------------------ | ---------------------------------------------------------------- |
| Alle tal = 0  | Forkert DB-nummer eller start-offset | Læs ét kendt INT-felt (`DB1.DBW0`) direkte i TIA-Online & Python |
| 10× for højt  | Endianness eller skalering           | Byt `bytearray[0:2]` om og check                                 |
| PLC Fault-bit | Ugyldigt skrive-offset eller længde  | Skriv **præcis** samme bufferlængde, som du læste                |

---

#### Videre læsning

* *System Manual S7-1200: Memory areas* – kapitel om data types og addressing.
* Official **python-snap7** docs (`Client.read_area`, `util.*`) – eksempelkode til både BOOL-, INT- og REAL-felter.
* *IEC 61131-3* – standarden bag PLC-datatyper, hjælper når du skal matche DWORD, LREAL osv.

Denne udvidede gennemgang gør dig i stand til at **analysere, validere og manipulere** PLC-data sikkert fra Python, hvilket er fundamentet for de efterfølgende opgaver om logging, smoothing og dashboard-visualisering.

---

## 🛠️ Kompetencer

after opgaven kan du

* implementere `snap7.client.Client` med timeout‑håndtering,
* udregne korrekte byte/bits‑offsets fra TIA Portal‑adresser,
* anvende `snap7.util` sikkert (undgå off‑by‑one‑fejl),
* strukturere koden i *connect*‑, *read*‑ og *parse*‑lag.

---

## 📝 Opgaven

1. **Opsæt konstanter**
   Tilføj følgende i `src/connect.py` eller en ny fil `plc_read.py`:

   ```python
   PLC_IP   = "192.168.0.1"   # flyt til .env i praksis
   RACK, SLOT = 0, 1
   DB_NUM   = 1
   SIZE     = 8   # læser DBB0–7 (BOOL, INT, REAL)
   OFFSETS  = {
       "pump_running":  ("bool", 0, 0),  # DBX0.0
       "setpoint_rpm":  ("int", 2),      # DBW2
       "tank_level":    ("real", 4),     # DBD4
   }
   ```
2. **Opret klient & læs buffer**

   ```python
   import snap7, time
   from snap7.snap7types import S7AreaDB
   from snap7.util import get_bool, get_int, get_real

   cli = snap7.client.Client()
   cli.set_connection_params(PLC_IP.encode(), RACK, SLOT)
   cli.connect()

   raw = cli.read_area(S7AreaDB, DB_NUM, 0, SIZE)
   ```
3. **Pak værdier**

   ```python
   vals = {}
   for name, spec in OFFSETS.items():
       typ = spec[0]
       if typ == "bool":
           vals[name] = get_bool(raw, spec[1], spec[2])
       elif typ == "int":
           vals[name] = get_int(raw, spec[1])
       elif typ == "real":
           vals[name] = round(get_real(raw, spec[1]), 2)
   print(vals)
   ```
4. **Loop & log**
   Pak ovenstående i en `while True:`‑løkke med `time.sleep(1)` og udskriv værdierne hvert sekund.
5. **Dokumentér offsets**
   Tilføj en Markdown‑tabel i denne fil eller i `DB1_layout.md`:

   ```markdown
   | Signal | Type | Adresse | Beskrivelse |
   |--------|------|---------|-------------|
   | pump_running | BOOL | DB1.DBX0.0 | Pumpestatus |
   | setpoint_rpm | INT  | DB1.DBW2   | Setpunkt, RPM |
   | tank_level   | REAL | DB1.DBD4   | Tankniveau i % |
   ```

### 💾 Aflevering

* Fil **`plc_read.py`** (eller tilsvarende) i `src/`‑mappen.
* Skærmbillede eller tekstfil `read_output.txt` med tre kontinuerlige udlæsninger.
* Markdown‑tabel med DB‑layout og korte signal­beskrivelser.

---

## ✅ Peer‑review tjekliste

* [ ] Scriptet forbinder uden timeout og lukker med `Ctrl+C`.
* [ ] Alle tre datatyper udlæses korrekt (visuelt tjek i TIA Portal).
* [ ] Offsets stemmer med tabel; ingen "magic numbers" i kode.
* [ ] Koden er opdelt i funktioner: `connect()`, `read_db()`, `parse()`.
* [ ] `.env.example` er opdateret (PLC\_IP, DB\_NUM).

---

*Tip:* Brug `cli.disconnect()` i en `finally:`‑blok for at frigive forbindelse, selv ved fejl.\*
