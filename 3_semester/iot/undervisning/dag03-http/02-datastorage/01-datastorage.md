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

## 🔴 Del 4 – Forberedelse til databaseintegration

### 🎯 Læringsmål
* Du forstår, hvordan data kan håndteres midlertidigt og gemmes i filer, mens vi forbereder os på databaseintegration senere i forløbet.

---

### 🔧 Opgave

#### 1. Midlertidig lagring i flow memory
1. Fortsæt med at gemme og hente data midlertidigt i Node-RED's flow memory ved hjælp af `flow.set()` og `flow.get()`, som vist i tidligere opgaver.

#### 2. Permanent lagring i filer
1. Brug den eksisterende tilgang til at gemme data i en JSON-fil ved hjælp af `file`-noden. Dette giver dig en simpel metode til vedvarende lagring uden en database.

#### 3. Introduktion til databaseforberedelse
1. Forstå, at databaseintegration vil blive introduceret senere i forløbet for at håndtere større datamængder og mere komplekse forespørgsler.
2. Når vi når til databaserne, vil du arbejde med værktøjer som MariaDB og lære at:
    - Oprette tabeller til struktureret datalagring.
    - Skrive data til databasen via REST-endpoints.
    - Hente historiske data gennem SQL-forespørgsler.

💬 **Refleksion:** Hvordan kan midlertidig lagring og filbaseret lagring hjælpe dig med at forstå grundlæggende REST-datahåndtering, før du arbejder med databaser?

---

## 🧭 Afslutning og overblik

📋 **Tjekliste:**
* [ ] Har du gemt data midlertidigt i `flow.set()`?
* [ ] Har du prøvet at gemme data i en JSON-fil?
* [ ] Er du klar til næste trin, hvor vi introducerer databaser?

🧠 **Ekstra:**
* Lav en backup-rutine for dine filer (f.eks. eksport af JSON hver time).
* Integrér visning i et dashboard med `ui_table` eller `ui_text`-noder.
* Tænk over, hvordan du kunne bruge en database til at håndtere flere data.

📌 Brug af midlertidig lagring og filer giver dig et godt fundament for at forstå REST-datahåndtering, inden du går videre til mere avancerede teknologier som databaser.