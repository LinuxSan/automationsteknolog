# Dag 08 – Python Databehandling

> Teknologi & Projektudvikling · 2. semester · 5 ECTS

## 🔍 Formål

At omsætte rå måledata fra et **ESP32‑baseret sensor‑board** (gassensor, **DHT22** temperatur / luftfugtighed samt **LDR** lysstyrke) – eller fra PLC‑kilde – til et **renset**, **struktureret** og **dokumenteret** datasæt, klar til analyse & rapportering.

## 🎯 Læringsmål

Efter dagen kan du

1. Importere rå CSV‑filer til `pandas.DataFrame`.
2. Udføre sanity‑checks: datatyper, NaN‑rækker og grænseværdier.
3. Identificere + fjerne outliers via IQR‑ eller z‑score‑metode.
4. Glatte data med rullende middelværdi
   $\tilde{x}_i = \frac{1}{k}\sum_{j=i-\lfloor k/2 \rfloor}^{i+\lfloor k/2 \rfloor} x_j$
5. Gemme det rensede datasæt som `clean_data.csv`.
6. Visualisere tidsserier (gas‑ppm, °C, %RH, lux) i **matplotlib** med akse‑labels & grid.
7. Dokumentere pipeline samt push til GitHub.

## 🧰 Forudsætninger

| Fra dag | Viden/artefakt               | Anvendelse i dag 08                         |
| ------: | ---------------------------- | ------------------------------------------- |
|      03 | ESP32 datalogger‑firmware    | Logger gassensor + DHT22 + LDR til UART/CSV |
|      04 | `pyserial` datalogger‑script | Produceret `raw_data.csv`                   |
|      05 | Matplotlib‑plots             | Visning af sensor‑ og referencekurver       |
|      06 | Sanity‑check script          | Genbruges & udvides                         |

## 💪 Øvelser

> Hver øvelse ligger i sin egen undermappe (`øvelser/01-…` → `05-…`) og indeholder start‑kode, rå data og en peer‑review‑tjekliste.

1. **01‑Robust‑Smoothing** – Undersøg effekten af rullende *median* kontra *middel* på **gassensor‑ og temperatursignaler** og vurder hvilken glatning der bedst bevarer hurtige ændringer i koncentration/temperatur.
2. **02‑Uniform‑Resampling** – Resampler et uregelmæssigt tidsstempel‑datasæt (gas, °C, %RH, lux) til præcise 1 s‑intervaller og kvantificér interpolationsfejlen for hver sensor.
3. **03‑Multisensor‑Merge** – Slå målinger fra gas‑, DHT22‑ og LDR‑kanalerne sammen med et reference‑datasæt og beregn absolut samt relativ afvigelse pr. tidsprøve.
4. **04‑Auto‑Report** – Generér automatisk en kort Markdown‑rapport med nøgle­statistik (mean, std, outlier‑count), et før/efter‑plot for hver sensor og en tabel over bortfiltrerede outliers.
5. **05‑Parameter‑Tuning** – Lav et lille eksperiment hvor du varierer vindues­størrelsen $k$ i glatnings­algoritmen og plotter **MSE for hver af de tre sensorer** som funktion af $k$ for at finde et kompromis mellem støj­reduktion og signal‑latenstid.

## 📦 Aflevering

* Push følgende til repoet:

  ```
  dag08/
  ├── clean_data.csv
  ├── analysis.py / .ipynb
  ├── øvelser/
  │   ├── 01-Robust-Smoothing/
  │   ├── 02-Uniform-Resampling/
  │   ├── 03-Multisensor-Merge/
  │   ├── 04-Auto-Report/
  │   └── 05-Parameter-Tuning/
  └── README.md   ← (denne fil)
  ```
* Husk meningsfulde commits og Pull‑Request‑review.

## ✅ Checkliste

* [ ] Ingen NaN‑ eller outlier‑alarmer i `clean_data.csv`
* [ ] Plot for **alle tre sensorer** med titel, akse‑etiketter & enhed
* [ ] README opdateret med metoder & resultater
* [ ] Kode kører uden warnings på undervisnings‑PC
