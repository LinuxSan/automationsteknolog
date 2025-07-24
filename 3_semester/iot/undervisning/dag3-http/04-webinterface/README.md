# 🖥️ HTTP REST – Webinterface (Teori)

I dette afsnit lærer du, hvordan REST-API'er præsenteres og interageres med gennem webinterfaces. Det handler om at forbinde data og funktioner fra REST-endpoints til grafiske brugerflader.

---

## 🎯 Læringsmål

* Forstå hvordan REST bruges i frontend/web-UI
* Kende forskel på data-præsentation og interaktion
* Kende værktøjer til REST-UI integration (Node-RED Dashboard, Home Assistant Lovelace, custom HTML)

---

## 🌐 Hvad er et webinterface?

Et webinterface er en grafisk præsentation, hvor brugeren kan:

* Se data fra REST (GET)
* Sende data til REST (POST, PUT)
* Udtrykke valg via knapper, sliders, inputfelter osv.

REST bliver altså ikke bare et programmatisk interface – men også et **brugerinterface**.

---

## 📋 Typer af integration

| Interface          | Eksempel                                  |
| ------------------ | ----------------------------------------- |
| Node-RED Dashboard | `ui_text`, `ui_gauge`, `ui_button`        |
| Home Assistant     | Lovelace: Entities, Glance, Gauge, Button |
| HTML/JS frontend   | Fetch/axios + Bootstrap/Chart.js          |
| No-code værktøj    | Grafana, n8n, Make, AppGyver              |

---

## 📊 Præsentation af REST-data

* GET kaldes automatisk ved UI-opdatering eller med `inject`
* JSON svar parses og vises i widgets:

  * Tekst (værdi)
  * Gauge (måling)
  * Liste (collection)
  * Ikon eller farve (status)

Eksempel:

```javascript
GET /api/temperature
→ Response: { "room": "living", "value": 22.3 }
→ Vis i tekst eller gauge-widget
```

---

## 🕹 Interaktion via REST

REST endpoints kan bruges til at:

* Tænde/slukke enhed (`POST /api/lights/kitchen`)
* Opdatere indstillinger (`PUT /api/thermostat/bedroom`)
* Sende kommandoer (`POST /api/scene/movie_mode`)

UI-komponenter:

* Button → `POST`
* Slider → `PATCH`
* Input → `POST` eller `PUT`

---

## 🔁 Dataflow mellem UI og REST

1. Bruger klikker
2. UI sender REST-kald
3. Backend udfører handling
4. Ny status hentes via `GET`
5. UI opdateres

> Node-RED og Home Assistant understøtter dette flow som standard.

---

## 🔐 Sikkerhed og rettigheder

* Nogle REST-kald kræver token eller login
* UI bør ikke vise funktioner som brugeren ikke må aktivere
* Overvej read-only dashboards til gæster

---

## 📦 OpenAPI og dokumentation

* OpenAPI/Swagger bruges til at dokumentere REST endpoints
* Gør det lettere at bygge UI’er, når API’et er dokumenteret

---

## 🧠 Refleksion

* Hvorfor er det vigtigt at REST-data præsenteres forståeligt i UI?
* Hvordan balancerer man kompleksitet og brugervenlighed?
* Hvornår skal UI opdatere automatisk – og hvornår manuelt?

---

📌 Et REST Webinterface forbinder mennesker og maskiner – og gør IoT og REST-data tilgængelige, anvendelige og overskuelige.
