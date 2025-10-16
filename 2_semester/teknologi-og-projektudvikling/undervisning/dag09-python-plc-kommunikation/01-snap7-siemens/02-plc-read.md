## 1) Opgave 1 – Gør PLC og TIA klar (med billeder)

**Mål:** Du skal gøre PLC’en klar til at blive læst med Python/snap7.

### Trin A – Lav et Data Block (DB) med faste adresser
1. Opret et DB, fx **`snap7-data [DB1]`**.  
2. Opret 4 felter (se billede). De skal ligge på **præcise adresser**:
   - `bool` → **Bool** → **Offset 0.0**  → adresse: `DBX0.0`
   - `int`  → **Int**  → **Offset 2.0**  → adresse: `DBW2`
   - `real` → **Real** → **Offset 4.0**  → adresse: `DBD4`
   - `word` → **Word** → **Offset 8.0**  → adresse: `DBW8`  
3. Gem.

*Figur 1 – DB med bool/int/real/word*  
<img width="3035" height="1655" alt="fig1" src="https://github.com/user-attachments/assets/375832c4-3bc4-4a0a-9f92-0add878f7577" />

---

### Trin B – Giv CPU’en en IP-adresse
1. Gå til CPU → **General → Ethernet addresses**.  
2. Vælg **Set IP address in the project**.  
3. Sæt fx IP **192.168.1.100** og maske **255.255.255.0**.  
4. Download (hardware).  

*Figur 2 – IP-adresse*  
<img width="831" height="660" alt="fig2" src="https://github.com/user-attachments/assets/9dd4a635-39e6-49d1-b67c-cba988b562b1" />

---

### Trin C – Tillad PUT/GET (ellers kan snap7 ikke læse)
1. CPU → **Protection & Security → Connection mechanisms**.  
2. Sæt flueben ved **Permit access with PUT/GET communication from remote partner**.  
3. Download (software).  

*Figur 3 – PUT/GET*  
<img width="1560" height="1222" alt="fig3" src="https://github.com/user-attachments/assets/d151c557-56b8-4db4-a3a7-c5eb0f14bcb9" />

---

### Trin D – Slå “Optimized block access” fra på DB’et
1. Åbn **DB1** → **Properties → Attributes**.  
2. **Fjern** flueben ved **Optimized block access**.  
3. Gem og download DB’et.  

*Figur 4 – Optimized block access fra*  
<img width="1562" height="1220" alt="fig4" src="https://github.com/user-attachments/assets/6389100d-5ce6-496a-9da6-e1df8264b7b9" />

---

### Trin E – (Valgfrit) Brug PLCSIM Advanced
Hvis du simulerer:
1. Start **S7-PLCSIM Advanced**.  
2. Vælg **TCP/IP Single Adapter**.  
3. Opret instans, fx navn **snap7**, IP **192.168.1.100**.  
4. Start instansen (grøn lampe).  

*Figur 5 – PLCSIM Advanced*  
<img width="815" height="1690" alt="fig5" src="https://github.com/user-attachments/assets/bdf320d6-bc4a-4458-b904-38e310f0634c" />

---

### Notér til Python
- **IP:** fx `192.168.1.100`  
- **Rack/Slot:** S7-1200 = `0/1`, S7-1500 = `0/0`  
- **DB-nummer:** fx `1`  
- **Adresser:** `DBX0.0`, `DBW2`, `DBD4`, `DBW8`

> **Quick-check:** Du kan *ping’e* IP’en, TIA kan gå *Online*, PUT/GET er slået til, og DB’et er **ikke** optimeret. Nu er du klar.

---

# Læs i Python (helt simpelt)

> Installer pakken én gang i et terminalvindue:
>
> ```bash
> pip install python-snap7
> ```

---

## 2) Opgave 2 – Læs en **BOOL** (DBX)

**Hvad skal du kende fra TIA:**  
IP, RACK, SLOT, DB-nummer, og hvor i DB’et din BOOL ligger (her: `DBX0.0`).

