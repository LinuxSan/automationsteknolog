# 🧪 Opgaver – HTTP REST Webinterface

Disse opgaver hjælper dig med at forbinde REST-endpoints til et brugervenligt webinterface. Du lærer at præsentere, manipulere og interagere med REST-data i Node-RED Dashboard og Home Assistant Lovelace.

> 🧠 Fokus: REST-visualisering, brugerinput og UI-dataflow

---

## 🟢 Del 1 – Præsenter REST-data i Node-RED Dashboard

### 🎯 Læringsmål

* Du kan hente REST-data og vise dem i en grafisk widget

### 🔧 Opgave

1. Lav et GET-call til `http://api.coindesk.com/v1/bpi/currentprice/EUR.json`
2. Parse resultatet i en function node:

```javascript
msg.payload = parseFloat(msg.payload.bpi.EUR.rate);
return msg;
```

3. Vis resultatet i en `ui_gauge` eller `ui_text`
4. Brug `inject` node til at opdatere hvert 10. minut

💬 Refleksion: Hvordan håndterer du fejl eller nedetid i API?

---

## 🔵 Del 2 – Brug UI-komponenter til at sende REST-kald

### 🎯 Læringsmål

* Du kan sende kommandoer via REST fra et UI

### 🔧 Opgave

1. Lav en `ui_button` med label "Tænd lys"
2. Forbind til `http request` node:

   * Method: POST
   * URL: `http://<HA_IP>:8123/api/webhook/tænd_køkkenlys`
3. Tryk på knappen og tjek i Home Assistant at lyset tænder

💬 Refleksion: Hvilke REST-metoder passer bedst til forskellige UI-elementer?

---

## 🟡 Del 3 – Vis REST-data i Home Assistant

### 🎯 Læringsmål

* Du kan vise REST-data i Lovelace-dashboard

### 🔧 Opgave

1. Konfigurer en REST-sensor i HA:

```yaml
sensor:
  - platform: rest
    name: Bitcoin Kurs
    resource: https://api.coindesk.com/v1/bpi/currentprice/EUR.json
    value_template: '{{ value_json.bpi.EUR.rate_float }}'
    unit_of_measurement: "EUR"
```

2. Vis den i et `entities`- eller `gauge`-kort i UI

💬 Refleksion: Hvordan kan du sikre at data ikke vises forkert ved API-fejl?

---

## 🔴 Del 4 – Skriv og vis data fra brugerinput

### 🎯 Læringsmål

* Du kan sende input fra UI som REST POST og vise resultat

### 🔧 Opgave

1. Lav en `ui_text_input` + `ui_button`
2. Send POST til `/api/note` i Node-RED
3. Gem data i `flow.set("notes")`
4. Lav GET endpoint der returnerer alle noter
5. Vis listen med `ui_template` eller `ui_text`

💬 Refleksion: Hvordan sikrer du, at brugeren får feedback på at input er gemt?

---

## 🧭 Afslutning og overblik

📋 Tjekliste:

* [ ] Har du hentet REST-data og vist i dashboard?
* [ ] Har du sendt kommando via knap eller input?
* [ ] Har du bygget både REST GET og POST integration?
* [ ] Har du testet med både Node-RED og HA?

🧠 Ekstra:

* Brug `ui_chart` til at vise historik
* Send feedback som snackbar eller popup i UI
* Lav validering af input før POST

---

📌 Disse opgaver giver erfaring i at binde REST-data og funktionalitet sammen med et brugervenligt interface – så både mennesker og maskiner kan interagere med dit system.
