# 🧪 Opgaver – CoAP 02: Node-RED og ESP32

Disse øvelser guider dig i at få en ESP32 til at fungere som CoAP-server, og få Node-RED til at forespørge og visualisere data.

---

## 🟢 Opgave 1 – Kør CoAP-server på ESP32

1. Installer `CoAP-simple-library` i Arduino IDE
2. Skriv sketch der:

   * Forbinder til WiFi
   * Starter CoAP-server
   * Returnerer temperatur ved GET `/temp`
3. Upload til ESP32 og tjek IP i `Serial Monitor`

✅ *ESP32 svarer med fx "23.4" på CoAP GET-anmodning*

---

## 🔵 Opgave 2 – Forespørg ESP32 fra Node-RED

1. Installer `node-red-contrib-coap`
2. Lav flow med:

   * `inject node` → `coap request` → `debug`
   * URL: `coap://<ESP_IP>/temp`
3. Tjek svaret i debug-vinduet

✅ *Temperaturdata vises i Node-RED debug*

---

## 🟡 Opgave 3 – Visualiser i dashboard

1. Parse JSON-svaret fra ESP32 med `function node`
2. Send til `gauge` i dashboard:

```javascript
let data = JSON.parse(msg.payload);
msg.payload = data.temperature;
return msg;
```

3. Gentag for fugtighed hvis tilgængelig

✅ *Sensorværdier vises live i UI*

---

## 🔁 Opgave 4 – Styr LED via PUT-anmodning

1. Tilføj CoAP `PUT /led` endpoint i ESP32 der tænder/slukker LED
2. I Node-RED:

   * Brug `inject` med "ON" / "OFF"
   * Send til `coap request` med metode `PUT`
3. LED på ESP32 skal skifte status

✅ *Node-RED styrer fysisk komponent via CoAP*

---

## 🧠 Refleksion

* Hvad er fordelene ved CoAP ift. REST/MQTT i små systemer?
* Hvad er dine observationer ift. responstid og stabilitet?
* Hvordan ville du bygge en gateway mellem CoAP og MQTT?

---

📌 Du har nu testet tovejskommunikation mellem ESP32 og Node-RED med CoAP, og grundlagt basis for RESTful IoT uden HTTP-overhead.
