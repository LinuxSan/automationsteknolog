# 🔐 HTTP REST – Security (Teori)

Dette afsnit handler om, hvordan REST API'er kan sikres mod uautoriseret adgang og manipulation. Du lærer om tokens, adgangskontrol, HTTPS og hvordan man beskytter endpoints – særligt i forbindelse med IoT og automatisering.

---

## 🎯 Læringsmål

* Kende trusler mod REST endpoints
* Forstå hvordan man sikrer REST API'er med nøgler, tokens og HTTPS
* Forstå rollebaseret adgang og begrænsninger

---

## 🛡 Hvorfor skal REST sikres?

REST API'er kan blive misbrugt, hvis de er:

* Tilgængelige for alle
* Uden godkendelse
* Uden kryptering

> Eksempel: En ubeskyttet POST-endpoint kan udløse alarmer, tænde lys eller ændre data uden tilladelse.

---

## 🔐 Autentifikationstyper

| Type           | Beskrivelse                           |
| -------------- | ------------------------------------- |
| API-nøgle      | Lang token, ofte i header eller query |
| Bearer Token   | JWT eller adgangstoken med udløbstid  |
| Basic Auth     | Brugernavn + kode (base64-encoded)    |
| Session Cookie | Bruges i browserbaserede logins       |

Eksempel (curl):

```bash
curl -H "Authorization: Bearer abc123" http://example.com/api/status
```

---

## 🧱 Adgangskontrol (RBAC)

REST endpoints bør understøtte rollebaseret adgang:

* Admin: fuld adgang (POST, DELETE, PUT)
* Bruger: kun GET og egne data
* Gæst: begrænset adgang

Node-RED og HA kan simulere dette med flowlogik eller automatiseringer.

---

## 🔒 HTTPS og TLS

* Uden HTTPS sendes data i klartekst
* TLS sikrer, at kommunikation er krypteret og integritet bevares
* Påkrævet ved adgang udefra eller via internet

Certifikater kan være:

* Selvsigneret (lokale tests)
* Udstedt af CA (produktion, Let’s Encrypt)

---

## 📊 Rate limiting og brute force

* Begræns antallet af requests per IP/time
* Afvis eller sæt ventetid ved overdreven adgang
* Brug middleware eller proxy til at håndtere

---

## 🔍 Logging og audit

* Log alle POST/DELETE-anmodninger
* Gem bruger-ID, tidspunkt, IP og input-data
* Bruges til fejlfinding og sikkerhedsrevision

---

## ⚠ Eksempler på sårbarhed

* Åbne webhooks uden adgangskontrol
* Misbrug af GET til at ændre data (skal være POST/PUT)
* Manglende validering af input (fx JavaScript injection)

---

## 🧠 Refleksion

* Hvad kan en uautoriseret bruger udrette med adgang til dit API?
* Hvornår er HTTPS absolut nødvendigt?
* Hvordan balancerer du sikkerhed med brugervenlighed?

---

📌 REST-sikkerhed handler om at beskytte både data, brugere og systemhandlinger. Med korrekt autentifikation, kryptering og kontrol undgår du utilsigtede hændelser og bevarer tilliden til dit system.
