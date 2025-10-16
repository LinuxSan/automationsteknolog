# 05 – PLC-Connect & **Write** BOOL/INT/REAL/WORD

> **For begyndere – helt simpelt.**  
> Forudsætninger (samme som ved read):
> - CPU tillader **PUT/GET**.
> - DB’et er **uden** “Optimized block access”.
> - Adresser (som i jeres DB):  
>   - `DBX0.0` (BOOL), `DBW2` (INT), `DBD4` (REAL), `DBW8` (WORD)

Installer pakken (hvis du ikke allerede har gjort det):
```bash
pip install python-snap7
````

---

## 9) Opgave 9 – **Skriv en BOOL** (DBX)

**Idé:** Når man skriver en **bit**, må man først læse **hele byten**, ændre den ene bit, og så skrive byten tilbage. På den måde ødelægger vi ikke de andre bits i samme byte.

```python
# gem som: opg9_write_bool.py
# kør: python opg9_write_bool.py

import snap7
from snap7.util import set_bool

# Udfyld efter dit projekt
ip = "192.168.1.100"
rack = 0
slot = 1           # S7-1500: brug 0
db_number = 1

# Hvor ligger din BOOL i DB'et?
bool_byte = 0      # DBX<byte>.<bit>  -> byte-delen (0..)
bool_bit  = 0      # DBX<byte>.<bit>  -> bit-delen  (0..7)

# Hvilken værdi vil du skrive?
nyt_bool = True    # prøv også False

# 1) Forbind
client = snap7.client.Client()
client.connect(ip, rack, slot)

# 2) Læs den ENE byte, der indeholder bit'en
buf = bytearray(client.db_read(db_number, bool_byte, 1))

# 3) Sæt/ryd bit'en i byten
set_bool(buf, 0, bool_bit, nyt_bool)

# 4) Skriv byten tilbage
client.db_write(db_number, bool_byte, buf)

print("skrevet bool:", nyt_bool)

# 5) Luk
client.disconnect()
client.destroy()
```

---

## 10) Opgave 10 – **Skriv en INT** (DBW)

**Idé:** En **INT** er 2 bytes. Vi laver en 2-byte buffer, putter tallet i, og skriver den til det rigtige start-byte.

```python
# gem som: opg10_write_int.py
# kør: python opg10_write_int.py

import snap7
from snap7.util import set_int

ip = "192.168.1.100"
rack = 0
slot = 1           # S7-1500: 0
db_number = 1

int_start = 2      # DBW2 starter ved byte 2
nyt_int   = 1234   # tilladte værdier: -32768 .. 32767

client = snap7.client.Client()
client.connect(ip, rack, slot)

buf = bytearray(2)
set_int(buf, 0, nyt_int)
client.db_write(db_number, int_start, buf)

print("skrevet int:", nyt_int)

client.disconnect()
client.destroy()
```

---

## 11) Opgave 11 – **Skriv en REAL** (DBD)

**Idé:** En **REAL** (float) er 4 bytes. Samme fremgangsmåde som INT, bare 4 bytes.

```python
# gem som: opg11_write_real.py
# kør: python opg11_write_real.py

import snap7
from snap7.util import set_real

ip = "192.168.1.100"
rack = 0
slot = 1           # S7-1500: 0
db_number = 1

real_start = 4     # DBD4 starter ved byte 4
nyt_real   = 3.14  # hvilket som helst flydende tal

client = snap7.client.Client()
client.connect(ip, rack, slot)

buf = bytearray(4)
set_real(buf, 0, nyt_real)
client.db_write(db_number, real_start, buf)

print("skrevet real:", nyt_real)

client.disconnect()
client.destroy()
```

---

## 12) Opgave 12 – **Skriv en WORD** (DBW)

**Idé:** En **WORD** er 2 bytes (usigneret). Brug `set_word`.

```python
# gem som: opg12_write_word.py
# kør: python opg12_write_word.py

import snap7
from snap7.util import set_word

ip = "192.168.1.100"
rack = 0
slot = 1           # S7-1500: 0
db_number = 1

word_start = 8     # DBW8 starter ved byte 8
nyt_word   = 0xBEEF  # 0 .. 65535 (du kan også skrive fx 5000)

client = snap7.client.Client()
client.connect(ip, rack, slot)

buf = bytearray(2)
set_word(buf, 0, nyt_word)
client.db_write(db_number, word_start, buf)

print("skrevet word:", nyt_word)

client.disconnect()
client.destroy()
```

---

## Lille huskeseddel

* **Adresser:**

  * BOOL: `DBX<byte>.<bit>`
  * INT/WORD: `DBW<byte>` (2 bytes)
  * REAL/DINT: `DBD<byte>` (4 bytes)
* **Ranges:**

  * INT: −32768 … 32767
  * WORD: 0 … 65535
* **1200 vs. 1500:** typisk `rack=0`. **slot** er normalt **1** (S7-1200) og **0** (S7-1500).
* **PUT/GET + ikke-optimeret DB** er must, ellers fejler skrivning.

> **Vil du teste, at værdierne kom frem?**
> Kør dine tidligere *read*-skripter efter hver skrivning og se værdierne i terminalen.
