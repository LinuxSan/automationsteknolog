# 🧩 Tillæg – Node-RED og Webhooks

Dette dokument forklarer, hvordan du bruger **webhooks i Node-RED** – dvs. endpoints som eksterne systemer kan kalde via HTTP for at udløse handlinger i dit flow.

---

## 🎯 Hvad er en webhook?

En webhook er et URL-baseret REST endpoint, som kan modtage data (typisk via POST). Når et andet system (fx Home Assistant, GitHub, IFTTT, Discord) sender en HTTP-forespørgsel til denne URL, aktiveres et flow i Node-RED.

---

## 🔧 Eksempel – Tænd lampe ved webhook-opkald

1. Opret `http in` node:

   * Method: POST
   * URL: `/webhook/lamp_on`

2. Tilføj `function` node:

```javascript
msg.payload = { payload: true };
return msg;
```

3. Tilføj MQTT eller udgangsnode (fx GPIO eller Home Assistant service call)

4. Afslut med `http response` node:

```javascript
msg.statusCode = 200;
msg.payload = { status: "ok" };
return msg;
```

5. Test webhook:

```bash
curl -X POST http://<NODE_RED_IP>:1880/webhook/lamp_on
```

---

## 🌐 Brugsscenarier

* Brug Node-RED til at reagere på GitHub pushes (CI/CD)
* Tænd/Sluk lys eller systemer fra en ekstern app
* Aktiver alarmer eller beskeder ved REST-kald fra et 3. parts-system
* Integrér med IFTTT, Zapier, n8n eller Webhook.site

---

## 🔒 Sikkerhed

* Webhooks bør være svære at gætte (fx: `/webhook/lamp_on_abc123xyz`)
* Brug evt. headers eller token som godkendelse
* Begræns adgang til LAN eller til bestemte IP’er via firewall

---

## 🧠 Refleksion

* Hvad adskiller et webhook fra et almindeligt REST API endpoint?
* Hvordan sikrer du, at webhooks ikke misbruges?
* Hvornår er webhooks smartere end polling?

---

📌 Webhooks gør Node-RED til en reaktiv enhed i et større system – klar til at handle når eksterne begivenheder opstår.
