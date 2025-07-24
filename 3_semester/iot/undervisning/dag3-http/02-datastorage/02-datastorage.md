# 🧪 Opgaver – HTTP REST Data Storage

Disse opgaver giver dig hands-on erfaring med at lagre data i REST-miljøer. Du lærer at modtage, gemme, hente og strukturere data i Node-RED, samt arbejde med JSON, filer og flow memory.

> 🧠 Fokus: CRUD, dataformat, persistens og lagringsstrategi.

---

## 🟢 Del 1 – Gem data i flow memory

### 🎯 Læringsmål

* Du kan gemme data midlertidigt med `flow.set()`

### 🔧 Opgave

1. Lav en POST endpoint i Node-RED: `/api/temperature`
2. Modtag JSON med fx:

```json
{ "sensor": "kitchen", "value": 22.1 }
```

3. Gem data i en array med `flow.set("temperatures")`
4. Lav GET endpoint `/api/temperature` der returnerer hele arrayet

💬 Refleksion: Hvad sker der med data efter en genstart?

---

## 🔵 Del 2 – Gem data i en JSON-fil

### 🎯 Læringsmål

* Du kan bruge `file`-node til simpel persistens

### 🔧 Opgave

1. Brug en function node til at formatere input:

```javascript
msg.payload = JSON.stringify(msg.payload) + "\n";
return msg;
```

2. Tilslut til `file` node:

* Filename: `data/temperature_log.json`
* Append mode: Ja

3. Send POST-data og tjek filens indhold

💬 Refleksion: Hvordan håndterer du mange samtidige POSTs?

---

## 🟡 Del 3 – Lav CRUD-mock API i Node-RED

### 🎯 Læringsmål

* Du forstår Create, Read, Update og Delete i REST

### 🔧 Opgave

1. Lav fire endpoints:

   * POST `/api/devices` → Tilføj til array
   * GET `/api/devices` → Returnér hele array
   * PUT `/api/devices/:id` → Erstat enhed med nyt indhold
   * DELETE `/api/devices/:id` → Fjern fra array

2. Gem i `flow.set("devices")`

3. Brug `switch` og `function` nodes til logik og ID-match

💬 Refleksion: Hvad er fordel og ulempe ved array i memory?

---

## 🔴 Del 4 – Brug SQLite eller InfluxDB til persistence

### 🎯 Læringsmål

* Du kan gemme data i database via REST input

### 🔧 Opgave

1. Installer `node-red-node-sqlite` eller `node-red-contrib-influxdb`
2. Lav POST endpoint til at skrive til DB:

   * SQLite: `INSERT INTO temperature VALUES (...)`
   * InfluxDB: `sensor=room value=22.5`
3. Lav GET endpoint til at læse historik

💬 Refleksion: Hvornår er database bedre end fil eller memory?

---

## 🧭 Afslutning og overblik

📋 Tjekliste:

* [ ] Har du gemt data med `flow.set()`?
* [ ] Har du skrevet til en JSON-fil?
* [ ] Har du CRUD-endpoints med korrekt logik?
* [ ] Har du prøvet at gemme til database?

🧠 Ekstra:

* Lav backup-rutine (fx eksport af JSON hver time)
* Integrér visning i dashboard med `ui_table` eller `ui_text`-noder
* Kombinér storage med adgangskontrol (kun POST med token)

---

📌 Disse øvelser giver dig grundlæggende erfaring med REST-lagring – både i hukommelse, fil og database – som fundament for mere avancerede IoT-løsninger.
