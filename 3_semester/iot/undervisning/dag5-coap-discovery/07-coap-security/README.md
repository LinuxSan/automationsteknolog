# 🔐 CoAP-MQTT Gateway – Security (Teori)

I dette modul fokuserer vi på sikkerhed i forbindelse med CoAP-MQTT gateways. Vi ser på hvordan man kan sikre transport, autentificering og adgangskontrol i gateways, der forbinder ressourcestærke og ressourcestærke enheder.

---

## 🎯 Læringsmål

* Forstå forskellene mellem sikkerhed i CoAP og MQTT
* Forstå hvordan DTLS og TLS sikrer transportlaget
* Kende til metoder for autentificering og adgangskontrol
* Få overblik over typiske trusler og hvordan de håndteres

---

## 🧱 Transportlags-sikkerhed

### CoAP → DTLS (Datagram Transport Layer Security)

* Anvendes oven på UDP (ligesom TLS over TCP)
* Understøtter PSK (Pre-shared key), RPK (Raw Public Key) og certifikater
* Typisk brugt:

  * PSK i embedded devices
  * Certifikatbaseret i gateways

### MQTT → TLS

* Standardiseret som MQTT over TLS (MQTTS)
* Bruges med:

  * Servercertifikat (TLS one-way)
  * Klientcertifikat (TLS mutual)
  * Bruger/kodeord + TLS

### Gateway bridging:

* TLS bruges til MQTT-forbindelsen
* DTLS bruges til CoAP-trafikken (eller klartekst ved udvikling)

---

## 🧾 Autentificering

| Protokol | Metoder                                   |
| -------- | ----------------------------------------- |
| CoAP     | PSK, RPK, certifikat, token (OAuth2 m.m.) |
| MQTT     | Bruger/kodeord, klientcertifikat, token   |

**Gatewayen skal sikre, at:**

* Kun godkendte MQTT-klienter får adgang
* Kun autoriserede CoAP-enheder tilgås og modtages fra
* Tokens eller signaturer kan verificeres hvis anvendt

---

## 🛡 Adgangskontrol

* Whitelisting af CoAP URI'er og MQTT-topics
* Rollebasede adgangsregler:

  * F.eks. kun `sensor-role` må skrive til `coap/sensors/#`
  * `admin-role` må sende til `commands/#`
* Kombination af topic-filters og brugerrettigheder i MQTT-brokere

---

## ⚠ Trusselsbillede og modforanstaltninger

| Trussel              | Modforanstaltning              |
| -------------------- | ------------------------------ |
| Man-in-the-middle    | TLS/DTLS, certifikatvalidering |
| Replay attacks       | Tidsstempler, tokens med udløb |
| Uautoriseret adgang  | Whitelist, rollebaseret ACL    |
| Kompromitteret enhed | Identitetsstyring, overvågning |
| Payload manipulation | Signering, kryptering          |

---

## 🔍 Logging og overvågning

* Gateway bør logge:

  * Auth-forsøg (succes og fejl)
  * Anmodninger og kommandoer (med metadata)
  * Netværksfejl og genforbindelser

* Logs kan publiceres til:

  * MQTT topic: `gateway/log`
  * Ekstern logserver (fx syslog, InfluxDB)

---

## ✅ Sammenfatning

For at bygge en sikker CoAP-MQTT gateway skal man:

* Bruge DTLS og TLS til at beskytte transport
* Kontrollere adgang og roller via MQTT ACL og URI-filtre
* Implementere passende autentificering
* Overvåge og logge hændelser løbende

---

👉 Næste skridt: Implementér sikkerhed i dine egne gateways – se tilhørende opgaver i næste dokument.
