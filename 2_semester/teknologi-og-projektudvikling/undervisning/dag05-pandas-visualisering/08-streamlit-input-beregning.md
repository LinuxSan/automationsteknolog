# 🧮 08 – Brugerinput og beregninger i Streamlit

Streamlit understøtter dynamisk input fra brugeren, hvilket betyder at du kan tilføje felter, hvor man indtaster værdier, vælger mellem muligheder eller sætter grænser. Disse input kan bruges til at foretage beregninger, konfigurere visualiseringer eller justere, hvordan data vises og behandles.

Dette modul introducerer brugen af `st.number_input()`, `st.text_input()`, `st.selectbox()` og andre interaktive kontroller. Du lærer, hvordan man binder input til beregninger og bruger det i grafer, datafiltrering eller analyser.

---

## 🎯 Læringsmål

* Indsamle tal og tekst fra brugeren via inputfelter
* Dynamisk tilpasse beregninger og visualiseringer baseret på input
* Forstå, hvordan interaktive widgets opdaterer appens tilstand

---

## 💻 Eksempel – Juster beregning med brugerinput

```python
import streamlit as st
import pandas as pd

# Indtast justeringsfaktor
offset = st.number_input("Indtast offset for sensormåling", value=0.0, step=0.1)

# Upload data
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    data["justeret"] = data["værdi"] + offset

    st.line_chart(data["justeret"])
```

---

## 🧠 Brug af flere inputtyper

Streamlit har mange input-widgets:

```python
# Tekstinput
brugernavn = st.text_input("Skriv dit navn")

# Vælg én mulighed
sensor = st.selectbox("Vælg sensor", ["Temperatur", "Fugt", "CO2"])

# Vælg flere muligheder
kanaler = st.multiselect("Vælg målekanaler", ["CH1", "CH2", "CH3"])

# Afkrydsningsfelt
vis_graf = st.checkbox("Vis graf")
```

---

## 📊 Dynamisk filtrering og kontrol

```python
# Filter på en tærskelværdi
grænse = st.slider("Maksimum tilladt værdi", 0, 1023, 800)
data_filtreret = data[data["værdi"] < grænse]
st.line_chart(data_filtreret["værdi"])
```

Du kan kombinere input-felter for at lave interaktive beregninger, som ændrer sig i realtid, alt efter hvad brugeren vælger.

---

## 🧪 Øvelser

1. Tilføj et offset- eller gain-input og justér datavisningen
2. Brug `text_input` til at navngive en graf eller datapakke
3. Brug `selectbox` til at vælge mellem flere kolonner i datasættet
4. Kombinér slider og checkbox til at skjule/filtrere data
5. Lav en beregning på baggrund af to bruger-input og vis resultatet

---

## ✅ Tjekliste

* [ ] Jeg har brugt mindst to forskellige input-widgets i Streamlit
* [ ] Jeg har koblet brugerinput til en beregning eller graf
* [ ] Jeg har testet hvordan ændringer i input påvirker resultatet
* [ ] Jeg har brugt inputfelter til at ændre layout eller indhold dynamisk

---

> Når brugeren kan påvirke visningen og beregningen, bliver dashboardet langt mere interaktivt og brugervenligt. Det gør dine visualiseringer relevante – hver gang.
