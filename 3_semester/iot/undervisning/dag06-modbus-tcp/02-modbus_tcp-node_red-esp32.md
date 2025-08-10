# 🧪 Opgaver – Node-RED → ESP32 (MicroPython)

Disse øvelser fokuserer på at sende Modbus TCP-anmodninger fra Node-RED til en ESP32-enhed, der opfører sig som Modbus TCP-server. Du lærer at sende og fortolke kommandoer, arbejde med registre og teste funktionalitet i realtid.

---

## 🟢 Opgave 1 – Opsæt ESP32 som Modbus TCP-server

**Formål:** Kør en simpel Modbus TCP-server på ESP32 med MicroPython, som svarer på forespørgsler.

**Materialer:**

* ESP32 med MicroPython
* `uModbus` eller `mbserver` bibliotek

**Trin:**

1. Installer nødvendige biblioteker
2. Opsæt en server, der svarer på READ HOLDING REGISTER (funktionskode 03)
3. Implementér et register med temperaturværdi (fx værdi 235 = 23.5°C)

**Eksempel:**

```python
from umodbus.tcp import TCPServer

registers = {
    0: 235  # Holding register 40001 → 23.5°C
}

server = TCPServer(regs=registers)
server.start(ip='0.0.0.0', port=502)
```

---

## 🟠 Opgave 2 – Læs register fra Node-RED

**Formål:** Brug Node-RED til at sende en Modbus TCP-request og læse data fra ESP32-serveren.

**Materialer:**

* Node-RED med `node-red-contrib-modbus`
* Flow med `inject` → `modbus-read` → `debug`

**Trin:**

1. Tilføj `modbus-read` node
2. Sæt IP til ESP32, port 502, og læs 1 holding register fra adresse 0
3. Brug `inject` til at trigge læsningen
4. Brug `debug`-node til at vise resultat

**Udvidelse:**

* Vis værdien på et dashboard (gauge eller tekst)

---

## 🔵 Opgave 3 – Kontrol via skrivekommando

**Formål:** Skriv til et register på ESP32 fra Node-RED for at simulere aktuatorstyring (fx LED).

**Materialer:**

* `modbus-write` node i Node-RED
* ESP32-script med write-handler

**ESP32-udvidelse:**
Tilføj write-understøttelse:

```python
from umodbus.tcp import TCPServer

registers = {0: 0}  # fx LED-styring

def on_write(address, value):
    print(f"Skrevet: adresse {address}, værdi {value}")
    if address == 0 and value == 1:
        # Tænd LED her
        pass

server = TCPServer(regs=registers, on_write=on_write)
server.start(ip='0.0.0.0', port=502)
```

**Node-RED:**

1. Brug `inject`-node til at sende fx værdi 1
2. Brug `modbus-write` til at skrive til adresse 0
3. Se at ESP32 reagerer korrekt i konsol eller med LED

---

## 🧠 Refleksionsspørgsmål

* Hvilke forskelle er der i registrenes håndtering på ESP32 kontra industrienheder?
* Hvordan sikrer du korrekt byte order og adresseoffset?
* Hvordan valideres at Modbus-serveren kører korrekt på ESP32?
