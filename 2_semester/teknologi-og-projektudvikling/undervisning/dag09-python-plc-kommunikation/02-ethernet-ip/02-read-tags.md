# 02 – Connect & **Read** tags (Rockwell)
*(CompactLogix, ControlLogix og Logix Echo)*

> **For begyndere.** Vi holder koden enkel, én ting ad gangen, og forklarer hvert trin.

**Hvad skal være klar fra “01 – Install”:**
- PLC’ens IP-adresse.
- Hvis du har **ControlLogix/Echo**: CPU’ens **slot** i chassiset.
- Tre controller-tags (Controller Scope) med **External Access = Read/Write**:
  - `MyBool` (BOOL), `MyInt` (INT), `MyReal` (REAL).

**Pakken du skal bruge:**
```bash
pip install pycomm3
````

---

## 1) Opgave 1 – Vælg din forbindelsesstreng (Compact vs. ControlLogix/Echo)

I Rockwell verdenen er **forbindelsesstien** bare en tekststreng:

* **CompactLogix:** kun IP (eksempel: `"192.168.1.50"`).
* **ControlLogix/Echo:** IP **+ slot** (eksempel: `"192.168.1.60/0"` hvis CPU står i slot 0).

Du vælger **præcis én** linje og lader de andre stå som kommentar.

```python
# gem som: opg1_pick_plc.py
from pycomm3 import LogixDriver

# VÆLG KUN ÉN af disse tre linjer:
PLC = "192.168.1.50"     # CompactLogix (kun IP)
# PLC = "192.168.1.60/0" # ControlLogix (ENxT-IP / CPU-slot)
# PLC = "192.168.1.70/0" # Logix Echo (ENxT-IP / CPU-slot)

# lille test: åbn og luk forbindelsen
with LogixDriver(PLC) as plc:
    pass

print("Forbindelse OK:", PLC)
```

**Kør:**

```bash
python opg1_pick_plc.py
```

---

## 2) Opgave 2 – Læs en **BOOL** (`MyBool`)

**Idé:** Åbn forbindelse, læs ét tag, print værdien, luk forbindelsen igen.

```python
# gem som: opg2_read_bool.py
from pycomm3 import LogixDriver

# vælg din PLC-sti som i Opgave 1
PLC = "192.168.1.50"      # eller "192.168.1.60/0" for ControlLogix / Echo

with LogixDriver(PLC) as plc:
    value = plc.read("MyBool").value   # læs tagget
    print("MyBool:", value)            # vis resultatet
```

**Kør:**

```bash
python opg2_read_bool.py
```

---

## 3) Opgave 3 – Læs en **INT** (`MyInt`)

```python
# gem som: opg3_read_int.py
from pycomm3 import LogixDriver

PLC = "192.168.1.50"      # eller "192.168.1.60/0"

with LogixDriver(PLC) as plc:
    value = plc.read("MyInt").value
    print("MyInt:", value)
```

**Kør:**

```bash
python opg3_read_int.py
```

---

## 4) Opgave 4 – Læs en **REAL** (`MyReal`)

```python
# gem som: opg4_read_real.py
from pycomm3 import LogixDriver

PLC = "192.168.1.50"      # eller "192.168.1.60/0"

with LogixDriver(PLC) as plc:
    value = plc.read("MyReal").value
    print("MyReal:", value)
```

**Kør:**

```bash
python opg4_read_real.py
```

---

## 5) Opgave 5 – Læs **alle tre** i samme script

**Idé:** Læs tre tags efter hinanden og print dem. Det er stadig én simpel sekvens.

```python
# gem som: opg5_read_all.py
from pycomm3 import LogixDriver

PLC = "192.168.1.50"      # eller "192.168.1.60/0"

with LogixDriver(PLC) as plc:
    v_bool = plc.read("MyBool").value
    v_int  = plc.read("MyInt").value
    v_real = plc.read("MyReal").value

print("MyBool:", v_bool)
print("MyInt :", v_int)
print("MyReal:", v_real)
```

**Kør:**

```bash
python opg5_read_all.py
```

---

## 6) Opgave 6 – (Valgfri) Læs et **Program Tag**

Hvis dit tag ligger under et program (ikke Controller Tags), skal navnet have **program-stien** med:

* Eksempel: Programmet hedder `MainProgram` og tagget hedder `SpeedRef`.
* Så hedder det fulde navn: `Program:MainProgram.SpeedRef`

```python
# gem som: opg6_read_program_tag.py
from pycomm3 import LogixDriver

PLC = "192.168.1.60/0"    # eksempel: ControlLogix i slot 0
FULL_TAG = "Program:MainProgram.SpeedRef"

with LogixDriver(PLC) as plc:
    value = plc.read(FULL_TAG).value
    print("SpeedRef:", value)
```

---

## Hvad gør koden – helt kort

* `from pycomm3 import LogixDriver` – importerer drivermodulet.
* `with LogixDriver(PLC) as plc:` – åbner forbindelsen og lukker den **automatisk** igen, når blokken er færdig.
* `plc.read("TagNavn").value` – læser direkte på **tag-navnet** og giver dig Python-værdien (bool, int, float).

---

## Fejlfinding (tjek i denne rækkefølge)

1. **Kan du ping’e PLC’ens IP?**
2. **ControlLogix/Echo:** Er **slot** i stien korrekt? (ofte `.../0`)
3. **Stavning af tag-navn:** 1:1 som i Studio 5000.
4. **Scope:** Ligger tagget i **Controller Tags**? Hvis det er et **Program Tag**, brug `Program:<Navn>.Tag`.
5. **External Access:** Skal være **Read/Write** (ellers kan du ikke skrive – men du kan normalt læse).

---

## Næste kapitel

* **03 – Write-tags:** samme øvelser, bare skriv i stedet for at læse.
* Live-læsning med simpel løkke eller `FuncAnimation` + CSV-log kan vi tage i “04 – Plot & Log”.
