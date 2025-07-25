# 🧪 CoAP-MQTT Gateway – Opgaver med Home Assistant

Disse opgaver udvider gateway-modulet og viser, hvordan du integrerer CoAP-enheder i Home Assistant via MQTT. Du vil arbejde med visualisering, styring, statusovervågning og automatisering.

---

## 🧩 Opgave 1 – Vis CoAP-sensor i Home Assistant

**Formål:** Vis en temperaturværdi fra en CoAP-enhed i Home Assistant via MQTT

### Trin

1. Sørg for at gateway publicerer til:

```
coap/sensors/temperature
```

2. Tilføj i `configuration.yaml`:

```yaml
mqtt:
  sensor:
    - name: "Temperatur fra CoAP"
      state_topic: "coap/sensors/temperature"
      unit_of_measurement: "°C"
      device_class: temperature
```

3. Genstart Home Assistant og tilføj sensoren til dashboard

---

## 🔁 Opgave 2 – Styr CoAP-aktuator fra Home Assistant

**Formål:** Send kommandoer fra Home Assistant til en CoAP-enhed via MQTT

### Trin

1. Sørg for at din gateway lytter på:

```
commands/device/led
```

2. Tilføj i `configuration.yaml`:

```yaml
mqtt:
  switch:
    - name: "LED via CoAP"
      command_topic: "commands/device/led"
      payload_on: "1"
      payload_off: "0"
      retain: true
```

3. Brug Home Assistant UI til at tænde/slukke LED’en

---

## 🔍 Opgave 3 – Automatisk visning af ressourcer

**Formål:** Brug CoAP-gatewayens discovery-topic til at vise dynamiske ressourcer

### Trin

1. Sørg for at gateway publicerer til:

```
coap/discovery
```

2. Eksempel-payload:

```json
{
  "resources": [
    {"uri": "/temp", "type": "temperature", "observable": true},
    {"uri": "/led", "type": "switch"}
  ]
}
```

3. Brug en `template sensor` i Home Assistant til dynamisk at vise antal eller navne:

```yaml
sensor:
  - platform: mqtt
    name: "Antal CoAP-ressourcer"
    state_topic: "coap/discovery"
    value_template: "{{ value_json.resources | length }}"
```

---

## 📊 Opgave 4 – Overvåg gatewayens tilstand

**Formål:** Vis status fra gateway i Home Assistant UI

### Trin

1. Gateway publicerer JSON til:

```
gateway/status
```

Eksempel:

```json
{
  "connected": true,
  "mqtt_alive": true,
  "coap_alive": true,
  "uptime": 24812
}
```

2. Tilføj sensor i Home Assistant:

```yaml
sensor:
  - platform: mqtt
    name: "Gateway online"
    state_topic: "gateway/status"
    value_template: "{{ value_json.connected }}"
```

3. Vis den på dashboard som indikator

---

## ⚙️ Opgave 5 – Automatisering med CoAP-data

**Formål:** Brug temperaturdata fra CoAP til at aktivere ventilator

### Trin

1. Brug sensoren fra Opgave 1
2. Tilføj i `automations.yaml`:

```yaml
- alias: "Tænd ventilator ved >25°C"
  trigger:
    - platform: numeric_state
      entity_id: sensor.temperatur_fra_coap
      above: 25
  action:
    - service: mqtt.publish
      data:
        topic: "commands/device/fan"
        payload: "1"
```

3. Tilføj en automation der slukker ved < 23°C

---

✅ Disse opgaver viser, hvordan Home Assistant kan bruges som frontend og kontrolcenter for dine CoAP-enheder – via MQTT og gatewayen som bindeled.
