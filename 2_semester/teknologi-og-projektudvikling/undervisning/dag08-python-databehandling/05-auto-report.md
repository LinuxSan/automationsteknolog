# 05 – Auto‑Report

*Del af **Dag 08 – Python‑databehandling***

---

## 🎯 Formål

Efter at have renset, glattet og samkørt dine målinger skal du nu producere en **automatisk rapport**, der på få sekunder giver undervisere, medstuderende og eksterne interessenter et klart billede af datasættets kvalitet og hovedresultater. Opgaven demonstrerer

1. hvordan man kombinerer **numeriske nøgletal** og **grafiske illustrationer** i en læsbar Markdown‑fil,
2. hvordan man strukturerer et projekt‑script, så rapporten kan regenereres med ét kommando‑kald, og
3. hvordan man integrerer **Git‑workflow** (commit + push) i sluttrinnet.

Dermed adresserer opgaven læringsmål **5 & 7**.

---

## 📂 Forudsætninger

| Krav                     | Beskrivelse                                                                                               |
| ------------------------ | --------------------------------------------------------------------------------------------------------- |
| Renset & glattet datasæt | `resampled_1s.csv` fra Opgave 03 **plus** glatte kolonner (fx `gas_mean`, `temp_median`, …) fra Opgave 02 |
| Mappestruktur            |                                                                                                           |

````text
└── dag08-python-databehandling/
    ├── 05-auto-report.md     ← denne fil
    ├── resampled_1s.csv
    ├── figures/              ← genereres automatisk
    ├── stats.md              ← genereres automatisk
    ├── report.md             ← genereres automatisk
    └── auto_report.py / .ipynb
```|
| Biblioteker | `pandas`, `matplotlib`, `tabulate` (valgfri), `pathlib`, `datetime` |

---

## 🔧 Trin for trin

> **Tip:** Gem alle konstanter (kanalliste, filstier, fig‑dpi) som **globale variabler** i toppen af scriptet, så ændringer foretages ét sted.

### 1. Import & forbered mapper
```python
import pandas as pd, matplotlib.pyplot as plt
from pathlib import Path
from datetime import date

# ------- parametre ---------
CHANNELS = ["gas", "temp", "hum", "lux"]
FIG_DIR  = Path("figures")
FIG_DIR.mkdir(exist_ok=True)

# ---------------------------

df = pd.read_csv("resampled_1s.csv", parse_dates=["timestamp"])
````

### 2. Generér plots (før vs. efter)

```python
for col in CHANNELS:
    plt.figure(figsize=(9, 3))
    plt.plot(df["timestamp"], df[col], alpha=0.35, label=f"{col} raw")

    # find alle glatte varianter af samme kanal
    smooth_cols = [c for c in df.columns if c.startswith(col) and c != col]
    for s in smooth_cols:
        plt.plot(df["timestamp"], df[s], label=s)

    plt.title(f"{col.upper()} – Rå vs. glattet")
    plt.xlabel("Tid"); plt.ylabel(col)
    plt.grid(True); plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / f"{col}.png", dpi=150)
    plt.close()
```

> **Bemærk:** Hvis du får for mange labels, kan du reducere til kun at vise *bedste* glatte kolonne (fx med laveste MSE).

### 3. Beregn nøgletal

```python
stats = df[CHANNELS + smooth_cols].describe().loc[["mean", "std", "min", "max"]]
stats.to_markdown("stats.md")
```

### 4. Skriv rapporten programmæssigt

```python
sections = []
sections.append(f"# Datalog‑rapport – {date.today().isoformat()}\n")
sections.append("## Nøgletal (mean / std / min / max)\n")
sections.append(stats.to_markdown())
sections.append("\n## Sensorplots\n")
for col in CHANNELS:
    sections.append(f"### {col.upper()}\n")
    sections.append(f"![{col}]({FIG_DIR / f'{col}.png'})\n")

# Konklusion
sections.append("---\n## Konklusion\n")
sections.append("Alle sensorer ligger inden for forventede grænser efter rensning og glatning. Gas‑sensoren viser dog stadig større variation end de øvrige kanaler, og en ny kalibrering overvejes.\n")

with open("report.md", "w", encoding="utf-8") as f:
    f.write("\n".join(sections))
```

### 5. Git‑workflow

```bash
git add figures/ stats.md report.md auto_report.py
git commit -m "Auto‑report generated (Dag 08)"
git push
```

> Hvis du arbejder i **GitHub Classroom**, sørg for at commit‑historikken viser én commit pr. hovedfunktionalitet (fx “Add plotting”, “Add stats”, “Generate report”).

---

## ✅ Peer‑review tjekliste

* [ ] Scriptet/Notebook kører **uden warnings** og skaber de tre artefakter (`figures/`, `stats.md`, `report.md`).
* [ ] `report.md` indeholder **både** tabel og figurer samt en kort konklusion.
* [ ] Fil‑ og mappenavne er relative; ingen hårdkodede absolutte paths.
* [ ] Koden følger **PEP 8**: funktions‑/variabelnavne er snake\_case, der er mellemrum omkring operatorer osv.
* [ ] Git‑historikken har mindst **tre commits**: data‑loading, plot‑generering, rapport.

---

### 📌 Ekstra idéer (frivilligt)

* Generér **PDF** af rapporten med `pandoc` (`pandoc report.md -o report.pdf`).
* Udvid plottene med **sekundær y‑akse** for lux, hvis værdierne er meget større end de øvrige kanaler.
* Tilføj interaktive HTML‑plots med `plotly` og link dem i rapporten.
* Lav en GitHub Action eller Make‑fil, der kører scriptet automatisk ved hvert push.

---

*Tip:* Hold øje med filstørrelsen på figurer; `dpi=150` er ofte et godt kompromis mellem kvalitet og repo‑størrelse. Brug `optipng` eller tilsvarende, hvis du vil komprimere PNG‑filer yderligere.
