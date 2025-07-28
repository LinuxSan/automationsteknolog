# 🧾 02 – Modtag seriel data i Python

I denne guide lærer du at modtage struktureret data fra ESP32 i realtid via seriel kommunikation. Du bruger `pyserial` til at læse data og konverterer hver linje til målinger, som du senere kan gemme eller analysere.

---

## 🎯 Mål for modulet

* Læse ESP32-output med `pyserial`
* Splitte CSV-lignende data i Python
* Konvertere tekstlinjer til tal og timestamp

---

## 📤 Forudsætning: ESP32 skal sende struktureret data

Fra MicroPython på ESP32 skal du have noget der ligner dette:

```
1725024971,812
1725024972,834
```

Hver linje består af: `timestamp,værdi`

---

## 📥 Læs og parse data i Python

```python
import serial

ser = serial.Serial('COM3', 115200)  # Ret porten til din ESP32

while True:
    linje = ser.readline()
    tekst = linje.decode().strip()
    print("Rå linje:", tekst)

    try:
        ts_str, val_str = tekst.split(",")
        ts = int(ts_str)
        val = int(val_str)
        print(f"Tid: {ts}, Værdi: {val}")
    except:
        print("Ugyldig linje")
```

---

## 🧠 Tip

* `strip()` fjerner linjeskift
* `split(",")` opdeler CSV-format
* `try/except` sikrer at fejl ikke stopper loopet

---

## 🧪 Øvelser

1. Kør ESP32 med script der sender CSV-data
2. Kør Python-scriptet og modtag linjerne
3. Konverter `timestamp` og `værdi` til variabler
4. Udvid print med: `print(val > 1000)` hvis du vil lave betingelser

---

## ✅ Tjekliste

* [ ] Jeg har læst seriel data i Python
* [ ] Jeg har splittet hver linje og udtrukket tal
* [ ] Jeg har håndteret ukendte linjer med `try/except`
* [ ] Jeg forstår hvordan ESP32 og Python taler sammen via COM-port

---

> Du kan nu læse og forstå dine egne ESP32-målinger i Python!
