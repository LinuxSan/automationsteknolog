# 🏭 Industrielt Netværk – PLC, Bus & Industriel Integration

*12 × 3 timer • Aarhus Maskinmesterskole • 2025*

> Hands‑on kursus hvor maskinmestre arbejder med industriel netværksopsætning, protokoller, segmentering og fejlfinding – uden at skulle være netværkseksperter fra starten.

---

## 🎯 Læringsmål

Efter forløbet kan du …

1. **Analysere og opbygge industrielle netværk** (topologi, udstyr, VLAN, subnet).
2. **Sætte adresser og fejlfinde på IP‑ og MAC‑niveau** (GNS3/fysisk).
3. **Segmentere og sikre OT‑trafik** vha. VLAN og access control.
4. **Opsætte og forstå centrale OT‑protokoller:**  
   - Profibus, Profinet, IO-Link, EtherNet/IP, Modbus TCP/RTU
5. **Integrere PLC, HMI og robot (UR/AUBO)** via industrielle protokoller.
6. **Fejlfinde på netværk og protokoller** (ping, traceroute, netværksdokumentation).
7. **Dokumentere, visualisere og præsentere netværksopsætning** for andre (diagram, skriftligt, Github).

---

## 📦 Centrale teknologier & værktøjer

| Kategori     | Værktøj / udstyr                        |
| ------------ | --------------------------------------- |
| Netværk      | GNS3, fysisk switch/router, Siemens PLC |
| Simulation   | GNS3, TIA Portal, Node-RED              |
| Industriel HW| Siemens PLC, Rockwell PLC, UR/AUBO      |
| Protokoller  | Profibus, Profinet, IO-Link, Modbus, EtherNet/IP |
| Analyse      | Ping, traceroute, (Wireshark hvis muligt)|
| Visualisering| Node-RED dashboard (kun OT, ikke IoT)   |
| Sikkerhed    | VLAN, Access-lister, Firewall (GNS3)    |
| Versionsstyring | Git / GitHub                          |

---

## 📁 Repo-struktur (eksempel)

```text
industrielt-netvaerk/
├── README.md
├── forloebsplan.md
├── common/
│   ├── netvaerksdiagram-skabeloner/
│   ├── assets/ (billeder, slides, ekstra opgaver)
│
├── dag01-it-netvaerk/
├── dag02-subnet-vlan/
├── dag03-profibus-io-link-teori/
├── dag04-rotation1-profibus-io-link-modbus/
├── dag05-dokumentation/
├── dag06-profinet-ethernetip-teori/
├── dag07-rotation2-profinet-ethernetip/
├── dag08-fejlfinding-sikkerhed/
├── dag09-integration-dokumentation/
├── dag10-visualisering-dataflow/
├── dag11-projektopgaver/
├── dag12-opsamling/
````

> **Bemærk:**
> Hver *dag-mappe* indeholder:
> • *README.md* → mål, ressourcer, opgaver
> • Opgavefiler (.md, evt. pdf/skabelon)
> • Evt. billeder eller netværksdiagrammer
> • Evt. bonus- eller “stretch”-opgaver

---

## 🧩 Moduloversigt

| Modul  | Fokus                        | Centrale teknologier/værktøjer     |
| ------ | ---------------------------- | ---------------------------------- |
| **01** | IT-netværk & IP              | GNS3, ipconfig, netværkstopologi   |
| **02** | Subnet, VLAN, segmentering   | GNS3, routing, ping/traceroute     |
| **03** | Profibus & IO-Link (teori)   | Slides, quiz, case-eksempler       |
| **04** | Rotationsøvelser 1           | Fysisk Profibus/IO-Link/Modbus     |
| **05** | Siemens Opgaver              | Siemens kommunikation              |
| **06** | Profinet & EtherNet/IP       | TIA Portal, GNS3, video/quiz       |
| **07** | Rotationsøvelser 2           | Fysisk/virtuel PLC, UR/AUBO, tags  |
| **08** | Fejlfinding & sikkerhed      | GNS3 firewall/ACL, fejlscenarier   |
| **09** | Integration & dokumentation  | PLC/robot/HMI samspil, rapport     |
| **10** | Visualisering (Node-RED)     | Node-RED dashboard, Modbus, OPC UA |
| **11** | Projektdag                   | Eget projekt, dokumentation        |
| **12** | Opsamling & ekstraopgaver    | Repetition, refleksion             |

---

## ✅ Slutmål

* Du kan bygge, fejlfinde og dokumentere et industrielt netværk med PLC, bus og segmentering.
* Du kan dokumentere og aflevere dine løsninger i GitHub (markdown + billeder).
* Du kan forklare og demonstrere OT-sikkerhed, netværksdesign og protokolvalg for en industriel case.

---

## 🤝 Hjælp & support

Har du brug for hjælp?
👉 Opret et GitHub issue eller spørg underviseren

---

God arbejdslyst – og velkommen til det industrielle netværksunivers! 🏭🦾
