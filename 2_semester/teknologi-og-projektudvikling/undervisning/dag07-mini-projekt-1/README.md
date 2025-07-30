# 🏡 Dag 07 – Mini-projekt: Sensorbaseret måling (ESP32 ↔ Python)

I dette mini-projekt skal du samle de teknikker, du har lært i de forrige moduler, i ét sammenhængende forløb. Du skal opsamle målinger fra et ESP32-baseret sensormodul, gemme og analysere data i Python samt visualisere og validere værdier med sanity checks og plausibilitetstests.

Projektet bruger tre specifikke sensorer:
- DHT22 (temperatur og luftfugtighed)
- LDR (lyssensor)
- MQ2 (gassensor)

Sensorerne tilsluttes ESP32, og data sendes til computeren over seriel port.

---

## 🎯 Mål for projektet

- Læse data fra DHT22, LDR og MQ2 med ESP32 og MicroPython
- Sende data i fast format over seriel port (fx: `25.4,48.1,700`)
- Tidsstemple og gemme data i Pandas på PC'en via VS Code
- Validere data med sanity check og plausibilitetstest
- Visualisere sensordata og markere fejl
- (Bonus) Byg videre med watchdog eller live-graf i Streamlit

---

## 📦 Hardware og software

- ESP32 med MicroPython installeret (brug Thonny til upload)
- Sensorer: DHT22, LDR og MQ2 (gassensor)
- VS Code på PC med Python + Pandas + Matplotlib
- Seriel forbindelse (USB)

---

## 📁 Mappestruktur (forslag)

```
sensorprojekt/
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

Eksempel på script (tilpas til dine pins):

```python
from machine import Pin, ADC
from dht import DHT22
import time

sensor = DHT22(Pin(14))           # DHT22
ldr = ADC(Pin(34))                # LDR
ldr.atten(ADC.ATTN_11DB)
gas = ADC(Pin(35))                # MQ2
gas.atten(ADC.ATTN_11DB)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        lys = ldr.read()
        gas_val = gas.read()
        print(f"{temp},{hum},{lys},{gas_val}")
        time.sleep(1)
    except:
        print("Fejl i måling")
        time.sleep(1)
```

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
    if linje.count(',') == 3:
        try:
            temp, hum, lys, gas = map(float, linje.split(","))
            data.append({
                "tid": pd.Timestamp.now(),
                "temp": temp,
                "fugt": hum,
                "lys": lys,
                "gas": gas
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
- `0 < lys < 4096`
- `0 < gas < 4096`
- ændring fra sidste måling må ikke overstige defineret tærskel

---

## 📈 Trin 4 – Visualisering

Lav to grafer:
- Rå vs. filtrerede data (sanity + plausibilitet)
- Fejltælling over tid eller pr. sensor

---

## ✅ Evaluering og aflevering

- [ ] ESP32-script dokumenteret og funktionelt
- [ ] Python logger opretter og gemmer korrekt datasæt
- [ ] Der er sanity check og plausibilitetstest
- [ ] Der er en eller flere meningsfulde visualiseringer
- [ ] Mappestruktur og README.md er oprettet

---

> Data er kun brugbare, hvis de giver mening. Dette projekt lærer dig at forbinde sensorer, analysere signaler og sikre datas kvalitet med både teknik og sund fornuft.
