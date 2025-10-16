## 6) Opgave 6 – Kontinuerlig “main” (KUN while True)

**Mål:** Programmet skal køre i en løkke og hente værdierne igen og igen.

**Forudsætninger (som i Opgave 1):**
- PUT/GET er slået til på CPU.
- DB’et er **uden** “Optimized block access”.
- Adresser:
  - `DBX0.0`  (BOOL)
  - `DBW2`    (INT)
  - `DBD4`    (REAL)
  - `DBW8`    (WORD)

**Stop programmet:** Tryk `Ctrl + C` i terminalen.  
*(Her håndterer vi ikke stop pænt endnu—det kommer i næste opgave med `try/except/finally`.)*

```python
# gem som: opg6_poll_main_simple.py
# kør: python opg6_poll_main_simple.py

import time
import snap7
from snap7.util import get_bool, get_int, get_real, get_word

# 1) UDFYLD DISSE VÆRDIER (fra TIA)
ip = "192.168.1.100"   # PLC'ens IP-adresse
rack = 0               # i undervisning altid 0
slot = 1               # S7-1200: 1  |  S7-1500: 0  (skift hvis du har 1500)
db_number = 1          # DB-nummer

# 2) HVOR OFTE SKAL VI LÆSE?
ventetid = 1.0         # sekunder mellem hver læsning, fx 1.0 = hvert sekund

# 3) VI LÆSER ET LILLE VINDUE AF DB'ET (0..9)
start_byte = 0         # vi starter ved byte 0
laengde = 10           # vi henter 10 bytes, så vi dækker alle 4 værdier

# 4) LAV FORBINDELSE TIL PLC
client = snap7.client.Client()
client.connect(ip, rack, slot)

print("Starter kontinuerlig læsning... (tryk Ctrl + C for at stoppe)")
# 5) KONTINUERLIG LØKKE — UDEN try/except
while True:
    # 5a) Læs 10 bytes fra DB'et (fra byte 0)
    data = client.db_read(db_number, start_byte, laengde)

    # 5b) Pak de fire værdier ud fra de rigtige adresser i den buffer vi lige læste
    #     - BOOL  ligger i byte 0, bit 0  (DBX0.0)
    #     - INT   starter ved byte 2      (DBW2)
    #     - REAL  starter ved byte 4      (DBD4)
    #     - WORD  starter ved byte 8      (DBW8)
    v_bool = get_bool(data, 0, 0)
    v_int  = get_int(data, 2)
    v_real = get_real(data, 4)
    v_word = get_word(data, 8)

    # 5c) Vis en linje med et lille tidsstempel og de fire værdier
    tidspunkt = time.strftime("%H:%M:%S")
    print("tid:", tidspunkt, "bool:", v_bool, "int:", v_int, "real:", v_real, "word:", v_word)

    # 5d) Vent lidt, så vi ikke spammer PLC'en
    time.sleep(ventetid)

# 6) BEMÆRK:
#     Her når koden aldrig hertil, fordi while True kører for evigt.
#     I næste opgave lærer vi at bruge try/except/finally,
#     så vi kan stoppe pænt og lukke forbindelsen korrekt.
````

### Hvad sker der trin for trin?

1. Vi importerer `time` og de små “hjælperfunktioner” til at læse de rigtige datatyper.
2. Vi skriver PLC-oplysninger (ip/rack/slot/DB).
3. Vi beslutter, hvor ofte vi vil læse (`ventetid`).
4. Vi forbinder til PLC’en.
5. I `while True`:

   * Læser vi **10 bytes** fra DB’et (fra byte 0).
   * Plukker hver værdi ud fra den rigtige placering i bufferen.
   * Printer værdierne på én simpel linje.
   * Sover et øjeblik, så PLC’en ikke bliver overbelastet.

---

## 7) Opgave 7 – Kontinuerlig “main” med `try / except / finally`

**Mål:** Det samme som i forrige opgave (kontinuerlig læsning), men nu stopper programmet **pænt** og lukker forbindelsen **altid** – også hvis der sker en fejl.

**Forudsætninger:**
- PUT/GET er slået til på CPU.
- DB’et er **uden** “Optimized block access”.
- Adresser: `DBX0.0` (BOOL), `DBW2` (INT), `DBD4` (REAL), `DBW8` (WORD).

```python
# gem som: opg7_poll_main_try.py
# kør: python opg7_poll_main_try.py

