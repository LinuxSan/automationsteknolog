# 🌐 CoAP – Moduloversigt og Introduktion

Dette modul giver en samlet introduktion til, hvordan CoAP (Constrained Application Protocol) bruges i praksis på ESP32, i Python, Node.js, Node-RED og Home Assistant. Fokus er på:

* Praktisk kommunikation mellem enheder
* Simpel klient- og serveropsætning
* Discovery og selvbeskrivelse
* Letvægts sikkerhedsforanstaltninger (PSK, whitelisting)

Modulet samler teori, eksempler og opgaver på tværs af platforme for at give dig et fuldt billede af CoAP i IoT.

---

## 🎯 Læringsmål

* Forstå CoAP’s rolle i IoT-systemer
* Opsætte en CoAP-server og -klient på ESP32 og i Python
* Forstå forskelle og fordele ift. HTTP og MQTT
* Arbejde med ressourceopdagelse og payloadstruktur
* Eksperimentere med sikkerhedsstrategier som PSK og whitelisting
* Integrere CoAP med platforme som Node-RED og Home Assistant

---

## 🔄 Oversigt over indhold

| Lektion | Titel                      | Kort beskrivelse                                                                      |
| ------- | -------------------------- | ------------------------------------------------------------------------------------- |
| CoAP 01 | Grundbegreber              | Hvad er CoAP, hvordan virker det, og hvordan adskiller det sig fra HTTP?              |
| CoAP 02 | ESP32 + Node-RED           | Kommunikation mellem CoAP-server på ESP32 og CoAP-klient i Node-RED.                  |
| CoAP 03 | Server                     | Opsætning af en CoAP-server i ESP32 og Python, og design af endpoints.                |
| CoAP 04 | Klient                     | Hvordan man bygger en klient til at læse og skrive CoAP-ressourcer.                   |
| CoAP 05 | Discovery                  | Hvordan man bruger /.well-known/core til dynamisk at finde enhedens ressourcer.       |
| CoAP 06 | Praktiske serversider      | Simpel datamodtagelse i Python/Node.js uden framework – simuleret CoAP-kommunikation. |
| CoAP 07 | Sikkerhed (PSK og kontrol) | PSK, whitelisting, logning og rate-limiting – uden DTLS.                              |

---

## 🧱 Platforme du arbejder med

* **ESP32 (MicroPython og Arduino)**: Sensor- og aktuatorkommunikation
* **Python**: Servere og klienter med aiocoap eller rå socket-servere
* **Node.js**: Letvægtsservere til test og logik
* **Node-RED**: Visualisering og dataflow uden kode
* **Home Assistant**: Integration og visualisering i smart home miljø

---

## 🔐 Hvad med sikkerhed?

I dette modul introduceres CoAP-sikkerhed trin for trin:

* PSK-baseret identifikation (delt nøgle i header)
* Whitelisting af device\_id
* Logning og begrænsning af gentagne adgangsforsøg
* (Avanceret) kryptering og DTLS er nævnt, men ikke påkrævet

Alt dette foregår med **simpel kode og uden eksterne biblioteker**.

---

## 🧠 Refleksionspunkter

* Hvornår er CoAP mere egnet end HTTP eller MQTT?
* Hvordan bygger man RESTful endpoints med minimal kode?
* Hvilke sikkerhedsforanstaltninger er realistiske i små enheder?
* Hvordan kan man kombinere discovery og automatisering?

---

📌 Dette modul giver dig et komplet praksisbaseret overblik over CoAP i edge devices og lokale netværk. Du får hands-on erfaring med både klient- og serverkode, samt mulighed for at tilføje kontrol, discovery og let sikkerhed. Klar til at gå videre med opgaverne?

