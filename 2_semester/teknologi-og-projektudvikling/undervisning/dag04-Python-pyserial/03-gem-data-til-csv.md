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

# Importér seriel (pyserial) til COM-port, time til tidsstempler og pandas til CSV-skrivning
import serial, time, pandas as pd
# Path (fra pathlib) bruges som fil-sti-objekt; p.exists() kan tjekke om filen findes
from pathlib import Path

# Åbn seriel port 'COM3' med 115200 baud; timeout=1s gør readline ikke-blokerende (returnerer b'' ved stilhed)
ser = serial.Serial('COM3', 115200, timeout=1)

# Opret et sti-objekt til CSV-filen. 'p' er altså blot "håndtaget" til filen data.csv
p = Path('data.csv')

# Uendelig løkke — stop programmet med Ctrl+C i terminalen
while True:
    # Læs én linje bytes fra seriel, dekod som UTF-8. errors='replace' erstatter ugyldige bytes med � i stedet for at crashe.
    line = ser.readline().decode('utf-8', errors='replace').strip()

    # Kun hvis der kom indhold (tom streng betyder typisk timeout uden data)
    if line:
        try:
            # Fortolk linjen som temperatur (tal). float() håndterer både "23", "23.5" m.m.
            temperature = float(line)
        except ValueError:
            # Hvis linjen ikke er et tal (fx headers/diagnose), spring den over
            continue

        # Opret en mini-DataFrame med én række (to kolonner: 'tid' og 'temperature') ...
        # ... og skriv den til CSV:
        #   - p: selve stien (Path-objektet til 'data.csv')
        #   - mode='a': "append" — opret filen hvis den ikke findes, ellers tilføj i bunden (overskriver ikke)
        #   - index=False: skriv ikke DataFrame-indekset som ekstra kolonne i CSV
        #   - header=not p.exists(): skriv kolonnenavne KUN første gang (når filen endnu ikke findes)
        pd.DataFrame([{'tid': time.time(), 'temperature': temperature}]).to_csv(
            p,
            mode='a',
            index=False,
            header=not p.exists()
        )

        # Vis temperaturen i konsollen, så man kan se hvad der blev logget
        print(f"Temp: {temperature}")


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
