# 🚀 IoT-Bootcamp – Node-RED, ESP32 & Industrial Integration

*12 × 3 timer • Aarhus Maskinmesterskole • 2025*

> Hands‑on kursus hvor automationsteknologer konfigurerer sensorer, dashboards, OTA‑opdatering og netværks­sikkerhed – uden at skulle blive fuldblods programmører.

---

## 🎯 Læringsmål

Efter endt forløb kan du …

1. **Opbygge fulde dataflows** i Node‑RED (inject, debug, function, change, switch, template m.m.).
2. **Publicere telemetri med MQTT/TLS** og forstå topics, QoS, LWT og heartbeat‑konceptet.
3. **Sende kommandoer via REST/HTTPS** og bygge simple webhooks.
4. **Integrere Home Assistant** (MQTT auto‑discovery, Lovelace, automations).
5. **Gateway’e Modbus TCP‑registre** til MQTT for “brown‑field” PLC‑data.
6. **Udrulle OTA‑opdateringer** til ESP32 vha. HTTPS og versionsstyring.
7. **Segmentere IoT‑trafik i VLAN** (pfSense/GNS3) og anvende certifikat‑autentificering.
8. **Visualisere og alarmere** live‑data med node‑red-dashboard.
9. **Synkronisere data til sky og lokal database** med Firebase og SQL.
10. **Analysere netværkstrafik** og beskytte CoAP/MQTT via Wireshark.
11. **Præsentere teknologikæden** i en 5‑min video (sensor → cloud → dashboard + sikkerhed).

---

## 📦 Teknologier & værktøjer

| Kategori        | Værktøj / bibliotek                              |
| --------------- | ------------------------------------------------ |
| Flow‑motor      | Node‑RED (Docker eller lokal)                    |
| Hardware        | ESP32 DevKit + KeyStudio‑sensorer                |
| Visualisering   | node‑red-dashboard, Home Assistant               |
| Protokoller     | MQTT + TLS, REST (HTTP/JSON), Modbus TCP, CoAP   |
| Databaser       | Firebase Realtime DB, Microsoft SQL Server       |
| Netværk         | Docker‑networks, pfSense (GNS3), Wireshark       |
| OTA             | MicroPython (`ota.py`), HTTPS static file‑server |
| Sikkerhed       | Certifikat‑baseret auth, VLAN‑segmentering       |
| Versionsstyring | Git / GitHub (1 branch pr. dag)                  |

---

## 📁 Repo‑struktur (eksempel)

```text
iot-bootcamp/
├── README.md
├── COURSE_SCHEDULE.md
├── common/
│   ├── certificates/
│   ├── docker-compose.core.yml
│   └── assets/ (firmware, scripts, billeder)
│
├── dag1-node-red-intro/
├── dag2-iot-monitoring/
├── dag3-http/
├── dag4-home-assistant/
├── dag5-coap-discovery/
├── dag6-modbus-integration/
├── dag7-netværkssikkerhed/
├── dag8-sky-og-lokal-baseret-lagring/
└── dag9-mini-project/
```

> **Bemærk:** Hver *dag‑mappe* indeholder
> • *README.md* → teori‑resume, læringsmål, opgaver
> • *Node‑RED‑flows (.json)* klar til import
> • *assets/* → firmware, certifikater, billeder, scripts
> • *extras/* (til stretch-goals) når relevant.

---

## 🧩 Moduloversigt

| Modul  | Fokus                            | Centrale teknologier og værktøjer            |
| ------ | -------------------------------- | -------------------------------------------- |
| **01** | Introduktion til Node‑RED        | inject, debug, function, ui\_gauge           |
| **02** | MQTT-telemetri & TLS             | mqtt in/out, ESP32, broker, certifikater     |
| **03** | HTTP & REST-integration          | http in/out, webhook, API-test               |
| **04** | Home Assistant                   | mqtt discovery, automations, Lovelace        |
| **05** | CoAP-discovery                   | /.well-known/core, ESP32, Node-RED, HA       |
| **06** | Modbus TCP-integration           | modbus-klient/server, esp32, HA, gateway     |
| **07** | Netværkssikkerhed & Wireshark    | MITM, sniffing, analyse, DTLS, TLS           |
| **08** | Sky- og lokalbaseret datalagring | Firebase, Microsoft SQL, Node.js, Python     |
| **09** | Mini-projekt                     | Valgfrit fokus, integration og dokumentation |

---

## ✅ Slutresultat

* Du kan levere en fuldt fungerende IoT-prototype **(sensor → dashboard)**,
  opdateret via OTA og adskilt i sikkert VLAN.
* Du dokumenterer flows og designvalg i GitHub.
* Du præsenterer løsningen i en **5‑min video** med live data og sikkerhedsovervejelser.
