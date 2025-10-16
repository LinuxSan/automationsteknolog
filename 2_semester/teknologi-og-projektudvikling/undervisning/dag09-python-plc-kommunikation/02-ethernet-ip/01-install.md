# 01 – Install & “Hello PLC” for Rockwell (CompactLogix/ControlLogix/Micro800)

> **Mål:** Få din PC og PLC til at snakke sammen via **EtherNet/IP (CIP)** med Python.  
> Vi bruger **pycomm3** (nem og stabil). Ingen OPC, ingen tunge drivere.

---

## 0) Hvad du skal bruge

- **En Rockwell PLC**  
  - CompactLogix 53xx/54xx/55xx eller ControlLogix (1756).  
  - Micro800 (820/850/870) virker også — brug samme opskrift.
- **IP-adresse** på PLC’en (fx `192.168.1.50`).  
- **En controller-tag** du kan læse/skriv (vi laver dem i Trin A).

> Porten der bruges er **44818/TCP** (EtherNet/IP). Hvis du har Windows-firewall, så sørg for at Python må snakke ud.

---

## A) PLC: forbered i Studio 5000 / CCW (step-by-step)

1) **Sæt IP på PLC**  
   - CompactLogix/ControlLogix: IP sættes på CPU’ens Ethernet-port eller på et ENxT-modul.  
   - Micro800 (CCW): sæt IP i controllerens kommunikationsindstillinger.

2) **Lav 3 enkle controller-tags** (Controller Scope)  
   - `MyBool`  : **BOOL**, External Access = **Read/Write**  
   - `MyInt`   : **INT** (16-bit), External Access = **Read/Write**  
   - `MyReal`  : **REAL** (float), External Access = **Read/Write**  
   *(External Access er vigtig — ellers kan man ikke skrive udefra.)*

3) **Download** til PLC og sæt i **Run**.

4) **Find slot-nummer (kun ControlLogix i chassis)**  
   - CPU’en står i et **slot** (typisk **0**). Du skal bruge slot i forbindelsesstien senere.  
   - CompactLogix/Micro800 bruger bare IP (ingen slot).

> Mini-tjek: Kan du **ping’e** PLC-IP’en fra din PC?

---

## B) PC: Python og pakker (step-by-step)

1) Installer Python 3.10+ (Windows/Mac/Linux).  
2) (Valgfrit) Lav et projekt-miljø:

```bash   
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   # source .venv/bin/activate  # Mac/Linux
````

3. Installer pakken:

```bash
pip install pycomm3
```

---

## C) Første læsning – “Hello PLC” (meget simpelt)

> **CompactLogix/Micro800:** brug bare `"PLC_IP"`
> **ControlLogix:** brug `"PLC_IP/slot"` (fx `"192.168.1.50/0"` hvis CPU står i slot 0)

```python
# gem som: hello_read.py
from pycomm3 import LogixDriver

PLC = "192.168.1.50"   # CompactLogix/Micro800
# PLC = "192.168.1.50/0"  # ControlLogix: /<slot>

with LogixDriver(PLC) as plc:
    val_bool = plc.read("MyBool").value
    val_int  = plc.read("MyInt").value
    val_real = plc.read("MyReal").value

print("MyBool:", val_bool)
print("MyInt :", val_int)
print("MyReal:", val_real)
```

Kør:

```bash
python hello_read.py
```

**Hvis det fejler:**

* IP rigtig?
* For ControlLogix: er **slot** korrekt?
* Er tag-navnene præcis de samme (store/små bogstaver er ok, men stavning skal matche)?
* Er “External Access” sat til **Read/Write** på tagget?

---

## D) Første skrivning – toggle og tal

```python
# gem som: hello_write.py
from pycomm3 import LogixDriver

PLC = "192.168.1.50"   # eller "192.168.1.50/0" for ControlLogix

with LogixDriver(PLC) as plc:
    # 1) Toggle MyBool
    current = plc.read("MyBool").value
    plc.write("MyBool", not current)

    # 2) Skriv en INT og en REAL
    plc.write("MyInt", 1234)       # INT (−32768..32767)
    plc.write("MyReal", 3.14)      # REAL (float)

print("Skrevet: MyBool toggled, MyInt=1234, MyReal=3.14")
```

Kør:

```bash
python hello_write.py
```

> Du behøver ikke læse/skrive bytes/bit manuelt som med S7.
> I Logix skriver/læser du **direkte på tag-navne**.

---

## E) “Smoke test” – ét script der læser, skriver og læser igen

```python
# gem som: smoke_test.py
from pycomm3 import LogixDriver

PLC = "192.168.1.50"   # Compact/Micro
# PLC = "192.168.1.50/0"  # ControlLogix

with LogixDriver(PLC) as plc:
    # Læs før
    b0 = plc.read("MyBool").value
    i0 = plc.read("MyInt").value
    r0 = plc.read("MyReal").value
    print("FØR  ->", b0, i0, r0)

    # Skriv nye værdier
    plc.write("MyBool", not b0)
    plc.write("MyInt",  i0 + 1)
    plc.write("MyReal", r0 + 0.1)

    # Læs efter
    b1 = plc.read("MyBool").value
    i1 = plc.read("MyInt").value
    r1 = plc.read("MyReal").value
    print("EFTER ->", b1, i1, r1)
```

---

## F) Hurtig fejlfinding

* **Timeout / kan ikke forbinde**

  * Tjek at du kan **ping’e** IP’en.
  * Windows-firewall: tillad Python på **udgående**; port **44818/TCP**.
  * Forkert slot på ControlLogix? Prøv `.../0`.
* **Tag ikke fundet**

  * Stavning og scope: er det **Controller Tags** (ikke kun Program Tags)?
  * Hvis det **er** et Program Tag: brug `Program:<ProgramNavn>.TagNavn` (fx `Program:MainProgram.MyInt`).
* **Kan ikke skrive**

  * Tjek at taggenes **External Access = Read/Write**.
  * Nogle strukturer/alias’er kan være Read-only — test med simple base-typer først (BOOL/INT/REAL/DINT).
* **Micro800**

  * Brug kun IP (ingen slot). Navngivning af tags skal matche det, du har i CCW.

---

## G) Hvad er næste skridt?

* **02 – Read & plot:** Læs flere tags og vis dem i et simpelt print eller Matplotlib.
* **03 – Write-øvelser:** Knapper i Python der toggler/skriversættet.
* **04 – Logging:** Py + `pandas` til CSV (som I gjorde til S7).
* **Bonus:** Vis `FuncAnimation` live-plot af et REAL-tag og samtidig CSV-log (samme mønster som S7-opgaven).
