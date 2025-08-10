# 🧪 Opgaver – ESP32 (MicroPython klient) → Home Assistant (Modbus TCP-server)

I disse øvelser lærer du, hvordan du kan sende Modbus TCP-anmodninger fra en ESP32, der fungerer som klient, til en Modbus TCP-server konfigureret i Home Assistant. Da HA ikke har en indbygget Modbus-server, bruges en ekstern komponent (fx modbus\_server over MQTT eller TCP) eller et HA Add-on.

> 🔧 OBS: Home Assistant fungerer primært som Modbus-klient. For disse opgaver bruges enten en 3. parts TCP-server add-on, eller du opsætter en HA-kontrolleret proxy-server.

---

## 🟢 Opgave 1 – Opsæt Modbus TCP-server til HA

**Formål:** Brug fx `modbus-tcp-server` Add-on eller ekstern Node.js/Python server styret af HA, som eksponerer skrivevenlige registre

**Alternativer:**

* Kør `modbus-server` via docker eller add-on
* Eksponér register 0 som LED (0/1) og register 1 som temperatur

---

## 🟠 Opgave 2 – ESP32 skriver data til HA-server

**Formål:** ESP32 sender data (fx temperatur) til HA via Modbus TCP

**ESP32 MicroPython eksempel:**

```python
from umodbus.tcp import TCPClient

client = TCPClient(host='192.168.1.50', port=502)
temp = 245  # svarer til 24.5°C hvis skala 0.1
client.write_single_register(address=1, value=temp)
```

**HA Setup:**

* Registrér register 1 som sensor i `configuration.yaml`
* Skala og enhed tilpasses

```yaml
sensor:
  - platform: modbus
    registers:
      - name: "ESP32 Temperatur"
        hub: ha_server
        register: 1
        scale: 0.1
        unit_of_measurement: "°C"
```

---

## 🔵 Opgave 3 – ESP32 læser status fra HA

**Formål:** Læs fx et LED-styringsregister fra HA for at tænde/slukke lokalt output på ESP32

**ESP32:**

```python
led_status = client.read_holding_registers(address=0, count=1)[0]
if led_status == 1:
    # Tænd LED
    pass
```

**HA:**

* Tilføj Modbus register som `input_number` eller `switch`
* Skriv via HA UI for at sende værdi til ESP32

---

## 🧠 Refleksionsspørgsmål

* Hvordan kan Home Assistant stilles til rådighed som Modbus TCP-server i et produktionsmiljø?
* Hvad er alternativet til Modbus i denne integration (fx MQTT, REST)?
* Hvordan ville du sikre datavalidering og overvågning på HA-siden?
