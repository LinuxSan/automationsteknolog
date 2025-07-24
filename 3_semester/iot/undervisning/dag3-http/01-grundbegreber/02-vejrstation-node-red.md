# ☁️ Tillægsopgave – Byg en vejrstation i Node-RED med Weatherstack API

> I denne opgave skal du bruge en ekstern REST-tjeneste til at hente live vejrdata og præsentere det i Node-RED som en del af dit smart home-dashboard.

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

## 📦 Trin 1 – Sæt API-opkald op i Node-RED

1. Gå til [weatherstack.com](https://weatherstack.com) og opret en gratis konto
2. Find din API-nøgle i dashboardet
3. I Node-RED, lav følgende flow:

   * `inject node` (gentag fx hvert 10. minut)
   * `http request node` med URL som:

```http
http://api.weatherstack.com/current?access_key=DIN_API_NØGLE&query=Copenhagen
```

* `json node` for at parse svaret
* `function node` til at udtrække relevante data, fx:

```javascript
msg.payload = {
  temperature: msg.payload.current.temperature,
  humidity: msg.payload.current.humidity,
  description: msg.payload.current.weather_descriptions[0]
};
return msg;
```

* `ui_gauge` til temperatur og fugtighed
* `ui_text` til vejrbeskrivelse

---

## 🧪 Trin 2 – Test og valider

1. Tryk på `inject` og se data i debug
2. Tilføj visning af data i dashboard
3. Skift by-navn i URL’en og gentest

---

## 💡 Ekstraudfordringer

* Brug en dropdown-menu i dashboard til at vælge by
* Gem vejrdata med `flow.set()` og vis “seneste opdatering”
* Kombinér vejrdata med indendørs temperatur fra ESP32

---

## 🧠 Refleksion

* Hvordan adskiller et offentligt REST API sig fra lokale endpoints?
* Hvad sker der, hvis API-nøglen mangler eller er forkert?
* Hvordan kan du sikre dig mod afbrudt internetforbindelse i dit system?

---

📌 Denne øvelse kobler REST-teori sammen med realtidsintegration, API-nøgler og visualisering i Node-RED – og giver et konkret indblik i eksterne data som en del af IoT-løsninger.
