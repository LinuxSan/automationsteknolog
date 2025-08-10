# 🧪 Opgaver – Home Assistant: Sensorer

Disse øvelser guider dig gennem opsætning og visualisering af sensorer i Home Assistant. Du arbejder med MQTT Discovery, grafisk præsentation og tilstandsovervågning.

---

## 🟢 Opgave 1 – MQTT sensor via Discovery

1. Send følgende payload fra terminal eller Node-RED:

```bash
mosquitto_pub -h localhost -t "homeassistant/sensor/stue_temp/config" -m '{"name": "Stue Temperatur", "state_topic": "smarthouse/stue/temperature", "unit_of_measurement": "°C", "device_class": "temperature", "unique_id": "sensor_stue_temp_01"}' -r
```

2. Bekræft at sensoren vises i Home Assistant
3. Send fx `22.7` til `smarthouse/stue/temperature` og se opdatering

✅ *Sensorværdien skal afspejles i UI med det samme*

---

## 🔵 Opgave 2 – Visualisering i dashboard

1. Gå til dashboard-editor
2. Tilføj et `Gauge Card` for `sensor.stue_temp`
3. Sæt passende grænser (fx 0–40°C)
4. Tilføj evt. `History Graph Card` for at se historik

✅ *Dashboardet skal give et klart overblik over sensorens målinger*

---

## 🟡 Opgave 3 – Binary sensor med tilstand

1. Send følgende discovery-konfiguration:

```bash
mosquitto_pub -h localhost -t "homeassistant/binary_sensor/dor/config" -m '{"name": "Hoveddør", "device_class": "door", "state_topic": "smarthouse/door", "payload_on": "OPEN", "payload_off": "CLOSED", "unique_id": "door_sensor_01"}' -r
```

2. Test med følgende:

```bash
mosquitto_pub -h localhost -t "smarthouse/door" -m "OPEN"
```

3. Bekræft at tilstand og ikon ændres i UI

✅ *Visuel feedback skal være tydelig (fx åben/lukket dør ikon)*

---

## 🔁 Opgave 4 – Tidsbaseret måling (Node-RED)

1. Brug `inject` node til at sende sensorværdier hvert minut
2. Brug `mqtt out` til `smarthouse/stue/temperature`
3. Brug `function node` til at simulere værdier (fx random mellem 20–25)
4. Observer ændringer og grafer i HA dashboard

✅ *Sensorer kan nu bruges til realtidsvisning og automatisering*

---

## 🧠 Refleksion

* Hvad er forskellen på en sensor og en binary\_sensor?
* Hvordan ville du bruge sensordata i automations?
* Hvad sker der hvis en sensor ikke sender nyt data i lang tid?

---

📌 Sensorer er afgørende for overvågning og beslutninger i Home Assistant. Korrekt opsætning sikrer pålidelige målinger og brugbar visualisering.