import time
import snap7
from snap7.util import get_bool, get_int, get_real, get_word

# 1) UDFYLD DISSE VÆRDIER (fra TIA)
ip = "192.168.1.100"   # PLC'ens IP-adresse
rack = 0               # i undervisning altid 0
slot = 1               # S7-1200: 1  |  S7-1500: 0  (skift hvis du har 1500)
db_number = 1          # DB-nummer

# 2) HVOR OFTE SKAL VI LÆSE?
ventetid = 1.0         # sekunder mellem hver læsning

# 3) VI LÆSER ET LILLE VINDUE AF DB'ET (0..9)
start_byte = 0         # vi starter ved byte 0
laengde = 10           # dækker DBX0.0, DBW2, DBD4, DBW8

# 4) Opret klient (uden at forbinde endnu)
client = snap7.client.Client()

try:
    # 5) Forbind til PLC
    client.connect(ip, rack, slot)
    print("Forbundet. Starter kontinuerlig læsning... (tryk Ctrl + C for at stoppe)")

    # 6) Kør for evigt, indtil brugeren stopper eller der sker en fejl
    while True:
        # 6a) Læs 10 bytes fra DB'et
        data = client.db_read(db_number, start_byte, laengde)

        # 6b) Pak de fire værdier ud fra bufferen
        v_bool = get_bool(data, 0, 0)   # DBX0.0
        v_int  = get_int(data, 2)       # DBW2
        v_real = get_real(data, 4)      # DBD4
        v_word = get_word(data, 8)      # DBW8

        # 6c) Print værdierne sammen med et lille tidsstempel
        tidspunkt = time.strftime("%H:%M:%S")
        print("tid:", tidspunkt, "bool:", v_bool, "int:", v_int, "real:", v_real, "word:", v_word)

        # 6d) Vent lidt før næste læsning
        time.sleep(ventetid)

# 7) Brugeren trykker Ctrl + C
except KeyboardInterrupt:
    print("\nStopper efter Ctrl + C (bruger-stop).")

# 8) Andre fejl (fx netværksfejl)
except Exception as e:
    print("\nDer opstod en fejl.")
    print("Fejlbesked:", e)

# 9) Kør ALTID til sidst – luk forbindelsen pænt
finally:
    try:
        client.disconnect()
        client.destroy()
        print("Forbindelse lukket.")
    except:
        # Hvis forbindelsen allerede er væk, ignorerer vi fejlen her
        print("Forbindelse var allerede lukket.")
````

### Hvad sker der trin for trin?

1. Vi sætter IP, rack/slot, DB-nummer og hvor ofte vi vil læse.
2. Vi opretter en `client`.
3. **`try:`** vi forbinder og kører `while True` med læsning/udpakning/print/sleep.
4. **`except KeyboardInterrupt:`** bliver aktiveret, når du trykker `Ctrl + C`.
5. **`except Exception as e:`** fanger andre fejl (fx netværk nede).
6. **`finally:`** kører **altid** til sidst og sørger for, at forbindelsen lukkes pænt.

### Små øvelser/idéer

* Skru `ventetid` ned til `0.2` og snak om belastning.
* Træk netværkskablet ud for at fremprovokere en fejl og se `except`-delen virke.
* Flyt en adresse i TIA (fx `DBW2` → `DBW10`) og opdater Python-koden tilsvarende for at forstå, hvorfor adresser skal matche.

---

