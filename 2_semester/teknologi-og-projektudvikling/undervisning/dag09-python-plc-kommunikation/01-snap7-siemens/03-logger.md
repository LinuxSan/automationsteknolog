<!-- File: dag09-snap7/03-logger.md -->

# 03 – Real‑time Logger til CSV

*Del af **Dag 09 – Python ⇄ Siemens S7 med snap7***

---

## 📘 Introduktion

Et af de hyppigste industrikrav er at gemme proces­data som **historik** – både til fejlfinding og til efterfølgende analyse. I denne opgave bygger du et lille Python‑program, der **cyklisk** læser udvalgte PLC‑variabler hvert sekund og gemmer dem i en **CSV‑fil** med tidsstempel. Loggeren kører, indtil du trykker `Ctrl+C`, og skal håndtere netværksudfald uden at miste data.

---

## 🎯 Formål

Efter opgaven kan du

1. opsætte en kontinuerlig *read‑loop* med snap7,
2. tidsstemple målinger med `datetime.now()` eller `time.time()`,
3. skrive værdier til CSV (stream‑append) uden at indlæse hele filen i RAM,
4. genforbinde automatisk til PLC’en, hvis forbindelsen ryger,
5. strukturere kode, så loginterval og output‑mappe kan ændres via **environment‑variabler**.

---

### 🧑‍🏫 Teori — hvorfor en robust PLC-logger kræver mere end bare en `while True`

Når man bygger en tidskritisk datalogger til en PLC, er det fristende blot at køre en uendelig løkke med et enkelt `time.sleep(1)` – men driftssikre industrielle systemer stiller større krav. Følgende fem begreber danner rygraden i en professionel logger, som kan køre døgnets 24 timer uden at miste værdifulde datapunkter.

---

#### 1. Sample-tid (fast interval)

*Definition*
Sample-tiden er den **nominelle periode** mellem to målinger – i vores kursusopgaver typisk 1 sekund. En konstant sample-tid gør det enkelt at sammenligne time-serier, beregne afledte størrelser (hastighed, acceleration) og sætte alarmer på “manglende data”.

*Hvorfor er det svært?*
Python er ikke et realtids-OS. Selve `read_area()`-kaldet, disk-IO, og endda bag­grundsprocesser kan gøre løkken langsommere end planlagt.

*Bedste praksis*
Mål den tid, hver iteration faktisk tager, og træk den fra den planlagte pause:

```python
t0 = time.perf_counter()
…  # læs PLC, skriv CSV
dt_loop = time.perf_counter() - t0
time.sleep(max(0, PERIOD - dt_loop))
```

Så holder du det **effektive** interval tæt på den teoretiske sample-tid.

---

#### 2. Δt-jitter (variation i sample-tid)

*Definition*
Δt-jitter er forskellen mellem den **ideelle** sample-tid og den **reelle**.
Hvis du sigter mod 1.000 s og måler 1.013 s, er jitteren 13 ms.

*Konsekvenser*
Ved lave frekvenser (1 Hz) er små afvigelser udramatiske. Men når man senere ned­prøver (resampler) eller beregner integraler, kan kumuleret jitter skævvride resultaterne.

*Bedste praksis*

1. Gem **både** det planlagte tidsstempel (`t_plan = t_prev + PERIOD`) og det faktiske (`t_real = datetime.now()`), hvis du har brug for høj tidsopløsning.
2. Brug f.eks. Pandas’ `resample('1S', origin='start')` til at forene små afvigelser i efterbehandlingen.

---

#### 3. CSV-append (kontinuerlig filskrivning)

*Definition*
Med append-modus (`'a'`) åbnes filen én gang og **nulstilles ikke**, hver gang du skriver en ny række. Dermed sparer du disk-seek og undgår race conditions.

*Faldgrube*
Operativ­systemet buffer skriver til disk. Hvis din Raspberry Pi mister strøm inden bufferen er tømt, kan du miste de sidste rækker.

*Bedste praksis*

* Sørg for at kalde `f.flush()` eller åbne filen med `newline=''` (for korrekt CRLF-håndtering).
* På Linux kan du tilføje `os.fsync(f.fileno())` efter flush, hvis datatab er kritisk.
* Rul logfilen dagligt med tidsstempel i filnavnet (`log_YYYYMMDD.csv`), så filen ikke bliver flere gigabyte stor.

---

#### 4. Reconnect (netværksrobusthed)

*Problem*
Et enkelt tabt TCP-pakke eller et skævt Wi-Fi-signal kan få `snap7.client` til at kaste `Snap7Exception`. Hvis du blot lader scriptet crashe, mister du hele måleserien.

*Strategi*

1. Kapsl dine PLC-kald i en `try/except`-blok.
2. Vent et kort, stigende tidsrum (exponential back-off: 1 s, 2 s, 4 s …) før et nyt `connect()`-forsøg.
3. Log hændelsen til konsol eller en separat fejl-log, så du kan analysere oppetid senere.

*Eksempel*

```python
try:
    raw = cli.read_area(...)
except snap7.Snap7Exception as e:
    print("PLC-fejl:", e)
    time.sleep(2)
    cli = connect_plc()   # genopretter client-objektet
```

---

#### 5. Signal-håndtering (pæn nedlukning)

