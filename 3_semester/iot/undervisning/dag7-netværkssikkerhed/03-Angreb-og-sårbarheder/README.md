# ⚠️ Netværkssikkerhed – Afsnit 03: Angreb og sårbarheder

I dette afsnit lærer du om typiske netværksangreb og sårbarheder i IoT-systemer. Du får indsigt i, hvordan angribere kan udnytte svagheder i protokoller og konfigurationer – og hvordan du kan opdage og forstå disse angreb gennem simulering og analyse.

---

## 🛠 Hvad er en sårbarhed?

En sårbarhed er en svaghed i systemet, som kan udnyttes til at påvirke fortrolighed, integritet eller tilgængelighed.

IoT-systemer er ofte sårbare fordi:

* Enheder bruger standardkoder (admin/admin)
* Trafik sendes i klartekst
* Netværket er åbent eller ukontrolleret

---

## 💣 Almindelige netværksangreb

| Type                     | Beskrivelse                                                  | Eksempel i IoT                  |
| ------------------------ | ------------------------------------------------------------ | ------------------------------- |
| MITM (Man-in-the-Middle) | Angriberen opsnapper og evt. ændrer trafik mellem to enheder | Ændrer sensorværdi i farten     |
| Spoofing                 | Enhed udgiver sig for at være en anden                       | ESP32 spoofes som trusted enhed |
| Brute force              | Systematisk gætte adgangskoder                               | MQTT broker med weak password   |
| DoS (Denial of Service)  | Overbelaster enhed/broker med trafik                         | Ubrugelig enhed via flooding    |
| ARP Poisoning            | Forfalskede ARP-opslag leder trafik forkert                  | MITM via gateway-redirect       |

---

## 🔐 Eksempler på svage punkter

* MQTT uden brugernavn/kodeord
* CoAP uden DTLS og frit tilgængeligt /.well-known/core
* ESP32 med åben port 80 og default HTML-login
* Modbus TCP med fuld adgang til registre uden validering

---

## 🔍 Sådan opdages angreb

Med værktøjer som **Wireshark** og **GNS3** kan du:

* Identificere usædvanlig trafikmængde (DoS)
* Spotte ukendte MAC/IP-adresser (spoofing)
* Se hvis pakker ændres undervejs (MITM)
* Kontrollere login-forsøg og brute force-mønstre

> 🧪 I praksismoduler kan du prøve at simulere disse angreb i et kontrolleret testmiljø

---

## 🧠 Hvad bør man gøre?

* Begræns adgang til netværket med whitelist eller MAC-filter
* Brug altid TLS/DTLS hvor det er muligt
* Sørg for, at IoT-enheder ikke bruger standard-koder
* Segmentér netværket, så IoT ikke har direkte adgang til administrative systemer

---

📌 I næste afsnit fokuserer vi på beskyttelse og sikring – hvordan du kan opbygge en sikker netværksarkitektur og konfigurere dine enheder korrekt.
