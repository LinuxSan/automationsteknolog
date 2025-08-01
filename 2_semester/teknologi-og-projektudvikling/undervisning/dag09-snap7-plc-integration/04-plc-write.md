<!-- File: dag09-snap7/04-plc-write.md -->

# 04 – Skriv Set‑points til PLC

*Del af **Dag 09 – Python ⇄ Siemens S7 med snap7***

---

## 📘 Introduktion

Efter at have lært at læse data fra PLC’en og logge dem, skal du nu prøve den modsatte vej: **at skrive værdier til en datablock**. Typiske eksempler er set‑punkter (temperatur, RPM), grænseværdier eller boolske styreflag. Sikker skrivning kræver, at du respekterer PLC’ens datatype, byte‑rækkefølge og samtidige adgang fra HMI eller andre klienter.

---

## 🎯 Formål

Når denne opgave er løst, kan du

1. konvertere Python‑typer (bool, int, float) til rå bytes med `snap7.util.set_*`,
2. implementere mønsteret **læs → patch → skriv**, så du ikke overskriver nabo‑data,
3. bekræfte i TIA Portal, at værdien ændres – uden at PLC’en går i fault.

---

### 🧑‍🏫 Teori – sådan skriver du sikkert til en Siemens S7-PLC

At **læse** data er risikofrit – du kan højst opleve en timeout.
At **skrive** data er derimod som at skifte hjul på en kørende lastbil: du kan spænde skruerne for hårdt (CPU-fault), skrue på det forkerte hjul (forkerte bytes) eller blive afbrudt midt i arbejdet (race-condition).
For at undgå det — og stadig bevare et hurtigt, enkelt Python-flow — skal du kende de fire grundbegreber i tabellen nedenfor.

| Begreb                | Hvad betyder det i praksis?                                                                                                                                                                                                                                | Venlig tommelfingerregel                                                                                                                                                        |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Write-mask**        | PLC’en kan ikke skrive en **enkel bit** ad gangen over TCP; du sender altid hele det byte-felt, hvor bit-ten bor. Hvis du vil ændre `DB1.DBX0.2`, skal du derfor først hente de relevante 2 byte, flippe bit-ten lokalt og skrive de samme 2 byte tilbage. | “Læs → patch → skriv” — aldrig “skriv én bit”.                                                                                                                                  |
| **Access-level**      | Hver S7-CPU har et beskyttelsesniveau (read-only, HMI-niveau eller full access). Hvis Python forsøger at skrive til en read-only CPU, får du en *“No access”*-fejl.                                                                                        | Sørg for at **Protection Level 1** (read/write) er aktiveret under *Device Access* i TIA, eller opret en særskilt **HMI-område** til dine set-points.                           |
| **Consistent length** | Multibyte-felter (INT = 2 B, REAL = 4 B) skal skrives i **samme længde**, som de blev defineret. Hvis du sender 3 bytes til et REAL-felt, antager CPU’en korrupt data og går i STOP med rød Fault-LED.                                                     | Brug helper-funktionerne `set_int`, `set_real`, som automatisk skriver præcis 2 / 4 bytes.                                                                                      |
| **OPC-race**          | I et rigtigt anlæg har du ofte flere klienter: et HMI-panel, et SCADA-system, måske en OPC-UA-server … og nu også dit Python-script. Hvis to parter skriver til samme DB samtidig, kan du få “åndssvage” tal eller overskrive hinandens bits.              | Definér én “single source of truth” (fx Python logger *kun* til DB2, HMI til DB3), **eller** lav et *lock-byte*: klienten sætter bit 0 = 1, skriver data, og rydder bit 0 igen. |

---

#### Hvordan ser det ud i kode?

```python
from snap7.util import get_bool, set_bool, set_int, set_real
from snap7.snap7types import S7AreaDB

# 1. Læs den eksisterende buffer (8 bytes rækker til 1 BOOL + 1 INT + 1 REAL)
buf = client.read_area(S7AreaDB, db_number=1, start=0, size=8)

# 2. Patch værdierne lokalt – ­bemærk at set_xx() ændrer buf *in-place*
set_bool(buf, byte_index=0, bit_index=0, value=True)      # DBX0.0 = pump_enable
set_int (buf, byte_index=2,          value=1500)          # DBW2   = target_rpm
set_real(buf, byte_index=4,          value=42.5)          # DBD4   = target_temp

# 3. Skriv HELE 8-bytes-blokken tilbage i én transaktion
client.write_area(S7AreaDB, db_number=1, start=0, data=buf)
```

