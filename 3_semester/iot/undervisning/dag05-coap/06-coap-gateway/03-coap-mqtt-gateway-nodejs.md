# 🧪 CoAP-MQTT Gateway – Node.js Opgaver

Disse opgaver fokuserer på at implementere en CoAP-MQTT gateway i Node.js, hvor CoAP-requests og -observationer oversættes til MQTT-publikationer og omvendt.

---

## 🧩 Opgave 1 – Simpel CoAP til MQTT

**Formål:** Forward CoAP-data til MQTT-topic

### Trin

1. Installer nødvendige pakker:

```bash
npm install coap mqtt
```

2. Opret en simpel CoAP-server (`server.js`):

```javascript
const coap = require('coap');
const mqtt = require('mqtt');
const server = coap.createServer();
const client = mqtt.connect('mqtt://localhost');

server.on('request', (req, res) => {
  if (req.method === 'GET' && req.url === '/temp') {
    const temp = '22.5';
    res.end(temp);
    client.publish('coap/sensors/temperature', temp);
  }
});

server.listen(() => console.log('CoAP server running'));
```

---

## 🧩 Opgave 2 – MQTT til CoAP (kommandoer)

**Formål:** Send MQTT-kommando som CoAP PUT-anmodning

### Trin

1. Opret ny fil `mqtt2coap.js`

```javascript
const mqtt = require('mqtt');
const coap = require('coap');
const client = mqtt.connect('mqtt://localhost');

client.on('connect', () => {
  client.subscribe('commands/device/led');
});

client.on('message', (topic, message) => {
  const req = coap.request({
    hostname: 'localhost',
    pathname: '/led',
    method: 'PUT'
  });

  req.write(message.toString());
  req.end();
});
```

2. Kør både CoAP-server og MQTT-to-CoAP bridge

---

## 🔁 Opgave 3 – Dynamisk mapping med JSON

**Formål:** Konverter mellem URI og topic ud fra en configfil

### Trin

1. Opret `mapping.json`:

```json
{
  "/temp": "coap/sensors/temperature",
  "/led": "commands/device/led"
}
```

2. Indlæs og brug denne i både server og bridge:

```javascript
const fs = require('fs');
const mapping = JSON.parse(fs.readFileSync('./mapping.json'));
```

3. Brug `Object.entries()` eller `Object.keys()` til at slå op

---

## 🔍 Opgave 4 – Resource discovery

**Formål:** Parse `/.well-known/core` og publicer til MQTT

### Trin

1. Send GET til `coap://device/.well-known/core`
2. Parse link-format til JSON:

```javascript
<temp>;rt="temperature",<led>;rt="switch"
```

3. Publicer som JSON til fx `coap/discovery`

---

## 📊 Opgave 5 – Overvågning og status-topic

**Formål:** Publicer gatewayens status løbende

### Trin

1. Hver 30 sekunder, publicér til `gateway/status`:

```json
{
  "connected": true,
  "coap_alive": true,
  "mqtt_alive": true,
  "uptime": 120
}
```

2. Brug `setInterval()` og `Date.now()`
3. Tilføj genopkoblingsstrategi hvis forbindelser fejler

---

✅ Disse opgaver giver en komplet CoAP↔MQTT gateway i Node.js, som kan bruges standalone eller sammen med fx Home Assistant og andre MQTT-klienter.
