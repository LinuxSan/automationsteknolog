# 🧪 Opgaver – HTTP REST System Integration

Disse opgaver træner dig i at integrere forskellige systemer via REST. Du kombinerer ESP32, Node-RED, Home Assistant og evt. eksterne tjenester i én løsning, hvor systemerne kommunikerer via HTTP.

> 🧠 Fokus: REST på tværs af systemer – IoT, automation og lagring

---

## 🟢 Del 1 – ESP32 → Node-RED via POST

### 🎯 Læringsmål

* Du kan sende data fra en embedded enhed til REST API

### 🔧 Opgave

1. Programmer din ESP32 (Arduino/PlatformIO):

   * Læs temperatur (DHT11 el. mock)
   * Send POST til `http://<NODE_RED_IP>:1880/api/temperature`
   * Payload:

```json
{ "sensor": "living_room", "value": 22.3 }
```

2. I Node-RED:

   * `http in` → `json` → `function` (gem til flow\.set)
3. Vis i dashboard eller send videre

💬 Refleksion: Hvordan håndteres forbindelsesfejl fra ESP’en?

---

## 🔵 Del 2 – Node-RED → Home Assistant via REST

### 🎯 Læringsmål

* Du kan sende REST-kald fra Node-RED til HA webhook

### 🔧 Opgave

1. I Home Assistant:

   * Lav automation med webhook `vand_læk`
   * Trigger tænder sirene eller sender notifikation

2. I Node-RED:

   * Brug `http request` node med POST til:

```http
http://<HA_IP>:8123/api/webhook/vand_læk
```

* Test via `inject` + `debug`

💬 Refleksion: Hvordan sikrer du at beskeden kun sendes én gang ved alarm?

---

## 🟡 Del 3 – Node-RED → InfluxDB via REST

### 🎯 Læringsmål

* Du kan gemme målinger fra REST i database

### 🔧 Opgave

1. Installer InfluxDB lokalt eller via Docker
2. Lav endpoint i Node-RED `/api/temperature`
3. Ved modtagelse af måling:

   * Send POST til InfluxDB API med sensor-data
   * Fx:

```text
temp,sensor=living_room value=22.3
```

4. Bekræft at målinger optræder i InfluxDB (brug UI eller `curl`)

💬 Refleksion: Hvad er fordelene ved REST frem for MQTT til lagring?

---

## 🔴 Del 4 – REST Integration Flow (komplet kæde)

### 🎯 Læringsmål

* Du kan forbinde alle dele i en REST-integreret pipeline

### 🔧 Opgave

1. ESP32 → Node-RED: Temperaturmåling
2. Node-RED:

   * Gem i `flow`
   * Send webhook til Home Assistant
   * Send måling til InfluxDB
3. Home Assistant:

   * Trigger notification eller UI-opdatering

💬 Refleksion: Hvor i kæden kan der opstå flaskehalse?

---

## 🧭 Afslutning og overblik

📋 Tjekliste:

* [ ] ESP32 sender data via POST?
* [ ] Node-RED modtager og håndterer?
* [ ] Data sendes videre til database og/eller HA?
* [ ] REST bruges til 2+ systemer sammenkoblet?

🧠 Ekstra:

* Tilføj logging af REST-kald med timestamp og IP
* Tilføj sikkerhed (token/HTTPS)
* Dokumentér alle endpoints og dataformater

---

📌 REST gør det muligt at samle enheder og platforme til ét system, hvor hver komponent arbejder uafhængigt – men i fællesskab.
