# 🧪 Opgaver – CoAP 03: Server

Disse opgaver fokuserer på at oprette og teste en CoAP-server, enten med ESP32 (Arduino) eller med Python (aiocoap).

---

## 🟢 Opgave 1 – Start en simpel CoAP-server

**ESP32 (Arduino IDE):**

1. Installer `CoAP-simple-library`
2. Opret en `coap.server()` med endpoint `/temp`
3. Returnér fast temperatur-værdi eller sensor-læsning
4. Test med CoAP-klient (fx `aiocoap-client` eller Copper)

**Python (aiocoap):**

1. Installer `aiocoap`
2. Opret en `Resource` der svarer med "22.5" på GET `/temp`

✅ *Server svarer korrekt med payload ved GET-anmodning*

---

## 🔵 Opgave 2 – Tilføj flere endpoints

1. Tilføj `/led` endpoint der accepterer PUT-anmodninger

   * ESP32: tænd/sluk GPIO-udgang
   * Python: log ON/OFF i terminalen
2. Test med `aiocoap-client`:

```bash
aiocoap-client -m put coap://<IP>/led -b "ON"
```

3. Bekræft at handlingen sker

✅ *CoAP-server reagerer på PUT og ændrer intern tilstand*

---

## 🟡 Opgave 3 – Returnér JSON-data

1. Lav `/status` endpoint der returnerer:

```json
{ "uptime": 120, "wifi": -65 }
```

2. Parse og vis svaret i Node-RED eller terminal

✅ *Server sender strukturerede data – klient forstår formatet*

---

## 🔁 Opgave 4 – Simulér ugyldige forespørgsler

1. Send GET til ikke-eksisterende endpoint `/xyz`
2. Send POST til endpoint som kun accepterer GET
3. Observer hvordan serveren håndterer fejl (fx kode 4.04 eller 4.05)

✅ *Server returnerer meningsfulde fejlkoder*

---

## 🧠 Refleksion

* Hvordan ville du organisere mange endpoints (naming, formål)?
* Hvilke input-valideringer ville du tilføje?
* Skal enheden logge hvem der tilgår hvilke endpoints?

---

📌 CoAP-servere er fleksible og effektive – men kræver omtanke i design og test. Med disse øvelser har du nu grundlaget for stabile RESTful IoT-tjenester over UDP.
