# 💾 03 – Gem seriel## 📥 Trin 2: Lav Python-script med Pandasdata til CSV-fil

I denne guide lærer du trin for trin at gemme data fra ESP32 til en CSV-fil ved hjælp af Pandas. Vi modtager data og gemmer det struktureret.

---

## 🎯 Mål for modulet

* Bruge Pandas til at gemme data til CSV
* Strukturere data i en DataFrame
* Forstå grundlæggende Pandas og CSV

---

## 📤 Trin 1: Sørg for at ESP32 sender data

Brug det samme ESP32-script som før, der sender beskeder som "Hej fra ESP32!".

---

## � Trin 2: Lav Python-script til at gemme data

Opret en ny Python-fil:

```python
import serial
import pandas as pd
import time

ser = serial.Serial('COM3', 115200)  # Ret porten

data_liste = []  # Liste til data

for i in range(10):  # Modtag 10 linjer
    linje = ser.readline()
    tekst = linje.decode().strip()
    print("Modtaget:", tekst)
    # Tilføj til liste med timestamp
    data_liste.append({"tid": time.time(), "besked": tekst})

# Lav DataFrame og gem til CSV
df = pd.DataFrame(data_liste)
df.to_csv("data.csv", index=False)
print("Data gemt til data.csv")
```

> Dette modtager 10 beskeder og gemmer dem i CSV med Pandas.

---

## 📥 Trin 3: Kør scriptet

1. Start ESP32-scriptet.
2. Kør Python-scriptet.
3. Åbn "data.csv" i Excel eller VS Code.

---

## 🧠 Tip

* `pd.DataFrame()` laver en tabel af data.
* `to_csv()` gemmer til CSV-fil.
* `index=False` undgår ekstra kolonne.

---

## 🧪 Øvelser

1. Ændr antal linjer til 20.
2. Tilføj en kolonne: `data_liste.append({"tid": time.time(), "besked": tekst, "nummer": i})`.
3. Åbn CSV-filen og tjek indholdet.

---

## ✅ Tjekliste

* [ ] Jeg har installeret Pandas
* [ ] Jeg har kørt scriptet og set data i CSV
* [ ] Jeg har åbnet filen og forstået strukturen
* [ ] Jeg forstår hvordan Pandas gemmer data

---

## 🔧 DIY: Gem til JSON i stedet

**Ekstra opgave:** Gem data til JSON-fil i stedet for CSV.

**Trin:**
1. I stedet for `df.to_csv()`, brug `df.to_json("data.json")`.
2. Åbn "data.json" og se formatet.
3. Prøv at læse JSON tilbage: `pd.read_json("data.json")`.

> JSON er godt til struktureret data – prøv det!

---

> Du har nu lært at gemme data med Pandas – klar til analyse!
