# 🧪 Opgaver – HTTP REST Security

Disse opgaver fokuserer på at sikre dine REST-endpoints mod uautoriseret adgang og datamisbrug. Du arbejder med tokens, TLS, rollestyring og god praksis i Node-RED og Home Assistant.

> 🧠 Fokus: Autentifikation, HTTPS, rollebaseret adgang, validering

---

## 🟢 Del 1 – Beskyt et endpoint med adgangstoken (Node-RED)

### 🎯 Læringsmål

* Du kan beskytte et REST endpoint med en adgangsnøgle

### 🔧 Opgave

1. Lav et `http in` endpoint `/api/alarm`
2. Tilføj `function node` i starten med token-check:

```javascript
const token = msg.req.headers['authorization'];
if (token !== 'Bearer secret123') {
    msg.statusCode = 401;
    msg.payload = { error: 'Unauthorized' };
    return [null, msg];
}
return [msg, null];
```

3. Brug `http response` til både success og fejlgrene
4. Test med curl:

```bash
curl -H "Authorization: Bearer secret123" -X POST http://localhost:1880/api/alarm
```

💬 Refleksion: Hvad sker der uden header – og hvad ser brugeren?

---

## 🔵 Del 2 – Tilføj TLS/HTTPS til Node-RED

### 🎯 Læringsmål

* Du forstår hvordan man krypterer REST-trafik

### 🔧 Opgave

1. Generér selvsigneret certifikat:

```bash
openssl req -x509 -newkey rsa:2048 -nodes -keyout key.pem -out cert.pem -days 365
```

2. Tilføj til Node-RED settings.js:

```javascript
https: {
    key: fs.readFileSync("/data/key.pem"),
    cert: fs.readFileSync("/data/cert.pem")
},
requireHttps: true,
```

3. Genstart Node-RED og brug `https://localhost:1880`
4. Test curl med `-k` for selvsigneret:

```bash
curl -k https://localhost:1880/api/status
```

💬 Refleksion: Hvornår er selvsigneret OK – og hvornår kræves ægte certifikat?

---

## 🟡 Del 3 – Rollebaseret adgang i Home Assistant

### 🎯 Læringsmål

* Du kan begrænse REST-funktioner baseret på brugerrolle

### 🔧 Opgave

1. Opret en bruger i Home Assistant med læserettigheder
2. Lav REST-sensor eller webhook i HA der kræver token
3. Test POST fra admin og fra gæstebruker:

```bash
curl -H "Authorization: Bearer <long-lived-token>" -X POST https://<HA>/api/webhook/test
```

4. Lav en automation, der nægter adgang hvis bruger ikke er admin

💬 Refleksion: Hvordan kan du skelne brugertyper via token eller ID?

---

## 🔴 Del 4 – Input-validering og fejlhåndtering

### 🎯 Læringsmål

* Du kan forhindre forkert eller farlig input via REST

### 🔧 Opgave

1. Lav et endpoint `/api/note` hvor brugeren sender tekst
2. Tjek om `msg.payload.note` findes og er under 100 tegn
3. Returnér 400 hvis fejl:

```javascript
if (!msg.payload.note || msg.payload.note.length > 100) {
    msg.statusCode = 400;
    msg.payload = { error: "Invalid input" };
    return msg;
}
```

4. Gem i flow memory hvis OK

💬 Refleksion: Hvad kunne gå galt uden validering?

---

## 🧭 Afslutning og overblik

📋 Tjekliste:

* [ ] Har du brugt Authorization header?
* [ ] Har du testet HTTPS med certifikat?
* [ ] Har du valideret input på dine POST endpoints?
* [ ] Har du prøvet rollebegrænsning i Home Assistant?

🧠 Ekstra:

* Log IP-adresser og tidspunkt for alle POST-kald
* Lav et read-only REST dashboard
* Brug UUID'er som API-nøgler til adgangsstyring

---

📌 REST-sikkerhed er afgørende for at beskytte funktioner, data og brugere. Disse øvelser hjælper dig med at indføre realistiske og praktiske sikringsmetoder i dine IoT-løsninger.
