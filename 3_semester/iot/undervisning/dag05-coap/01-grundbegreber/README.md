# 🌐 CoAP – 01: Grundbegreber

CoAP (Constrained Application Protocol) er en letvægtsprotokol designet til små enheder og netværk med begrænsede ressourcer – fx IoT-enheder. Den fungerer på samme måde som HTTP, men med færre krav og lavere overhead.

---

## 🎯 Læringsmål

* Forstå hvad CoAP er og hvorfor det bruges
* Kende forskelle mellem CoAP og HTTP
* Introduktion til basisfunktioner i CoAP

---

## 🔍 Hvad er CoAP?

CoAP er en RESTful applikationsprotokol baseret på UDP og designet til:

* Sensorer og aktuatorer med lav strøm
* Netværk med høj latenstid eller pakkedrop
* Kommunikation i både LAN og trådløse net

---

## ⚙️ Tekniske egenskaber

| Egenskab           | CoAP                          | HTTP               |
| ------------------ | ----------------------------- | ------------------ |
| Transportprotokol  | UDP                           | TCP                |
| Ressourceadgang    | REST (GET, POST, PUT, DELETE) | REST               |
| Letvægt            | Ja (compact binary format)    | Nej (tekstbaseret) |
| Port               | 5683                          | 80 / 443           |
| Understøtter proxy | Ja                            | Ja                 |

---

## 📦 Typisk brug

* ESP32 kommunikerer med en CoAP-server (eller anden ESP32)
* En klient anmoder fx om temperaturen fra en sensor
* Server svarer med payload i JSON eller tekst

Eksempel:

```plaintext
GET coap://192.168.1.50/temp
Response: 22.3
```

---

## ✉️ CoAP Pakker

CoAP understøtter:

* Bekræftede beskeder (CON)
* Ikke-bekræftede beskeder (NON)
* Reset og acknowledgement (RST/ACK)

---

## 🔐 Sikkerhed

CoAP understøtter DTLS (Datagram TLS) for kryptering og godkendelse. Det kræver dog mere konfiguration og ressourcer.

---

## 🧠 Refleksion

* Hvorfor bruge CoAP fremfor HTTP eller MQTT?
* Hvornår er UDP en fordel fremfor TCP?
* Hvordan kan CoAP bruges mellem ESP32 og fx Node-RED?

---

📌 CoAP er designet til effektiv kommunikation i IoT-verdenen og er et stærkt alternativ til HTTP i systemer med mange enheder og begrænsede ressourcer.