*Situation*
Når operatøren trykker `Ctrl+C`, kaster Python et `KeyboardInterrupt`. Lukker du ikke PLC-forbindelsen og fil-handle’en pænt, kan du ende med en korrupt CSV-fil og en hængende TCP-session i PLC’en.

*Løsning*

* Brug `try/except KeyboardInterrupt` **eller** et `with`-statement, hvor filen automatisk lukkes.
* Placer `cli.disconnect()` i en `finally:`-blok, så den altid køres – også ved andre exceptions.

```python
try:
    main_loop()
except KeyboardInterrupt:
    print("Stopper logger...")
finally:
    f.close()
    cli.disconnect()
```

Det er ikke blot god stil – nogle PLC-er nægter næste log-in, hvis den gamle ses­sion aldrig blev lukket.

---

### Kort opsummeret

* **Hold sample-tiden stabil**, men mål altid den faktiske loop-tid.
* **Overvåg jitter** hvis du senere skal lave fin-tids-analyse.
* **Append og flush** regelmæssigt for at minimere datatab.
* **Genforbind** automatisk, så et netværksglimt ikke stopper loggeren.
* **Ryd ordentligt op** på `Ctrl+C`, så både fil og PLC har det godt bagefter.

Med disse principper er din logger ikke blot en øvelsesopgave, men et værktøj, du faktisk tør lade køre natten over i et rigtigt procesanlæg.

---

## 🛠️ Kompetencer

Når du er færdig, kan du:

* måle faktisk loop‑frekvens og justere sleep‑tid,
* buffe data i RAM og dumpe batch‑vist, hvis disk‑IO er en flaskehals,
* bruge **ISO‑8601** tidsstempel eller Unix‑epoch afhængigt af downstream‑system,
* skrive *unit‑tests* (fx via `pytest`) for functions `connect_plc()` og `read_values()`.

---

## 📝 Opgaven

1. **Konstanter & miljøvariabler**

   ```python
   import os, time, csv, datetime as dt, snap7
   from snap7.snap7types import S7AreaDB
   from snap7.util import get_bool, get_int, get_real

   PLC_IP = os.getenv("PLC_IP", "192.168.0.1")
   RACK   = int(os.getenv("RACK", 0))
   SLOT   = int(os.getenv("SLOT", 1))
   DB     = int(os.getenv("DB_NUM", 1))
   PERIOD = float(os.getenv("LOG_PERIOD", 1.0))  # sekunder

   OFFSETS = {
       "pump_running": ("bool", 0, 0),   # DBX0.0
       "setpoint_rpm": ("int", 2),       # DBW2
       "tank_level":   ("real", 4),      # DBD4
   }
   FIELDS = ["timestamp"] + list(OFFSETS.keys())
   logfile = dt.datetime.now().strftime("log_%Y%m%d_%H%M%S.csv")
   ```

2. **PLC‑forbindelse med auto‑reconnect**

   ```python
   def connect_plc():
       c = snap7.client.Client()
       c.connect(PLC_IP, RACK, SLOT)
       return c

   cli = connect_plc()
   ```

3. **Logger‑loop**

   ```python
   with open(logfile, "a", newline="", encoding="utf-8") as f:
       writer = csv.writer(f)
       writer.writerow(FIELDS)  # header

       try:
           while True:
               t0 = time.perf_counter()
               try:
                   raw = cli.read_area(S7AreaDB, DB, 0, 8)
               except Exception as e:
                   print("PLC error:", e)
                   time.sleep(2)
                   cli = connect_plc()
                   continue

               vals = [dt.datetime.now().isoformat(timespec="seconds")]
               for name, spec in OFFSETS.items():
                   typ = spec[0]
                   if typ == "bool":
                       vals.append(int(get_bool(raw, spec[1], spec[2])))
                   elif typ == "int":
                       vals.append(get_int(raw, spec[1]))
                   else:
                       vals.append(round(get_real(raw, spec[1]), 2))

               writer.writerow(vals)
               f.flush()

               dt_loop = time.perf_counter() - t0
               time.sleep(max(0, PERIOD - dt_loop))
       except KeyboardInterrupt:
           print("\nLogger stopped by user.")
           cli.disconnect()
   ```

4. **Kør programmet**

   ```bash
   PLC_IP=192.168.0.1 DB_NUM=1 python src/logger.py
   ```

5. **Valider CSV‑fil**
   Åbn `log_YYYYMMDD_HHMMSS.csv` i Excel eller `pandas` og verificér, at tidsstempel‑kolonnen er monoton stigende, og at værdierne matcher TIA‑online observationer.

### 💾 Aflevering

* **`logger.py`** i `src/`‑mappen.
* Logfil med mindst 2 minutters data.
* Kort notat `logger_notes.md` (5‑10 linjer): valgt periode, evtl. fejl, plan for forbedring.

---

## ✅ Peer‑review tjekliste

* [ ] Logfil har header + ≥ 120 rækker (1 Hz × 2 min).
* [ ] Missing data håndteres (fx genforbindelse efter kabeludtræk).
* [ ] IP/rack/slot/DB/period styres via env‑variabler, ikke hard‑kodet.
* [ ] Koden afslutter uden korrupt CSV ved `Ctrl+C`.
* [ ] Funktions‑ og variabelnavne er selvforklarende; PEP 8 overholdt.

---

*Tip:* For højere performance kan du buffer‑skrive hver 10. række (batch) i stedet for at flushe hver gang.\*
