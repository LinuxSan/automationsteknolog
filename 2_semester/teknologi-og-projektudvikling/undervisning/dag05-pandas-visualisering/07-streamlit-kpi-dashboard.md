# 📊 07 – KPI-dashboard og nøgletal med Streamlit

Et effektivt dashboard viser ikke kun grafer, men også de vigtigste nøgletal – de såkaldte KPI'er (Key Performance Indicators). Disse indikatorer giver et hurtigt overblik over systemets tilstand og hjælper med at identificere afvigelser, trends eller behov for handling. Eksempler på KPI’er i tekniske målesystemer kan være gennemsnitstemperatur, højeste luftfugtighed, antal alarmer over en tærskel, energiforbrug eller datahastighed.

Med Streamlit er det nemt at fremhæve vigtige nøgletal i toppen af dit dashboard ved hjælp af funktionen `st.metric()`. Denne guide viser, hvordan du opsætter et KPI-afsnit, der dynamisk beregner og viser centrale værdier baseret på data, som brugeren uploader. Du lærer også, hvordan du kan vise forskelle over tid, skabe betingede farver og kombinere nøgletal med grafer og brugerfiltre.

---

## 🎯 Læringsmål

* Forstå hvad KPI’er er, og hvorfor de bruges i dashboards
* Bruge `st.metric()` til at vise nøgletal med tekst og emojis
* Dynamisk beregne værdier fra realtids- eller måledata
* Kombinere KPI’er med grafisk visualisering
* Tilføje tendenser og advarsler med betinget formatering

---

## 💻 Eksempel – KPI-overskrift i dashboard

```python
import streamlit as st
import pandas as pd

# Indlæs CSV-data
data = pd.read_csv("maalinger.csv")

# Beregn nøgletal
middelværdi = data["værdi"].mean()
maksimum = data["værdi"].max()
minimum = data["værdi"].min()
antal_alarmer = (data["værdi"] > 800).sum()

# Vis nøgletal i dashboardet
st.metric("📉 Minimum", f"{minimum:.2f}")
st.metric("📏 Middelværdi", f"{middelværdi:.2f}")
st.metric("🚨 Maksimum", f"{maksimum:.2f}")
st.metric("⚠️ Målinger > 800", antal_alarmer)
```

> Brug af emojis og klare navne gør det nemmere at læse og fortolke nøgletallene – også for personer uden teknisk baggrund.

---

## 📊 Kombination med visualisering

KPI’erne fungerer bedst i kombination med visualisering, så man både får overblik og detaljer. Du kan placere grafer direkte under dine `st.metric()`-felter:

```python
st.line_chart(data["værdi"])
```

Hvis du viser filtrerede data, så sørg for at opdatere nøgletallene dynamisk, så de altid matcher det viste udsnit.

> Det skaber tillid, at KPI'er og grafer stemmer overens.

---

## 📈 Avanceret: Tilføj delta og betinget farve

Med `st.metric()` kan du også vise udviklingen i en værdi med en delta-indikator. Her ses eksempel med ændring i seneste måling:

```python
seneste = data["værdi"].iloc[-1]
forrige = data["værdi"].iloc[-2]
delta = seneste - forrige

st.metric("🔁 Seneste måling", f"{seneste:.1f}", delta=f"{delta:.1f}")
```

> Hvis du vil ændre farver eller give visuel feedback, kan du bruge `st.success()`, `st.warning()` eller `st.error()` i stedet for `st.metric()`.

---

## 🧪 Øvelser

1. Vis minimum, maksimum og gennemsnit med `st.metric()`
2. Brug `.diff()` til at vise ændring i seneste målinger (delta)
3. Tilføj en tæller for antal værdier over en bestemt tærskel
4. Brug `st.success()` til at vise "Alt OK" hvis maks < 700, ellers `st.warning()`
5. Udvid dashboardet med en ekstra række KPI'er for en anden kolonne (f.eks. temperatur og fugt)

---

## ✅ Tjekliste

* [ ] Jeg har brugt `st.metric()` til at vise mindst tre forskellige nøgletal
* [ ] Jeg har vist en delta-værdi, fx ændring fra sidste måling
* [ ] Jeg har vist eller skjult advarsler afhængig af data
* [ ] Jeg har koblet KPI'er sammen med graf eller tabeller
* [ ] Jeg har testet hvordan mine KPI’er ændrer sig ved filtrering af data

---

> Et godt dashboard viser både nøgleværdier og grafer – og understøtter hurtigt overblik og handling. KPI’er er dit værktøj til at fange opmærksomheden, før noget går galt.
