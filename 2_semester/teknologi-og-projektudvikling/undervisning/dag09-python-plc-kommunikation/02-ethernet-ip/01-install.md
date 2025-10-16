# 01 – Install & “Hello PLC” for Rockwell  
*(CompactLogix, ControlLogix og Logix Echo)*

> **Formål:** Få Python til at læse/skriv **direkte på tags** i Rockwell Logix-PLC’er via **EtherNet/IP (CIP)**.  
> Vi bruger **pycomm3**. Det er enkelt og kræver ikke OPC.

---

## 0) Hvad skal du have klar?

- **En PLC**:  
  - **CompactLogix** (53xx/54xx/55xx) **eller** **ControlLogix** (1756).  
  - **Logix Echo** (virtuel ControlLogix) kan også bruges – behandles som ControlLogix.
- **IP-adresse** til det Ethernet-interface, du vil forbinde til:
  - CompactLogix: CPU’ens indbyggede Ethernet.
  - ControlLogix: **ENxT Ethernet-modul** (f.eks. 1756-EN2T/EN3T).
  - Logix Echo: dit **virtuelle ENxT-moduls IP**.
- **3 simple controller-tags** i projektet (Controller Scope):  
  - `MyBool`  : **BOOL**, External Access = **Read/Write**  
  - `MyInt`   : **INT** (16-bit), External Access = **Read/Write**  
  - `MyReal`  : **REAL** (float), External Access = **Read/Write**

> Porten er **TCP 44818**. Sørg for at din firewall ikke blokerer.

---

## A) PLC – klargøring i Studio 5000 / Logix Echo (trin for trin)

### CompactLogix
1. **Sæt IP** på CPU’ens Ethernet (f.eks. `192.168.1.50`).  
2. Opret tags (`MyBool`, `MyInt`, `MyReal`) som **Controller Tags** med **External Access = Read/Write**.  
3. **Download** og sæt controller i **Run**.

### ControlLogix (1756-chassis)
1. Sæt IP på **ENxT-modulet** (f.eks. `192.168.1.60`).  
2. Find **CPU’ens slot-nummer** i chassiset (typisk **slot 0**, men kig i projektet).  
3. Opret tags som ovenfor → **Download** → **Run**.

### Logix Echo (virtuel)
1. Opret et virtuelt chassis i **FactoryTalk Logix Echo**.  
2. Tilføj et **virtuelt ENxT-modul** og giv det en **IP** (f.eks. `192.168.1.70`).  
3. Tilføj en **virtuel controller** (L8x). Notér **CPU-slot**.  
4. Opret tags i Studio 5000 mod Echo-controlleren → **Download** → **Run**.  
   *For Python er Echo = ControlLogix: du forbinder til ENxT-IP og angiver CPU-slot.*

---

## B) PC – Python og pycomm3

1. Installer Python 3.10+  
2. (Valgfrit) Lav et projekt-miljø:
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Mac/Linux
````

3. Installer pakken:

```bash
pip install pycomm3
```

---

## C) “Hello Read” – læs tre tags (meget simpelt)

> **CompactLogix:** brug **kun IP** (ingen slot).
> **ControlLogix / Echo:** brug **"IP/slot"** (f.eks. `"192.168.1.60/0"`).

```python
# gem som: hello_read.py
from pycomm3 import LogixDriver

# VÆLG ÉN af linjerne herunder:
PLC = "192.168.1.50"      # CompactLogix (kun IP)
# PLC = "192.168.1.60/0"  # ControlLogix (ENxT-IP / CPU-slot)
# PLC = "192.168.1.70/0"  # Logix Echo (ENxT-IP / CPU-slot)

with LogixDriver(PLC) as plc:
    b = plc.read("MyBool").value
    i = plc.read("MyInt").value
    r = plc.read("MyReal").value

print("MyBool:", b)
print("MyInt :", i)
print("MyReal:", r)
```

Kør:

```bash
python hello_read.py
```

---

## D) “Hello Write” – skriv og læs igen

```python
# gem som: hello_write.py
from pycomm3 import LogixDriver

PLC = "192.168.1.50"      # eller "192.168.1.60/0" (CLX) / "192.168.1.70/0" (Echo)

with LogixDriver(PLC) as plc:
    # toggle bool
    cur = plc.read("MyBool").value
    plc.write("MyBool", not cur)

    # skriv tal
    plc.write("MyInt", 1234)     # INT  (-32768..32767)
    plc.write("MyReal", 3.14)    # REAL (float)

    # læs tilbage
    b = plc.read("MyBool").value
    i = plc.read("MyInt").value
    r = plc.read("MyReal").value

print("Efter skriv -> MyBool:", b, " MyInt:", i, " MyReal:", r)
```

---

## E) Hurtig fejlfinding

* **Kan ikke forbinde / timeout**

  * Tjek at du kan `ping`e IP’en fra PC’en.
  * Firewall: tillad Python udgående på **TCP 44818**.
  * **ControlLogix/Echo:** er CPU-**slot** korrekt i stien `"IP/slot"`?
* **Tag ikke fundet**

  * Stavning 1:1 med Studio 5000.
  * Ligger tagget i **Controller Tags**? (Program Tags kræver stien `Program:<Navn>.Tag`).
* **Kan ikke skrive**

  * **External Access** skal være **Read/Write**.
  * Test først med simple base-typer (BOOL/INT/REAL).
* **Echo specifikt**

  * Brug **ENxT-modulets IP** + **CPU-slot** (samme som ControlLogix).
  * Hvis IP’en er på et isoleret virtuelt net, så sørg for, at din PC også kan nå det net (vNIC/adapter).

---

## F) Næste skridt

* Live-plot (`FuncAnimation`) af et REAL-tag + CSV-log (samme opskrift som S7-forløbet).
* Kontinuerlig “main” der læser flere tags.
* Små write-øvelser (knap i Python der toggler et BOOL-tag).

> **Note:** I Logix læser/skriver du **direkte på tag-navne**. Du skal ikke håndtere bytes/bit som på S7 – det er derfor `pycomm3` er dejligt begyndervenlig her.
