# 05 – **Write i loop** (Rockwell)
*(CompactLogix, ControlLogix og Logix Echo, via `pycomm3`)*

> For begyndere. Vi skriver værdier til tags i en **kontinuerlig løkke** og/eller via en **meget simpel menu**.
> Ingen smarte tricks – bare trin for trin.

**Forudsætninger fra 01–03:**
- Du kan forbinde til PLC (IP eller `IP/slot` for ControlLogix/Echo).
- Du har tre Controller Tags: `MyBool` (BOOL), `MyInt` (INT), `MyReal` (REAL).
- Installeret pakke:
```bash
pip install pycomm3
````

---

## 1) Opgave 1 – Toggle et BOOL **i en while-løkke** (ingen try/except)

**Idé:** Hvert sekund læser vi `MyBool`, skriver den modsatte værdi (toggle), og viser resultatet.
Stop med `Ctrl + C`.

```python
# gem som: opg1_toggle_bool_loop.py
# kør: python opg1_toggle_bool_loop.py

import time
from pycomm3 import LogixDriver

# VÆLG ÉN:
PLC = "192.168.1.50"      # CompactLogix
# PLC = "192.168.1.60/0"  # ControlLogix / Echo (IP/slot)

plc = LogixDriver(PLC)
plc.open()

print("Starter toggle af MyBool... (tryk Ctrl + C for at stoppe)")
while True:
    værdi_før = plc.read("MyBool").value
    plc.write("MyBool", not værdi_før)
    værdi_efter = plc.read("MyBool").value
    print("MyBool før:", værdi_før, " efter:", værdi_efter)
    time.sleep(1.0)  # vent 1 sekund mellem hver toggle

# bemærk: vi lukker ikke pænt her (det gør vi i næste opgave)
```

**Hvad sker der?**

1. åbn forbindelse → 2) læs → 3) skriv modsat → 4) læs igen → 5) print → 6) gentag.

---

## 2) Opgave 2 – Samme loop, men med **try / except / finally**

**Idé:** Vi vil altid lukke forbindelsen pænt, også ved fejl eller ved `Ctrl + C`.

```python
# gem som: opg2_toggle_bool_try.py
# kør: python opg2_toggle_bool_try.py

import time
from pycomm3 import LogixDriver

PLC = "192.168.1.50"
# PLC = "192.168.1.60/0"

plc = LogixDriver(PLC)

try:
    plc.open()
    print("Starter toggle af MyBool... (Ctrl + C for stop)")
    while True:
        v = plc.read("MyBool").value
        plc.write("MyBool", not v)
        print("MyBool:", not v)
        time.sleep(1.0)

except KeyboardInterrupt:
    print("\nStopper efter Ctrl + C.")

except Exception as e:
    print("\nDer skete en fejl.")
    print("Fejl:", e)

finally:
    try:
        plc.close()
        print("Forbindelse lukket.")
    except:
        print("Forbindelsen var allerede lukket.")
```

---

## 3) Opgave 3 – **Meget enkel menu**: toggle, sæt INT, sæt REAL

**Idé:** Vi viser en menu i terminalen. Brugeren vælger, hvad der skal skrives.

* `1` = toggle `MyBool`
* `2` = skriv ny `MyInt`
* `3` = skriv ny `MyReal`
* `r` = læs og vis alle tre
* `q` = afslut

```python
# gem som: opg3_cli_menu_write.py
# kør: python opg3_cli_menu_write.py

from pycomm3 import LogixDriver

PLC = "192.168.1.50"
# PLC = "192.168.1.60/0"

def vis_menu():
    print("\n--- MENU ---")
    print("1: Toggle MyBool")
    print("2: Skriv MyInt")
    print("3: Skriv MyReal")
    print("r: Læs og vis alle")
    print("q: Afslut")

