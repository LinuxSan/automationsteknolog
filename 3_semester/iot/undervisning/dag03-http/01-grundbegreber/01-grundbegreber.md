# 🧪 Opgaver – HTTP REST Grundbegreber (Smart House)

Disse opgaver giver dig hands-on erfaring med REST-API'er i et smart home-scenarie. Du vil arbejde med både ESP32, Node-RED og testværktøjer som curl eller Postman.

> 🧠 Fokus: Forstå hvordan HTTP-metoder, endpoints, ressourcer og statuskoder anvendes i praksis.

---

## 🟢 Del 1 – Undersøg et REST API med Postman eller curl

### 🎯 Læringsmål

* Du kan udføre HTTP GET, POST og DELETE requests
* Du forstår hvordan data sendes og modtages via JSON

### 📌 Om curl

`curl` er et kommandolinjeværktøj, der bruges til at sende HTTP-forespørgsler.

**Eksempler:**

```bash
# GET
curl http://localhost:1880/api/lights

# POST
curl -X POST http://localhost:1880/api/lights \
     -H "Content-Type: application/json" \
     -d '{ "room": "kitchen", "state": "on" }'

# DELETE
curl -X DELETE http://localhost:1880/api/lights/kitchen
```

> Du kan bruge dette i terminal, PowerShell eller VS Code terminal.

### 🔧 Opgave

1. Brug en REST-mock-service eller lokal Node-RED HTTP endpoint (fx `http in` node)
2. Send følgende requests:

   * `GET /api/lights`
   * `POST /api/lights` med følgende body:

     ```json
     { "room": "kitchen", "state": "on" }
     ```
   * `DELETE /api/lights/kitchen`
3. Notér statuskoder og responsindhold

💬 Refleksion: Hvad sker der, hvis du prøver at hente en ikke-eksisterende ressource?

---

## 🔵 Del 2 – ESP32 sender temperatur via HTTP POST

### 🎯 Læringsmål

* Du kan sende data fra ESP32 til REST endpoint
* Du forstår hvordan HTTP POST fungerer fra embedded system

### 🔧 Opgave

1. Skriv ESP32-kode (fx Arduino med WiFiClient) som:

   * Måler temperatur (fiktivt eller med sensor)
   * Sender JSON-data som POST til fx `http://<NODE_RED_IP>:1880/api/temperature`
   * Body:

     ```json
     { "sensor": "living_room", "value": 22.5 }
     ```
2. I Node-RED:

   * Brug `http in` + `json` + `debug` til at modtage og vise data

🔍 Test: Skift temperatur og observer ændring i payload

---

## 🟡 Del 3 – Lav din egen REST API i Node-RED

### 🎯 Læringsmål

* Du kan designe endpoints til typiske IoT-funktioner

### 🔧 Opgave

1. Opret følgende endpoints:

   * `GET /api/devices` → returnerer liste over sensorer (som statisk array)
   * `GET /api/devices/:id` → returnerer detaljer for én sensor
   * `POST /api/devices` → tilføjer ny sensor til liste (brug `flow.set` og `flow.get`)
2. Returnér JSON med passende `Content-Type` og statuskode (200, 201, 404)

💬 Refleksion: Hvordan ville en PUT eller DELETE se ud i samme flow?

---

## 🔴 Del 4 – Fejlhåndtering og statuskoder

### 🎯 Læringsmål

* Du kan sende og tolke relevante HTTP-statuskoder

### 🔧 Opgave

1. Tilføj logik i dine `http in` flows som:

   * Returnerer 404 hvis en sensor ikke findes
   * Returnerer 400 hvis input mangler felt
   * Returnerer 201 ved succesfuld oprettelse

2. Brug `http response`-noder med:

```json
msg.statusCode = 404;
msg.payload = { "error": "Not found" };
return msg;
```

💬 Refleksion: Hvorfor er det vigtigt med korrekte statuskoder i systemintegration?

---

## 🧭 Afslutning og overblik

📋 Tjekliste:

* [ ] Har du lavet en fungerende POST fra ESP32?
* [ ] Har du testet GET og DELETE endpoints?
* [ ] Har du brugt JSON korrekt i både ind- og output?
* [ ] Har du returneret relevante statuskoder?

🧠 Ekstra:

* Lav dokumentation (fx README eller swagger-lignende tekst) for dine REST endpoints
* Gør systemet klar til at andre grupper kan bruge dit API
