# 🔗 HTTP REST – System Integration (Teori)

Dette afsnit forklarer, hvordan REST bruges til at forbinde systemer, platforme og services i IoT, automation og softwarearkitektur. Integration handler om at gøre adskilte systemer i stand til at samarbejde via standardiserede API-kald.

---

## 🎯 Læringsmål

* Forstå hvordan REST forbinder systemer og komponenter
* Kende forskellen mellem system-til-system og bruger-til-system integration
* Få overblik over typiske REST-integrationer i praksis

---

## 🧩 Hvad er systemintegration?

Systemintegration betyder at to eller flere systemer deler data og funktionalitet. REST gør dette muligt via:

* Enkle HTTP-kald
* Ensartet datastruktur (typisk JSON)
* Løskobling (decoupling) – systemer er uafhængige

---

## 🧱 Integrationstyper

| Type                | Eksempel                                        |
| ------------------- | ----------------------------------------------- |
| ESP32 → Node-RED    | ESP sender temperatur til REST-endpoint         |
| Node-RED → HA       | Node-RED POST’er til webhook i Home Assistant   |
| Node-RED → InfluxDB | Målinger gemmes via HTTP POST til database      |
| HA → REST-sensor    | Henter data fra ekstern REST API (vejr, energi) |
| Grafana → HA        | Visualiserer REST-data i dashboards             |

---

## 🔁 REST som standard interface

REST er velegnet som grænseflade fordi:

* Det er let at bruge fra mange sprog og platforme
* Det fungerer både med maskiner og mennesker
* Det er internet-venligt og baseret på åbne standarder

REST er en *mellemstation* mellem sensorer, databaser, brugere og dashboards.

---

## 🧠 REST som del af microservices

I moderne arkitektur opdeles systemer i små services:

* Hver service har sit eget REST API
* Kommunikation sker via HTTP internt og eksternt
* REST sikrer isolering og fleksibel opskalering

---

## 🔗 Eksempler fra undervisning

* ESP32 sender måling til `/api/temperature`
* Node-RED lagrer i `flow.set()` og sender videre til Home Assistant
* HA viser data i Lovelace-dashboard via REST-sensor
* REST-kald går til InfluxDB eller MongoDB til logning

---

## 🔒 Integration med sikkerhed

Når systemer taler sammen, skal du overveje:

* Adgangsnøgler (API keys, tokens)
* Kryptering (TLS/HTTPS)
* Begrænset adgang (kun POST/GET som nødvendig)
* Rate-limiting for at beskytte mod overload

---

## 🔧 Teknologier der understøtter REST-integration

| System         | Funktion                         |
| -------------- | -------------------------------- |
| Node-RED       | Nem REST-server og -klient       |
| Home Assistant | Webhooks, rest\_command, sensors |
| ESP32/Arduino  | HTTPClient, WiFiClient, bearSSL  |
| InfluxDB       | HTTP API til lagring af data     |
| Grafana        | Visualisering af REST/DB-data    |

---

## 🧠 Refleksion

* Hvilke komponenter i dit system bør være REST-kunder, og hvilke REST-servere?
* Hvordan kan REST hjælpe med at debugge og overvåge systemstatus?
* Hvad er fordelene ved at have et REST API fremfor direkte koblinger mellem systemer?

---

📌 REST gør det muligt at bygge fleksible, modulære og skalerbare løsninger – uanset om det handler om IoT, frontend, databaser eller cloud-tjenester.
