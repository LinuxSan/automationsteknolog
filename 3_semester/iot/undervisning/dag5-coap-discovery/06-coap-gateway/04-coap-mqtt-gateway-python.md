# 🧪 CoAP-MQTT Gateway – Python Opgaver

Disse opgaver fokuserer på at opbygge en CoAP-MQTT gateway i Python med brug af `aiocoap` og `paho-mqtt`. Du lærer at oversætte mellem CoAP-ressourcer og MQTT-topics i begge retninger.

---

## 🧩 Opgave 1 – CoAP → MQTT publish

**Formål:** Forespørg en CoAP-ressource og publicér resultat til MQTT

### Trin

1. Installer nødvendige biblioteker:

```bash
pip install aiocoap paho-mqtt
```

2. Opret `coap_to_mqtt.py`:

```python
import asyncio
from aiocoap import Context, Message, GET
import paho.mqtt.client as mqtt

async def main():
    mqtt_client = mqtt.Client()
    mqtt_client.connect("localhost")

    protocol = await Context.create_client_context()
    request = Message(code=GET, uri='coap://localhost/temp')

    response = await protocol.request(request).response
    payload = response.payload.decode('utf-8')
    print("CoAP response:", payload)

    mqtt_client.publish("coap/sensors/temperature", payload)
    mqtt_client.disconnect()

asyncio.run(main())
```

---

## 🧩 Opgave 2 – MQTT → CoAP kommando

**Formål:** Lyt til MQTT og send CoAP PUT-anmodning ved besked

### Trin

1. Opret `mqtt_to_coap.py`:

```python
import asyncio
from aiocoap import *
import paho.mqtt.client as mqtt

async def send_coap(payload):
    context = await Context.create_client_context()
    msg = Message(code=PUT, uri='coap://localhost/led', payload=payload.encode())
    await context.request(msg).response

loop = asyncio.get_event_loop()

def on_message(client, userdata, msg):
    print("MQTT message received:", msg.payload.decode())
    loop.create_task(send_coap(msg.payload.decode()))

mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect("localhost")
mqtt_client.subscribe("commands/device/led")
mqtt_client.loop_start()

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
```

---

## 🔁 Opgave 3 – Dynamisk mapping via JSON-konfiguration

**Formål:** Brug en ekstern konfigurationsfil til at matche CoAP URI'er og MQTT-topics

### Trin

1. Opret `mapping.json`:

```json
{
  "/temp": "coap/sensors/temperature",
  "/led": "commands/device/led"
}
```

2. Indlæs med:

```python
import json
with open("mapping.json") as f:
    mapping = json.load(f)
```

3. Brug mapping i begge retninger i dine scripts

---

## 🔍 Opgave 4 – Ressourceopdagelse og publish

**Formål:** Hent `/.well-known/core`, parse link-format og publicér til MQTT

### Trin

1. Brug aiocoap GET-request til `coap://device/.well-known/core`
2. Parse svar som:

```text
</temp>;rt="temperature",</led>;rt="switch"
```

3. Konverter til JSON og publicér til `coap/discovery` topic

Eksempel:

```json
{
  "resources": [
    {"uri": "/temp", "rt": "temperature"},
    {"uri": "/led", "rt": "switch"}
  ]
}
```

---

## 📊 Opgave 5 – Gateway-status og overvågning

**Formål:** Publicér gatewayens status periodisk til MQTT

### Trin

1. Brug `asyncio.create_task()` til at lave en loop:

```python
import time
while True:
    status = json.dumps({
        "connected": True,
        "uptime": int(time.time())
    })
    mqtt_client.publish("gateway/status", status)
    await asyncio.sleep(30)
```

2. Vis i Home Assistant eller brug Node-RED til overvågning

---

✅ Med disse opgaver kan du bygge en komplet, asynkron gateway i Python, der kan fungere alene eller som mellemled til større IoT-systemer.
