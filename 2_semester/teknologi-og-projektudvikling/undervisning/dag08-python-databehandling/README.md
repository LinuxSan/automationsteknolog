# 🧮 Dag 08 – Python: Avanceret databehandling af sensormålinger

I dette modul skal du arbejde videre med det datasæt, du har opbygget i mini-projektet. Du skal forfine og strukturere dine data, analysere trends og udlede indsigt gennem databehandling med Pandas. Formålet er at lære, hvordan man systematisk renser, filtrerer og forbereder sensorbaserede datasæt til rapportering og dokumentation.

---

## 🎯 Læringsmål

- Rense og strukturere datasæt (fx fjern `NaN`, sortér, konverter typer)
- Fjerne ugyldige/uplausible målinger
- Beregne statistik og måleresuméer
- Tilføje beregnede kolonner (glidende gennemsnit, forskelle, mv.)
- Eksportere data i struktureret form til rapport eller dokumentation

---

## 📁 Forventet struktur

Filerne fra dagen bør ligge i:

```
sensorprojekt/
├── data/
│   ├── målinger.csv
│   └── renset_data.csv
├── python/
│   └── databehandling.py
```

---

## 👨‍💻 Eksempelkode – Rensning og analyse

```python
import pandas as pd

# Indlæs rå data
df = pd.read_csv("../data/målinger.csv")

# Fjern ugyldige/uplausible rækker
valid = (df["temp"].between(0, 40) &
         df["fugt"].between(20, 90) &
         df["lys"].between(0, 4096) &
         df["gas"].between(0, 4096))

df = df[valid].copy()

# Sortér og nulstil indeks
df = df.sort_values("tid").reset_index(drop=True)

# Beregn glidende gennemsnit (vindue på 5)
df["temp_glidende"] = df["temp"].rolling(window=5).mean()
df["fugt_glidende"] = df["fugt"].rolling(window=5).mean()

# Eksportér til ny CSV
df.to_csv("../data/renset_data.csv", index=False)

# Vis statistik
print(df.describe())
```

---

## 🧪 Øvelser

- Tilføj kolonner med differens: `delta_temp`, `delta_fugt`
- Beregn gennemsnit pr. time (brug `.resample()` hvis muligt)
- Tæl hvor mange målinger der blev sorteret fra
- Lav en funktion der wrapper hele rensnings-pipelinen

---

## ✅ Tjekliste

- [ ] Jeg har filtreret ugyldige målinger ud
- [ ] Jeg har sorteret datasættet og tilføjet beregnede kolonner
- [ ] Jeg har gemt den rensede version til ny CSV
- [ ] Jeg har brugt `.describe()` til at udlede statistik

---

> Rensede data er grundlaget for al pålidelig analyse. Lær at identificere og fjerne støj, så du får et datasæt du tør stole på.
