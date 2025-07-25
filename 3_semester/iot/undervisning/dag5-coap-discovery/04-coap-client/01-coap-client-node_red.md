# 🧪 Opgaver – CoAP 04: Client (Node-RED version)

I denne udvidede udgave arbejder vi med Node-RED som en fuldt funktionel CoAP-klient. Du lærer at sende forskellige typer anmodninger (GET og PUT) til CoAP-servere, modtage og tolke svar, overvåge fejl og integrere svarene i dashboards. Derudover arbejder du med avancerede funktioner såsom periodiske anmodninger og fejlhåndtering, hvilket gør dig i stand til at opbygge mere robuste IoT-systemer baseret på CoAP og Node-RED.

---

## 🟢 Opgave 1 – CoAP GET-anmodning fra Node-RED

1. Åbn Node-RED og gå til Menu → Manage Palette → Install.
2. Søg efter `node-red-contrib-coap` og klik "Install" for at tilføje CoAP-understøttelse.
3. Opret et simpelt flow bestående af:

   * `inject` node → `coap request` node → `debug` node
4. Konfigurer `inject` node:

   * Payload: tom streng ("")
   * Topic: (kan være tom)
   * Tryk på "Repeat" hvis du vil aktivere gentagelse
5. Konfigurer `coap request` node:

   * URL: `coap://<ESP32-IP>/temp`
   * Metode: `GET`
6. Deploy flowet og klik på inject-knappen for at sende anmodningen.

✅ *Du bør modtage svar i debug-vinduet, fx temperaturen som tekst eller JSON.*

---

## 🔵 Opgave 2 – Periodisk anmodning og dashboard

1. Rediger `inject` node til at sende automatisk hvert 10. sekund:

   * Vælg "inject once after" og "repeat every 10 seconds"
2. Tilføj en `function` node mellem `coap request` og `ui_gauge`:

```javascript
let data = parseFloat(msg.payload);
msg.payload = data;
return msg;
```

3. Tilføj `ui_gauge` fra `node-red-dashboard` palette:

   * Label: "Temperatur i rum A"
   * Range: fx 0–50°C
4. Deploy igen og observer realtidsvisning i dashboardet.

✅ *Temperatur opdateres live, og du har nu et fungerende CoAP-monitoreringsdashboard.*

---

## 🟡 Opgave 3 – CoAP PUT med JSON-payload (styring)

1. Lav et nyt flow til at sende kommandoer via CoAP:

   * `inject` node → `function` node → `coap request` node
2. I `inject` node: sæt payload til tom streng og metode til `once on deploy` (eller med knap)
3. I `function` node, indsæt følgende:

```javascript
msg.method = "PUT";
msg.payload = '{"led": "ON"}';
return msg;
```

4. I `coap request` node:

   * URL: `coap://<ESP32-IP>/led`
   * Type: `non-confirmable` eller `confirmable` alt efter opsætning
5. Tjek at ESP32 tænder/slukker LED og returnerer bekræftelse

✅ *Du har nu fjernkontrol over aktuatorer via CoAP og Node-RED.*

---

## 🔁 Opgave 4 – Fejlhåndtering og timeout-test

1. Simulér en fejlsituation ved at slukke eller frakoble din CoAP-server
2. Klik på `inject` node og se om `coap request` returnerer fejl (se debug)
3. Tilføj `catch` node og forbind den til `debug`, så du kan opfange globale fejl i dit flow
4. (Valgfrit) Tilføj et `status` node på `coap request` for at få visuel feedback

✅ *Flowet skal håndtere netværksfejl, og fejlmeldinger skal vises i debug eller UI.*

---

## 🧠 Refleksion

* Hvordan visualiserer du CoAP-data effektivt i Node-RED?
* Hvornår er `PUT` velegnet i stedet for `GET` – og hvorfor?
* Hvad er fordelene og begrænsningerne ved at bruge Node-RED som CoAP-klient i forhold til fx Python eller C?
* Hvordan kan du kombinere CoAP med MQTT i et flow, hvor ESP32 sender CoAP og Node-RED videresender til MQTT?

---

📌 Med Node-RED som CoAP-klient får du et visuelt og fleksibelt miljø til at integrere RESTful kommunikation mellem ESP32-enheder, sensorer og styringer – perfekt til undervisning og udvikling af IoT-løsninger. Du kan let udvide systemet med dashboard, automatisering, gateway-funktioner og dataanalyse.
