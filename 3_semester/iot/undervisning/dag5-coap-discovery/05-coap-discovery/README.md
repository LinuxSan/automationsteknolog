# 📡 CoAP – 05: Discovery (Teori)

I denne lektion fokuserer vi på, hvordan CoAP-enheder kan gøre deres ressourcer synlige og søgbare via såkaldt "discovery". Dette er særligt vigtigt i dynamiske IoT-netværk, hvor nye enheder skal kunne finde hinanden uden manuel konfiguration.

---

## 🎯 Læringsmål

* Forstå hvad `/.well-known/core` er, og hvordan det bruges
* Læse, forstå og tolke discovery-svar
* Identificere hvordan enheder og klienter kan bruge discovery i praksis

---

## 🔍 Hvad er CoAP Discovery?

Discovery i CoAP foregår typisk via en speciel URI:

```
GET /.well-known/core
```

Denne forespørgsel returnerer en liste over tilgængelige ressourcer på enheden i *link-format* (defineret i [RFC 6690](https://datatracker.ietf.org/doc/html/rfc6690)).

**Eksempel på svar:**

```
</temp>;rt="temperature-c";if="sensor",
</led>;rt="switch";if="actuator"
```

Dette betyder, at enheden har:

* En sensor `/temp` med resource-type `temperature-c`
* En aktuator `/led` med resource-type `switch`

Disse metadata kan bruges af klienter til at finde relevante endpoints automatisk.

---

## 📦 Felter og metadata

| Felt                 | Beskrivelse                                                             |
| -------------------- | ----------------------------------------------------------------------- |
| `</resource>`        | URI-sti til ressourcen                                                  |
| `rt` (resource type) | Beskriver funktionen – fx `temperature`, `switch`                       |
| `if` (interface)     | Angiver om det er en sensor, actuator osv.                              |
| `ct` (content type)  | Angiver datatype – fx `0` for `text/plain`, `50` for `application/json` |

---

## 🧐 Hvorfor er det nyttigt?

* Enheder kan tilføjes uden manuel konfiguration
* Klienter kan opdatere UI baseret på de tilgængelige funktioner
* Støtter automatisering og selvbeskrivende IoT-netværk
* Gør systemet skalerbart og fleksibelt

---

## 🛠 Implementering (ESP32 / Python / Node.js / Node-RED / Home Assistant)

### 🔌 ESP32 (Arduino-style CoAP)

```cpp
coap.server(callback1, "temp");
coap.server(callback2, "led");
coap.discovery("</temp>;rt=\"temperature-c\",</led>;rt=\"switch\"");
```

### 🐍 ESP32 med MicroPython

> Kræver CoAP-serverbibliotek (fx [micropython-coap](https://github.com/danni/micropython-coap))

```python
resources = {
    "/temp": {"rt": "temperature", "value": 22.5},
    "/led": {"rt": "switch", "state": "off"},
}

def handle_discovery():
    links = ",".join([f"<{res}>;rt=\"{data['rt']}\"" for res, data in resources.items()])
    return links
```

### 🐍 Python (aiocoap)

```python
from aiocoap import resource, Message

class CoreResource(resource.Resource):
    async def render_get(self, request):
        payload = b"</temp>;rt=\"temperature\",</led>;rt=\"switch\""
        return Message(payload=payload)
```

### 💡 Node.js (coap)

```javascript
const coap = require('coap');

coap.createServer((req, res) => {
  if (req.url === '/.well-known/core') {
    res.end('</temp>;rt="temperature",</led>;rt="switch"');
  }
}).listen(() => {
  console.log('CoAP server running');
});
```

### 🧱 Node-RED

> Kræver `node-red-contrib-coap`

1. Tilføj en CoAP input-node med metode `GET` og sti `/.well-known/core`
2. Tilføj en Function-node med følgende kode:

```javascript
msg.payload = "</temp>;rt=\"temperature\",</led>;rt=\"switch\"";
return msg;
```

3. Tilføj en CoAP response-node for at sende svaret

Dette tillader dynamisk opsætning af svar baseret på flows eller konfigurationer.

### 🏠 Home Assistant

Home Assistant understøtter ikke CoAP discovery direkte, men der er muligheder:

* Brug **ESPHome** til at eksponere sensorer via MQTT eller API
* Brug en **CoAP→MQTT bro** via fx Node-RED eller Python-script
* Brug `command_line` eller `rest` sensorer kombineret med `coap-client` eller script

Eksempel på indirekte integration via `command_line`:

```yaml
sensor:
  - platform: command_line
    name: "Temp via CoAP"
    command: 'coap-client -m get coap://192.168.1.10/temp'
    scan_interval: 60
```

---

## 🔐 Overvejelser

* Discovery kan slås fra eller begrænses af sikkerhedshensyn
* Overvej hvem der skal kunne se hvilke ressourcer
* Discovery bør ikke returnere følsomme eller administrative ressourcer

---

📌 **CoAP Discovery** er en nøgleteknologi i selvorganiserende IoT-miljøer. Ved at bruge `/.well-known/core` kan både simple og avancerede enheder eksponere deres funktioner uden at kende hinanden på forhånd – ideelt til automatisering og fleksible systemer.
