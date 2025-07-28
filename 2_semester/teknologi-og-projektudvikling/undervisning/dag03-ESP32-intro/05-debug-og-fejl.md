# 🐞 05 – Fejlfinding og debugging med ESP32

Denne guide hjælper dig med at identificere og løse almindelige problemer, du kan støde på når du arbejder med ESP32 og sensorer i MicroPython.

---

## 🎯 Mål for modulet

* Forstå almindelige fejltyper ved brug af ESP32
* Lære teknikker til fejlfinding i Thonny
* Være i stand til at tjekke hardware, kode og forbindelser

---

## 🛠️ Typiske fejl og løsninger

### 🚫 ESP32 vises ikke i Thonny

* Tjek USB-kabel – nogle kabler er kun til opladning
* Prøv en anden USB-port
* Installer driver (CH340 / CP210x afhængigt af board)
* Hold `BOOT` nede under tilslutning og slip efter 3 sek.

### ⚠️ "Device is busy" eller upload fejler

* Du kører måske et script med en `while True:`-løkke
* Stop programmet med **Ctrl+C** i shell eller knappen **Stop** i Thonny

### ❌ `ImportError` eller "module not found"

* Har du glemt at installere MicroPython på ESP32?
* Forkert board valgt i interpreter?
* Du bruger måske Arduino-syntaks i stedet for MicroPython

### 📉 Sensor returnerer 0 eller `None`

* Check forbindelser (GND, VCC, signal korrekt?)
* Brug `atten(ADC.ATTN_11DB)` på analog pins
* DHT22 kræver `sensor.measure()` før `.temperature()` og `.humidity()`
* Giv DHT22 et par sekunder til opstart efter tilslutning

---

## 🔍 Debug-teknikker

* Brug `print()` overalt til at se værdier og hvor din kode kører
* Del koden op i små sektioner
* Test én sensor ad gangen
* Brug `try:` / `except:` hvis du vil fange og ignorere fejl

```python
try:
    sensor.measure()
    print(sensor.temperature())
except OSError:
    print("Fejl i DHT-måling")
```

---

## ✅ Tjekliste

* [ ] Jeg kan identificere fejl i forbindelser og kode
* [ ] Jeg har prøvet at debugge med `print()` og `Ctrl+C`
* [ ] Jeg ved hvordan man nulstiller ESP32 og genstarter Thonny
* [ ] Jeg har lært at bruge `try/except` til robust måling

---

> Fejl er en naturlig del af hardwarearbejde – det vigtigste er, at du lærer at finde og løse dem.
