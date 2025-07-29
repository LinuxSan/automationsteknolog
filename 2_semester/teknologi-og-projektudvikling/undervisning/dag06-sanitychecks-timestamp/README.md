
# 📘 README – Dag 06: Sanity Checks og Tidsstempling

Velkommen til dag 06 i forløbet. I dag arbejder vi med kvaliteten af vores data – før vi analyserer eller visualiserer dem.

---

## 🧭 Formål med dagen

* Forstå hvad sanity checks er, og hvorfor de er vigtige i dataprojekter
* Lære at validere målinger, både fra ESP32 og simuleret input
* Tidsstemple målinger korrekt og strukturere dem i Pandas
* Forberede data til videre analyse og dokumentation

---

## 📚 Dagens guider og øvelser

Navigér til mappen:

```
undervisning/dag06_sanitychecks-timestamp/
```

Her finder du:

| Filnavn                           | Indhold                                  |
| --------------------------------- | ---------------------------------------- |
| `06-sanitychecks-timestamp.md`    | Guide til sanity checks og tidsstempling |
| `sanitycheck.py`                  | Python-skabelon til dagens opgaver       |
| `simulerede-data.csv` *(valgfri)* | Eksempeldata til test og udvikling       |

---

## 🧪 Dagens opgaver

**Opgave 1 – Simulerede målinger med timestamp**
Skriv et Python-script der genererer 50 tilfældige målinger og tilføjer et tidsstempel til hver række. Brug `pd.Timestamp.now()` og gem resultatet i en DataFrame.

**Opgave 2 – Sanity check-funktion**
Lav en funktion der validerer om en måling er gyldig (fx skal den være mellem 0 og 1023). Anvend funktionen på alle 50 målinger, og opret en kolonne `valid` med `True` eller `False`.

**Opgave 3 – Udvidet validering**
Udvid sanity check-funktionen med ekstra logik: fx afvis målinger som ændrer sig mere end 200 siden sidste måling. Opdater `valid`-kolonnen.

**Opgave 4 – Visualisering af datakvalitet**
Vis gyldige og ugyldige målinger i en graf – brug fx farver til at adskille dem. Alternativt vis dem i en tabel med filtre.

**Opgave 5 – Dubletdetektion og tidsanalyse**
Tilføj logik der markerer gentagne værdier og udregner tid mellem hver måling. Brug dette til at vurdere om sampling foregår jævnt.

---

## 💼 Relevans

I praksis er datavalidering afgørende i projekter med IIoT, SCADA og sensorintegration. Dårlige målinger kan føre til fejlbeslutninger og fejlanalyse. Ved at tjekke dine data og tidsstemple korrekt skaber du robusthed – og kvalitet i det videre projekt.

> Sanity checks er den tekniske samvittighed i ethvert dataprojekt.
