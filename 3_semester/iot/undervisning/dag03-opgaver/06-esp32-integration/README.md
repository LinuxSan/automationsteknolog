# 📲 Dag 4 – Home Assistant 07: ESP32 Integration

I denne lektion lærer du at integrere en ESP32-enhed med Home Assistant via MQTT. Du konfigurerer sensorer, aktuatorer og bruger discovery-protokollen til automatisk oprettelse.

---

## 🎯 Læringsmål

* Forstå hvordan ESP32 kommunikerer med HA
* Bruge MQTT til at sende og modtage data
* Implementere discovery-protokol på ESP32

---

## 🔌 Forbindelsesoversigt

1. ESP32 måler data eller modtager input
2. ESP32 sender MQTT-data til Mosquitto broker
3. Home Assistant abonnerer på topics og opretter enheder

---

## 🔧 Forudsætninger

* Mosquitto MQTT broker kører og er tilgængelig for ESP32
* ESP32 er konfigureret med WiFi og PubSubClient (eller lignende bibliotek)

---

## 🧪 Eksempel – Temperaturmåling

```cpp
client.publish("homeassistant/sensor/stue_temp/config",
  "{\"name\":\"Stue Temperatur\",\"state_topic\":\"smarthouse/stue/temperature\",\"unit_of_measurement\":\"°C\",\"device_class\":\"temperature\",\"unique_id\":\"esp32_temp_01\"}",
  true);

float temp = 22.5;
client.publish("smarthouse/stue/temperature", String(temp).c_str());
```

> HA opdager automatisk sensor og viser den i UI

---

## ⚙️ Eksempel – Aktuator (lys)

```cpp
client.subscribe("smarthouse/stue/light/set");

if (strcmp(topic, "smarthouse/stue/light/set") == 0) {
  if (strcmp(payload, "ON") == 0) digitalWrite(RELAY_PIN, HIGH);
  else if (strcmp(payload, "OFF") == 0) digitalWrite(RELAY_PIN, LOW);
}
```

---

## 🛡 Tips til robust integration

* Brug `retain` ved config og seneste state
* Brug `unique_id` og `device` info for stabil enheds-ID
* Send `last_will` for offline detection
* Tilføj heartbeat-topic med fast interval

---

## 🧠 Refleksion

* Hvordan opdager Home Assistant nye enheder?
* Hvordan sikrer du, at ESP32 ikke oversvømmer systemet med data?
* Hvordan kan ESP32 også modtage kommandoer og agere aktuator?

---

📌 Med MQTT og discovery kan ESP32 blive en fleksibel og kraftfuld enhed i Home Assistant – til både overvågning og styring.
