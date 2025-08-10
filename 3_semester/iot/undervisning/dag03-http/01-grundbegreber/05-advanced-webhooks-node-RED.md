# 🧩 Tillæg – Node-RED og Webhooks (Step-by-Step Guide)

Dette dokument forklarer, hvordan du bruger **webhooks i Node-RED** – URL-baserede endpoints som eksterne systemer kan kalde via HTTP for at udløse handlinger i dine flows.

---

## 🎯 Hvad er en webhook?

En webhook er et HTTP-endpoint, der fungerer som en "omvendt API":
- I stedet for at dit system spørger efter data (polling)
- Lytter systemet efter indkommende kald fra eksterne tjenester
- Når kaldet modtages, udføres en handling i dit Node-RED flow

Dette giver en mere effektiv, event-drevet arkitektur.

---

## 🔧 Trin 1 – Opret et simpelt webhook til at tænde en lampe

### 1A: Opret HTTP-indgangspunktet

1. **Åbn Node-RED** i din browser (typisk http://localhost:1880 eller din Raspberry Pi's IP-adresse)
2. **Tilføj en HTTP in-node**:
   * Træk en `http in` node fra venstre sidepanel til dit workspace
   * Dobbeltklik på noden for at konfigurere den
   * Indstil **Method** til "POST"
   * Indtast **URL** som "/webhook/lamp_on"
   * Sæt **Name** til "Tænd lampe webhook"
   * Klik på **Done** for at gemme konfigurationen

### 1B: Tilføj behandlingslogik

1. **Tilføj en function-node**:
   * Træk en `function` node til dit workspace
   * Forbind den til din HTTP in-node
   * Dobbeltklik for at konfigurere
   * Indtast følgende kode:
     ```javascript
     // Forbered besked til at tænde lampe
     msg.payload = { payload: true };
     // Tilføj tidsstempel
     msg.timestamp = new Date().toISOString();
     // Log i Node-RED
     node.log("Webhook kaldt - tænder lampe");
     return msg;
     ```
   * Navngiv noden "Forbered lampe-kommando"
   * Klik på **Done**

### 1C: Tilføj en udgangsnode

Afhængigt af dit setup, vælg én af følgende:

**For MQTT:**
1. Træk en `mqtt out` node til dit workspace
2. Forbind den til function-noden
3. Konfigurer med dit broker og emne (fx "home/light/livingroom/set")

**For Home Assistant:**
1. Træk en `call service` node til (kræver Home Assistant-integration)
2. Konfigurer til at kalde "light.turn_on"
3. Vælg din enhed i "Entity ID"

**For simulering (test):**
1. Træk en `debug` node til dit workspace
2. Indstil til at vise "msg.payload"
3. Navngiv den "Lampe tændt (simulering)"

### 1D: Tilføj HTTP-svar

1. **Tilføj en HTTP response-node**:
   * Træk en `http response` node til dit workspace
   * Forbind den til function-noden (eller til udgangsnoden via en ekstra wire)
   * Dobbeltklik for at konfigurere
   * Indstil **Status code** til "200: OK"
   * Valgfrit: Tilføj header "Content-Type" = "application/json"
   * Klik på **Done**

2. **Alternativt, brug en function-node til at skabe et tilpasset svar**:
   ```javascript
   msg.statusCode = 200;
   msg.payload = { 
       status: "success", 
       message: "Lampe tændingskommando sendt",
       timestamp: new Date().toISOString()
   };
   return msg;
   ```

### 1E: Deploy dit flow

1. Klik på den røde **Deploy** knap i øverste højre hjørne
2. Bekræft at status viser "Successfully deployed"

---

## 🔧 Trin 2 – Test dit webhook

### 2A: Test med curl fra terminal

1. Åbn en terminal på din computer
2. Kør følgende kommando (erstat med din Node-RED IP):
   ```bash
   curl -X POST http://localhost:1880/webhook/lamp_on
   ```
3. Du bør se et succesfuldt svar, fx: `{"status":"success","message":"Lampe tændingskommando sendt","timestamp":"2025-08-10T08:40:12.345Z"}`
4. Tjek din debug-fane i Node-RED for at verificere at flowet blev aktiveret

### 2B: Test med Postman (alternativ)

1. Åbn Postman eller en lignende HTTP-klient
2. Konfigurer en ny POST-request til `http://localhost:1880/webhook/lamp_on`
3. Klik på "Send" knappen
4. Bekræft at du modtager et 200 OK svar

---

## 🔧 Trin 3 – Udvid dit webhook til at modtage data

### 3A: Skab et mere avanceret webhook

1. **Tilføj en ny HTTP in-node**:
   * Konfigurer med Method: POST
   * URL: `/webhook/device_control`
   * Name: "Enhedskontrol webhook"

2. **Tilføj en JSON parser**:
   * Træk en `json` node til dit workspace
   * Forbind den til din nye HTTP in-node
   * Dette sikrer at indkommende JSON-data bliver konverteret korrekt

3. **Tilføj en switch-node til at håndtere forskellige enheder**:
   * Træk en `switch` node til dit workspace
   * Forbind den til json-noden
   * Konfigurer til at tjekke `msg.payload.device`:
     * Første regel: `==` `lamp`
     * Anden regel: `==` `fan`
     * Tredje regel: `==` `thermostat`
     * Tilføj en "otherwise" regel for ukendte enheder

4. **Tilføj function-noder for hver enhedstype**:
   * Opret separate function-noder for hver enhed
   * Eksempel for lampe:
     ```javascript
     const action = msg.payload.action || "toggle";
     const brightness = msg.payload.brightness || 255;
     
     if (action === "on" || action === "toggle") {
         msg.payload = { 
             state: "on",
             brightness: brightness
         };
     } else if (action === "off") {
         msg.payload = { state: "off" };
     }
     
     return msg;
     ```

5. **Tilføj udgangsnoder for hver enhedstype**

6. **Tilføj en samlet HTTP response-node**:
   * Forbind alle grene tilbage til én HTTP response-node
   * Alternativt: Brug separate function-noder til at skabe skræddersyede svar for hver enhedstype

### 3B: Test med JSON data

Test dit avancerede webhook med curl:
```bash
curl -X POST http://localhost:1880/webhook/device_control \
     -H "Content-Type: application/json" \
     -d '{"device":"lamp","action":"on","brightness":200}'
```

---

## 🔒 Trin 4 – Sikkerhedsforanstaltninger

### 4A: Tilføj simpel token-autentificering

1. **Opdater dit flow med en function-node til autentificering**:
   * Indsæt denne node mellem HTTP in og din behandlingslogik
   * Kodeeksempel:
     ```javascript
     const expectedToken = "din_hemmelige_token_abc123xyz";
     
     // Tjek header for token
     const authHeader = msg.req.headers["authorization"];
     if (authHeader && authHeader === `Bearer ${expectedToken}`) {
         // Token er korrekt, fortsæt flow
         return msg;
     }
     
     // Alternativt, tjek query parameter
     const queryToken = msg.req.query.token;
     if (queryToken && queryToken === expectedToken) {
         return msg;
     }
     
     // Ingen valid token fundet
     msg.statusCode = 401;
     msg.payload = { error: "Unauthorized" };
     return [null, msg];  // Send til anden udgang (fejl)
     ```
   * Tilføj to udgange fra denne node
   * Forbind første udgang til dit normale flow
   * Forbind anden udgang direkte til HTTP response

2. **Test med token**:
   ```bash
   curl -X POST http://localhost:1880/webhook/lamp_on \
        -H "Authorization: Bearer din_hemmelige_token_abc123xyz"
   ```

### 4B: Skjul webhook-sti

1. **Brug en kompliceret, tilfældig URL-sti**:
   * Ændr `/webhook/lamp_on` til noget som `/api/v1/hooks/lamp/a7f3d9e2c6b5`
   * Jo længere og mere tilfældig sti, jo sværere er den at gætte

2. **Opdater alle test-kald med den nye sti**

### 4C: Begræns adgang via netværk

1. Konfigurer din router til kun at tillade lokalt netværk adgang til Node-RED
2. Eller brug en reverse proxy (som Nginx) med IP-begrænsning
3. Du kan også tilføje IP-tjek i din function-node:
   ```javascript
   const allowedIPs = ["192.168.1.100", "192.168.1.101"];
   const clientIP = msg.req.ip || msg.req.connection.remoteAddress;
   
   if (!allowedIPs.includes(clientIP)) {
       msg.statusCode = 403;
       msg.payload = { error: "Forbidden" };
       return [null, msg];  // Send til fejl-udgang
   }
   
   return msg;  // IP er godkendt, fortsæt flow
   ```

---

## 🌐 Trin 5 – Integrer med eksterne tjenester

### 5A: Opsæt Node-RED til at modtage GitHub webhooks

1. **Opret et nyt GitHub webhook**:
   * Gå til dit GitHub repository
   * Gå til Settings > Webhooks > Add webhook
   * Indtast din Node-RED webhook URL (bemærk: GitHub kræver offentlig adgang)
   * Vælg "Just the push event"
   * Sæt Content type til "application/json"
   * Klik på "Add webhook"

2. **Opret et Node-RED flow til at håndtere GitHub events**:
   * HTTP in node: POST til `/webhook/github`
   * Function node til at analysere GitHub payload:
     ```javascript
     // Tjek for GitHub signature hvis du bruger en secret
     // Analysér push event
     const repo = msg.payload.repository.name;
     const branch = msg.payload.ref.split('/').pop();
     const commits = msg.payload.commits.length;
     
     msg.payload = {
         event: "push",
         repository: repo,
         branch: branch,
         commits: commits,
         sender: msg.payload.sender.login
     };
     
     return msg;
     ```
   * Forbind til relevante udgangsnoder (fx send besked, email, etc.)

### 5B: Integrer med IFTTT

1. **Opret en IFTTT applet**:
   * Vælg en trigger (fx en knap, vejrændring, etc.)
   * For action, vælg "Webhook" service
   * Indtast din Node-RED webhook URL
   * Vælg method "POST" og content type "application/json"
   * Tilføj data som IFTTT skal sende

2. **Opret et Node-RED flow til at håndtere IFTTT events**:
   * HTTP in node: POST til `/webhook/ifttt`
   * JSON parser node
   * Switch eller function noder baseret på indkommende data

---

## 🧠 Refleksion

* **Forskellen mellem webhooks og traditionelle REST endpoints**:
  * Webhooks er event-drevne og initieres af eksterne systemer
  * REST endpoints følger typisk request-response modellen og initieres af klienten
  * Webhooks reducerer behovet for polling og skaber mere realtids-responsiv adfærd

* **Sikkerhedsovervejelser for webhooks**:
  * Webhooks er offentlige endpoints, hvilket skaber potentielle sikkerhedsproblemer
  * Brug token-autentifikation, IP-filtrering og uforudsigelige URL'er
  * Overvej at validere og sanitere al indkommende data
  * Brug HTTPS når muligt, især for webhooks der er tilgængelige på internettet

* **Fordele ved webhooks frem for polling**:
  * Lavere ressourceforbrug (ingen konstante forespørgsler)
  * Hurtigere reaktionstid (næsten øjeblikkelig)
  * Reduceret belastning på servere og netværk
  * Simplere kode, da du ikke behøver at implementere polling-logik

---

## 📋 Fejlfinding

### Webhook udløses ikke:
* Kontroller at URL'en er korrekt (inklusive store/små bogstaver)
* Verificer at Node-RED er tilgængelig fra det kaldende system
* Tjek Node-RED logs for fejlmeddelelser
* Brug debug-noder til at se om kaldet når frem til dit flow

### Autentifikation fejler:
* Tjek om tokenet sendes korrekt (header, query parameter)
* Verificer at tokenværdien matcher præcis
* Undersøg om headeren er formateret korrekt: `Authorization: Bearer <token>`

### Problemer med JSON-data:
* Kontroller at Content-Type header er sat til "application/json"
* Verificer at JSON-syntaksen er valid
* Brug en JSON-validator til at teste dine payloads

---

📌 Webhooks gør Node-RED til en reaktiv enhed i et større system – klar til at handle når eksterne begivenheder opstår. De giver dig mulighed for at skabe sophifikerede automationer på tværs af forskellige platforme og tjenester.