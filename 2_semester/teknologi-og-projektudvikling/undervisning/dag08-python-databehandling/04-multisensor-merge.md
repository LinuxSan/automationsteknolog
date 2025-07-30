# 04 – Multisensor Merge

*Del af **Dag 08 – Python‑databehandling***

---

## 🎯 Formål

Dette mini‑projekt viser, hvordan du **samler** data fra flere sensorer og en referencekilde på én præcis tidsakse, hvorefter du **kvantificerer nøjagtigheden** af dine egne målinger. Du lærer at

1. bruge `pandas`‑join til at synkronisere datasæt,
2. beregne **absolut fejl** (Mean Absolute Error, MAE) og **relativ procentfejl** (Mean Relative Error, MRE %),
3. udforme en kort rapport, der kommunikerer resultaterne klart til både teknikere og ikke‑teknikere.

Dermed dækker opgaven læringsmål **1, 2 & 3**.

---

## 📂 Forudsætninger

| Krav              | Beskrivelse                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------ |
| Resamplet datasæt | `resampled_1s.csv` fra **Opgave 03** – indeholder gas, temp, hum, lux‑kolonner på 1 s‑grid |
| Reference­datasæt | `reference.csv` i mappen `data/` med identiske kolonnenavne og et `timestamp`‑felt         |
| Mappestruktur     |                                                                                            |

````text
└── dag08-python-databehandling/
    ├── 04-multisensor-merge.md   ← denne fil
    ├── resampled_1s.csv
    ├── data/
    │   └── reference.csv
    └── merge.py / .ipynb
```|
| Biblioteker | `pandas ≥ 2.0`, `numpy`, `tabulate` (valgfri til flot rapporttabel) |

---

## 🔧 Trin for trin

> **Tip:** Kopiér kodeblokkene til `merge.py`; hver blok kan køres isoleret, så du kan teste undervejs.

### 1. Indlæs datasæt
```python
import pandas as pd

sensor = pd.read_csv("resampled_1s.csv", parse_dates=["timestamp"], index_col="timestamp")
ref    = pd.read_csv("data/reference.csv",    parse_dates=["timestamp"], index_col="timestamp")

# Sikre kronologisk rækkefølge
sensor = sensor.sort_index()
ref    = ref.sort_index()
````

### 2. Merge på fælles tidsstempler

```python
merged = sensor.join(ref, lsuffix="_meas", rsuffix="_ref", how="inner")
print(f"Antal fælles tidsprøver: {len(merged):,}")
merged.to_csv("merged.csv")
```

`how="inner"` sikrer, at kun rækker hvor **begge** datasæt har målinger bevares; herved undgås kunstige NA‑felter.

### 3. Fejlberegning pr. kanal

```python
meas_cols = merged.filter(like="_meas").columns
ref_cols  = merged.filter(like="_ref").columns

abs_err = (merged[meas_cols] - merged[ref_cols].values).abs()
rel_err = abs_err.div(merged[ref_cols].replace(0, pd.NA).abs()) * 100  # %

summary = pd.concat({
    "MAE":    abs_err.mean().round(3),
    "MRE_%":  rel_err.mean().round(2)
}, axis=1)
```

> **Bemærk:** `.values` sikrer element‑wise subtraktion uanset kolonnenavne, men rækkefølgen **skal** være ens. Filtrene ovenfor sørger for korrekt sortering.

### 4. Gem og vis resultater

```python
summary.to_markdown("summary.md")
print(summary)
```

Eksempel på output:

```text
             MAE  MRE_%
 gas_meas   7.42   3.15
 temp_meas  0.18   0.29
 hum_meas   1.67   1.82
 lux_meas  12.50   2.05
```

### 5. Skriv kort rapport

Opret `merge_report.md` med:

* **Indledning** (2‑3 sætninger om formål og datasæt)
* Markdown‑tabel indsat fra `summary.md`
* **Analyse**: hvilke kanaler performer bedst/værst, mulige årsager (kalibrering, sensor­støj, reference­usikkerhed)
* **Anbefaling**: hvilke sensorer bør kalibreres, og hvor stor forbedring man forventer

Du kan automatisk generere rapporten med Python:

```python
with open("merge_report.md", "w", encoding="utf-8") as f:
    f.write("# Merge‑rapport\n\n")
    f.write("## Fejlsammenfatning\n\n")
    f.write(summary.to_markdown())
    f.write("\n\n> Gas‑sensoren viser den største absolutte fejl; en ny kalibrering anbefales.\n")
```

---

## ✅ Peer‑review tjekliste

* [ ] **Koden** kører uden fejl, og `merged.csv` + `summary.md` genereres.
* [ ] `summary.md` indeholder både **MAE** og **MRE %** med tre/fem relevante decimaler.
* [ ] Rapporten (`merge_report.md`) forklarer tydeligt resultatet på < 150 ord.
* [ ] Variabel‑ og funktionsnavne er sigende, og der er **inline‑kommentarer** til ikke‑triviale udtryk.
* [ ] Git‑historikken viser mindst **to commits**: én for kode, én for rapport.

---

### 📌 Ekstra idéer (frivilligt)

* Plot *error‑bands* over tid for hver sensor for at se driftsfejl.
* Udregn **Root Mean Square Error (RMSE)** og sammenlign med MAE.
* Brug `seaborn.regplot` til at visualisere korrelation mellem målt og reference.

---

*Tip:* Hvis reference‐filen indeholder data fra en **kalibreret laboratoriemåler**, kan du bruge regressionslinjen fra fejlplottet til at kompensere målingerne on‑the‑fly og forbedre nøjagtigheden i fremtidige logninger.
