# 📘 Node-RED: CoAP Discovery – Opgaver

Dette dokument indeholder opgaver relateret til implementering af CoAP discovery i Node-RED. Opgaverne er designet til at give forståelse for både statisk og dynamisk håndtering af `/.well-known/core`.

---

## 🧪 Opgave 1 – Simpel hardcoded discovery

**Formål:** Simulér en CoAP-enhed med statisk `/temp` og `/led` ressource

### Trin

1. Tilføj en **CoAP input-node** med URL `/\.well-known/core` og metode GET
2. Tilføj en **Function-node** med denne kode:

```javascript
msg.payload = "</temp>;rt=\"temperature\",</led>;rt=\"switch\"";
return msg;
```

3. Tilføj en **CoAP response-node**
4. Test med `coap-client` eller en anden CoAP-klient

---

## 🧪 Opgave 2 – Dynamisk link-format baseret på flow-variabler

**Formål:** Generer CoAP discovery-svar baseret på flow-variablet indhold

### Trin

1. Tilføj en **Inject-node** der sætter flow-variablen `resources`:

```javascript
flow.set("resources", [
  { uri: "/temp", rt: "temperature" },
  { uri: "/led", rt: "switch" }
]);
```

2. Tilføj en **Function-node** for at generere discovery-svaret:

```javascript
let resources = flow.get("resources") || [];
let payload = resources.map(r => `<${r.uri}>;rt=\"${r.rt}\"`).join(",");
msg.payload = payload;
return msg;
```

3. Forbind denne function til en CoAP response-node

---

## 🧪 Opgave 3 – Discovery for REST-endpoints

**Formål:** Lav en bro mellem HTTP-endpoints og CoAP discovery

### Trin

1. Tilføj HTTP endpoints i Node-RED (`/temp`, `/led`)
2. Ved opstart eller opdatering, registrer disse som ressourcer i `flow.set("resources", [...])`
3. Brug samme discovery-flow som i opgave 2 til at returnere CoAP discovery-data

---

## 💡 Bonusopgave – Tilføj metadata som `if` og `ct`

Udvid Function-node til:

```javascript
let resources = flow.get("resources") || [];
let payload = resources.map(r => `<${r.uri}>;rt=\"${r.rt}\";if=\"${r.if || 'sensor'}\";ct=\"0\"`).join(",");
msg.payload = payload;
return msg;
```

Tilføj `if` og `ct` i dine registrerede ressourcer.

---

✅ Disse opgaver dækker både statisk og dynamisk CoAP discovery i Node-RED og kan nemt tilpasses mere avancerede scenarier såsom autentificering eller integration med MQTT/Home Assistant.
