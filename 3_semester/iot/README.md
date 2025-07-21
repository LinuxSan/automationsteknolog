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
8. **Visualisere og alarmere** live‑data med node‑red-dashboard og Grafana.
9. **Dokumentere og SAT/FAT‑teste** en mikro‑SCADA/smarthome‑løsning.
10. **Præsentere teknologikæden** i en 5‑min video (sensor → cloud → dashboard + sikkerhed).

---

## 📦 Teknologier & værktøjer

| Kategori        | Værktøj / bibliotek                              |
| --------------- | ------------------------------------------------ |
| Flow‑motor      | Node‑RED (Docker eller lokal)                    |
| Hardware        | ESP32 DevKit + KeyStudio‑sensorer                |
| Visualisering   | node‑red-dashboard, Home Assistant, Grafana      |
| Protokoller     | MQTT + TLS, REST (HTTP/JSON), Modbus TCP         |
| Netværk         | Docker‑networks, pfSense (GNS3)                  |
| OTA             | MicroPython (`ota.py`), HTTPS static file‑server |
| Sikkerhed       | Certifikat‑baseret auth, VLAN‑segmentering       |
| Versionsstyring | Git / GitHub (1 branch pr. dag)                  |

---

## 📁 Repo‑struktur (eksempel)

```text
iot-bootcamp/
├── README.md                   # Denne fil
├── COURSE_SCHEDULE.md          # Dag-for-dag-oversigt
├── common/                     # Certifikater, compose, dashboards
│   ├── certificates/
│   ├── docker-compose.core.yml
│   └── grafana/dashboards/
│
├── dag01_node-red_intro/
│   ├── README.md
│   ├── 01_inject_debug.json
│   ├── 02_ui_gauge.json
│   └── assets/cheat_sheet.pdf
│
├── dag02_mqtt_telemetri/
│   ├── README.md
│   ├── 01_subscribe.json
│   ├── 02_dashboard.json
│   └── assets/esp32_sensor.py
│
├── dag03_heartbeat_watchdog/
│   ├── README.md
│   └── watchdog_subflow.json
│
├── dag04_rest_commando/
│   ├── README.md
│   ├── http_in_mqtt_out.json
│   └── assets/postman_collection.json
│
├── dag05_home_assistant/
│   ├── README.md
│   ├── discovery_example.json
│   └── assets/ha_lovelace_view.yaml
│
├── dag06_modbus_gateway/
│   ├── README.md
│   ├── modbus_to_mqtt.json
│   └── assets/modbus_simulator.csv
│
├── dag07_dashboards_alarms/
│   ├── README.md
│   ├── dashboard_with_alarm.json
│   └── assets/grafana_panel.json
│
├── dag08_ota_update/
│   ├── README.md
│   ├── ota_server_flow.json
│   ├── assets/ota_client.py
│   └── assets/firmware/v1.0.0/ …
│
├── dag09_netsikkerhed_vlan/
│   ├── README.md
│   ├── pfSense_rules.md
│   ├── assets/docker-compose.vlan.yml
│   └── assets/wireshark_filters.txt
│
├── dag10_systemdesign/
│   ├── README.md
│   └── assets/architecture_template.drawio
│
├── dag11_sat_fat/
│   ├── README.md
│   ├── sat_checklist.xlsx
│   └── fat_checklist.xlsx
│
└── dag12_demo_video/
    ├── README.md
    ├── video_guidelines.md
    └── example_pitch_structure.md
```

> **Bemærk:** Hver *dag‑mappe* indeholder
> • *README.md* → teori‑resume, læringsmål, opgaver
> • *Node‑RED‑flows (.json)* klar til import
> • *assets/* → firmware, certifikater, billeder, scripts
> • *extras/* (til stretch-goals) når relevant.

---

## 🧩 Moduloversigt

| Modul  | Fokus                     | Centrale noder / værktøjer       |
| ------ | ------------------------- | -------------------------------- |
| **01** | Introduktion til Node‑RED | inject, debug, ui\_gauge         |
| **02** | MQTT‑telemetri            | mqtt in/out, ui\_chart, TLS      |
| **03** | Heartbeat & Watchdog      | trigger, function, status        |
| **04** | REST‑kommando             | http in/response, change         |
| **05** | Home Assistant            | mqtt discovery, binary\_sensor   |
| **06** | Modbus‑gateway            | node-red-contrib-modbus          |
| **07** | Dashboards & alarmer      | ui\_led, switch, Grafana         |
| **08** | OTA‑update                | ota\_server flow, ota\_client.py |
| **09** | VLAN & sikkerhed          | pfSense/GNS3, cert-auth          |
| **10** | Systemdesign              | draw\.io, protokolvalg           |
| **11** | SAT/FAT-test              | test-flows, multimeter           |
| **12** | Demo & video              | OBS, peer-review                 |

---

## ✅ Slutresultat

* Du kan levere en fuldt fungerende IoT-prototype **(sensor → dashboard)**,
  opdateret via OTA og adskilt i sikkert VLAN.
* Du dokumenterer flows, sikkerhed, tests og designvalg i GitHub.
* Du præsenterer løsningen i en **5‑min video** med live data, alarms og failover‑demo.
