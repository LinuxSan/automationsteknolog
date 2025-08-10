# 📘 DAG 6 – Modbus TCP Integration

Modbus TCP bruges bredt i industrien som grænseflade mellem intelligente enheder og overordnede systemer. Mange enheder – fx Danfoss VLT, Schneider PowerTag, Carlo Gavazzi, WAGO mv. – eksponerer data via Modbus TCP. I dette modul lærer du at forstå protokollen, oprette klient/server-forbindelser og integrere data i andre systemer.

Modulet har fokus på praktiske integrationer med Node-RED, ESP32 og Home Assistant, og du lærer at arbejde med Modbus-data i konteksten af visualisering, automation og netværksintegration.

Vi lægger vægt på hands-on aktiviteter, hvor du lærer at aflæse og skrive værdier til faktiske enheder – med særligt fokus på datatyper, registerforståelse og pålidelig kommunikation. For mere erfarne deltagere introduceres Python og Node.js til avanceret brug.

---

## 🎯 Læringsmål

* Forstå Modbus TCP som industri-protokol
* Kunne læse og skrive registre fra fx PowerTags eller Danfoss-enheder
* Oprette klient/server kommunikation og forstå adressering
* Få kendskab til forskellen mellem TCP og RTU (uden at arbejde direkte med RTU)
* Integrere Modbus TCP-data i moderne systemer (fx Node-RED, MQTT, Home Assistant)

---

## 🧠 Afsnit 01 – Grundbegreber

### 🔌 Hvad er Modbus TCP?

Modbus TCP er en netværksbaseret version af Modbus-protokollen. Den bruges til kommunikation mellem master (klient) og slave (server) over Ethernet ved brug af TCP/IP. Den er velegnet til moderne industrielle netværk, hvor data skal transporteres effektivt og uden de fysiske begrænsninger ved seriel kommunikation.

### 🧱 Modbus TCP vs. Modbus RTU

| Egenskab      | Modbus TCP        | Modbus RTU          |
| ------------- | ----------------- | ------------------- |
| Transport     | TCP/IP (Ethernet) | RS485 (seriel)      |
| Adresseformat | IP + Unit ID      | Slave ID            |
| Netværkstype  | LAN               | Punkt-til-punkt/bus |
| Fejlkontrol   | TCP checksum      | CRC                 |

> RTU er stadig udbredt i feltudstyr, men Modbus TCP bruges oftest som interface til overordnede systemer.

### 📊 Registertyper og adresser

Modbus arbejder med faste adresser og registertyper. Hver type har et bestemt formål og understøtter forskellige operationer:

| Registertype      | Præfix | Beskrivelse               | Læs | Skriv |
| ----------------- | ------ | ------------------------- | --- | ----- |
| Coils             | 0xxxx  | Digitale outputs (on/off) | ✅   | ✅     |
| Discrete Inputs   | 1xxxx  | Digitale inputs           | ✅   | ❌     |
| Input Registers   | 3xxxx  | Analoge inputs (sensorer) | ✅   | ❌     |
| Holding Registers | 4xxxx  | Analoge outputs/data      | ✅   | ✅     |

Adressering afhænger af software og kan være **0-baseret** eller **1-baseret**. Eksempel: adresse 40001 kan internt være offset 0.

### ⚙️ Funktionkoder

Funktionkoder afgør hvad klienten beder serveren om:

| Funktion | Navn                     | Beskrivelse             |
| -------- | ------------------------ | ----------------------- |
| 01       | Read Coils               | Læs digitale outputs    |
| 02       | Read Discrete Inputs     | Læs digitale inputs     |
| 03       | Read Holding Registers   | Læs analoge data/output |
| 04       | Read Input Registers     | Læs sensordata          |
| 05       | Write Single Coil        | Skriv digitalt output   |
| 06       | Write Single Register    | Skriv ét register       |
| 16       | Write Multiple Registers | Skriv flere registre    |

### 🧠 Vigtige begreber

* **Unit ID**: bruges i gateways til at identificere RTU-enheder bag TCP
* **Endian**: byte-rækkefølge er vigtigt ved 32-bit og float (little vs. big endian)
* **Datatyper**: Modbus bruger 16-bit words. Alt større (fx float) kræver to registre
* **Timeouts**: Klienten må håndtere manglende svar eller ugyldige adresser

---

## 🛠 Kompetencer efter dette modul

Efter gennemført modul kan deltageren:

* Forklare forskellen på Modbus TCP og RTU på et grundlæggende niveau
* Analysere registertabeller og identificere relevante adresser og datatyper
* Opsætte og teste kommunikation mellem klient og server i et Modbus TCP-netværk
* Bruge værktøjer som Node-RED, ESP32 eller Home Assistant til at afprøve forbindelser
* Forstå principperne bag gateway-funktionalitet (uden at implementere RTU-kommunikation)
* Fejlsøge almindelige problemer som forkerte adresser, timeout og byte order
* Forstå hvordan Modbus TCP indgår som interface i hybride eller proprietære systemer

---

📌 Læs videre i afsnit 02 for at komme i gang med praktisk opsætning af Modbus TCP-server og klient.
