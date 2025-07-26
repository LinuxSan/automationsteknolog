# 📘 DAG 6 – Modbus TCP Integration

Modbus TCP bruges bredt i industrien som grænseflade mellem intelligente enheder og overordnede systemer. Mange enheder – fx Danfoss VLT, Schneider PowerTag, Carlo Gavazzi, WAGO mv. – eksponerer data via Modbus TCP. I dette modul lærer du at forstå protokollen, oprette klient/server-forbindelser og integrere data i andre systemer.

---

## 📦 Moduloversigt

| Afsnit | Titel         | Indhold                                                                                                 |
| ------ | ------------- | ------------------------------------------------------------------------------------------------------- |
| 01     | Grundbegreber | Adresseområder, registertyper, funktionskoder, forskellen mellem TCP og RTU                             |
| 02     | Server/Client | Praktisk kommunikation mellem Modbus TCP-klient og -server. Vi bruger simulatorer og ESP32 som eksempel |
| 03     | Gateway       | Forstå og bygge TCP ↔ RTU gateways. Node-RED og ESP32 som bro, brugsscenarier                           |

---

## 🎯 Læringsmål

* Forstå Modbus TCP som industri-protokol
* Kunne læse og skrive registre fra fx PowerTags eller Danfoss-enheder
* Oprette klient/server kommunikation og forstå adressering
* Opbygge en gateway fra TCP til Modbus RTU (RS485) og tilbage
* Integrere Modbus TCP-data i moderne systemer (fx Node-RED, MQTT, databases)

---

## 🔎 Teori (Afsnit 01 – Grundbegreber)

### 🔌 Hvad er Modbus TCP?

* Protokol til læsning/skrivning af registre
* Bruger TCP/IP i stedet for RS485 (Modbus RTU)
* Samme funktionskoder som RTU: 01, 02, 03, 04, 05, 06, 16
* Port 502 (standard)

### 📊 Registertyper

| Type  | Navn              | Funktion                     | Kan læses | Kan skrives |
| ----- | ----------------- | ---------------------------- | --------- | ----------- |
| 0xxxx | Coils             | Binære outputs               | ✅         | ✅           |
| 1xxxx | Discrete Inputs   | Binære inputs                | ✅         | ❌           |
| 3xxxx | Input Registers   | Sensorværdier                | ✅         | ❌           |
| 4xxxx | Holding Registers | Variabler (f.eks. setpoints) | ✅         | ✅           |

### 🧠 Adressering

* **Offset 0 vs. 1**: Adresse 40001 kan betyde offset 0 (intern adresse 0) eller offset 1 (vises som 40001)
* **Datatype**: 16-bit words → float og 32-bit kræver kombination af to registre
* **Byte order**: Little-endian vs. big-endian (kan give forkerte værdier!)

---

📌 Læs videre i afsnit 02 for at komme i gang med praktisk opsætning af Modbus TCP-server og klient.