> **Vigtigt:** Hvis du også skal ændre et felt i *nabo-datablocken* (DB2), skal du lave **et separat write-kald**. Snap7 tillader ikke, at du “skyder” data ind over DB-grænser.

---

#### Tre ekstra råd fra felten

1. **Range-check, før du skriver.**
   Kør `assert 0 <= rpm <= 3000` **før** du piller i bufferen; så falder Python-koden, ikke PLC’en, på urealistiske tal.

2. **Log alle writes** i samme CSV som dine reads – gerne med en “source”-kolonne, så du kan se, om tallet kom fra HMI eller Python.

3. **Test på en simulering først.** TIA’s PLCSIM (eller en “dummy” S71200 på skrivebordet) er guld værd, før du rører anlæggets rigtige CPU.

---

Med disse principper kan du skrive til PLC’en **uden sved på panden** – og uden at få den frygtede rød-blinkende Fault-LED.

---

## 🛠️ Kompetencer

Efter opgaven kan du:

* verificere skrive‑tilladelser i TIA Portal → Online & diagnostics,
* lave et Python‑wrapper‑modul `plc_io.py` med funktionerne `read_vars()` og `write_vars()`
  (Single Responsibility),
* anvende input‑validering (range‑check) før du sender data til PLC’en.

---

## 📝 Opgaven

1. **Mapping af set‑points**
   Tilføj følgende struktur i `src/plc_write.py`:

   ```python
   SETPOINTS = {
       "target_rpm":    ("int",  2),  # DBW2
       "target_temp":   ("real", 4), # DBD4
       "motor_enable":  ("bool", 0, 0), # DBX0.0
   }
   ```

   Det antages, at PLC‑programmet har alle tre felter i **DB1**.

2. **Helper‑funktion `write_var(name, value)`**

   ```python
   import snap7, os
   from snap7.snap7types import S7AreaDB
   from snap7.util import set_bool, set_int, set_real

   PLC_IP = os.getenv("PLC_IP", "192.168.0.1")
   cli = snap7.client.Client(); cli.connect(PLC_IP, 0, 1)

   def write_var(name, value, db_num=1):
       spec = SETPOINTS[name]
       typ = spec[0]
       # Læs først 8 bytes (nok til alle felter)
       buf = cli.read_area(S7AreaDB, db_num, 0, 8)
       if typ == "bool":
           set_bool(buf, spec[1], spec[2], bool(value))
       elif typ == "int":
           set_int(buf, spec[1], int(value))
       elif typ == "real":
           set_real(buf, spec[1], float(value))
       cli.write_area(S7AreaDB, db_num, 0, buf)
   ```

3. **CLI‑interface (argparse)**

   ```python
   if __name__ == "__main__":
       import argparse
       p = argparse.ArgumentParser(description="Sæt PLC‑set‑point")
       p.add_argument("name", choices=SETPOINTS.keys())
       p.add_argument("value")
       args = p.parse_args()
       write_var(args.name, args.value)
       print("OK –", args.name, "=", args.value)
   ```

4. **Test i TIA Portal**
   Kør f.eks.:

   ```bash
   PLC_IP=192.168.0.1 python src/plc_write.py target_temp 42.5
   ```

   Se i *Online & monitoring*, at `DB1.DBD4` ændres til 42.5 °C.

5. **Valider Fault‑LED**
   Sæt et ugyldigt tal (fx 40000 RPM hvis INT går i overflow) og observer, at PLC’en ikke går i STOP – fordi Python‑siden range‑checker.

### 💾 Aflevering

* **`plc_write.py`** i `src/`.
* Skærmklip fra TIA, der viser ændrede set‑points.
* Kort note `write_notes.md`: hvilke checks du implementerede (type, range, overflow).

---

## ✅ Peer‑review tjekliste

* [ ] CLI‑kommando ændrer værdi, og TIA viser samme værdi live.
* [ ] Koden læser → patcher → skriver **samme** buffer‑længde.
* [ ] Range‑check og type‑konvertering beskytter mod out‑of‑range.
* [ ] PLC‑forbindelsen lukkes efter endt skrivning.
* [ ] `.env.example` opdateret med `DB_NUM` hvis afviger fra 1.

---

*Tip:* Hvis du skal skrive flere felter på én gang, kan du patche **alle** offsets i bufferen, før du kalder `write_area()` – det er hurtigere og sikrere end flere enkeltkald.\*
