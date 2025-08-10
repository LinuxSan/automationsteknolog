# 🧪 Opgaver – CoAP 04: Client (Node.js version)

Denne udgave viser, hvordan du kan skrive en CoAP-klient i Node.js ved hjælp af biblioteket `coap`. Du lærer at sende GET- og PUT-anmodninger, håndtere svar og integrere med fx ESP32-enheder.

---

## 🟢 Opgave 1 – Opsætning af Node.js miljø

1. Sørg for at Node.js og npm er installeret:

```bash
node -v
npm -v
```

2. Opret en ny projektmappe:

```bash
mkdir coap-client
cd coap-client
npm init -y
```

3. Installer CoAP-biblioteket:

```bash
npm install coap
```

✅ *Projektet er klar til at sende forespørgsler med Node.js*

---

## 🔵 Opgave 2 – Send GET-anmodning

1. Opret en fil `get-temp.js` og indsæt:

```javascript
const coap = require('coap');
const req = coap.request('coap://<ESP32-IP>/temp');

req.on('response', (res) => {
  console.log('Svar:', res.payload.toString());
});

req.end();
```

2. Udskift `<ESP32-IP>` med korrekt IP
3. Kør scriptet:

```bash
node get-temp.js
```

✅ *Du modtager temperatur som svar i terminalen*

---

## 🟡 Opgave 3 – Send PUT-anmodning med payload

1. Opret fil `put-led.js` med:

```javascript
const coap = require('coap');
const req = coap.request({
  hostname: '<ESP32-IP>',
  pathname: '/led',
  method: 'PUT'
});

req.write('{"led": "ON"}');
req.on('response', (res) => {
  console.log('Svar:', res.payload.toString());
});
req.end();
```

2. Test med ESP32 der accepterer `/led` PUT-request

✅ *LED tændes og bekræftelse vises i terminalen*

---

## 🔁 Opgave 4 – Fejlhåndtering og timeout

1. Frakobl ESP32 midlertidigt
2. Kør GET- eller PUT-script og observer:

   * Timeout?
   * Manglende svar?
3. Tilføj fallback:

```javascript
req.setTimeout(3000, () => {
  console.error('Timeout på CoAP-anmodning');
});
```

✅ *Fejl håndteres uden crash – systemet er mere robust*

---

## 🧠 Refleksion

* Hvordan skalerer Node.js sammenlignet med fx Python i CoAP-klientscenarier?
* Hvad kræver det at konvertere et CoAP-svar til noget dashboard-kompatibelt?
* Hvordan ville du integrere Node.js-CoAP med fx en MQTT-broker?

---

📌 Node.js giver stor fleksibilitet til at bygge automatiserede CoAP-klienter og bro-løsninger til dashboards, databaser og meddelelse-tjenester.
