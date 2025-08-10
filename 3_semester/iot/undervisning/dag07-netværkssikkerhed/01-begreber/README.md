# 🔐 Netværkssikkerhed – Afsnit 01: Grundlæggende begreber

Dette afsnit introducerer de centrale koncepter, du skal kende for at forstå og arbejde med netværkssikkerhed i praksis – særligt i forbindelse med IoT. Vi ser på, hvordan data bevæger sig gennem netværket, og hvor sårbarheder opstår.

---

## 🌐 OSI-modellen – Hvor opstår sikkerhed?

OSI-modellen opdeler netværkskommunikation i 7 lag. Sikkerhedsmekanismer og sårbarheder kan findes i flere af disse:

| Lag | Navn                  | Relevans for sikkerhed                     |
| --- | --------------------- | ------------------------------------------ |
| 1   | Fysisk                | Aflytning, signalforstyrrelse              |
| 2   | Datalink              | MAC-spoofing, VLAN-hopping                 |
| 3   | Netværk               | IP-spoofing, routing-angreb                |
| 4   | Transport             | Portscanning, TCP hijacking, DoS           |
| 5-7 | Session → Applikation | Uautoriseret adgang, klartekst-protokoller |

🔎 Eksempel: MQTT, CoAP og HTTP arbejder primært i lag 7 og kræver applikationslagets sikkerhed (fx TLS, tokens, autentificering).

---

## 🔓 Klartekst vs. krypteret trafik

**Klartekst:**

* Kan aflæses direkte i pakkedata (fx brugernavne, sensordata)
* Protokoller: HTTP, MQTT (uden TLS), Modbus TCP

**Krypteret:**

* Beskyttet med TLS/SSL eller lignende mekanismer
* Protokoller: HTTPS, MQTTS, DTLS, SSH

> ⚠️ Mange IoT-enheder sender stadig data i klartekst – nemt at opsnappe med fx Wireshark

---

## 🔁 Trafiktyper og protokoller

| Protokol   | Bruges til            | Typisk sårbarhed                 |
| ---------- | --------------------- | -------------------------------- |
| HTTP       | Webkommunikation      | Klartekst, cookie hijacking      |
| MQTT       | IoT publish/subscribe | Ingen kryptering som standard    |
| CoAP       | RESTful IoT over UDP  | Ingen kryptering uden DTLS       |
| Modbus TCP | Industriel automation | Ingen autentificering/kryptering |
| DNS        | Navneopslag           | Spoofing, cache poisoning        |

---

## 🧠 Begreber du skal kende

* **MAC-adresse:** Unik identifikation på lag 2 – kan forfalskes
* **IP-adresse:** Adressering på netværkslaget – kan spoofes
* **Portnummer:** Bruges til at adressere services (fx 80 = HTTP)
* **Firewall:** Filtrerer trafik mellem netværkszoner
* **VLAN:** Segmenterer netværket logisk – hjælper med adskillelse
* **ARP:** Opløser IP → MAC. Kan udnyttes til MITM-angreb

---

## ✅ Check dig selv

* Kan du forklare, hvad der menes med "klartekstprotokol"?
* Ved du hvilke lag i OSI-modellen, hvor sikkerhed er vigtig?
* Kan du nævne en almindelig sårbarhed for IoT-enheder?

📌 Klar til næste afsnit? Vi skal bruge Wireshark og GNS3 til at analysere trafik og afsløre potentielle problemer i praksis.
