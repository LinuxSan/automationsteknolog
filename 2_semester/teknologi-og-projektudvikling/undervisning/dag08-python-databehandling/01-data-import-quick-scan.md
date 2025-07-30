<!-- File: dag08-python-databehandling/01-dataimport-quick-scan.md -->

# 01 – Dataimport & Quick‑Scan

*Del af **Dag 08 – Python‑databehandling***

## 🎯 Formål

Et lynhurtigt datakvalitets‑check af `raw_data.csv` (gas, temp, RH, lux) for at opfylde læringsmål **1 & 2**.

## 🔧 Trin for trin

1. **Opret miljø**
   Placér denne fil i mappen `dag08-python-databehandling/` sammen med `raw_data.csv` og opret `quick_scan.py` **eller** en Jupyter‑notebook.
2. **Indlæs data**

   ```python
   import pandas as pd
   df = pd.read_csv("raw_data.csv", parse_dates=["timestamp"])
   ```
3. **Grundlæggende overblik**
   Udskriv `df.head()`, `df.info()` og `df.describe()`.
4. **NaN‑tjek**

   ```python
   na_counts = df.isna().sum()
   ```
5. **Værdigrænser & out‑of‑range**

   ```python
   limits = {
       "gas":  (0, 4095),
       "temp": (-10, 60),
       "hum":  (0, 100),
       "lux":  (0, 1023),
   }
   outliers = {col: (~df[col].between(*rng)).sum() for col, rng in limits.items()}
   ```
6. **Rapportér resultater**
   Generér filen `data_overview.md` med Markdown‑tabel:

   ```markdown
   | Kanal | NaN | Out‑of‑range |
   |-------|----:|-------------:|
   | gas   | 0   | 12 |
   | temp  | 0   | 0 |
   | hum   | 3   | 5 |
   | lux   | 0   | 0 |
   ```

## ✅ Peer‑review tjekliste

* [ ] Scriptet/Notebook kører uden fejl på undervisnings‑PC.
* [ ] `data_overview.md` findes og viser både NaN‑ og out‑of‑range tællinger.
* [ ] Variabel‑ og funktionsnavne er meningsfulde, og koden er kommenteret.

---

*Tip:* Brug `df[ col ].between(*limits[col]).value_counts()` til hurtigt at se fordelingen inden for/uden for grænserne.
