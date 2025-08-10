# 🌡️ Dag 4 – Home Assistant 05: Sensorer

I denne lektion fokuserer vi på sensorer i Home Assistant. Sensorer giver dig adgang til information om miljø, bevægelse, tilstande og målinger – enten lokalt (ESP32) eller via netværk (MQTT, REST).

---

## 🎯 Læringsmål

* Forstå sensorens rolle i Home Assistant
* Modtage og visualisere data fra enheder
* Forstå MQTT og REST-sensorer

---

## 🔎 Hvad er en sensor i HA?

En sensor er en read-only entitet, som viser data fra fx:

* Temperatur, fugt, luftkvalitet
* Tilstedeværelse, bevægelse
* WiFi-styrke, systemdata
* Dør åbent/lukket

Typisk vises som `sensor.*` eller `binary_sensor.*`

---

## 🧪 Eksempel: MQTT Discovery Sensor

```json
Topic: homeassistant/sensor/stue_temp/config
Payload:
{
  "name": "Stue Temperatur",
  "state_topic": "smarthouse/stue/temperature",
  "unit_of_measurement": "°C",
  "device_class": "temperature",
  "unique_id": "stue_temp_sensor"
}
```

Når Home Assistant modtager denne besked, vises sensoren automatisk i UI.

---

## 🔁 Dataflow for sensor

1. Enhed måler og sender data via MQTT eller HTTP
2. HA lytter og opdaterer entitetens værdi
3. UI viser data i realtime

---

## 📡 Sensor input fra ESP32

ESP32 sender med fx:

```http
POST /api/temperature
{
  "sensor": "living_room",
  "value": 22.5
}
```

HA opdaterer REST-sensor eller webhook-sensor

---

## 📊 Visualisering

* Entities card → én eller flere sensorer
* Gauge card → måleværdier
* History Graph → udvikling over tid
* Conditional card → statusafhængig visning

---

## 🧠 Refleksion

* Hvilken type data bruger du i dine automations?
* Hvordan kan sensorer kombineres med regler og alarmer?
* Hvordan sikrer du valide og opdaterede målinger?

---

📌 Sensorer er øjne og ører i Home Assistant – de giver dig grundlaget for overvågning, automatisering og reaktion.
