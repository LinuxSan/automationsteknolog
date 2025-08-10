# 🧪 Opgaver – MQTT Systemovervågning og Validering

Disse opgaver bygger oven på MQTT-begreberne: heartbeat, watchdog og plausibility check. Du skal sende reelle sensorværdier fra en ESP32 og bruge Node-RED til at analysere og overvåge datastrømmen.

---

## 🟢 Del 1 – Data fra ESP32 til Node-RED

### 🎯 Læringsmål

* Du kan sende målinger fra en ESP32 til en MQTT-broker
* Du kan visualisere og analysere data i Node-RED

### 🔧 Udfør

1. Tilslut en DHT11 eller DHT22 temperatur- og fugtighedssensor til din ESP32
2. Skriv MicroPython eller Arduino-kode, som:

   * Læser temperatur og fugtighed
   * Udgiver det via MQTT hver 10. sekund
   * Topic: `sensor/temp` og `sensor/humidity`
3. Visualiser data i Node-RED ved brug af:

   * `mqtt in` → `debug`
   * `mqtt in` → `chart` (via `dashboard`)

---

## ❤️ Del 2 – Heartbeat

### 🎯 Læringsmål

* Du forstår hvorfor heartbeat er vigtig i et IoT-system
* Du kan bruge MQTT til at sende og overvåge livstegn

### 🔧 Udfør

1. Tilføj et separat MQTT-publish i din ESP32-kode:

   * Topic: `heartbeat/esp32_1`
   * Payload: `online`
   * Interval: hvert 10. sekund
2. I Node-RED:

   * Brug `mqtt in` → `debug` til at se beskeder
   * Brug `trigger` node til at opdage, hvis beskeder ikke modtages inden for 15 sekunder
   * Send evt. alarm til topic `alert/esp32_1`

> 💡 Bonus: Vis status på dashboard som “Online” / “Offline” (fx med en `ui_text` og farvekode)

---

## ⏱️ Del 3 – Watchdog-logik i Node-RED

### 🎯 Læringsmål

* Du kan simulere en software-watchdog, som aktiveres ved fejl i datastrøm

### 🔧 Udfør

1. Overvåg `sensor/temp`
2. Brug en `trigger`-node som:

   * “Send intet, medmindre der ikke kommer ny besked i 20 sekunder”
   * Hvis der ikke kommer besked → send besked til topic `alerts/temp_missing`
3. Visualiser alarmen i `debug` og evt. som rød indikator i `dashboard`

> 🛠 Brug evt. `rbe` for at undgå duplikerede beskeder

---

## 🧪 Del 4 – Plausibility Check

### 🎯 Læringsmål

* Du kan identificere usandsynlige målinger og reagere på dem

### 🔧 Udfør

1. Tilføj `switch`-node efter `mqtt in` for `sensor/temp`
2. Definér betingelser:

   * Temperatur < -10°C → “for lav”
   * Temperatur > 50°C → “for høj”
   * Andet → tillad videre behandling
3. Hvis målingen er ugyldig, send besked til:

   * Topic: `alerts/temperature_invalid`
   * Visualisér i dashboard som advarsel

> 💬 Ekstra: Brug `template`-node til at formulere beskedens indhold som tekst.

---

## 🕓 Ekstra – Gem sidste tidsstempel i flow

### 🎯 Læringsmål

* Du kan gemme og genbruge tidspunktet for seneste datamodtagelse

### 🔧 Udfør

1. Brug en `function` node efter din `mqtt in` node:

```javascript
flow.set("lastUpdate", new Date().toISOString());
return msg;
```

2. Brug en anden `inject` eller `ui_button` til at vise sidste opdatering:

```javascript
msg.payload = flow.get("lastUpdate");
return msg;
```

3. Vis tidsstempel i `debug` eller i `ui_text`

> 💡 Du kan også logge ændringer til en fil, database eller ekstern MQTT-topic.

---

## 📋 Afslutning og dokumentation

* Lav et skærmbillede af dit Node-RED flow og forklar det kort
* Beskriv hvilke typer fejl du har forsøgt at opfange (timeout, ekstremværdi, offline)
* Reflektér over hvordan disse begreber kan bruges i et industrielt setup

> Du må gerne kombinere opgaverne til ét samlet flow med tydelig datavej og overvågningspunkter.
