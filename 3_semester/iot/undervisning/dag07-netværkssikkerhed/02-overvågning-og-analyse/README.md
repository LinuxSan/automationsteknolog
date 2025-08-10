# 🔎 Netværkssikkerhed – Afsnit 02: Overvågning og analyse

Dette afsnit introducerer praktisk netværksovervågning og analyse med Wireshark. Du lærer at fange trafik fra IoT-enheder, filtrere relevante pakker og identificere potentielle risici i både klartekst- og krypteret kommunikation.

---

## 📡 Hvad er Wireshark?

Wireshark er et grafisk værktøj til analyse af netværkstrafik. Det viser individuelle pakker og giver mulighed for at filtrere og inspicere data på tværs af OSI-lagene.

Typisk brug:

* Undersøge, om data sendes i klartekst
* Identificere enheder og tjenester på netværket
* Fejlsøge kommunikationsproblemer

---

## 🎯 Mål med Wireshark i IoT-sammenhæng

* Analysere MQTT-, CoAP-, HTTP- eller Modbus TCP-trafik
* Filtrere trafik fra specifikke IP-adresser
* Afsløre protokoller uden kryptering
* Se MAC- og IP-adresser for tilsluttede enheder

---

## 🔍 Grundlæggende funktioner i Wireshark

| Funktion           | Beskrivelse                                  |
| ------------------ | -------------------------------------------- |
| Capture Interfaces | Vælg hvilket netværkskort der skal overvåges |
| Packet List        | Visning af alle fangede pakker               |
| Packet Details     | Analyse af enkeltpakkens indhold             |
| Display Filter     | Avanceret søgning i trafikken                |

Eksempler på display filters:

* `ip.addr == 192.168.1.100`
* `mqtt`
* `tcp.port == 502`
* `frame contains "ON"`

---

## ⚠ Typiske faresignaler i trafikken

* Klartekst brugernavne eller passwords
* Følsomme sensordata uden kryptering
* Ukendte forbindelser til eksterne IP’er
* Store mængder data sendt med få sekunders mellemrum

---

## 📘 Mini-case: MQTT-sensor

En ESP32 sender temperaturdata via MQTT til en broker (port 1883). Du fanger trafikken i Wireshark og ser:

* IP: `192.168.1.42 → 192.168.1.10`
* Topic: `sensors/temp`
* Payload: `22.6`

👉 Dette er ukrypteret – enhver med adgang til netværket kan aflæse data.

---

## 🛡 Næste skridt

I næste afsnit ser vi på aktive angreb og typiske sårbarheder – fx spoofing, brute force og MITM (Man-in-the-Middle).
