# 🧪 Opgave 1 – Beregn forskelle mellem målinger

## 📘 Introduktion

Når vi arbejder med tidsserier fra sensorer, kan det være nyttigt at se på, hvordan værdierne ændrer sig fra én måling til den næste. Det kan afsløre trends, ustabilitet eller pludselige ændringer, som kan være relevante for både analyser og plausibilitetstests.

Denne opgave fokuserer på at beregne ændringer over tid (delta) for temperatur og luftfugtighed, som er centrale målinger fra DHT22-sensoren.

---

## 🎯 Formål

- Forstå hvordan `diff()` i Pandas fungerer på tidsserier
- Lære at tilføje afledte kolonner til et eksisterende datasæt
- Forberede datasættet til mere avancerede analyser, fx fejldetektion

---

## 🛠️ Kompetencer

Ved at løse denne opgave træner du:
- Arbejde med rensede datasæt i Pandas
- Beregning af ændringer i målinger over tid
- Strukturering og berigelse af data

---

## 📂 Opgavebeskrivelse

Du skal indlæse det rensede datasæt `renset_data.csv`, beregne forskellen mellem hver måling og den forrige, og gemme det som nye kolonner i datasættet:
- `delta_temp` for ændring i temperatur
- `delta_fugt` for ændring i luftfugtighed

Anvend `pandas.DataFrame.diff()` til formålet. 

Gem det nye datasæt som `delta_data.csv` i din `data/` mappe.

---

## 💻 Eksempel

```python
import pandas as pd

df = pd.read_csv("../data/renset_data.csv")
df["delta_temp"] = df["temp"].diff()
df["delta_fugt"] = df["fugt"].diff()

df.to_csv("../data/delta_data.csv", index=False)
```

---

## ✅ Klar til næste skridt?

Når du har gennemført denne opgave og sikret dig at dine kolonner er korrekt beregnet og gemt, går du videre til:

📈 **Opgave 2 – Beregn gennemsnit pr. time**
