# 📡 06 – Simuleret realtidsbehandling i Python

I denne guide lærer du at simulere realtidsmålinger og behandle dem trin for trin med Python og Pandas. Dette er nyttigt, når du vil teste live-scripts uden at være koblet til f.eks. en ESP32.

---

## 🎯 Mål for modulet

* Simulere datastream med løkke og ventetid
* Tilføje data løbende til DataFrame
* Beregne glidende gennemsnit i realtid

---

## ⏳ Simuler en datakilde

```python
import pandas as pd
import time
import random

målinger = []

for i in range(20):
    ny_værdi = random.randint(0, 1023)
    timestamp = pd.Timestamp.now()
    målinger.append({"tid": timestamp, "værdi": ny_værdi})
    print(f"{timestamp} → {ny_værdi}")
    time.sleep(0.5)

# Konverter til DataFrame
data = pd.DataFrame(målinger)
```

---

## 🧮 Beregn glidende gennemsnit

```python
data["glidende"] = data["værdi"].rolling(window=5).mean()
print(data.tail())
```

---

## 📈 Plot målinger og glidende gennemsnit

```python
import matplotlib.pyplot as plt

plt.plot(data["tid"], data["værdi"], label="Rå værdi")
plt.plot(data["tid"], data["glidende"], label="Glidende gns.")
plt.legend()
plt.show()
```

---

## 🧪 Øvelser

1. Simulér 50 målinger med ventetid og random værdi
2. Beregn glidende gennemsnit med `window=10`
3. Plot både rå data og glidende gennemsnit
4. Eksporter til `simuleret.csv`
5. (Ekstra) Lav betinget advarsel hvis `værdi > 1000`

---

## ✅ Tjekliste

* [ ] Jeg har simuleret data med `time.sleep()` og `random`
* [ ] Jeg har brugt `rolling()` til glidende gennemsnit
* [ ] Jeg har gemt og visualiseret data løbende
* [ ] Jeg forstår hvordan realtidsdata struktureres i Pandas

---

Dette modul klargør dig til at arbejde med sensor-data i realtid.
