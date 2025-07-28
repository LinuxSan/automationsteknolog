# ⚙️ 05 – Udvidelser og fejlhåndtering i visualisering

I takt med at du begynder at arbejde med rigtige målinger fra ESP32, PLC eller andre kilder, vil du uundgåeligt møde målefejl, afvigelser og uregelmæssigheder i datasættet. Det kan være værdier, der ligger langt uden for det forventede område, manglende datapunkter (`NaN`) eller svingende dataserier med mange udsving. Hvis ikke disse behandles korrekt, risikerer du at præsentere grafer og resultater, der er misvisende eller direkte forkerte.

Dette modul handler derfor om at gøre dine visualiseringer robuste og informative – også når data ikke er perfekte. Du lærer at identificere outliers, rense datasæt, udfylde huller og tilpasse grafer, så de tydeligt formidler relevante indsigter. Desuden introduceres avancerede teknikker som betinget farvestyling og brug af subplots, så dine figurer bliver mere fleksible og læsbare.

---

## 🎯 Læringsmål

* At kunne identificere og fjerne outliers (ekstremt høje eller lave måleværdier)
* At håndtere manglende data (`NaN`) på en måde der bevarer datakvalitet
* At filtrere målinger baseret på betingelser – fx vis kun værdier over en tærskel
* At arbejde med betinget visualisering, hvor farver og form tilpasses måleværdi
* At strukturere visualiseringer med subplots og flere akser, så figurer bliver mere informative

---

## 🧼 Filtrering og fjernelse af outliers

Outliers kan fx skyldes elektrisk støj, fejl i måleudstyr eller forkerte skaleringer. Det er vigtigt at dokumentere, hvilke filtre man anvender.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Eksempel: fjern målinger over 1000 og under 0
data = pd.read_csv("maalinger.csv")
data = data[(data["værdi"] > 0) & (data["værdi"] < 1000)]
```

---

## 🕳️ Håndtering af manglende data

Hvis sensoren midlertidigt stopper med at sende data, kan det give `NaN` i måleserien. Der er flere strategier:

```python
# 1. Erstat NaN med gennemsnitsværdi
gns = data["værdi"].mean()
data["værdi"] = data["værdi"].fillna(gns)

# 2. Interpolér mellem værdier for glat overgang
data["værdi"] = data["værdi"].interpolate(method="linear")
```

---

## 🎨 Farvekodning og betinget styling

Farvekodning er nyttigt, hvis du vil vise f.eks. alarmer, overskridelser eller forskellige tilstande.

```python
colors = ["red" if v > 800 else "blue" for v in data["værdi"]]
plt.scatter(data["tid"], data["værdi"], c=colors)
plt.title("Målinger med betinget farve")
plt.xlabel("Tid")
plt.ylabel("Værdi")
plt.grid()
plt.tight_layout()
plt.show()
```

> Overvej at tilføje en forklaring (legend) til farverne manuelt med `plt.scatter(..., label="Alarm")`

---

## 🧩 Flere plots i én figur (subplots)

Hvis du har to eller flere måleserier (fx temperatur og luftfugtighed), kan det være nyttigt at opdele figuren i mindre underplots.

```python
fig, axs = plt.subplots(2, 1, sharex=True, figsize=(10,6))
axs[0].plot(data["tid"], data["temperatur"], label="Temperatur")
axs[0].set_ylabel("°C")
axs[1].plot(data["tid"], data["fugt"], label="Fugtighed", color="green")
axs[1].set_ylabel("%")
axs[0].legend()
axs[1].legend()
plt.xlabel("Tid")
plt.tight_layout()
plt.show()
```

> Subplots giver bedre overblik og gør det nemmere at sammenligne udvikling i flere sensorer over tid.

---

## 🧪 Øvelser

1. Filtrér dit datasæt for outliers – definer egne grænser (fx > 1000 eller < 0)
2. Erstat `NaN`-værdier med gennemsnit eller prøv interpolation
3. Lav en scatter-plot med farver, afhængigt af om en tærskelværdi overskrides
4. Visualisér to måletyper (fx temperatur og fugt) i subplots med aksetitler
5. Lav en figur med og uden datarensning – sammenlign forskellen visuelt
6. (Ekstra) Vis både rå og filtrerede data i samme plot for at sammenligne

---

## ✅ Tjekliste

* [ ] Jeg har filtreret datasættet for outliers og dokumenteret grænserne
* [ ] Jeg har behandlet `NaN`-værdier med enten gennemsnit eller interpolation
* [ ] Jeg har brugt farvekodning til at fremhæve vigtige datapunkter
* [ ] Jeg har delt mine visualiseringer op i subplots og brugt akseetiketter
* [ ] Jeg har reflekteret over, hvordan datakvalitet og fejlkilder påvirker mit plot

---

> Gode grafer starter med rene data – men de bedste grafer formidler også usikkerhed og dokumenterer hvad der er fjernet, renset og fremhævet.
