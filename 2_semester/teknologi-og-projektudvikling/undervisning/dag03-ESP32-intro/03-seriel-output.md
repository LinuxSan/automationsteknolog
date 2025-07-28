# 🖨️ 03 – Seriel output med MicroPython

I denne guide lærer du at sende struktureret seriel output fra ESP32 med MicroPython. Det er vigtigt, at dine måledata er lette at læse – både for dig selv og for Python, der skal analysere dem senere.

---

## 🎯 Mål for modulet

* Bruge `print()` til at vise sensordata i Thonny Shell
* Strukturere data som CSV-lignende linjer
* Klargøre seriel output til at kunne læses i Python

---

## 📤 Print dine data

```python
from machine import ADC, Pin
from time import sleep

sensor = ADC(Pin(34))  # fx LDR på GPIO34
sensor.atten(ADC.ATTN_11DB)  # 0–3.3V

while True:
    værdi = sensor.read()
    print(værdi)
    sleep(1)
```

---

## 📋 Strukturér output som CSV

For at kunne importere dine data i Pandas senere, bør du formatere hver linje sådan her:

```python
print("timestamp,værdi")
```

Eksempel:

```python
from machine import ADC, Pin
from time import sleep
from time import time

sensor = ADC(Pin(35))
sensor.atten(ADC.ATTN_11DB)

while True:
    ts = time()
    val = sensor.read()
    print(f"{ts},{val}")
    sleep(1)
```

> Resultatet bliver f.eks. `1725010892,865` – UNIX-tid og måleværdi

---

## 🧠 Tip

* UNIX-tid kan let konverteres til rigtig dato i Python
* Brug `sleep()` for at styre målefrekvens
* Hvis du måler flere sensorer: print flere kolonner adskilt af komma

---

## 🧪 Øvelser

1. Print målinger fra LDR som én værdi per linje
2. Strukturér dine data som `timestamp,værdi`
3. Tilføj evt. kolonnenavn som første linje
4. Afprøv `time.sleep_ms(500)` for hurtigere logning

---

## ✅ Tjekliste

* [ ] Jeg har printet sensordata i Thonny Shell
* [ ] Jeg har struktureret output som CSV-linje
* [ ] Jeg har testet med UNIX timestamp og værdi
* [ ] Jeg forstår, hvordan det kan bruges i Python senere

---

> Du har nu klargjort ESP32-output til Python-datalogning!
