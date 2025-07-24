# 🌐 HTTP REST – Grundbegreber (Teori)

Denne sektion introducerer de centrale koncepter i HTTP REST, som anvendes til at bygge og tilgå moderne web- og IoT-API’er.

---

## 🧠 Hvad betyder REST?

**REST** står for **Representational State Transfer** og er en arkitekturstil, der bygger på principper for kommunikation over HTTP.

REST bruges til at:

* Hente data fra et system
* Tilføje ny data
* Opdatere eller slette eksisterende data

REST API’er er:

* Letlæselige og strukturerede
* Bygget op omkring ressourcer
* Standardiseret omkring HTTP-metoder

---

## 🔑 Grundlæggende HTTP-metoder

| Metode | Funktion            | Bruges til             |
| ------ | ------------------- | ---------------------- |
| GET    | Hent data           | Læs information        |
| POST   | Opret ny data       | Send ny information    |
| PUT    | Erstat eksisterende | Opdater hele ressource |
| PATCH  | Delvis opdatering   | Ændr enkelte felter    |
| DELETE | Slet data           | Fjern en ressource     |

> Eksempel: `GET /api/temperature` henter alle temperaturmålinger.

---

## 📦 Ressourcer og URLs

I REST omtales data som **ressourcer**, og disse identificeres via URL'er (endpoints).

**Eksempler:**

```
/api/sensor → liste over sensorer
/api/sensor/42 → sensor med id 42
```

> Hver URL beskriver én entydig ressource eller samling.

---

## 🔁 Stateløshed

REST er **stateless**, hvilket betyder:

* Server gemmer ingen brugerstatus mellem forespørgsler
* Hver HTTP-forespørgsel skal være komplet og selvforklarende

Fordele:

* Let at skalere
* Let at debugge og logge

---

## 🔧 MIME-typer og formater

REST bruger ofte **JSON** som dataformat:

```json
{
  "temperature": 22.5,
  "unit": "C"
}
```

Andre mulige formater:

* XML
* HTML (til UI)
* Plain text

HTTP-headeren `Content-Type` fortæller serveren, hvilket format der sendes:

```
Content-Type: application/json
```

---

## 📋 Typisk REST-flow

1. Klient sender HTTP-forespørgsel (fx med fetch, axios eller curl)
2. Server returnerer svar med data eller statuskode

**Eksempel:**

```http
GET /api/sensor/1 HTTP/1.1
Host: iot.local
Accept: application/json
```

**Respons:**

```json
{
  "id": 1,
  "type": "temperature",
  "value": 21.4,
  "unit": "C"
}
```

---

## 🔢 HTTP Statuskoder

REST API’er bruger standard statuskoder:

| Kode | Beskrivelse               |
| ---- | ------------------------- |
| 200  | OK                        |
| 201  | Created                   |
| 204  | No Content (efter DELETE) |
| 400  | Bad Request               |
| 404  | Not Found                 |
| 500  | Server Error              |

---

## 🧭 Opsummering

REST handler om:

* At definere og tilgå ressourcer
* At bruge HTTP-metoder korrekt
* At arbejde stateless og med klare strukturer

Det er grundlaget for moderne IoT-systemer, databaser, webapps og integrationer.

> Næste skridt: Lær hvordan REST håndterer **data storage** (CRUD og persistence).
