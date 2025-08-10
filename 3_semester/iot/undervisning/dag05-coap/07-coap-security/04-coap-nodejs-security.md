# 🛡 CoAP – Sikkerhedsopgaver med ESP32 (MicroPython) og simpel Node.js-server

Disse opgaver viser, hvordan en ESP32-enhed kan sende data til en helt enkel Node.js-server – med fokus på adgangskontrol og logning. Der bruges kun Node.js' standardbiblioteker.

---

## 🔐 Opgave 1 – PSK-validering på ESP32 → Node.js

**Formål:** Godkend data baseret på en delt nøgle (PSK).

### ESP32 (MicroPython)

```python
import urequests
psk = "sensorkey123"
headers = {"Authorization": psk}
urequests.post("http://<server-ip>:8080", headers=headers, data="23.5")
```

### Simpel Node.js-server (server.js)

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.method === 'POST') {
    const key = req.headers['authorization'];
    if (key !== 'sensorkey123') {
      console.log('Afvist anmodning fra:', req.socket.remoteAddress);
      res.writeHead(403);
      return res.end();
    }

    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      console.log('Modtaget data:', body);
      res.writeHead(200);
      res.end('OK');
    });
  } else {
    res.writeHead(405);
    res.end();
  }
});

server.listen(8080, () => {
  console.log('Server kører på port 8080');
});
```

---

## 📛 Opgave 2 – Hvidliste af enheder med device\_id

**Formål:** Tillad kun bestemte enheder baseret på et `device_id` i payload.

### ESP32 (MicroPython)

```python
urequests.post("http://<server-ip>:8080", headers=headers, data="device_id=esp01&value=21.7")
```

### Node.js-server (udvidet)

```javascript
const whiteList = ['esp01', 'esp02'];

// i req.on('end'):
const data = new URLSearchParams(body);
const device = data.get('device_id');
if (!whiteList.includes(device)) {
  console.log('Ugyldig enhed:', device);
  res.writeHead(403);
  return res.end();
}
console.log(`${device} måler ${data.get('value')}`);
```

---

## 🔎 Opgave 3 – Log adgangsforsøg til tekstfil

**Formål:** Gem succes og fejl i en logfil.

### Udvid Node.js-server:

```javascript
const fs = require('fs');
function log(event, info) {
  const entry = `[${new Date().toISOString()}] ${event}: ${info}\n`;
  fs.appendFileSync('server_log.txt', entry);
}

// Brug fx:
log('auth_success', req.socket.remoteAddress);
log('auth_fail', req.socket.remoteAddress);
```

---

✅ Disse opgaver viser, hvordan du med få linjer Node.js kan modtage, validere og logge data fra ESP32 – uden brug af eksterne afhængigheder.
