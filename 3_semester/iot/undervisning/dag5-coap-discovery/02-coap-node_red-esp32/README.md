# 🤖 CoAP – 02: Node-RED og ESP32

Denne lektion fokuserer på praktisk integration mellem ESP32 og Node-RED via CoAP. Du lærer, hvordan du konfigurerer en simpel CoAP-server og -klient, og hvordan data udveksles med visualisering.

---

## 🎯 Læringsmål

* Køre en CoAP-server på ESP32
* Læse sensordata via CoAP i Node-RED
* Udvide med kommandoer og aktuatorkontrol

---

## 🧱 Komponenter

* **ESP32:** Kører CoAP-server (via Arduino CoAP-libraries)
* **Node-RED:** Fungerer som CoAP-klient (eller mellemstation)
* **Sensor:** F.eks. DHT11 for temperatur/fugt
* **Broker (valgfrit):** Mosquitto til hybrid MQTT-CoAP bridge

---

## 🔌 Opsætning: ESP32 med CoAP-server

1. Installer Arduino-biblioteket `CoAP-simple-library`
2. Konfigurer ESP32 som CoAP-server:

```cpp
coap.server(callback, "temp");
coap.start();
```

3. `callback()` returnerer f.eks. temperaturen fra DHT11

---

## 📡 Node-RED som klient

1. Brug `node-red-contrib-coap` palette
2. Opret en `coap request` node
3. URL: `coap://<ESP_IP>/temp`
4. Tilføj `inject` → `coap request` → `debug`

---

## 🧪 Eksempelflow

* ESP32 svarer på `GET /temp` med JSON:

```json
{ "temperature": 23.6, "humidity": 41 }
```

* Node-RED modtager og visualiserer data
* Mulighed for parsing og visning i dashboard

---

## 🛠 Udvidelse: ESP32 som aktuator

1. Tilføj endpoint `/led` på ESP32
2. Node-RED sender `PUT /led` med payload `"ON"`
3. ESP32 tænder LED og svarer med status

---

## 🧠 Refleksion

* Hvordan adskiller dette sig fra MQTT?
* Hvad er fordelene ved CoAP i små netværk?
* Hvilke udfordringer ser du ved sikkerhed og fejlhåndtering?

---

📌 CoAP åbner for RESTful interaktion direkte mellem microcontrollers og Node-RED uden tunge protokoller som HTTP eller MQTT.
