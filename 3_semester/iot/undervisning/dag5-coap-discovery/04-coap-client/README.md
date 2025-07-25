# 🌐 CoAP – 04: Client

Denne lektion fokuserer på at bygge en CoAP-klient, der kan anmode om data eller sende kommandoer til en CoAP-server – fx en ESP32 eller cloud-baseret ressource.

---

## 🎯 Læringsmål

* Forstå hvordan en CoAP-klient fungerer
* Implementere klient i Python og på ESP32
* Håndtere svar, fejl og UDP-pakker korrekt

---

## 🤖 CoAP-klient funktion

En CoAP-klient:

* Sender forespørgsler til specifikke ressourcer (URI)
* Vælger metode: GET, PUT, POST, DELETE
* Modtager svar og fortolker dem
* Styrer retransmissioner og timeouts (især for CON-pakker)

---

## 🐍 Python eksempel (aiocoap)

```python
from aiocoap import *
import asyncio

async def main():
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri='coap://192.168.1.100/temp')
    response = await protocol.request(request).response
    print('Result:', response.payload.decode())

asyncio.run(main())
```

---

## 🔌 ESP32 eksempel (Arduino CoAP)

```cpp
coap.put(IPAddress(192,168,1,50), 5683, "led", "ON");
```

ESP32 sender en PUT-anmodning til en anden enhed.

---

## 📟 Klientens ansvar

* Kunne retry ved tabt pakke (UDP er ikke garanteret)
* Kende endpoint-format (fx `/temp`, `/led`)
* Forstå og validere serverens svar (tekst, JSON, binær)

---

## 🧠 Refleksion

* Hvordan tester du klientens adfærd ved netværksfejl?
* Hvad sker der hvis serveren ikke svarer?
* Hvordan skalerer CoAP-klienter sammenlignet med MQTT-subscribers?

---

📌 CoAP-klienter er lette og effektive – men kræver ansvarlig håndtering af UDP-kommunikation og korrekt brug af RESTful principper.
