# 💡 Node.js: CoAP Discovery – Opgaver

Disse opgaver fokuserer på at implementere en CoAP-server og client i Node.js med støtte for discovery via `/.well-known/core`. Vi anvender `coap`-modulet fra npm.

---

## 🧪 Opgave 1 – Simpel CoAP-server med discovery

**Formål:** Implementér en statisk CoAP-server med `/temp`, `/led` og `/.well-known/core`

### Trin

1. Installer coap-modulet:

```bash
npm install coap
```

2. Opret en fil `server.js` med følgende:

```javascript
const coap = require('coap');
const server = coap.createServer();

server.on('request', (req, res) => {
  if (req.url === '/.well-known/core') {
    res.end('</temp>;rt="temperature",</led>;rt="switch"');
  } else if (req.url === '/temp') {
    res.end('23.1');
  } else if (req.url === '/led') {
    res.end('off');
  } else {
    res.code = '4.04';
    res.end();
  }
});

server.listen(() => console.log('CoAP server running'));
```

3. Test med `coap-client`:

```bash
coap-client -m get coap://localhost/.well-known/core
```

---

## 🧪 Opgave 2 – Dynamisk discovery via array

**Formål:** Generer link-format ud fra registrerede ressourcer i en struktur

### Trin

1. Tilføj dette array:

```javascript
const resources = [
  { uri: '/temp', rt: 'temperature' },
  { uri: '/led', rt: 'switch' }
];
```

2. I `/.well-known/core` håndtering:

```javascript
const links = resources.map(r => `<${r.uri}>;rt="${r.rt}"`).join(',');
res.end(links);
```

---

## 🧪 Opgave 3 – Client der læser discovery fra en anden enhed

**Formål:** Brug Node.js som CoAP-klient til at hente og parse discovery-data fra en anden CoAP-server

### Trin

1. Lav en ny fil `client.js`:

```javascript
const coap = require('coap');
const req = coap.request('coap://192.168.1.50/.well-known/core');

req.on('response', res => {
  console.log('Discovery response:', res.payload.toString());
});

req.end();
```

2. Udvid med parsing af `res.payload.toString()` til at vise hver ressource separat

---

## 💡 Bonus – Tilføj metadata (if/ct) og parse som JSON

**Ekstra**

1. Udvid hvert resource-objekt i arrayet med `if` og `ct`:

```javascript
{ uri: '/temp', rt: 'temperature', if: 'sensor', ct: '0' }
```

2. Tilpas `links`-generationen:

```javascript
const links = resources.map(r => `<${r.uri}>;rt="${r.rt}";if="${r.if}";ct="${r.ct}"`).join(',');
```

---

✅ Disse opgaver dækker både server- og klientperspektiv i Node.js med CoAP – og lægger fundamentet for bridges, parsere og dynamiske løsninger.
