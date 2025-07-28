# 🧪 04 – Eksperimenter med ESP32 og sensorer

I denne guide prøver du forskellige sensoropsætninger og eksperimenter. Formålet er at producere meningsfulde måledata, som du senere kan analysere i Python.

---

## 🎯 Mål for modulet

* Afprøve flere sensorer (analog og digital)
* Producere real-world måledata med tidsstempler
* Forstå hvordan sensoropsætning påvirker data

---

## 📊 Forslag til eksperimenter

### 🔦 Lysmåling med LDR

* Tilslut LDR til GPIO34 + 10kΩ modstand til GND
* Mål lysstyrke i forskellige lysforhold (mørkt, dagslys, lommelygte)

```python
from machine import ADC, Pin
from time import sleep

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

while True:
    print(ldr.read())
    sleep(1)
```

### 🌬️ Luftfugtighed og temperatur med DHT22

* Tilslut DHT22 til GPIO4 med pull-up modstand (4.7k–10kΩ)
* Mål temperatur og luftfugtighed i forskellige rum og tidspunkter

```python
import dht
from machine import Pin
from time import sleep

sensor = dht.DHT22(Pin(4))

while True:
    sensor.measure()
    print(sensor.temperature(), sensor.humidity())
    sleep(2)
```

### 🧪 Gas-eksperiment med MQ-sensor

* Tilslut analogt output til GPIO35
* Mål reaktion ved fx parfume, håndsprit, røg

```python
gas = ADC(Pin(35))
gas.atten(ADC.ATTN_11DB)

while True:
    print(gas.read())
    sleep(1)
```

---

## 📋 Opgaver

1. Vælg to sensorer og lav målinger i minimum 2 omgivelser
2. Gem måledata (kopier fra Thonny eller brug logfil-plugin)
3. Strukturér målingerne med `timestamp,værdi`
4. Notér forskelle i output ved forskellige påvirkninger

---

## ✅ Tjekliste

* [ ] Jeg har lavet målinger med min(e) sensor(er)
* [ ] Jeg har sammenlignet output i to forskellige omgivelser
* [ ] Jeg har logget mine målinger som tekst eller CSV
* [ ] Jeg forstår hvordan sensorvalg og miljø påvirker output

---

> Disse data kan du bruge i Python fra næste undervisningsdag – gem dem!
