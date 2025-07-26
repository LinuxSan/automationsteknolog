# 🌐 Netværkssikkerhed – Ekstra modul: Analyse og sikring af CoAP-trafik

Dette ekstra modul fokuserer på praktisk analyse og beskyttelse af CoAP-trafik i et IoT-netværk. Du lærer, hvordan man bruger Wireshark til at inspicere CoAP-pakker, og hvordan man beskytter kommunikationen mod indblik udefra.

---

## 🔍 Del 1 – Analyse af ukrypteret CoAP

CoAP (Constrained Application Protocol) bruges i lette IoT-enheder som ESP32. Den kører over UDP (typisk port 5683) og er ofte ukrypteret, hvilket gør den let at opsnappe med værktøjer som Wireshark.

### Eksempel på klartekst-analyse:

1. **Start netværkstrafik** med en ESP32 eller lignende enhed, der sender temperaturdata via CoAP
2. **Start Wireshark** og vælg din aktive netværksinterface
3. Brug filter:

```wireshark
coap
```

4. Find en pakke og analyser:

   * Type: Confirmable (CON) eller Non-confirmable (NON)
   * URI-path: Fx `/temp`, `/led`
   * Payload: Fx `22.7` eller `{"humidity":45}`

> 💡 Du kan læse både URI og payload direkte – data er ikke beskyttet mod aflæsning

---

## 🔐 Del 2 – Beskyttelse med DTLS

DTLS (Datagram Transport Layer Security) er "UDP-versionen" af TLS og bruges til at beskytte CoAP-kommunikation. Det sikrer:

* Kryptering af hele payload og header-felter
* Autentificering mellem klient og server
* Integritet og anti-replay-sikring

### Effekten af DTLS:

Når DTLS er aktiv:

* Wireshark vil **stadig kunne se CoAP-pakkerne**, men **payload er uforståelig**
* URI, metode og eventuelt token vil være krypteret
* Trafik ser ud som "Encrypted Handshake" eller "DTLS Application Data"

---

## 📘 Sammenligning: Ukrypteret vs. sikret CoAP

| Funktion                   | Ukrypteret CoAP | CoAP med DTLS   |
| -------------------------- | --------------- | --------------- |
| Læsbar payload             | Ja              | Nej             |
| URI synlig                 | Ja              | Nej             |
| Risiko for MITM            | Høj             | Lav             |
| Angriber kan sende pakker? | Ja              | Ikke uden nøgle |

> ⚠️ Mange IoT-platforme understøtter stadig ikke DTLS – men det er vigtigt at forstå behovet og alternativerne (fx VPN eller netværkssegmentering)

---

## 🧪 Opgaver

### 🟢 Opgave 1 – Opsnap en CoAP-pakke

1. Start Wireshark og fang trafik fra en ESP32, der svarer på `/temp`
2. Brug filter: `coap`
3. Find og dokumentér:

   * IP-adresser
   * URI-path
   * Payload
   * Bekræft at data er i klartekst

### 🟠 Opgave 2 – Aktiver (eller simuler) DTLS

1. Brug en CoAP-klient/server med DTLS-support (fx aiocoap eller Californium)
2. Fang trafikken i Wireshark
3. Brug filter: `udp.port == 5684`
4. Besvar:

   * Kan du læse URI og payload?
   * Hvordan identificerer du at DTLS er aktivt?

> Alternativ: Brug en reference-pcap fil fra en DTLS-session, hvis du ikke har et DTLS-setup

### 🔵 Opgave 3 – Sammenlign

1. Sammenlign to pakker: én ukrypteret og én krypteret
2. Notér forskelle i:

   * Læsbarhed
   * Header-struktur
   * Wireshark-protokolbeskrivelse

---

📌 Brug denne øvelse til at forstå både sårbarhed og beskyttelse i CoAP-baseret kommunikation. Kombinér med tidligere moduler for fuld sikkerhedsforståelse.
