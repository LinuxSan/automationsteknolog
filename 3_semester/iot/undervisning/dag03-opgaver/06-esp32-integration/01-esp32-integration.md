# 🧪 Opgaver – Home Assistant: ESP32 Integration

Disse opgaver guider dig i at forbinde en ESP32-enhed med Home Assistant via MQTT. Du lærer at sende målinger, modtage kommandoer og oprette enheder automatisk med discovery.

---

## 🟢 Opgave 1 – Forbind ESP32 til WiFi og MQTT

1. Sørg for at din ESP32 har kode til WiFi og MQTT (fx med PubSubClient)
2. Forbind til Mosquitto broker og tjek connection i `Serial Monitor`
3. Tilføj `last will` og `keep alive`-interval

✅ *ESP32 skal forbinde og holde forbindelsen til MQTT*

---

## 🔵 Opgave 2 – Send temperatur med MQTT Discovery

1. Fra ESP32, publicér denne discovery-payload:

```json
Topic: homeassistant/sensor/stue_temp/config
Payload:
{
  "name": "ESP Stue Temp",
  "state_topic": "esp32/stue/temperature",
  "unit_of_measurement": "°C",
  "device_class": "temperature",
  "unique_id": "esp32_temp_01"
}
```

2. Send testværdi fx `22.4` til `esp32/stue/temperature`

✅ *Sensor vises automatisk i Home Assistant med korrekt ikon og navn*

---

## 🟡 Opgave 3 – Aktuatorstyring fra HA til ESP32

1. ESP32 subscribes til topic `esp32/relay1/set`
2. I HA: Send følgende discovery-payload:

```json
Topic: homeassistant/switch/esp32_relay/config
Payload:
{
  "name": "ESP32 Relæ",
  "command_topic": "esp32/relay1/set",
  "state_topic": "esp32/relay1",
  "payload_on": "ON",
  "payload_off": "OFF",
  "unique_id": "esp32_relay_01"
}
```

3. ESP32 skal reagere med `digitalWrite()` på kommandoen
4. ESP32 publicerer aktuel status til `esp32/relay1`

✅ *Styr relæet fra Home Assistant og se status opdateres*

---

## 🔁 Opgave 4 – Heartbeat og availability

1. ESP32 sender `online` hvert 30. sekund til `esp32/status`
2. I discovery-payload tilføj:

```json
"availability_topic": "esp32/status",
"payload_available": "online",
"payload_not_available": "offline"
```

3. Simulér frakobling og observer HA-skift til offline

✅ *Home Assistant viser korrekt tilgængelighedsstatus*

---

## 🧠 Refleksion

* Hvordan sikrer du, at data fra ESP32 ikke overskrives forkert?
* Hvad sker der, hvis ESP32 genstarter uden at sende config igen?
* Hvordan kunne du udvide dette med flere sensorer eller styring?

---

📌 Ved hjælp af MQTT Discovery og stabil ESP32-kode kan du nemt oprette og vedligeholde dynamiske IoT-integrationer i Home Assistant.
