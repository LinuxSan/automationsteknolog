# 🔄 Dag 4 – Home Assistant 06: HA Kommunikation med Node-RED

I denne lektion lærer du, hvordan Home Assistant og Node-RED kommunikerer via REST, MQTT og native integration. Kombinationen giver avanceret logik, visualisering og tværgående automation.

---

## 🎯 Læringsmål

* Forstå hvordan HA og Node-RED kan udveksle data
* Bruge REST webhooks og `rest_command`
* Bruge MQTT til tovejskommunikation
* Integrere via `node-red-contrib-home-assistant-websocket`

---

## 🔗 Metoder til kommunikation

| Metode            | Retning        | Funktion                     |
| ----------------- | -------------- | ---------------------------- |
| MQTT              | Bi-direktional | Sensor- og aktuatordata      |
| REST Webhooks     | HA → Node-RED  | Trigger flows fra automation |
| rest\_command     | Node-RED → HA  | Aktiver handling i HA        |
| WebSocket (addon) | Bi-direktional | Direkte adgang til entiteter |

---

## 🧪 Eksempel 1 – HA webhook → Node-RED

1. I HA automation:

```yaml
automation:
  - alias: "Bevægelse registreret"
    trigger:
      - platform: state
        entity_id: binary_sensor.pir_gang
        to: "on"
    action:
      - service: rest_command.notify_nodered
```

2. I `configuration.yaml`:

```yaml
rest_command:
  notify_nodered:
    url: "http://<NODE_RED_IP>:1880/webhook/bevaegelse"
    method: POST
```

3. I Node-RED:

   * `http in` node på `/webhook/bevaegelse`
   * Udløs et flow eller send til MQTT

---

## 🔁 Eksempel 2 – Node-RED sender til HA

* Brug `http request` node til at kalde `rest_command`
* Alternativt: Send MQTT som HA allerede abonnerer på

---

## 🔄 Eksempel 3 – WebSocket-integration

1. Installer Home Assistant WebSocket i Node-RED palette
2. Autentificér med token
3. Brug `events: state`, `call service`, `get entities`, osv.
4. Reager på ændringer direkte i HA

---

## 🧠 Refleksion

* Hvornår er det bedst at bruge REST, og hvornår MQTT?
* Hvad er fordelene ved websocket-integration?
* Hvordan kan du sikre, at flows og automation ikke konflikter?

---

📌 Home Assistant og Node-RED er et stærkt makkerpar – REST, MQTT og websockets muliggør samarbejde og fleksibilitet på tværs af systemer og enheder.
