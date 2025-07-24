# 🧪 Opgaver – HTTP REST Endpoints

Disse opgaver giver dig hands-on træning i at opbygge og teste REST-endpoints, både til læsning og ændring af data. Du arbejder med samlinger og enkeltrressourcer i et smart house-scenarie via Node-RED.

> 🧠 Fokus: REST-URL-struktur, korrekte metoder, meningsfulde endpoints.

---

## 🟢 Del 1 – Lav endpoints til sensorsamling

### 🎯 Læringsmål

* Du kan oprette REST-endpoints med GET og POST

### 🔧 Opgave

1. Lav et endpoint `/api/sensors` i Node-RED med:

   * `GET` → returnerer en liste med sensorer (fx 3 dummy-objekter)
   * `POST` → tilføjer en ny sensor med JSON-input

2. Brug `flow.get("sensors")` og `flow.set("sensors")`

3. Returnér `200 OK` eller `201 Created` afhængig af metode

💬 Refleksion: Hvad gør POST anderledes end GET på samme endpoint?

---

## 🔵 Del 2 – Adgang til enkelte ressourcer

### 🎯 Læringsmål

* Du forstår brug af path parameters til specifik ressourceadgang

### 🔧 Opgave

1. Lav endpoint `/api/sensors/:id`

   * `GET` → returnerer sensor med matchende id
   * `PUT` → overskriver sensorens data
   * `DELETE` → fjerner sensor

2. Parse `req.params.id` i function node:

```javascript
const id = msg.req.params.id;
```

💬 Refleksion: Hvordan kan man validere, om ID’et findes?

---

## 🟡 Del 3 – Strukturér endpoints til smart house

### 🎯 Læringsmål

* Du kan designe REST URL’er ud fra kontekst

### 🔧 Opgave

1. Lav endpoints til:

   * Lys i rum: `/api/lights`, `/api/lights/kitchen`
   * Temperaturer: `/api/temperature/living_room`
   * Brugere: `/api/users`, `/api/users/42`

2. Beslut hvilke endpoints der har GET, POST, DELETE, PATCH

3. Lav oversigtstabel med:

   * URL
   * Metode
   * Funktion

💬 Refleksion: Hvor går grænsen mellem “samling” og “objekt” i din struktur?

---

## 🔴 Del 4 – Filtrering med query parameters

### 🎯 Læringsmål

* Du kan håndtere og fortolke query strings

### 🔧 Opgave

1. Lav endpoint `/api/sensors?type=temperature`
2. Parse query via:

```javascript
const type = msg.req.query.type;
```

3. Returnér kun matchende sensorer
4. Test med curl eller Postman:

```bash
curl http://localhost:1880/api/sensors?type=motion
```

💬 Refleksion: Hvornår bør man bruge query fremfor path?

---

## 🧭 Afslutning og overblik

📋 Tjekliste:

* [ ] Har du lavet endpoints til både samlinger og enkelte ressourcer?
* [ ] Har du anvendt GET, POST, PUT og DELETE korrekt?
* [ ] Har du håndteret path og query korrekt?

🧠 Ekstra:

* Tilføj versionsnummer i din URL (fx `/api/v1/sensors`)
* Tilføj validering (fx manglende felter giver 400)
* Lav en README med alle dine endpoints og eksempel-calls

---

📌 Denne øvelse træner dine evner i REST-endpoint-design, strukturering og interaktion – som du senere skal bruge til sikkerhed, integration og frontend-visning.
