<!-- File: dag08-python-databehandling/03-uniform-resampling.md -->

# 03 – Uniform Resampling

*Del af **Dag 08 – Python-databehandling***

## 🎯 Formål

At ensarte tidsbasen til faste **1 sekund‑intervaller** for alle kanaler (gas, temp, RH, lux) og kvantificere den interpolationsfejl der introduceres. Dette adresserer læringsmål **1, 2 & 3**.

## 📂 Forudsætninger

* Kør først Opgave 01 (Quick‑Scan) og sørg for, at du har et validt `raw_data.csv`.
* Optionelt: kør Opgave 02 (Robust Smoothing) hvis du vil resample et glattet datasæt.

## 🔧 Trin for trin

1. **Indlæs og forbered**

   ```python
   import pandas as pd
   df = pd.read_csv("raw_data.csv", parse_dates=["timestamp"])
   df = df.set_index("timestamp").sort_index()  # sæt tidsstempel som index
   ```
2. **Resample til 1 s‑grid**

   ```python
   df_resampled = df.resample("1S").mean()
   # håndter manglende værdier med lineær interpolation
   df_resampled = df_resampled.interpolate(method="linear")
   ```
3. **Interpolationsfejl**
   For tidsstempler hvor der fandtes en original måling, beregn forskellen mellem dens værdi og den resamplede værdi.

   ```python
   common_idx = df.index.intersection(df_resampled.index)
   errors = (df.loc[common_idx] - df_resampled.loc[common_idx]).abs()
   mae = errors.mean()  # Mean Absolute Error pr. kanal
   ```
4. **Gem resultater**

   ```python
   df_resampled.to_csv("resampled_1s.csv")
   ```
5. **Rapport**
   Opret `resampling_report.md` og indsæt

   * Antal indsatte/interpulerede rækker pr. kanal (`df_resampled.isna().sum()` før interpolation)
   * MAE pr. kanal (fra `mae`)
   * Kort refleksion over om 1 s‑intervaller er passende eller om en anden opløsning er bedre.

## ✅ Peer‑review tjekliste

* [ ] `resampled_1s.csv` findes og har præcis 1 s‑spacing mellem rækker.
* [ ] `resampling_report.md` dokumenterer MAE og indsatte rækker.
* [ ] Koden er veldokumenteret, bruger `interpolate()` og håndterer indeks korrekt.

---

*Tip:* Prøv også `df.resample("500L")` (0,5 s) eller `"5S"` (5 s) og sammenlign MAE for at se effekten af opløsningen.
