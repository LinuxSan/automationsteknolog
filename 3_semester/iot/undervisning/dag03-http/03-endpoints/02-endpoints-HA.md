# 🧪 Opgaver – HTTP REST Endpoints i Home Assistant (HA)

I disse opgaver lærer du at bruge REST-endpoints i Home Assistant – både som input via webhooks og som udløsere og handlinger. Du skal oprette, strukturere og kalde REST URL’er i HA-konfiguration og automationer.

> 🧠 Fokus: Endpoints i praksis med Home Assistant og REST-webhooks

---

## 🟢 Del 1 – Webhook-endpoint til handling

### 🎯 Læringsmål

* Du kan oprette REST webhook-endpoint i HA

### 🔧 Opgave

1. Lav en automation i `automations.yaml` eller UI:

```yaml
automation:
  - alias: "Webhook tænder lys"
    trigger:
      - platform: webhook
        webhook_id: tænd_køkkenlys
    action:
      - service: light.turn_on
        target:
          entity_id: light.kitchen_lamp
```

2. Test med curl:

```bash
curl -X POST http://<HA_IP>:8123/api/webhook/tænd_køkkenlys
```

> Husk: Ingen token kræves for webhook-endpoints, men URL skal være hemmelig

💬 Refleksion: Hvad er forskellen på dette og et almindeligt POST endpoint?

---

## 🔵 Del 2 – Brug `rest_command` til at sende data ud

### 🎯 Læringsmål

* Du kan sende HTTP-anmodninger fra Home Assistant

### 🔧 Opgave

1. Tilføj til `configuration.yaml`:

```yaml
rest_command:
  post_temperature:
    url: "http://<NODE_RED_IP>:1880/api/temperature"
    method: post
    headers:
      Content-Type: application/json
    payload: '{"sensor": "living_room", "value": 21.9}'
```

2. Lav en automation, der kalder `rest_command.post_temperature` hvis en sensor ændrer værdi

💬 Refleksion: Hvorfor skal Content-Type sættes manuelt?

---

## 🟡 Del 3 – Strukturér endpoints til smart house

### 🎯 Læringsmål

* Du forstår REST-URL-struktur med brug i HA

### 🔧 Opgave

1. Definér følgende interne endpoints:

   * `/api/webhook/dørkontakt`
   * `/api/webhook/temperaturalarm`
   * `/api/webhook/lys_tænd`

2. Lav automations til hver webhook, som:

   * Logger besked i Notification
   * Udfører en handling (lys, alarm, notifikation)

3. Brug `curl` eller Node-RED til at kalde endpoints

💬 Refleksion: Hvorfor kalder vi det stadig et endpoint, når det er webhook?

---

## 🔴 Del 4 – Simuler CRUD i Home Assistant

### 🎯 Læringsmål

* Du forstår hvordan HA kan fungere som REST-server og REST-klient

### 🔧 Opgave

1. Lav en `input_text` til sensorstatus:

```yaml
input_text:
  sensor_status:
    name: Sensorstatus
    initial: "unknown"
```

2. Lav webhook `/api/webhook/sensor_opdatering` som modtager POST med:

```json
{ "status": "online" }
```

3. Brug `template` og `set_value` til at opdatere `input_text`
4. Lav GET endpoint via `template sensor` der returnerer status

💬 Refleksion: Hvad er forskellen på dette og ægte database-CRUD?

---

## 🧭 Afslutning og overblik

📋 Tjekliste:

* [ ] Har du lavet REST endpoints med webhook?
* [ ] Har du testet `rest_command` til POST?
* [ ] Har du struktureret dine endpoints logisk?
* [ ] Har du testet webhook-kald fra terminal eller Node-RED?

🧠 Ekstra:

* Brug token-beskyttede API-kald med `/api/states`
* Byg dokumentation over dine HA-endpoints
* Kombinér webhook og rest\_command i en tovejskommunikation

---

📌 Disse opgaver lærer dig REST endpoints i Home Assistant – som et bindeled mellem verden udenfor og automatiseringer indenfor.
