# 🔐 DAG 7 – Netværkssikkerhed i IoT-systemer

Netværkssikkerhed er en afgørende disciplin i moderne IoT-miljøer, hvor mange enheder kommunikerer åbent over lokale og cloud-baserede netværk. I dette modul lærer du, hvordan man identificerer sårbarheder, overvåger kommunikation og beskytter data mod uautoriseret adgang.

Vi tager udgangspunkt i værktøjer som **Wireshark** og **GNS3**, samt praktiske scenarier med ESP32, Raspberry Pi og softwarebaserede gateways. Fokus er på hands-on øvelser, trusselsforståelse og sikker konfiguration.

---

## 📦 Moduloversigt

| Afsnit | Titel                    | Indhold                                                                   |
| ------ | ------------------------ | ------------------------------------------------------------------------- |
| 01     | Grundlæggende begreber   | OSI-modellen, netværkstyper, pakkestruktur, klartekst vs krypteret trafik |
| 02     | Overvågning og analyse   | Opsætning af Wireshark og GNS3 til at fange og analysere IoT-trafik       |
| 03     | Angreb og sårbarheder    | Typiske angreb (MITM, spoofing, brute force), svagheder i protokoller     |
| 04     | Beskyttelse og hardening | Segmentering, VLAN, VPN, adgangskontrol, sikring af ESP32 og MQTT         |

> 💡 Vi arbejder med realistiske netværksscenarier og simulerede angreb – men altid etisk og kontrolleret.

---

## 🎯 Læringsmål

Efter dette modul kan du:

* Beskrive de vigtigste sikkerhedsudfordringer i IoT-netværk
* Bruge Wireshark til at analysere netværkstrafik og identificere risici
* Opsætte og simulere IoT-netværk i GNS3 med ESP32 eller virtuelle enheder
* Forstå almindelige angrebsvektorer mod IoT-protokoller som MQTT, CoAP og HTTP
* Implementere grundlæggende netværksbeskyttelse: firewall, VLAN, adgangskontrol, TLS

---

## 🛠 Anbefalet software og udstyr

| Værktøj         | Funktion                              |
| --------------- | ------------------------------------- |
| Wireshark       | Pakkesniffer og analyseværktøj        |
| GNS3            | Virtuel netværkssimulering og routing |
| ESP32 / RPi     | Repræsenterer IoT-enheder             |
| Mosquitto       | MQTT-broker til tests og simulation   |
| DNS / DHCP sim. | Angreb via spoofing og redirect       |

---

## 📌 Videre arbejde

I tilhørende opgaver får du mulighed for at:

* Fange og analysere trafik fra ESP32 til en MQTT-broker
* Identificere usikre protokolvalg (fx klartekst MQTT eller HTTP)
* Simulere spoofing eller brute force i GNS3
* Implementere afgrænsning via segmentering og filtrering
* Sammenligne klartekst vs TLS-beskyttet kommunikation i praksis

