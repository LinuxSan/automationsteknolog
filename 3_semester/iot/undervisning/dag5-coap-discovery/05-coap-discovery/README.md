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

```text
GET /.well-known/core
```

Denne forespørgsel returnerer en liste over tilgængelige ressourcer på enheden i **link-format** (defineret i RFC 6690).

Eksempel på svar:

```text
</temp>;rt="temperature-c";if="sensor",
/led;rt="switch";if="actuator"
```

Dette betyder, at enheden har:

* En sensor `/temp` med resource-type `temperature-c`
* En aktuator `/led` med resource-type `switch`

Disse metadata kan bruges af klienter til at finde relevante endpoints automatisk.

---

## 📦 Felter og metadata

* `</resource>`: URI-sti til ressourcen
* `rt` (resource type): Beskriver funktionen – fx `temperature`, `switch`
* `if` (interface): Angiver om det er en sensor, actuator osv.
* `ct` (content type): Kan angive datatype – fx `0` for text/plain, `50` for JSON

---

## 🧠 Hvorfor er det nyttigt?

* Enheder kan tilføjes uden manuel konfiguration
* Klienter kan opdatere UI baseret på de tilgængelige funktioner
* Støtter automatisering og selvbeskrivende IoT-netværk
* Gør systemet skalerbart og fleksibelt

---

## 🛠 Implementering (ESP32 / Python)

### ESP32 (Arduino CoAP):

```cpp
coap.server(callback1, "temp");
coap.server(callback2, "led");
coap.discovery("</temp>;rt=\"temperature-c\",</led>;rt=\"switch\"");
```

### Python (aiocoap):

```python
class CoreResource(resource.Resource):
    async def render_get(self, request):
        payload = b"</temp>;rt=\"temperature\",</led>;rt=\"switch\""
        return Message(payload=payload)
```

---

## 🔐 Overvejelser

* Discovery kan slås fra eller begrænses af sikkerhedshensyn
* Overvej hvem der skal kunne se hvilke ressourcer
* Discovery bør ikke returnere følsomme eller administrative ressourcer

---

📌 CoAP Discovery er en nøgleteknologi i selvorganiserende IoT-miljøer. Ved at bruge `/.well-known/core` kan både simple og avancerede enheder eksponere deres funktioner uden at kende hinanden på forhånd – ideelt til automatisering og fleksible systemer.
