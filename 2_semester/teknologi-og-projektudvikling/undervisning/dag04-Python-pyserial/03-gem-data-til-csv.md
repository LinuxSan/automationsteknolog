# 💾 03 – Gem seriel data til CSV-fil

I denne guide lærer du at gemme dine ESP32-målinger direkte til en CSV-fil, mens du modtager dem. På den måde kan du efterfølgende åbne filen i Pandas og analysere data.

---

## 🎯 Mål for modulet

* Skrive seriel data direkte til `.csv`-fil
* Strukturere data med kolonnenavne
* Sikre korrekt håndtering af tekstfiler i Python

---

## 📁 Gem data undervejs i loopet

```python
import serial
import csv

ser = serial.Serial('COM3', 115200)

with open("data.csv", "w", newline="") as fil:
    writer = csv.writer(fil)
    writer.writerow(["timestamp", "værdi"])  # header

    while True:
        linje = ser.readline()
        tekst = linje.decode().strip()

        try:
            ts_str, val_str = tekst.split(",")
            ts = int(ts_str)
            val = int(val_str)
            print(f"Gemmer: {ts}, {val}")
            writer.writerow([ts, val])
        except:
            print("Ugyldig linje")
```

> Brug `Ctrl+C` i terminalen for at stoppe scriptet.

---

## 🧠 Tip

* Brug `newline=""` i `open()` så linjerne ikke adskilles med ekstra mellemrum
* CSV-filen oprettes i samme mappe som scriptet – brug `os.getcwd()` hvis du er i tvivl
* Brug `with open(...)` så filen lukkes korrekt

---

## 🧪 Øvelser

1. Udvid dit tidligere script til at skrive til `data.csv`
2. Stop scriptet efter fx 20 linjer (brug en tæller eller `break`)
3. Åbn CSV-filen i Excel og i Pandas for at kontrollere indhold

```python
import pandas as pd
data = pd.read_csv("data.csv")
print(data.head())
```

---

## ✅ Tjekliste

* [ ] Jeg har oprettet og skrevet til en `.csv`-fil
* [ ] Jeg har tilføjet kolonnenavne (header)
* [ ] Jeg har testet output i Excel og Pandas
* [ ] Jeg kan stoppe og genbruge datafilen til analyse

---

> Du logger nu rigtige sensormålinger – klar til at analysere!
