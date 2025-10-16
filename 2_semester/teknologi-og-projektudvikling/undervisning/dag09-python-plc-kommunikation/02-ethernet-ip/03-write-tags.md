# 03 – Connect & **Write** tags (Rockwell)
*(CompactLogix, ControlLogix og Logix Echo)*

> **For begyndere.** Vi skriver helt enkelt til tre tags: `MyBool`, `MyInt`, `MyReal`.  
> Du læste dem i “02 – Read”. Nu skriver vi værdier.

**Krav fra “01 – Install”:**
- PLC-IP er kendt.
- **ControlLogix/Echo:** du kender CPU’ens **slot** (ofte `0`).
- Tags findes som **Controller Tags** med **External Access = Read/Write**.

**Pakke:**
```bash
pip install pycomm3
````

---

## 1) Opgave 1 – Vælg din PLC-sti (samme som i 02)

* **CompactLogix:** kun IP (fx `"192.168.1.50"`).
* **ControlLogix/Echo:** `"IP/slot"` (fx `"192.168.1.60/0"`).

```python
# gem som: opg1_pick_plc_write.py
from pycomm3 import LogixDriver

# VÆLG KUN ÉN linje:
PLC = "192.168.1.50"     # CompactLogix
# PLC = "192.168.1.60/0" # ControlLogix
# PLC = "192.168.1.70/0" # Logix Echo

with LogixDriver(PLC) as plc:
    pass

print("Forbindelse OK:", PLC)
```

Kør:

```bash
python opg1_pick_plc_write.py
```

---

## 2) Opgave 2 – **Skriv en BOOL** (`MyBool`)

**Idé:** Læs først nuværende værdi. Skriv så den modsatte (toggle). Læs igen for at se resultatet.

```python
# gem som: opg2_write_bool.py
from pycomm3 import LogixDriver

PLC = "192.168.1.50"      # eller "192.168.1.60/0" (CLX/Echo)

with LogixDriver(PLC) as plc:
    før = plc.read("MyBool").value       # læs før
    plc.write("MyBool", not før)         # skriv modsat værdi
    efter = plc.read("MyBool").value     # læs efter

print("MyBool før:", før)
print("MyBool efter:", efter)
```

Kør:

```bash
python opg2_write_bool.py
```

---

## 3) Opgave 3 – **Skriv en INT** (`MyInt`)

**Idé:** Sæt et bestemt tal. Læs bagefter for at tjekke.

```python
# gem som: opg3_write_int.py
from pycomm3 import LogixDriver

PLC = "192.168.1.50"      # eller "192.168.1.60/0"
ny_int = 1234             # INT-område: -32768 .. 32767

with LogixDriver(PLC) as plc:
    plc.write("MyInt", ny_int)
    værdi = plc.read("MyInt").value

print("MyInt (skrevet):", ny_int)
print("MyInt (læst)   :", værdi)
```

---

## 4) Opgave 4 – **Skriv en REAL** (`MyReal`)

```python
# gem som: opg4_write_real.py
from pycomm3 import LogixDriver

PLC = "192.168.1.50"      # eller "192.168.1.60/0"
ny_real = 3.14            # hvilket som helst float-tal

with LogixDriver(PLC) as plc:
    plc.write("MyReal", ny_real)
    værdi = plc.read("MyReal").value

print("MyReal (skrevet):", ny_real)
print("MyReal (læst)   :", værdi)
```

---

## 5) Opgave 5 – **Skriv alle tre** i ét script

```python
# gem som: opg5_write_all.py
from pycomm3 import LogixDriver

PLC = "192.168.1.50"      # eller "192.168.1.60/0"

ny_bool = True
ny_int  = 2000
ny_real = 12.34

with LogixDriver(PLC) as plc:
    plc.write("MyBool", ny_bool)
    plc.write("MyInt",  ny_int)
    plc.write("MyReal", ny_real)

    # læs tilbage
    v_bool = plc.read("MyBool").value
    v_int  = plc.read("MyInt").value
    v_real = plc.read("MyReal").value

print("Efter skrivning:")
print("  MyBool:", v_bool)
print("  MyInt :", v_int)
print("  MyReal:", v_real)
```

---

## 6) Opgave 6 – (Valgfri) Skriv et **Program Tag**

Hvis dit tag ligger i et program, så brug program-stien:

* Eksempel: Program = `MainProgram`, Tag = `SpeedRef`
* Fuldt navn: `Program:MainProgram.SpeedRef`

```python
# gem som: opg6_write_program_tag.py
from pycomm3 import LogixDriver

PLC = "192.168.1.60/0"     # ControlLogix eller Echo
FULL_TAG = "Program:MainProgram.SpeedRef"
ny_værdi = 45.0            # eksempel: REAL

with LogixDriver(PLC) as plc:
    plc.write(FULL_TAG, ny_værdi)
    værdi = plc.read(FULL_TAG).value

print("SpeedRef (skrevet):", ny_værdi)
print("SpeedRef (læst)   :", værdi)
```

---

## Fejlfinding (kort)

* **Kan ikke skrive**

  * Tjek at tagget har **External Access = Read/Write**.
  * Prøv med helt simple base-typer først (BOOL/INT/REAL).
* **“Tag not found”**

  * Stavning 1:1 som i Studio 5000.
  * **Scope**: Controller Tag (ellers brug `Program:<Navn>.Tag`).
* **Timeout / ingen forbindelse**

  * IP korrekt? Kan du `ping`e?
  * **CLX/Echo:** Er **slot** rigtigt i stien (`"IP/0"` er ofte korrekt)?
  * Firewall: tillad Python udgående på **TCP 44818**.

---

## Næste trin

* “04 – Plot & Log”: Læs jævnligt, vis `REAL` som live-plot med **FuncAnimation**, og log samtidig til **CSV**.
* “05 – Write i loop”: Små knapper/CLI der sætter setpoints eller toggler bits i et kontrolleret loop.