with LogixDriver(PLC) as plc:
    print("Forbundet til:", PLC)
    vis_menu()

    while True:
        valg = input("Vælg: ").strip().lower()

        if valg == "1":
            før = plc.read("MyBool").value
            plc.write("MyBool", not før)
            print("MyBool toggled. Ny værdi:", plc.read("MyBool").value)

        elif valg == "2":
            tekst = input("Skriv heltal til MyInt: ").strip()
            try:
                ny_int = int(tekst)
                plc.write("MyInt", ny_int)
                print("MyInt =", plc.read("MyInt").value)
            except ValueError:
                print("Det var ikke et heltal.")

        elif valg == "3":
            tekst = input("Skriv tal (float) til MyReal: ").strip()
            try:
                ny_real = float(tekst)
                plc.write("MyReal", ny_real)
                print("MyReal =", plc.read("MyReal").value)
            except ValueError:
                print("Det var ikke et tal.")

        elif valg == "r":
            v_bool = plc.read("MyBool").value
            v_int  = plc.read("MyInt").value
            v_real = plc.read("MyReal").value
            print("Læsning -> MyBool:", v_bool, " MyInt:", v_int, " MyReal:", v_real)

        elif valg == "q":
            print("Farvel.")
            break

        else:
            print("Ukendt valg.")
            vis_menu()
```

**Bemærk:** `with LogixDriver(PLC) as plc:` lukker automatisk forbindelsen, når `while`-løkke og `with`-blok er slut.

---

## 4) Opgave 4 – **Ramp** af et REAL-setpoint (trinvis op/ned i loop)

**Idé:** Vi ændrer `MyReal` lidt ad gangen, så det “kører op og ned” mellem to grænser.
Stop med `Ctrl + C`.

```python
# gem som: opg4_ramp_real_loop.py
# kør: python opg4_ramp_real_loop.py

import time
from pycomm3 import LogixDriver

PLC = "192.168.1.50"
# PLC = "192.168.1.60/0"

min_værdi = 0.0
max_værdi = 10.0
trin = 0.5          # hvor meget vi ændrer pr. skridt
pause = 0.5         # sekunder mellem skridt

plc = LogixDriver(PLC)

try:
    plc.open()
    nu = plc.read("MyReal").value  # start fra aktuel værdi
    retning = +1                   # +1 = op, -1 = ned
    print("Starter ramp af MyReal... (Ctrl + C for stop)")

    while True:
        # skriv nuværende værdi
        plc.write("MyReal", nu)
        print("MyReal =", nu)

        # forbered næste værdi
        nu = nu + (trin * retning)

        # hvis vi rammer grænserne, skift retning
        if nu >= max_værdi:
            nu = max_værdi
            retning = -1
        elif nu <= min_værdi:
            nu = min_værdi
            retning = +1

        time.sleep(pause)

except KeyboardInterrupt:
    print("\nStopper ramp.")

finally:
    try:
        plc.close()
        print("Forbindelse lukket.")
    except:
        pass
```

---

## 5) Opgave 5 – (Valgfri) **Kombinér** menu + ramp-toggle

**Idé:** Brug menupunkt til at **starte/stoppe** ramp fra Opgave 4, mens du stadig kan læse/toggle/sætte værdier.
Det er en fin øvelse i at tænke programflow. (Hold det enkelt: én “tilstand” ad gangen – enten ramp kører, eller menu venter på input.)

*Hint:* Du kan have en variabel `ramp_aktiv = False`.
Når brugeren vælger “start ramp”, sæt `ramp_aktiv = True` og kør en **lille** løkke, der kan stoppes på tastetryk (fx “s” for stop).

---

## Fejlfinding (kort)

* **Timeout / ingen forbindelse:** IP/slot korrekt? Kan du ping’e? Firewall på TCP 44818?
* **Kan ikke skrive:** External Access = Read/Write på tagget?
* **Værdier “hopper ikke”:** Opdaterer du hurtigt nok? Tjek at du faktisk skriver (print hjælper).
* **Menu virker “langsomt”:** `input()` venter på tastatur – det er meningen. For mere “live” UI skal man senere prøve tråde (ikke nødvendigt til denne lektion).

---

## Hvad er næste skridt?

* **06 – Plot + Write:** Live-plot af `MyReal` (FuncAnimation) **mens** du kan trykke en tast for at toggle `MyBool`.
* **07 – CSV + Ramp:** Log både rampens setpoint og et faktisk proces-tag (feedback) i samme fil.
