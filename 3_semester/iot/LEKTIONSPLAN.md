
# Detaljeret Forløbsplan  
## IoT-undervisning (12 dage)  
**Aarhus Maskinmesterskole**  
**Underviser:** Anders S. Østergaard  
**Opdateret:** Juli 2025

---

## Indholdsfortegnelse
1. [Dag 1: Node-RED Introduktion](#dag-1-node-red-introduktion)
2. [Dag 2: IoT Monitoring (MQTT)](#dag-2-iot-monitoring-mqtt)
3. [Dag 3: REST Kommandoer & Data Storage](#dag-3-rest-kommandoer--data-storage)
4. [Dag 4: Home Assistant & Integrering](#dag-4-home-assistant--integrering)
5. [Dag 5: CoAP & Resource Discovery](#dag-5-coap--resource-discovery)
6. [Dag 6: Modbus-integration](#dag-6-modbus-integration)
7. [Dag 7: Netværk & Sikkerhed](#dag-7-netværk--sikkerhed)
8. [Dag 8: Mini-projekt](#dag-8-mini-projekt)

---

## Dag 1: Node-RED Introduktion
**Emne:** Flow-baseret programmering, installation og grundlæggende brug af Node-RED.  
**Indhold:**  
- Installation og opstart af Node-RED (fx via Docker)
- Editor-tour: palette, workspace, deploy-knap
- Simpel flow-opbygning: inject → debug → ui_gauge
- Grundlæggende databehandling i function nodes

**Læringsaktiviteter:**  
- Udfør simple flows: inject til debug, value til gauge
- Eksport/import af flows
- Node-RED cheat-sheet

**Materialer/Opgaver:**  
- Opgaver i Node-RED
- Eksporter JSON flow til GitHub

---

## Dag 2: IoT Monitoring (MQTT)
**Emne:** MQTT, telemetri, topics og QoS  
**Indhold:**  
- MQTT broker setup (fx Mosquitto via Docker)
- Forstå topics og payload
- ESP32 publicerer data til MQTT
- Node-RED subscriber til MQTT-data

**Læringsaktiviteter:**  
- Simulere og visualisere sensordata
- Brug Wireshark til at analysere MQTT-trafik

**Materialer/Opgaver:**  
- MQTT flow
- Wireshark capture

---

## Dag 3: REST Kommandoer & Data Storage
**Emne:** REST API, HTTP endpoints, data storage og CRUD  
**Indhold:**  
- Grundlæggende REST koncepter for IoT
- Opsætning af POST/GET endpoints i Node-RED
- Data storage: flow memory, JSON-fil, database (SQLite/InfluxDB)
- CRUD principper i Node-RED
- Integration med eksisterende IoT-systemer og sikkerhed

**Læringsaktiviteter:**  
- Opret POST og GET endpoints for temperaturmålinger
- Gem data i memory, fil og database
- Implementer CRUD-API for devices
- Reflekter over fordele/ulemper ved forskellige lagringsmetoder

**Materialer/Opgaver:**  
- Hands-on opgaver med flow.set(), file-node, SQLite/InfluxDB
- Ekstra: adgangskontrol, backup-rutine, dashboard-integration

**Moduler:**  
1. REST API Grundbegreber  
2. REST Grundbegreber  
3. IoT Data Storage i Skyen  
4. HTTP Endpoints  
5. Actuator Control  
6. Avanceret Data Visualisering  
7. Predictive Analytics for IoT Data  
8. Web Interface  
9. Security  
10. System Integration & Automatisering  

**Den røde tråd:**  
Bygger videre på Node-RED og MQTT, forbereder til integration og sikkerhed.

---

## Dag 4: Home Assistant & Integrering
**Emne:** Integrering af Home Assistant  
**Indhold:**  
- MQTT discovery
- Integration af sensorer og aktuatorer
- Dashboard/visualisering i Home Assistant

**Læringsaktiviteter:**  
- Opsætning af Home Assistant
- Konfiguration af devices via MQTT discovery
- Visning og styring via Lovelace dashboard

**Materialer/Opgaver:**  
- Compose-fil, sample-YAML, test af offline/online status

---

## Dag 5: CoAP & Resource Discovery
**Emne:** Constrained Application Protocol, ressourceopdagelse  
**Indhold:**  
- ESP32 som CoAP-server
- Node-RED CoAP client
- CoAP GET/OBSERVE, resource discovery

**Læringsaktiviteter:**  
- Implementer CoAP endpoints på ESP32
- Gateway-løsning: CoAP til MQTT
- Sammenligning: CoAP vs HTTP/MQTT

**Materialer/Opgaver:**  
- Battery life test, discovery log, opgave om power consumption

---

## Dag 6: Modbus-integration
**Emne:** Gateway mellem Modbus og moderne IoT  
**Indhold:**  
- Modbus TCP opsætning
- Node-RED Modbus integration
- Gateway pattern: Modbus til MQTT

**Læringsaktiviteter:**  
- Læse data fra Modbus-enheder
- Publicere Modbus-data via MQTT

**Materialer/Opgaver:**  
- Node-RED flows til Modbus/MQTT

---

## Dag 7: Netværk & Sikkerhed
**Emne:** VLAN, credentials, TLS, heartbeat-overvågning  
**Indhold:**  
- Netværkssegmentering (fx pfSense)
- Sikkerhedstjek, firewall-rules
- MQTT heartbeat og timeout test

**Læringsaktiviteter:**  
- Sæt pfSense op med flere VLANs
- Test firewall og heartbeat-overvågning
- Security checklist og threat modeling

**Materialer/Opgaver:**  
- GNS3-projekt, checklist, security-diskussion

---

## Dag 8: Mini-projekt
**Emne:** Projektarbejde, integration og demo  
**Indhold:**  
- Mini-projekt: sensor → cloud → visualisering
- Færdiggørelse og præsentation af prototype
- Dokumentation og afsluttende video/demo

**Læringsaktiviteter:**  
- Udarbejde en fuld IoT-løsning i grupper/par
- Dokumentere og præsentere løsningen

**Materialer/Opgaver:**  
- Projekt-canvas, SAT/FAT worksheet, video

---

*Denne plan er et forslag. Indsæt gerne flere detaljer fra de enkelte dag-README hvis du vil have endnu mere præcision!*
