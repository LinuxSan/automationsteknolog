# 💾 HTTP REST – Data Storage (Teori)

Dette afsnit forklarer, hvordan data lagres og struktureres i REST-baserede systemer. Fokus er på begreber som CRUD, persistens og integration med databaser – både i embedded systemer, Node-RED og Home Assistant.

---

## 🎯 Læringsmål

* Forstå CRUD-operationer i REST
* Kende forskellen på statisk og persistent storage
* Forstå hvordan data lagres i REST-miljøer (JSON, databases, memory)

---

## 📚 Hvad betyder CRUD?

CRUD er et akronym for:

| Operation | REST-metode | Funktion           |
| --------- | ----------- | ------------------ |
| Create    | POST        | Opret ny ressource |
| Read      | GET         | Hent eksisterende  |
| Update    | PUT / PATCH | Ændr eksisterende  |
| Delete    | DELETE      | Fjern ressource    |

Et REST API bør understøtte hele CRUD-flowet for hver ressource.

---

## 💡 Hvor gemmes data i REST?

REST-API’er i sig selv lagrer ikke data – de fungerer som adgangspunkter. Data kan gemmes i:

* 🔹 RAM (fx `flow.set()` i Node-RED – midlertidigt)
* 🔸 Filer (fx JSON eller CSV på disk)
* 🧱 Databaser (fx SQLite, MongoDB, PostgreSQL)

> Embedded enheder kan gemme til EEPROM, SPIFFS eller sende videre til REST-server med storage.

---

## 🧠 Memory vs. Persistence

| Type     | Eksempel                  | Bliver slettet ved genstart? |
| -------- | ------------------------- | ---------------------------- |
| Memory   | `flow.set()`, array i RAM | ✅ Ja                         |
| File     | `data.json`, log.txt      | ❌ Nej                        |
| Database | SQLite, InfluxDB, MariaDB | ❌ Nej                        |

Ved REST-lagring skal du vælge niveau:

* Midlertidigt (stateless, cache)
* Semipermanent (logfil, fil-baseret)
* Permanent (database med forespørgsler og backup)

---

## 🧱 Eksempel: JSON-fil som storage

Et REST API i fx Node-RED kan simulere lagring i en fil:

```json
[
  { "sensor": "kitchen", "value": 22.1 },
  { "sensor": "bathroom", "value": 24.3 }
]
```

Ved POST lægges ny data ind, ved GET returneres hele arrayet. Data kan læses/skrive med `fs` (fil-system) i JavaScript eller Python.

---

## 🔗 Node-RED storage-muligheder

| Teknik             | Beskrivelse                                  |
| ------------------ | -------------------------------------------- |
| `flow.set()`       | Gemmer i RAM                                 |
| `file` node        | Skriver data til tekstfil                    |
| `sqlite` node      | Gemmer data i lille database (fx målinger)   |
| `influxdb` node    | Til time-series data                         |
| `localStorage` API | Kan bruges via frontend/script integrationer |

---

## 🛡 Håndtering af konflikter og fejl

* Hvis to POST-forespørgsler sker samtidigt, kan data overskrives (race conditions)
* Systemet bør give feedback med statuskode: 201 Created, 409 Conflict osv.
* Brug `etag`, versionsnummer eller timestamps hvis muligt

---

## 🔁 Eksempel på lagringsflow

```http
POST /api/temperature
Body:
{ "sensor": "living_room", "value": 21.9 }
```

* Server gemmer til array / DB / fil
* Returnerer `201 Created`
* GET returnerer samlet historik eller seneste værdi

---

## 🧠 Refleksion

* Hvornår giver det mening at gemme alle datapunkter – og hvornår kun det seneste?
* Hvad er fordele og ulemper ved at bruge en database kontra en fil?
* Hvilke lagringsformer passer bedst til embedded, cloud og undervisning?

---

📌 REST og storage hænger tæt sammen: API’et fungerer som adgangsgrænse – og bagved ligger struktureret, persistent lagring. Det sikrer, at dine data er tilgængelige, forståelige og genbrugelige.