```python
# gem som: opg2_read_bool.py

import snap7
from snap7.util import get_bool

ip = "192.168.1.100"  # PLC'ens IP-adresse
rack = 0              # i undervisning altid 0
slot = 1              # S7-1200: 1  |  S7-1500: 0  (ret hvis du har 1500)
db_number = 1         # dit DB-nummer
byte_offset = 0       # DBX<byte>.<bit>  -> her: byte = 0
bit_index = 0         # DBX<byte>.<bit>  -> her: bit  = 0

# 1) Lav forbindelse til PLC
client = snap7.client.Client()
client.connect(ip, rack, slot)

# 2) Læs 1 byte fra DB'et (den byte der indeholder vores bit)
data = client.db_read(db_number, byte_offset, 1)

# 3) Hent bit-værdien ud af den byte vi lige læste
my_bool = get_bool(data, 0, bit_index)

# 4) Vis resultatet
print("my_bool:", my_bool)

# 5) Luk forbindelsen
client.disconnect()
````

**Hvad gør koden (trin for trin)?**

1. Importerer snap7 og en hjælperfunktion til at læse en bit.
2. Sætter de oplysninger du kender (ip, rack, slot, DB, byte, bit).
3. Forbinder til PLC.
4. Læser **1 byte** fra DB’et.
5. Plukker **den ene bit** ud af byten.
6. Printer værdien.
7. Afbryder forbindelsen.

Kør:

```bash
python opg2_read_bool.py
```

---

## 3) Opgave 3 – Læs en **INT** (DBW)

**Adresse i TIA:** `DBW2` ⇒ start-byte er **2** og vi skal bruge **2 bytes**.

```python
# gem som: opg3_read_int.py

import snap7
from snap7.util import get_int

ip = "192.168.1.100"
rack = 0
slot = 1            # S7-1500? skift til 0
db_number = 1

start_byte = 2      # DBW2 starter ved byte 2
length = 2          # en INT fylder 2 bytes

client = snap7.client.Client()
client.connect(ip, rack, slot)

data = client.db_read(db_number, start_byte, length)
my_int = get_int(data, 0)   # 0 = start i vores lille buffer

print("my_int:", my_int)

client.disconnect()
```

Kør:

```bash
python opg3_read_int.py
```

---

## 4) Opgave 4 – Læs en **REAL** (DBD)

**Adresse i TIA:** `DBD4` ⇒ start-byte er **4** og vi skal bruge **4 bytes**.

```python
# gem som: opg4_read_real.py

import snap7
from snap7.util import get_real

ip = "192.168.1.100"
rack = 0
slot = 1            # S7-1500? skift til 0
db_number = 1

start_byte = 4      # DBD4 starter ved byte 4
length = 4          # en REAL fylder 4 bytes (float)

client = snap7.client.Client()
client.connect(ip, rack, slot)

data = client.db_read(db_number, start_byte, length)
my_real = get_real(data, 0)

print("my_real:", my_real)

client.disconnect()
```

Kør:

```bash
python opg4_read_real.py
```

---

## 5) Opgave 5 – Læs en **WORD** (DBW)

**Adresse i TIA:** `DBW8` ⇒ start-byte er **8** og vi skal bruge **2 bytes**.

```python
# gem som: opg5_read_word.py

import snap7
from snap7.util import get_word

ip = "192.168.1.100"
rack = 0
slot = 1            # S7-1500? skift til 0
db_number = 1

start_byte = 8      # DBW8 starter ved byte 8
length = 2          # en WORD fylder 2 bytes (uint16)

client = snap7.client.Client()
client.connect(ip, rack, slot)

data = client.db_read(db_number, start_byte, length)
my_word = get_word(data, 0)

print("my_word:", my_word)

client.disconnect()
```

Kør:

```bash
python opg5_read_word.py
```

---

## Fejlfinding (meget kort)

* **Kan ikke forbinde:** Tjek IP. Prøv at *ping’e* IP’en.
* **Fejl ved læsning:** Tjek at **PUT/GET** er slået til.
* **Forkerte tal:** Tjek at DB’et **ikke** er “Optimized block access”, og at adresserne er præcis som i Opgave 1.
* **Rack/Slot forkert:** S7-1200 = `0/1`. S7-1500 = `0/0`.

> Når du har læst disse fire typer, kan du genbruge samme idé til andre adresser: ændr bare start-byte, længde og `get_*`-funktionen.
