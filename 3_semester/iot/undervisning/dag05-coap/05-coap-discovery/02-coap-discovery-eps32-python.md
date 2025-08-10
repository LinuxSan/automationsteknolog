# 📘 ESP32 & Python: CoAP Discovery – Opgaver

Dette dokument indeholder praktiske opgaver til implementering af CoAP discovery med **ESP32 (Arduino og MicroPython)** samt **Python (aiocoap)**.

---

## 🧪 Opgave 1 – ESP32 (Arduino) – statisk resource-eksponering

**Formål:** Brug CoAP-server på ESP32 til at eksponere `/temp` og `/led`

### Trin

1. Brug et CoAP-bibliotek (fx `CoAP-simple-library` eller `microcoap`)
2. Implementér statiske CoAP endpoints:

```cpp
coap.server(callback1, "temp");
coap.server(callback2, "led");
coap.discovery("</temp>;rt=\"temperature\",</led>;rt=\"switch\"");
```

3. Test med `coap-client` fra en PC:

```bash
coap-client -m get coap://[ESP32-IP]/.well-known/core
```

---

## 🧪 Opgave 2 – ESP32 med MicroPython – dynamisk discovery

**Formål:** Returnér dynamisk genereret link-format baseret på et Python-dictionary

### Trin

1. Installer MicroPython firmware og uploader et CoAP-server script
2. Brug følgende struktur:

```python
resources = {
    "/temp": {"rt": "temperature", "value": 22.5},
    "/led": {"rt": "switch", "state": "off"},
}

def handle_discovery():
    links = ",".join([f"<{uri}>;rt=\"{meta['rt']}\"" for uri, meta in resources.items()])
    return links
```

3. Sørg for at `/\.well-known/core` ruten returnerer output fra `handle_discovery()`

---

## 🧪 Opgave 3 – Python (aiocoap) – Custom Resource Server

**Formål:** Brug Python til at simulere en CoAP-server med discovery support

### Trin

1. Installer aiocoap:

```bash
pip install aiocoap
```

2. Implementér følgende serverkode:

```python
from aiocoap import resource, Message

class CoreResource(resource.Resource):
    async def render_get(self, request):
        payload = b"</temp>;rt=\"temperature\",</led>;rt=\"switch\""
        return Message(payload=payload)
```

3. Tilføj flere endpoints med `resource.Site()`
4. Test med `coap-client`

---

## 🧪 Opgave 4 – Tilføj metadata og content type

**Formål:** Udvid svaret med `if` og `ct` for bedre selvbeskrivelse

```python
payload = b"</temp>;rt=\"temperature\";if=\"sensor\";ct=0,</led>;rt=\"switch\";if=\"actuator\";ct=0"
```

---

## 💡 Bonus – CoAP Discovery Broker (Python)

**Formål:** Lav en Python-app der spørger flere CoAP-enheder og samler deres discovery-respons

### Trin

1. Brug `aiocoap` som klient
2. Send GET-requests til `/.well-known/core` på en liste af IP’er
3. Saml og vis alle link-format-svar i én samlet struktur

---

✅ Disse opgaver giver træning i både embedded og softwarebaseret CoAP discovery, og de kan nemt udvides med autentificering, Observe eller multicast-discovery.
