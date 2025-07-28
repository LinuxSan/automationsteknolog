# 🐍 README – Dag 04: Python + Seriel datamodtagelse

På denne undervisningsdag lærer du at forbinde din computer med ESP32 via seriel kommunikation. Du bruger `pyserial` i Python til at læse data, gemme det i CSV-filer og gøre det klar til videre analyse i Pandas.

Dette modul bygger bro mellem dine målinger på ESP32 og den databehandling du allerede har lært i Python.

---

## 🎯 Formål med dagen

* Installere og teste `pyserial`
* Læse seriel data fra ESP32 i Python
* Gemme data struktureret i CSV-format
* Forberede realtidsmålinger til analyse og visualisering

---

## 📚 Modulstruktur og filer

```
dag04-python-serial/
├── 01-installation-pyserial.md       # Installer og test pyserial
├── 02-modtag-seriel-data.md         # Læsning og split af seriel data
├── 03-gem-data-til-csv.md           # Skriv data direkte til fil
├── 04-live-visualisering.md         # Real-time visning med matplotlib (valgfri)
├── 05-debug-seriel.md               # Fejlfinding med porte og dataformat
```

---

## 💼 Relevans for praksis

I mange industrielle og embedded systemer sendes målinger over UART/seriel forbindelse. Det er vigtigt at kunne:

* Fange og analysere data i realtid
* Skrive data til filer der kan gemmes og dokumenteres
* Sammenkoble hardware og software på tværs af systemer

---

## ✅ Output for dagen

* Python-script der kan læse fra ESP32
* CSV-fil med sensordata og tidsstempel
* Grundlag for at analysere eller visualisere egne målinger

---

> Nu kobler du din ESP32 til Python – og får endelig dine egne målinger gjort brugbare.
