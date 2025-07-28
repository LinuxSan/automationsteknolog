# 🌐 06 – Interaktivt dashboard med Streamlit

Streamlit er et moderne Python-værktøj, der gør det nemt at bygge interaktive visualiseringer direkte i browseren – uden behov for HTML, CSS eller JavaScript. Det er særligt velegnet til at præsentere måledata i realtid eller til at give brugeren mulighed for at filtrere og analysere datasæt visuelt. Det bruges ofte i data science, prototyper og undervisningsprojekter, hvor man hurtigt vil formidle indsigt i et datasæt på en letforståelig måde.

I dette modul bygger du et simpelt dashboard, hvor du kan loade en CSV-fil, vælge kolonner, filtrere data og vise grafer – alt sammen via en enkel brugerflade. Det fungerer som en introduktion til frontend-baseret datapræsentation i Python og åbner op for, hvordan du selv kan formidle analyser og sensordata uden at være afhængig af webudvikling.

---

## 🎯 Læringsmål

* Bruge `streamlit` til at oprette et interaktivt brugerinterface i browseren
* Indlæse og filtrere data dynamisk via widgets (f.eks. selectbox, slider, checkbox)
* Vise figurer med Matplotlib, Pandas og Streamlits egne visualiseringsfunktioner
* Forstå, hvordan Python-scriptet kører som en webapplikation
* Klargøre data og grafik til rapport, præsentation eller interaktiv analyse

---

## ⚙️ Installation og opstart

Først skal du sikre dig, at `streamlit` er installeret i dit Python-miljø. Installer med pip:

```bash
pip install streamlit
```

Du starter et dashboard ved at køre scriptet via terminalen:

```bash
streamlit run dashboard.py
```

Det åbner automatisk en browser med dashboardet. Hvis ikke, kan du selv åbne den viste URL i din browser (typisk [http://localhost:8501](http://localhost:8501)).

---

## 💻 Eksempel – dashboard.py

Herunder ses et simpelt eksempel på et dashboard, hvor brugeren kan uploade en CSV-fil, vælge en kolonne, indstille en grænseværdi og få vist et filtreret plot.

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🔎 Live datavisualisering")

uploaded_file = st.file_uploader("Vælg en CSV-fil", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    st.subheader("📊 Oversigt")
    st.write(data.describe())

    sensor_valg = st.selectbox("Vælg sensor-kolonne", data.columns)

    grænse = st.slider("Maks tilladt værdi", 0, 1023, 800)

    filtreret = data[data[sensor_valg] < grænse]

    fig, ax = plt.subplots()
    filtreret[sensor_valg].plot(ax=ax)
    ax.set_title(f"{sensor_valg} – filtreret visning")
    ax.set_ylabel("Værdi")
    st.pyplot(fig)
```

Dette script demonstrerer, hvordan et simpelt Python-program hurtigt kan blive til en dynamisk, brugerstyret datavisualisering.

---

## 🧪 Øvelser

1. Brug `st.line_chart()` eller `st.bar_chart()` som alternativ til Matplotlib-plot
2. Tilføj en `st.checkbox()` der kan vise eller skjule data over grænseværdien
3. Udvid med muligheden for at vælge to sensorkolonner og vise begge grafer samtidig
4. Brug `st.sidebar` til at flytte interaktive elementer ud til venstremenuen
5. Tilføj `st.download_button()` der gør det muligt at eksportere det filtrerede datasæt
6. Vis en tabel med `st.dataframe()` og lad brugeren selv filtrere via interaktive felter
7. Brug `st.markdown()` til at tilføje overskrifter, info og forklarende tekst i dit dashboard

---

## ✅ Tjekliste

* [ ] Jeg har oprettet og kørt et Streamlit-dashboard lokalt
* [ ] Jeg har uploadet et datasæt og filtreret det med widgets
* [ ] Jeg har visualiseret filtreret data via graf eller tabel
* [ ] Jeg har eksporteret eller givet mulighed for download
* [ ] Jeg har evalueret brugeroplevelsen og layoutet
* [ ] Jeg har forstået, hvordan dette kan anvendes i eksamensprojekt eller dokumentation

---

> Streamlit er en nem vej til at bygge interaktive værktøjer til analyse og visualisering – især når du vil præsentere data for andre uden at vise koden. Det giver en effektiv og professionel måde at dele indsigt og gøre tekniske analyser tilgængelige for ikke-programmører.
