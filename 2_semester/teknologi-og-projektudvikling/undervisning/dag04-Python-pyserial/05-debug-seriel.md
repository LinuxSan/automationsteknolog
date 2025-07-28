# 🧯 05 – Fejlfinding ved seriel kommunikation

Når du arbejder med ESP32 og seriel data i Python, kan der opstå en række klassiske problemer. Denne guide hjælper dig med at finde og løse dem hurtigt.

---

## 🎯 Mål for modulet

* Forstå typiske fejl ved COM-porte og dataformat
* Kunne afhjælpe ukendt output og forbindelsesfejl
* Blive sikker i at håndtere realtidsforbindelser robust

---

## 🛠️ Typiske problemer og løsninger

### 🚫 COM-port ikke fundet

* Er ESP32 tilsluttet korrekt? Prøv andet kabel/port
* Brug `Thonny` til at teste forbindelsen først
* På Windows: Tjek Enhedshåndtering → Porte
* På Linux/macOS: `ls /dev/ttyUSB*` eller `ls /dev/tty.*`

### ⚠️ Timeout eller ingen data

* Er ESP32-scriptet startet og kører det?
* Print ESP32-data i Thonny først, og se om noget bliver sendt
* Tjek at baudrate stemmer overens (`115200`)

### ❌ Uforståelig output

* Brug `.decode(errors='ignore')` hvis enkelte tegn driller
* Brug `.strip()` til at fjerne `\n` og `\r`
* Kontrollér om `print()` på ESP32 sender i CSV-format

### 🔁 Data skrives ikke til CSV

* Brug `with open(...)` for korrekt håndtering
* Tjek `writer.writerow(...)` og brug `try/except`
* Luk ikke filen manuelt under kørsel

---

## 🧪 Fejlfindingstips

* Print hele rå linje fra ESP32: `print(repr(linje))`
* Brug `time.sleep(0.1)` i loop for at undgå overload
* Lav tests med dummy-data hvis du vil udelukke hardware

```python
linje = b"1725039999,832\r\n"
print(linje.decode().strip())
```

---

## ✅ Tjekliste

* [ ] Jeg har testet ESP32-output i Thonny inden Python
* [ ] Jeg har brugt `strip()`, `split()` og `decode()` korrekt
* [ ] Jeg har løst problemer med COM-port eller encoding
* [ ] Jeg har lært at fejlfinde og afgrænse problemet

---

> Fejl i datakommunikation er uundgåelige – men de kan næsten altid forklares.
