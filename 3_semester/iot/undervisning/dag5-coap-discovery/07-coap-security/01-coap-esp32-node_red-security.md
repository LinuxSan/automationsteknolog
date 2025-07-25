# 🛡 CoAP – Sikkerhedsopgaver med Node-RED og ESP32 (MicroPython)

Disse opgaver viser, hvordan du kan sikre en CoAP-baseret løsning i Node-RED, med fokus på enkel autentificering, adgangskontrol og hændelsesovervågning. Vi bruger ESP32 med MicroPython som eksempel på en CoAP-klient.

---

## 🔐 Opgave 1 – Simuler adgangskontrol med Pre-Shared Key (PSK)

**Formål:** Simulér en enkel form for adgangskontrol baseret på PSK – uden DTLS.

### Trin

1. På ESP32 (MicroPython), send CoAP-lignende HTTP-anmodning:

```python
import urequests
psk = "mysecretkey"
headers = {"Authorization": psk}
urequests.put("http://<node-red-ip>:1880/coap-endpoint", headers=headers, data="42.1")
```

2. I Node-RED:

   * Brug en HTTP-in node med metode `PUT` og URL `/coap-endpoint`
   * Tilføj en Function-node:

```javascript
if (msg.req.headers['authorization'] !== 'mysecretkey') {
    msg.payload = 'Unauthorized';
    msg.statusCode = 403;
    return [null, msg];
}
return [msg, null];
```

* Tilføj en HTTP-response-node og evt. en debug-node for godkendte forespørgsler

---

## 📛 Opgave 2 – Begræns adgang med liste over godkendte enheder

**Formål:** Tillad kun kendte identiteter adgang – baseret på predefineret liste.

### Trin

1. Udvid Function-node med liste over gyldige nøgler:

```javascript
let validKeys = ['sensor123', 'esp1', 'roomnode'];
if (!validKeys.includes(msg.req.headers['authorization'])) {
    msg.payload = 'Forbidden';
    msg.statusCode = 403;
    return [null, msg];
}
return [msg, null];
```

2. Test med forskellige ESP32 enheder, hvor nogle bruger en ugyldig key

---

## 🔎 Opgave 3 – Log hændelser ved godkendelse og afvisning

**Formål:** Overvåg og gem sikkerhedsrelaterede hændelser i Node-RED.

### Trin

1. Udvid Function-node til at tilføje hændelsesmetadata:

```javascript
let log = {
    event: msg.statusCode === 403 ? 'auth_fail' : 'auth_success',
    source_ip: msg.req._req.connection.remoteAddress,
    timestamp: new Date().toISOString()
};
msg.log = log;
return [msg, null];
```

2. Brug en `change`-node til at sætte `msg.payload = msg.log`
3. Send loggen til fx `file` node eller `debug` → gem evt. til filsystem med `file out`

---

## ⚙️ Opgave 4 – Indfør timeout eller frekvensbegrænsning

**Formål:** Beskyt Node-RED mod gentagne anmodninger fra uautoriserede klienter

### Trin

1. I Function-node, log tidspunkt for sidste adgang i `flow.set()` eller `context`
2. Afvis anmodninger, hvis der er mindre end X sekunder siden sidste fra samme IP

Eksempel:

```javascript
let now = Date.now();
let ip = msg.req._req.connection.remoteAddress;
let last = flow.get(ip) || 0;
if (now - last < 5000) {
    msg.payload = 'Too Many Requests';
    msg.statusCode = 429;
    return [null, msg];
}
flow.set(ip, now);
return [msg, null];
```

---

✅ Disse opgaver fokuserer på basal sikkerhed i CoAP-lignende integrationer i Node-RED – uden brug af MQTT eller avanceret gateway-logik. Du lærer at beskytte endpointet med PSK-lignende logik og overvåge adgang lokalt.
