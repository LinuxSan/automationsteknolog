# 🧪 Opgave 2 – Beregn gennemsnit pr. time

## 📘 Introduktion

Ved at gruppere målinger efter tid – fx én gang i timen – kan du danne et mere overskueligt og informativt overblik over trends og ændringer. Det bruges bl.a. til at generere rapporter, overvåge systemers drift eller finde mønstre, som er svære at få øje på i rå data.

Denne opgave træner dig i at bruge Pandas’ `resample()`-funktion til at aggregere sensordata over tid.

---

## 🎯 Formål

- Forstå hvordan man grupperer målinger pr. tidsinterval
- Lære at anvende `resample()` med datetime-index
- Udtrække opsummerende statistik pr. time (middelværdi)

---

## 🛠️ Kompetencer

Ved at løse denne opgave træner du:
- Håndtering af tidsserier med datetime-format
- Tidsbaseret dataopsummering i Pandas
- Eksport og analyse af aggregerede datasæt

---

## 📂 Opgavebeskrivelse

1. Indlæs `delta_data.csv` fra din `data/` mappe.
2. Konverter kolonnen `tid` til `datetime` med `pd.to_datetime()`.
3. Sæt kolonnen `tid` som index.
4. Brug `resample("1H").mean()` til at beregne gennemsnit pr. time.
5. Gem det nye datasæt som `time_stats.csv`.

---

## 💻 Eksempel

```python
import pandas as pd

df = pd.read_csv("../data/delta_data.csv")
df["tid"] = pd.to_datetime(df["tid"])
df = df.set_index("tid")

time_stats = df.resample("1H").mean()
time_stats.to_csv("../data/time_stats.csv")
```

---

## ✅ Klar til næste skridt?

Når du har genereret et aggregeret datasæt pr. time og verificeret indholdet, er du klar til:

🔍 **Opgave 3 – Tæl hvor mange målinger der blev sorteret fra**
