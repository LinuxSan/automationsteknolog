# 🏠 Home Assistant: CoAP Discovery – Opgaver

Disse opgaver fokuserer på, hvordan man kan integrere CoAP-enheder i Home Assistant – direkte eller indirekte – via fx `command_line` sensorer, MQTT eller en bro som Node-RED.

---

## 🧪 Opgave 1 – Brug af command\_line sensor med `coap-client`

**Formål:** Hent en temperaturværdi fra en CoAP-enhed og vis den i Home Assistant

### Forudsætninger

* Home Assistant kører på en enhed med adgang til `coap-client` (fx Linux eller Docker med bash)

### Trin

1. Installer `libcoap` hvis ikke allerede tilgængelig:

```bash
sudo apt install libcoap2-bin
```

2. Tilføj følgende til `configuration.yaml`:

```yaml
sensor:
  - platform: command_line
    name: "Temp via CoAP"
    command: 'coap-client -m get coap://192.168.1.50/temp | tail -n 1'
    scan_interval: 60
```

3. Genstart Home Assistant

---

## 🧪 Opgave 2 – Parse discovery-data fra enheder

**Formål:** Brug en REST-sensor til at vise enhedsressourcer fra `/.well-known/core`

> OBS: Home Assistant understøtter ikke CoAP direkte – du skal bruge en bro (fx Node-RED eller proxy-script)

### Trin

1. Lav et Python-script der spørger en CoAP-enhed:

```python
import os
os.system("coap-client -m get coap://192.168.1.50/.well-known/core > /config/core.txt")
```

2. Kør scriptet periodisk (fx via automation eller cron)
3. Brug en `file`-sensor i Home Assistant til at læse `/config/core.txt`

---

## 🧪 Opgave 3 – Indirekte integration via Node-RED bro

**Formål:** Brug Node-RED til at hente CoAP data og publicere dem som MQTT topics, som Home Assistant kan opdage automatisk

### Trin

1. I Node-RED:

   * Tilføj en CoAP input-node (`/.well-known/core` eller fx `/temp`)
   * Parse svaret og send det videre som JSON til en MQTT out-node

2. I Home Assistant:

```yaml
mqtt:
  sensor:
    - name: "Temp via MQTT"
      state_topic: "iot/temp"
      unit_of_measurement: "°C"
```

3. Sørg for at Home Assistant er forbundet til samme MQTT-broker

---

## 💡 Bonus – Brug ESPHome (hvis ESP32 er anvendt)

**Formål:** Eksponer CoAP-lignende sensorer uden at bruge CoAP direkte

### Trin

1. Installer ESPHome og lav følgende konfiguration:

```yaml
temperature_sensor:
  - platform: dallas
    address: 0x12345678
    name: "ESP Temperatur"
```

2. ESPHome opretter automatisk sensoren i Home Assistant

---

✅ Disse opgaver viser både direkte og indirekte metoder til at integrere CoAP-enheder med Home Assistant – afhængigt af platform og netværksmuligheder.
