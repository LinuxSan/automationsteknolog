## 8) Opgave 8 – Log til **CSV** med **pandas** (kontinuerlig læsning)

**Mål:** Programmet skal køre i en løkke, læse `BOOL`, `INT`, `REAL`, `WORD` fra dit DB og **gemme** værdierne i en **CSV-fil** med tidsstempel.

**Installation (én gang):**
```bash
pip install python-snap7 pandas
````

**Forudsætninger (samme som tidligere):**

* PUT/GET er slået til på CPU.
* DB’et er **uden** “Optimized block access”.
* Adresser: `DBX0.0` (BOOL), `DBW2` (INT), `DBD4` (REAL), `DBW8` (WORD).

```python
# gem som: opg8_log_csv.py
# kør: python opg8_log_csv.py

import time
import datetime
import snap7
import pandas as pd
from snap7.util import get_bool, get_int, get_real, get_word

# 1) Oplysninger fra TIA
ip = "192.168.1.100"   # PLC'ens IP-adresse
rack = 0               # i undervisning altid 0
slot = 1               # S7-1200: 1  |  S7-1500: 0  (skift hvis du har 1500)
db_number = 1          # DB-nummer

# 2) Adresser og læse-vindue
start_byte = 0         # vi starter ved byte 0
laengde = 10           # vi henter 10 bytes (dækker DBX0.0, DBW2, DBD4, DBW8)

# 3) Logging-indstillinger
csv_fil = "plc_log.csv"   # navnet på din logfil
periode = 1.0             # sekunder mellem målinger (fx 1.0 = hvert sekund)
batch_size = 10           # hvor mange rækker vi samler før vi skriver til fil

# 4) Forbind til PLC
client = snap7.client.Client()
client.connect(ip, rack, slot)
print("Forbundet. Starter logging til CSV... (tryk Ctrl + C for at stoppe)")

# 5) Klargør en lille "buffer" til rækker
rækker = []          # her lægger vi målinger ind som dicts
første_skriv = True  # vi skriver kolonnenavne første gang vi gemmer

try:
    while True:
        # 6) Læs bytes fra DB
        data = client.db_read(db_number, start_byte, laengde)

        # 7) Pak værdierne ud
        v_bool = get_bool(data, 0, 0)  # DBX0.0
        v_int  = get_int(data, 2)      # DBW2
        v_real = get_real(data, 4)     # DBD4
        v_word = get_word(data, 8)     # DBW8

        # 8) Lav én række med tidsstempel
        nu = datetime.datetime.now().isoformat(timespec="seconds")
        række = {
            "timestamp": nu,
            "bool": bool(v_bool),
            "int": int(v_int),
            "real": float(v_real),
            "word": int(v_word)
        }
        rækker.append(række)

        # 9) Skriv til CSV hver gang vi har samlet batch_size rækker
        if len(rækker) >= batch_size:
            df = pd.DataFrame(rækker)
            df.to_csv(csv_fil, mode="a", index=False, header=første_skriv)
            første_skriv = False
            rækker = []   # tøm bufferen, vi er klar til næste batch
            print("gemt", batch_size, "rækker i", csv_fil)

        # 10) Vent et øjeblik før næste måling
        time.sleep(periode)

except KeyboardInterrupt:
    # brugeren stoppede programmet (Ctrl + C)
    print("\nStopper logging...")

except Exception as e:
    # en anden fejl skete (fx netværk)
    print("\nDer opstod en fejl:")
    print(e)

finally:
    # 11) Gem det sidste, hvis der ligger rester i bufferen
    if len(rækker) > 0:
        df = pd.DataFrame(rækker)
        df.to_csv(csv_fil, mode="a", index=False, header=første_skriv)
        print("gemt de sidste", len(rækker), "rækker i", csv_fil)

    # 12) Luk forbindelsen pænt
    try:
        client.disconnect()
        client.destroy()
    except:
        pass
    print("Forbindelse lukket. Færdig.")
```

### Hvad gør programmet?

* Læser de fire værdier fra PLC’en igen og igen (hver `periode` sekund).
* Lægger hver måling i en **buffer** (`rækker`).
* Når bufferen har `batch_size` rækker, bliver de skrevet til **CSV** med `pandas`.
* I `finally` bliver eventuelle **rester** skrevet, så du ikke mister data, hvis du stopper midt i en batch.
* Kolonnenavne skrives kun første gang i denne kørsel (`første_skriv = True`).

### Sådan åbner du filen

* Åbn `plc_log.csv` i Excel, Google Sheets eller et tekstprogram.
* Kolonner: `timestamp, bool, int, real, word`.

### Små øvelser

* Ændr `periode` til `0.5` og se hvor hurtigt den logger.
* Ændr `batch_size` til `1` for at skrive hver måling direkte (flere skriveoperationer).
* Stop programmet med `Ctrl + C` og tjek, at de sidste rækker også er kommet i filen.
