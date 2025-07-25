# 🔄 CoAP-MQTT Gateway – Teori

I dette modul lærer du, hvordan du kan bygge en gateway mellem CoAP og MQTT-protokollerne. Dette muliggør integration af ressourcebegrænsede CoAP-enheder i større IoT-økosystemer baseret på MQTT.

---

## 🎯 Læringsmål

* Forstå forskelle og ligheder mellem CoAP og MQTT
* Lære hvordan en gateway kan oversætte mellem protokollerne
* Forstå mapping mellem URI'er og topics samt payload-formater
* Forstå hvordan QoS og Observe håndteres i en gateway

---

## 🌐 Hvorfor en CoAP-MQTT Gateway?

**CoAP**:

* RESTful, URI-baseret
* Bruges af små enheder (UDP)
* Typisk direkte forespørgsel/svar eller Observe

**MQTT**:

* Broker-baseret publish/subscribe
* Pålidelig levering (QoS)
* Letvægts, men robust

**En gateway giver dig mulighed for at:**

* Modtage data fra CoAP og publicere dem til MQTT-topics
* Konvertere MQTT-kommandoer til CoAP-anmodninger
* Aggregere data fra mange enheder til ét system

---

## 🏗 Arkitekturer

**1. Proxy-model:**

* Gateway oversætter uden at klienterne ved det

**2. Oversættelsesmodel:**

* Tydelig mapping mellem CoAP-ressourcer og MQTT-topics

**3. Aggregeringsmodel:**

* Gateway samler data og videresender til MQTT

---

## 🔁 Mapping: URI til Topic

**Eksempel:**

* CoAP URI: `coap://device/sensors/temperature`
* MQTT Topic: `coap/device/sensors/temperature`

**Kommandoer:**

* MQTT Topic: `commands/device/actuators/led`
* CoAP URI: `coap://device/actuators/led`

---

## 📦 Payload og Format

* CoAP bruger Content-Format (fx `application/json`)
* MQTT har ingen standard – formater skal defineres

**Gateway opgaver:**

* Konvertering mellem binær/tekst
* Tilføjelse af metadata (timestamp, enheder)

---

## 🔐 QoS og Pålidelighed

| CoAP | MQTT  |
| ---- | ----- |
| CON  | QoS 1 |
| NON  | QoS 0 |

* Gateway skal vælge passende QoS og sikre levering

---

## 👀 Observe og Subscribe

* CoAP Observe → MQTT publish
* MQTT Subscribe → CoAP PUT/POST

Gatewayen skal oversætte begge veje og holde forbindelserne i live.

---

## 🔍 Dynamisk ressourceopdagelse

1. Send GET `/.well-known/core`
2. Læs URI'er og metadata (rt, if, ct)
3. Opret MQTT-topics baseret på ressourcer
4. Publicer discovery-info til fx `coap/discovery`

---

## ✅ Konklusion

En CoAP-MQTT gateway forener to IoT-verdener og gør det muligt at bygge skalerbare, fleksible og effektive systemer, hvor små enheder kan tale med store platforme uden kompleks konfiguration.

---

👉 I næste dokument finder du opgaver til både ESP32, Node-RED og en avanceret udfordring med automatisk discovery og observe support.
