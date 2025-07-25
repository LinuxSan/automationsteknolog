# 🌐 CoAP – 03: Server

Denne lektion fokuserer på, hvordan man implementerer og konfigurerer en CoAP-server, især med fokus på ESP32 eller Python-baserede systemer.

---

## 🎯 Læringsmål

* Forstå hvad der kendetegner en CoAP-server
* Lære at implementere serverfunktionalitet på ESP32 eller i Python
* Tilbyde ressourcer som temperatur, LED, status osv.

---

## 🔌 CoAP-server funktion

En CoAP-server:

* Lytter på port 5683 (UDP)
* Eksponerer ressource-stier (fx `/temp`, `/led`, `/status`)
* Svarer på GET/PUT/POST/DELETE requests

---

## 🧱 Eksempel (ESP32 med Arduino)

```cpp
coap.server(callback, "temp");
coap.server(callbackLED, "led");
coap.start();
```

Her eksponeres to endpoints: `/temp` og `/led`

`callback()` returnerer fx temperatur som tekst:

```cpp
String(tempSensor.read())
```

---

## 🐍 Eksempel (Python med aiocoap)

```python
class TempResource(resource.Resource):
    async def render_get(self, request):
        payload = b"22.7"
        return Message(payload=payload)
```

---

## 🛠 Ressource-design

Tænk REST:

* `GET /temp` → retur temperatur
* `PUT /led` → tænd/sluk LED
* `GET /status` → retur uptime, signalstyrke

Brug korte, logiske URL-stier og tekstbaserede svar eller JSON.

---

## 🔐 Tilgængelighed og sikkerhed

* Brug kun nødvendige endpoints
* Undgå følsom data uden kryptering (brug evt. DTLS)
* Rate-limit forespørgsler hvis nødvendigt

---

## 🧠 Refleksion

* Hvordan adskiller en CoAP-server sig fra en HTTP-server?
* Hvordan strukturerer man letforståelige og stabile endpoints?
* Hvordan skal serveren reagere ved ugyldig request?

---

📌 En CoAP-server gør det muligt for andre enheder at forespørge eller kontrollere data – hurtigt og ressourcebesparende, særligt i begrænsede IoT-miljøer.
