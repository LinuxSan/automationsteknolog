# 🏡 Dag 07 – Mini-projekt: Smart House Dataflow (ESP32 ↔ Python)

I dette mini-projekt skal du samle de teknikker, du har lært i de forrige moduler, i ét sammenhængende forløb. Du skal opsamle målinger fra et ESP32-baseret Smart House-sæt (fra Keyestudio), gemme og analysere data i Python samt visualisere og validere værdier med sanity checks og plausibilitetstests.

Projektet bygger på sensorer monteret i dit Smart House-kit, f.eks. DHT22 (temp/fugt), LDR (lys), MQ2 (gas). Sensorer kan vælges og kombineres efter eget valg.

---

## 🎯 Mål for projektet

- Læse data fra én eller flere sensorer på ESP32 (MicroPython)
- Sende data i fast format over seriel port (fx: `25.4,48.1,700`)
- Tidsstemple og gemme data i Pandas på PC'en via VS Code
- Validere data med sanity check og plausibilitetstest
- Visualisere sensordata og markere fejl
- (Bonus) Byg videre med watchdog eller live-graf i Streamlit

---

## 📦 Hardware og software

- ESP32 med MicroPython installeret (brug Thonny til upload)
- Keyestudio Smart House-kit (KS5009)
- Sensorer: DHT22, LDR, MQ2, m.m.
- VS Code på PC med Python + Pandas + Matplotlib
- Seriel forbindelse (USB)

---

## 📁 Mappestruktur (forslag)

```
smart-house-project/
├── esp32/
│   └── main.py             # MicroPython-script til ESP32
├── python/
│   ├── main_logger.py      # Logger der læser data og gemmer CSV
│   ├── analyse.py          # Sanity check og plausibilitet
│   └── visualisering.py    # Plots og evt. Streamlit
└── data/
    └── målinger.csv
```

---

## 📡 Trin 1 – ESP32 kode (MicroPython i Thonny)

Eksempel på script (tilpas til dine sensorer):

```python
from machine import Pin
from dht import DHT22
import time

sensor = DHT22(Pin(14))
ldr = machine.ADC(Pin(34))
ldr.atten(machine.ADC.ATTN_11DB)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        lys = ldr.read()
        print(f"{temp},{hum},{lys}")
        time.sleep(1)
    except:
        print("Fejl i måling")
        time.sleep(1)
```

Upload scriptet med **Thonny** til din ESP32 og kør det direkte derfra.

---

## 💻 Trin 2 – Python logger (VS Code)

Script der læser data over seriel port og gemmer:

```python
import pandas as pd
import serial
import time

ser = serial.Serial('COM3', 115200, timeout=1)
data = []

while len(data) < 100:
    linje = ser.readline().decode().strip()
    if linje.count(',') == 2:
        try:
            temp, hum, lys = map(float, linje.split(","))
            data.append({
                "tid": pd.Timestamp.now(),
                "temp": temp,
                "fugt": hum,
                "lys": lys
            })
        except:
            continue

ser.close()
pd.DataFrame(data).to_csv("data/målinger.csv", index=False)
```

---

## 🔍 Trin 3 – Sanity check og plausibilitet

Brug funktioner fra tidligere opgaver til at filtrere:
- `0 < temp < 40`
- `20 < fugt < 90`
- `lys < 4096`
- ændring fra sidste måling må ikke overstige defineret tærskel

---

## 📈 Trin 4 – Visualisering

Lav to grafer:
- Rå vs. filtrerede data (sanity + plausibilitet)
- Fejltælling over tid

---

## ✅ Evaluering og aflevering

- [ ] ESP32-script dokumenteret og funktionelt
- [ ] Python logger opretter og gemmer korrekt datasæt
- [ ] Der er sanity check og plausibilitetstest
- [ ] Der er en eller flere meningsfulde visualiseringer
- [ ] Mappestruktur og README.md er oprettet

---

> Et Smart House uden sensorkontrol er bare en kasse med lys i. Giv det intelligens med Python og ESP32!

