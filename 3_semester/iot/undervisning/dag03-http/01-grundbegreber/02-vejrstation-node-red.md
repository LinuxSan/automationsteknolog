# ☁️ Byg en vejrstation i Node-RED med Weatherstack API

I denne opgave skal du bruge en ekstern REST-tjeneste til at hente live vejrdata og præsentere det i Node-RED som en del af dit smart home-dashboard.

---

## 🎯 Læringsmål

* Du kan kalde et eksternt REST API (Weatherstack)
* Du kan formatere og visualisere svar i Node-RED
* Du forstår forskellen mellem interne og eksterne REST endpoints

---

## 🔧 Forudsætninger

* En gratis API-nøgle fra [https://weatherstack.com](https://weatherstack.com)
* Node-RED med internetadgang
* Installeret `node-red-dashboard` (for visning)
* By i fokus (fx Copenhagen, Odense eller Århus)

---

## 📦 Trin 1 – Opret en konto på Weatherstack

1. Åbn din browser og gå til [weatherstack.com](https://weatherstack.com)
2. Klik på "Sign Up Free" knappen
3. Udfyld registreringsformularen med dit navn, e-mail og adgangskode
4. Vælg den gratis plan ("Free") og bekræft registreringen
5. Efter registrering vil du blive ført til dit dashboard
6. Find sektionen med din API-nøgle og noter den - du skal bruge den i næste trin

---

## 📦 Trin 2 – Forbered Node-RED

1. Åbn Node-RED i din browser (typisk på http://localhost:1880)
2. Kontroller at du har installeret dashboard-pakken:
   * Klik på menu-ikonet i øverste højre hjørne
   * Vælg "Manage palette"
   * Gå til "Install"-fanebladet
   * Søg efter "node-red-dashboard"
   * Installer den, hvis den ikke allerede er installeret

---

## 📦 Trin 3 – Opbyg vejrdata-flowet

1. **Tilføj en inject node**:
   * Træk en `inject`-node fra venstre sidepanel til dit workspace
   * Dobbeltklik på noden for at konfigurere
   * Indstil gentagelse til "interval" og sæt tiden til 10 minutter
   * Klik på "Done"

2. **Tilføj en http request node**:
   * Træk en `http request`-node fra venstre sidepanel til dit workspace
   * Dobbeltklik på noden for at konfigurere
   * Indstil metoden til "GET"
   * Indtast følgende URL (erstat DIN_API_NØGLE med din rigtige API-nøgle):
     ```
     http://api.weatherstack.com/current?access_key=DIN_API_NØGLE&query=Copenhagen
     ```
   * Sæt "Return" til "a parsed JSON object"
   * Klik på "Done"

3. **Forbind noderne**:
   * Træk en linje fra `inject`-noden til `http request`-noden

4. **Tilføj en debug node til test**:
   * Træk en `debug`-node fra venstre sidepanel til dit workspace
   * Forbind `http request`-noden til `debug`-noden
   * Klik på "Deploy" knappen øverst til højre
   * Klik på inject-noden og tjek debug-panelet til højre for at se, om du modtager data

---

## 📦 Trin 4 – Behandl vejrdata

1. **Tilføj en function node til at behandle data**:
   * Træk en `function`-node fra venstre sidepanel til dit workspace
   * Dobbeltklik på noden for at konfigurere
   * Indtast følgende kode:
     ```javascript
     // Tjek om der er en gyldig respons
     if (msg.payload && msg.payload.current) {
         // Udtræk kun de data, vi har brug for
         msg.payload = {
             temperature: msg.payload.current.temperature,
             humidity: msg.payload.current.humidity,
             description: msg.payload.current.weather_descriptions[0],
             icon: msg.payload.current.weather_icons[0],
             location: msg.payload.location.name,
             country: msg.payload.location.country,
             localtime: msg.payload.location.localtime
         };
         
         // Gem data i flow-memory så vi kan se, hvornår det sidst blev opdateret
         flow.set("lastWeatherUpdate", new Date().toLocaleTimeString());
         flow.set("weatherData", msg.payload);
         
         return msg;
     } else {
         // Håndter fejl
         node.error("Kunne ikke hente vejrdata - tjek API-nøgle og forbindelse");
         return null;
     }
     ```
   * Klik på "Done"

2. **Forbind http request til function**:
   * Fjern forbindelsen mellem `http request` og `debug`
   * Forbind `http request`-noden til `function`-noden
   * Forbind `function`-noden til `debug`-noden
   * Klik på "Deploy" og test igen ved at klikke på `inject`-noden

---

## 📦 Trin 5 – Opret dashboard til vejrvisning

1. **Opret en ny dashboard-fane**:
   * Klik på "Dashboard"-ikonet i højre sidepanel
   * Klik på "+" ikonet ud for "Tabs" for at oprette en ny fane
   * Navngiv fanen "Vejrstation"
   * Klik på "+" ikonet ud for din nye fane for at tilføje en gruppe
   * Navngiv gruppen "Aktuelt vejr"

2. **Tilføj gauge til temperatur**:
   * Træk en `ui_gauge`-node fra venstre sidepanel til dit workspace
   * Dobbeltklik for at konfigurere
   * Vælg din "Vejrstation" fane og "Aktuelt vejr" gruppe
   * Navngiv den "Temperatur"
   * Indstil enheden til "°C"
   * Sæt min-værdi til -10 og max-værdi til 40
   * Klik på "Done"

3. **Tilføj gauge til luftfugtighed**:
   * Træk en ny `ui_gauge`-node til dit workspace
   * Konfigurer den til samme gruppe
   * Navngiv den "Luftfugtighed"
   * Indstil enheden til "%"
   * Sæt min-værdi til 0 og max-værdi til 100
   * Klik på "Done"

4. **Tilføj tekst til vejrbeskrivelse**:
   * Træk en `ui_text`-node til dit workspace
   * Konfigurer den til samme gruppe
   * Navngiv den "Beskrivelse"
   * Klik på "Done"

5. **Tilføj tekst til seneste opdatering**:
   * Træk en `ui_text`-node til dit workspace
   * Konfigurer den til samme gruppe
   * Navngiv den "Sidst opdateret"
   * Klik på "Done"

---

## 📦 Trin 6 – Forbind function til dashboard-elementerne

1. **Tilføj yderligere function nodes til at dele data**:
   * Træk tre nye `function`-noder til dit workspace
   * Konfigurer den første med:
     ```javascript
     msg.payload = msg.payload.temperature;
     return msg;
     ```
   * Konfigurer den anden med:
     ```javascript
     msg.payload = msg.payload.humidity;
     return msg;
     ```
   * Konfigurer den tredje med:
     ```javascript
     msg.payload = `${msg.payload.description} i ${msg.payload.location}`;
     return msg;
     ```
   * Konfigurer en fjerde med:
     ```javascript
     msg.payload = "Sidst opdateret: " + flow.get("lastWeatherUpdate");
     return msg;
     ```

2. **Forbind dem alle sammen**:
   * Forbind hoved-`function`-noden til de tre nye function-noder
   * Forbind den første function-node til temperatur-gaugen
   * Forbind den anden function-node til luftfugtigheds-gaugen
   * Forbind den tredje function-node til beskrivelse-teksten
   * Forbind den fjerde function-node til opdateringsteksten

3. **Tilføj en inject node til opdateringsteksten**:
   * Træk en ny `inject`-node til workspace
   * Indstil den til at køre hver minut
   * Forbind denne inject-node til den fjerde function-node (den med "Sidst opdateret")

---

## 📦 Trin 7 – Test og juster dit dashboard

1. **Klik på "Deploy" for at aktivere dit flow**
2. **Åbn dashboard**:
   * Klik på "Dashboard"-ikonet i sidepanelet
   * Klik på lancerings-ikonet (pil) for at åbne dit dashboard i en ny fane
3. **Test dit dashboard**:
   * Tjek om gauges og tekstfelter viser vejrdata korrekt
   * Gå tilbage til Node-RED og klik på inject-noden for at hente nye data

---

## 💡 Ekstraudfordringer

1. **Tilføj by-vælger**:
   * Træk en `ui_dropdown`-node til dit workspace
   * Konfigurer den med en liste af byer (fx Copenhagen, Aarhus, Odense)
   * Tilføj en function-node, der ændrer URL'en baseret på det valgte
   * Forbind dropdown til denne funktion og derefter til http request

2. **Vis vejrikon**:
   * Træk en `ui_template`-node til dit workspace
   * Brug følgende HTML til at vise vejrikonet:
     ```html
     <div style="text-align: center;">
       <img src="{{msg.payload.icon}}" alt="Vejrikon" style="max-width: 100px;">
     </div>
     ```
   * Forbind din hoved-function-node til denne template

3. **Gem historiske data**:
   * Brug en `function`-node til at gemme temperatur over tid
   * Tilføj en `ui_chart`-node til at vise tendenser

---

## 🧠 Refleksion

* Hvordan adskiller et offentligt REST API sig fra lokale endpoints?
* Hvad sker der, hvis API-nøglen mangler eller er forkert?
* Hvordan kan du sikre dig mod afbrudt internetforbindelse i dit system?
* Hvorfor er det vigtigt at strukturere og filtrere API-data, før du viser det?

---

📌 Denne øvelse kobler REST-teori sammen med realtidsintegration, API-nøgler og visualisering i Node-RED – og giver et konkret indblik i eksterne data som en del af IoT-løsninger.