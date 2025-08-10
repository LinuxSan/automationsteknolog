# 🛡 CoAP – Sikkerhedsopgaver med Home Assistant og ESP32 (MicroPython)

Disse opgaver viser, hvordan du kan arbejde med enkel sikkerhed i et CoAP-lignende setup, hvor ESP32-enheder kommunikerer med Home Assistant – enten direkte via Webhooks eller via en mellemserver. Fokus er på identifikation, validering og reaktionslogik.

---

## 🔐 Opgave 1 – Simuler PSK-adgang via Webhook i Home Assistant

**Formål:** Brug en webhook til at modtage data fra en ESP32 med en indlejret PSK (Pre-Shared Key).

### Trin

1. I Home Assistant, tilføj en webhook automation i `automations.yaml`:

```yaml
- alias: "ESP32 temperatur webhook"
  trigger:
    - platform: webhook
      webhook_id: coap_psk
  condition:
    - condition: template
      value_template: >
        {{ trigger.json.authorization == 'mysecretkey' }}
  action:
    - service: input_number.set_value
      data:
        entity_id: input_number.esp32_temp
        value: "{{ trigger.json.value | float }}"
```

2. Opret en `input_number` i `configuration.yaml`:

```yaml
input_number:
  esp32_temp:
    name: ESP32 Temperatur
    min: -20
    max: 100
    step: 0.1
```

3. På ESP32 (MicroPython):

```python
import urequests
headers = {"Content-Type": "application/json"}
data = {"authorization": "mysecretkey", "value": 22.3}
urequests.post("http://<ha-ip>:8123/api/webhook/coap_psk", json=data, headers=headers)
```

---

## 📛 Opgave 2 – Bloker ukendte enheder

**Formål:** Udvid sikkerhedslogik, så kun kendte enheder kan sende data.

### Trin

1. I automation, tilføj en ekstra betingelse:

```yaml
    - condition: template
      value_template: >
        {{ trigger.json.device_id in ['esp32-01', 'esp32-02'] }}
```

2. Tilføj `device_id` til payload fra ESP32:

```python
data = {"authorization": "mysecretkey", "device_id": "esp32-01", "value": 22.3}
```

3. Bekræft at ukendte enheder bliver ignoreret

---

## 🔎 Opgave 3 – Overvåg sikkerhedshændelser i Home Assistant

**Formål:** Log adgangsforsøg og opret notifikationer ved fejl.

### Trin

1. Udvid automationens `action` med en fejllog:

```yaml
    - service: persistent_notification.create
      data:
        message: "Afvist adgangsforsøg fra {{ trigger.json.device_id or 'ukendt enhed' }}"
        title: "CoAP Sikkerhed"
```

2. Alternativt: log til MQTT-topic, InfluxDB eller vis i Lovelace

---

## ⚙️ Opgave 4 – Begræns opdateringsfrekvens fra samme enhed

**Formål:** Undgå at en enhed oversvømmer systemet med anmodninger

### Trin

1. Brug `input_datetime.last_update_esp32` til at gemme sidste adgangstidspunkt:

```yaml
input_datetime:
  last_update_esp32:
    name: Sidst modtaget fra ESP32
    has_date: true
    has_time: true
```

2. I automation, tilføj betingelse:

```yaml
    - condition: template
      value_template: >
        {{ (as_timestamp(now()) - as_timestamp(states.input_datetime.last_update_esp32.state)) > 30 }}
```

3. Tilføj handling for at opdatere `input_datetime`

```yaml
    - service: input_datetime.set_datetime
      data:
        entity_id: input_datetime.last_update_esp32
        datetime: "{{ now().isoformat() }}"
```

---

✅ Disse opgaver giver dig en let og robust måde at integrere sikkerhedslogik i Home Assistant for data sendt fra ESP32-enheder via webhooks – uden behov for fuld CoAP-understøttelse eller DTLS.
