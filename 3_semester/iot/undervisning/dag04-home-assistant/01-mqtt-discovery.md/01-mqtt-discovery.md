
# 🧪 Opgaver – Home Assistant: MQTT Discovery

Disse øvelser giver dig praktisk erfaring med MQTT Discovery i Home Assistant. Du lærer at registrere sensorer og aktuatorer automatisk uden manuel YAML-konfiguration.

---

## 🟢 Opgave 1 – Konfigurer Mosquitto og HA

1. Bekræft at din MQTT broker (Mosquitto) kører
2. Sørg for, at Home Assistant har MQTT integration aktiveret:

   * Gå til `Indstillinger` → `Enheder & Services` → `Tilføj Integration` → MQTT
3. Tilføj din broker-adresse og klik "Udfør"

✅ *Tjek at HA viser forbindelsesstatus som "Connected"*

---

## 🔵 Opgave 2 – Udgiv en sensor via MQTT Discovery

1. Brug fx Node-RED, MQTT Explorer eller terminal (`mosquitto_pub`)
2. Send følgende payload:

```bash
mosquitto_pub -h localhost -t "homeassistant/sensor/kitchen_temp/config" -m '{"name": "Kitchen Temp", "state_topic": "sensors/kitchen/temperature", "unit_of_measurement": "°C", "device_class": "temperature", "unique_id": "kitchen_temp_01"}' -r
```

3. Bekræft at "Kitchen Temp" dukker op i HA under Enheder
4. Send måling:

```bash
mosquitto_pub -h localhost -t "sensors/kitchen/temperature" -m "21.4"
```

✅ *Tjek at UI viser opdateret værdi i entiteten*

---

## 🟡 Opgave 3 – Udgiv en switch-aktuator via MQTT Discovery

1. Send denne konfiguration:

```bash
mosquitto_pub -h localhost -t "homeassistant/switch/ventilator/config" -m '{"name": "Ventilator", "command_topic": "devices/fan/set", "state_topic": "devices/fan", "payload_on": "ON", "payload_off": "OFF", "unique_id": "fan_01"}' -r
```

2. Tænd/sluk fra Home Assistant UI
3. Send selv kommando med terminal:

```bash
mosquitto_pub -h localhost -t "devices/fan/set" -m "ON"
mosquitto_pub -h localhost -t "devices/fan" -m "ON"
```

✅ *Tjek at HA-UI skifter status korrekt når state-topic opdateres*

---

## 🔁 Opgave 4 – Tilføj availability og retain

1. Redigér din `sensor` config og tilføj:

```json
"availability_topic": "devices/kitchen/status",
"payload_available": "online",
"payload_not_available": "offline"
```

2. Udgiv "online" på status-topic og se resultat i HA
3. Stop MQTT-forbindelse og observer ændring til "utilgængelig"

✅ *HA viser entiteten som offline, når heartbeat forsvinder*

---

## 🔄 Opgave 5 – Brug Node-RED til Discovery

1. Lav et inject node med discovery-payload (fx sensor)
2. Brug `mqtt out` til at sende til `homeassistant/sensor/.../config`
3. Bekræft at Home Assistant opretter enheden

✅ *Tilknyt automatisk dataflow fra sensor eller simulation*

---

## 🧠 Refleksion

* Hvorfor er det en fordel at bruge `retain`-flaget?
* Hvad er vigtigt ved `unique_id`?
* Hvad sker der, hvis to enheder bruger samme `object_id`?

---

📌 Du har nu praktisk erfaring med at automatisere integrationen mellem enheder og Home Assistant via MQTT Discovery. Klar til at udbygge dit smarthome dynamisk og uden YAML!
