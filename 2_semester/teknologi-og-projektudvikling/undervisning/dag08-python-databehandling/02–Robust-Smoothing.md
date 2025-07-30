<!-- File: dag08-python-databehandling/02-robust-smoothing.md -->

# 02 – Robust Smoothing

*Del af **Dag 08 – Python‑databehandling***

## 🎯 Formål

At sammenligne rullende *median* og rullende *middel* på **gassensor‑ og temperatursignaler** for at vurdere, hvilken glatning der bedst bevarer hurtige ændringer – læringsmål **3 & 4**.

## 📂 Forudsætninger

Kør først Opgave 01 og sikre, at `raw_data.csv` er indlæst korrekt. Du kan arbejde direkte på den rå fil *eller* først filtrere NaN /out‑of‑range data.

## 🔧 Trin for trin

1. **Indlæs data**

   ```python
   import pandas as pd
   df = pd.read_csv("raw_data.csv", parse_dates=["timestamp"])
   # evt. drop NaN eller filtrér outliers her
   ```
2. **Definér parametre**

   ```python
   WINDOW = 5  # prøv også 3 og 11 senere
   cols = ["gas", "temp"]  # kolonner der skal glattes
   ```
3. **Beregn rullende middel & median**

   ```python
   df_mean = df[cols].rolling(window=WINDOW, center=True).mean().add_suffix("_mean")
   df_median = df[cols].rolling(window=WINDOW, center=True).median().add_suffix("_median")
   df = pd.concat([df, df_mean, df_median], axis=1)
   ```
4. **Visualiser forskellen**

   ```python
   import matplotlib.pyplot as plt

   fig, ax = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
   for i, col in enumerate(cols):
       ax[i].plot(df["timestamp"], df[col], alpha=0.4, label="Raw")
       ax[i].plot(df["timestamp"], df[f"{col}_mean"], label="Mean")
       ax[i].plot(df["timestamp"], df[f"{col}_median"], label="Median")
       ax[i].set_ylabel(col)
       ax[i].grid(True)
       ax[i].legend()
   plt.savefig("figures/robust_smoothing.png", dpi=150)
   ```
5. **Kvantiﬁcer glatningen**
   Beregn *Mean Squared Error* (MSE) mellem de glattede serier og den rå serie for hvert vindue‐valg:

   ```python
   from sklearn.metrics import mean_squared_error

   mse_mean = mean_squared_error(df["gas"].dropna(), df["gas_mean"].dropna())
   mse_median = mean_squared_error(df["gas"].dropna(), df["gas_median"].dropna())
   ```

   Gentag for `temp` og evt. flere vinduesstørrelser.
6. **Rapportér resultater**
   Opret `smoothing_report.md` og indsæt:

   * tabel over MSE for alle testede vinduesstørrelser
   * figuren `figures/robust_smoothing.png`
   * kort tekstkonklusion (hvilken metode/vindue du anbefaler og hvorfor).

## ✅ Peer‑review tjekliste

* [ ] Koden kører uden fejl og bruger rullende mean **og** median.
* [ ] Figuren viser rå data, mean og median for både gas & temp.
* [ ] `smoothing_report.md` indeholder MSE‑tabel og refleksion.
* [ ] Variabel‑ og funktionsnavne er sigende, og koden er kommenteret.

---

*Tip:* Brug `df[col].rolling(window, center=True).median()` for at undgå fase‑forskydning, og eksperimenter med forskellige `WINDOW`‑størrelser for at se trade‑offs mellem støj‐reduktion og signal‑latenstid.
