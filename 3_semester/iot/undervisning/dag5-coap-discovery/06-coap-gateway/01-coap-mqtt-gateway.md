# 🧪 CoAP-MQTT Gateway – Opgaver

Dette dokument indeholder praktiske opgaver til implementering af en CoAP-MQTT gateway. Opgaverne spænder fra grundlæggende kommunikation med ESP32 til fuld integration i Node-RED – samt en udfordring for viderekomne.

---

## 🧩 Opgave 1 – Grundlæggende gateway med ESP32

**Formål:** Oversæt data fra en CoAP-sensor til MQTT og kommandoer fra MQTT til CoAP.

### Trin

1. Opsæt en ESP32 med Wi-Fi og installer `coap-simple` og `PubSubClient` biblioteker
2. Brug CoAP til at anmode en ekstern CoAP-server om fx `/sensors/temperature`
3. Publicer svaret til MQTT med topic `coap/sensors/temperature`
4. Lyt til `commands/led` på MQTT og send det som CoAP PUT til `/led`

### Ekstra

* Brug `Serial.println()` til at vise flow
* Tilføj reconnect-logik

---

## 🔁 Opgave 2 – Node-RED Gateway

**Formål:** Byg en CoAP-MQTT gateway med Node-RED

### Trin

1. Installér `node-red-contrib-coap` og `node-red-dashboard`
2. Lav et flow som:

   * MQTT in → Function → CoAP request (PUT)
   * CoAP Observe → Function → MQTT out
3. Lav mapping mellem fx `commands/led` og `coap://device/led`
4. Brug dashboard til at vise live-data og sende kommandoer

### Ekstra

* Parse `/.well-known/core` og generér MQTT discovery-topic

---

## 🔍 Opgave 3 – Dynamisk ressourceopdagelse

**Formål:** Udnyt `/.well-known/core` til automatisk mapping

### Trin

1. Lav CoAP GET til `/.well-known/core`
2. Parse svaret og opret en liste over ressourcer
3. For hver observerbar ressource:

   * Start Observe
   * Publicer data til MQTT topic ud fra URI
4. Publicer JSON med oversigt til `coap/discovery`

### Format eksempel:

```json
{
  "resources": [
    {"uri": "/temp", "type": "temperature", "observable": true}
  ]
}
```

---

## 🧠 Udfordring – Byg en enterprise-grade gateway

**Krav:**

* Understøt alle metoder (GET, POST, PUT, DELETE)
* Map CoAP CON/NON til MQTT QoS 1/0
* Konverter JSON payloads og tilføj metadata
* Automatisk genopdagelse af ressourcer hver 5. minut
* Understøt Observe og MQTT retain/QoS korrekt
* Publicer heartbeat/status til fx `gateway/status`

### Valgfrit

* Brug TLS (MQTTS) og/eller DTLS til CoAP
* Log hændelser til fil eller MQTT
* Understøt brugerdefineret mapping-konfiguration fra YAML/JSON

---

✅ Disse opgaver hjælper dig med at bygge robuste bro-løsninger mellem CoAP og MQTT – både som embedded løsning og visuel gateway i Node-RED.
