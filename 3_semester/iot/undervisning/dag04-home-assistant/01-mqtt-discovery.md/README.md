# 📡 Dag 4 – Home Assistant 02: MQTT Discovery

I denne lektion lærer du, hvordan Home Assistant automatisk opdager enheder via MQTT. Discovery-protokollen gør det nemt at integrere ESP32, Node-RED og andre IoT-enheder uden manuel konfiguration.

---

## 🎯 Læringsmål

* Forstå hvordan MQTT Discovery fungerer
* Udgive discovery-payloads fra ESP32 eller Node-RED
* Se enheder automatisk i Home Assistant UI

---

## 📦 Hvad er MQTT Discovery?

* Et sæt standardiserede MQTT-beskeder
* Sendes til topics under `homeassistant/...`
* Indeholder metadata om enheden og dens egenskaber
* Home Assistant abonnerer og registrerer enheder dynamisk

---

## 🔧 Krav

* MQTT broker (fx Mosquitto) kører
* Home Assistant har MQTT integration aktiv
* `discovery` er slået til (som standard)

---

## 🧪 Eksempel: Temperatur-sensor

Send dette fra Node-RED eller ESP32:

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

Når Home Assistant modtager dette, oprettes en ny sensor automatisk.

---

## 🕹 Aktuatorer (fx lys, switches)

Topic: `homeassistant/switch/kontorlys/config`

```json
{
  "name": "Kontorlys",
  "command_topic": "smarthouse/kontor/lys/set",
  "state_topic": "smarthouse/kontor/lys",
  "payload_on": "ON",
  "payload_off": "OFF",
  "unique_id": "kontor_lys_switch"
}
```

---

## 🔁 Dataflow

1. Enhed publicerer `config`-payload (en gang eller ved opstart)
2. Home Assistant registrerer og viser enheden
3. Enheden sender/lytter på `state_topic` og `command_topic`

---

## 🔒 Sikkerhed

* Discovery bør kun tillades fra kendte enheder
* Du kan begrænse topics i Mosquitto via ACL
* Anvend `retain`-flag så HA kan hente konfiguration efter genstart

---

## 🧠 Refleksion

* Hvad er fordelene ved MQTT Discovery fremfor manuel YAML-konfiguration?
* Hvordan kan du versionere eller ændre en MQTT-enhed?
* Hvorfor er det vigtigt med `unique_id`?

---

📌 MQTT Discovery gør Home Assistant ekstremt fleksibel og skalerbar – og giver en nem vej til integration af egne enheder og systemer.
