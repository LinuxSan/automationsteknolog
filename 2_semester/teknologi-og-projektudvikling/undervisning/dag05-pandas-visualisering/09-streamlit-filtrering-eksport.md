# 🗂️ 09 – Filtrering og eksport af data i Streamlit

Et centralt element i et interaktivt dashboard er muligheden for at fokusere på det, der er relevant. Når man arbejder med målinger, dataserier og store CSV-filer, har man sjældent brug for at se det hele på én gang. I stedet har man brug for fleksible filtre, der kan vise en specifik tidsperiode, et bestemt måleområde eller et relevant datasæt baseret på værdier, sensortyper eller fejlmarkeringer.

Streamlit tilbyder brugervenlige værktøjer til netop dette formål. Med widgets som `slider`, `checkbox`, `selectbox`, `multiselect` og `date_input` kan brugeren nemt vælge hvilke data, der skal vises, og hvilke der skal filtreres væk. Disse filtre reagerer i realtid og gør det muligt for brugeren at tilpasse visningen, så den passer til den aktuelle analyseopgave.

Når det ønskede udsnit er valgt, kan det vises i en tabel eller graf – og derefter eksporteres med et enkelt klik som CSV. Denne funktionalitet, baseret på `st.download_button()`, gør det muligt at integrere analyse, visualisering og datadeling i ét sammenhængende workflow.

Dette modul introducerer filtrering og eksport – to funktioner der tilsammen skaber en stærk kobling mellem interaktiv datavisualisering og teknisk dokumentation. Du lærer at bygge et filter-interface, som både er intuitivt og funktionelt, samt at give brugeren kontrol over eksporten.

---

## 🎯 Læringsmål

* Oprette interaktive filtre med widgets som `slider`, `checkbox`, `selectbox`, `multiselect`
* Dynamisk vise et subset af datasættet i en interaktiv tabel
* Gøre det muligt at eksportere det filtrerede udsnit med `st.download_button`
* Lade brugeren vælge filnavn eller automatisk generere det med dato og metadata
* Kombinere filtre og eksport med visualisering og KPI'er for at skabe et komplet værktøj

---

## 📥 Eksempel – Tids- og værdifiltrering

```python
import streamlit as st
import pandas as pd
from io import StringIO

# Indlæs data (kan også være fra file_uploader)
data = pd.read_csv("data.csv")

# Konverter evt. tid til datetime
data["tid"] = pd.to_datetime(data["tid"])

# Filterværdi for sensorværdi
min_val, max_val = st.slider("Værdier mellem", 0, 1023, (200, 800))
filtreret = data[(data["værdi"] >= min_val) & (data["værdi"] <= max_val)]

# Brug selectbox til sensor-type hvis relevant
if "sensor" in data.columns:
    valgt_sensor = st.selectbox("Vælg sensor", data["sensor"].unique())
    filtreret = filtreret[filtreret["sensor"] == valgt_sensor]

# Vis det filtrerede udsnit
st.subheader("📊 Filtreret datatabel")
st.dataframe(filtreret, use_container_width=True)
```

Du kan tilføje yderligere widgets til at filtrere på tid, kategorier, eller manglende værdier. Kombiner flere betingelser for komplekse analyser.

---

## 💾 Eksport med download-knap

Når du har et filtreret datasæt, kan du nemt give mulighed for download med valgfrit navn og format:

```python
csv = filtreret.to_csv(index=False)
st.download_button(
    label="📥 Download filtreret CSV",
    data=csv,
    file_name="filtreret_data.csv",
    mime="text/csv"
)
```

### 📌 Dynamisk filnavn baseret på dato eller brugerinput

```python
import datetime

dato = datetime.date.today().strftime("%Y-%m-%d")
filnavn_default = f"sensorlog_{dato}.csv"
navn_input = st.text_input("Angiv filnavn (uden .csv)", value="mine_data")
filnavn = navn_input + ".csv"
```

> Du kan også inkludere sensortype, dato, eller anvendt filter i filnavnet – det gør dokumentation nemmere senere.

---

## 🧪 Øvelser

1. Tilføj et `slider`-filter for at vælge værdier mellem 10 og 30 (f.eks. temperatur)
2. Brug `checkbox` til at vise/skjule bestemte kategorier (f.eks. sensortyper eller fejlflag)
3. Vis kun rækker med `NaN` i én kolonne ved hjælp af `.isna()` og `.dropna()`
4. Brug `selectbox` eller `multiselect` til at vælge kolonner, der skal med i eksportfilen
5. Giv brugeren mulighed for at vælge om CSV-filen skal indeholde tidspunkter eller ej
6. Tilføj `st.data_editor()` til at lade brugeren rette data manuelt før eksport
7. Tilføj download-format som `.xlsx` (ekstra – kræver `openpyxl`)

---

## ✅ Tjekliste

* [ ] Jeg har filtreret data dynamisk med mindst to widgets
* [ ] Jeg har brugt `st.dataframe()` eller `st.data_editor()` til at vise data
* [ ] Jeg har givet brugeren mulighed for at eksportere til CSV med valgfrit navn
* [ ] Jeg har testet forskellige kombinationer af filtre og kontrolleret eksporten
* [ ] Jeg har reflekteret over hvordan brugeren oplever workflow og output

---

> Et dashboard der både kan filtrere og eksportere data bliver langt mere brugbart og fleksibelt – både for analyse, dokumentation og rapportering. Det styrker samarbejdet mellem udvikler, bruger og kunde.
