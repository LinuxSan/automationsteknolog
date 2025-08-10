# 🧪 Opgaver – Home Assistant (Client) → ESP32 (MicroPython)

Disse øvelser fokuserer på, hvordan Home Assistant (HA) kan læse og skrive data til en Modbus TCP-server, der kører på en ESP32 med MicroPython. Du lærer at konfigurere Modbus-integration i HA og få adgang til ESP32’s registre via YAML-konfiguration.

---

## 🟢 Opgave 1 – Opsæt ESP32 som Modbus TCP-server

**Formål:** Kør en simpel Modbus TCP-server på ESP32 med MicroPython, som eksponerer mindst ét holding register.

**MicroPython:**

```python
from umodbus.tcp import TCPServer

registers = {
    0: 235,  # fx temperatur 23.5°C
    1: 0     # fx LED-styring
}

server = TCPServer(regs=registers)
server.start(ip='0.0.0.0', port=502)
```

**Test:** Sørg for at du kan tilgå ESP32’s IP på netværket fra en anden maskine (ping-test).

---

## 🟠 Opgave 2 – Konfigurér Home Assistant til at læse registrene

**Formål:** Brug `modbus`-platformen i Home Assistant til at hente data fra ESP32’s holding register.

**Trin:**

1. Gå til `configuration.yaml`
2. Tilføj følgende:

```yaml
modbus:
  - name: esp32
    type: tcp
    host: 192.168.1.50
    port: 502
    sensors:
      - name: "Temperatur ESP32"
        unit_of_measurement: "°C"
        address: 0
        input_type: holding
        scale: 0.1
        precision: 1
```

3. Genstart Home Assistant
4. Gå til Developer Tools → States og find `sensor.temperatur_esp32`

**Udvidelse:** Vis på dashboard med gauge eller line-chart

---

## 🔵 Opgave 3 – Skriv til ESP32 fra HA (fx LED-styring)

**Formål:** Brug HA til at sende en kommando til ESP32 via skrivning til et register

**ESP32:**

```python
from umodbus.tcp import TCPServer

def on_write(address, value):
    print(f"Skrevet: adresse {address}, værdi {value}")
    if address == 1 and value == 1:
        # Tænd LED
        pass

server = TCPServer(regs={0: 235, 1: 0}, on_write=on_write)
server.start(ip='0.0.0.0', port=502)
```

**Home Assistant:**
Tilføj i `switches:`

```yaml
switch:
  - platform: modbus
    coils:
      - name: "ESP32 LED"
        hub: esp32
        slave: 1
        address: 1
```

> OBS: Ved brug af holding register i stedet for coil, anvend `write_type: holding`

**Test:** Tænd/sluk via HA-interface og se ESP32's output i seriel monitor.

---

## 🧠 Refleksionsspørgsmål

* Hvilke udfordringer havde du med at finde ESP32 på netværket fra Home Assistant?
* Hvordan kan du sikre, at dataene vises med korrekt skala og enhed?
* Hvad ville næste skridt være for at gøre dette produktionsklar?
