# 🧪 Opgaver – Home Assistant og Node-RED Kommunikation

Disse øvelser guider dig i at integrere Home Assistant og Node-RED via REST, Webhooks og MQTT. Du lærer at udveksle data og styre funktioner på tværs af systemerne.

---

## 🟢 Opgave 1 – Trigger webhook fra Home Assistant

1. I HA: Opret en automation som udløses af fx sensor eller tidspunkt
2. I `configuration.yaml` tilføj:

```yaml
rest_command:
  trigger_node_red:
    url: "http://<NODE_RED_IP>:1880/webhook/alert"
    method: POST
```

3. Opret automation der kalder `rest_command.trigger_node_red`
4. I Node-RED: Tilføj en `http in` node på `/webhook/alert` og forbind til `debug`

✅ *Tjek at Node-RED modtager og logger webhook data*

---

## 🔵 Opgave 2 – Node-RED sender til Home Assistant via rest\_command

1. I Home Assistant: Tilføj `rest_command.toggle_lampe`:

```yaml
rest_command:
  toggle_lampe:
    url: "http://homeassistant.local:8123/api/services/switch/toggle"
    method: POST
    headers:
      authorization: "Bearer DIT_LONG_LIVED_TOKEN"
    content_type: "application/json"
    payload: '{"entity_id": "switch.loftlampe"}'
```

2. I Node-RED: Brug `http request` node til at kalde denne URL
3. Udløs HTTP-kald fra fx `inject` node

✅ *Tjek at lampen toggles i Home Assistant ved flow-aktivering*

---

## 🟡 Opgave 3 – Lyt til tilstande med HA WebSocket i Node-RED

1. Installer `node-red-contrib-home-assistant-websocket`
2. Tilføj node `events: state`
3. Vælg en entitet (fx `sensor.stue_temperature`)
4. Log data i `debug` node

✅ *Node-RED opfanger alle tilstandsændringer fra HA i realtime*

---

## 🔁 Opgave 4 – Brug MQTT som mellemled

1. I Node-RED: Publicér til MQTT topic (fx `alert/status`) ved event
2. I HA: Lyt på topic via MQTT-sensor eller automation trigger
3. Alternativ: HA sender besked til `node-red/input` topic

✅ *Begge systemer kan sende/modtage beskeder via broker*

---

## 🧠 Refleksion

* Hvornår er webhook bedst – og hvornår bør du bruge MQTT?
* Hvad er fordelene ved websocket-integration frem for REST?
* Hvordan kan Node-RED hjælpe med at udvide HA-logik?

---

📌 Samspillet mellem Home Assistant og Node-RED muliggør fleksibel styring, avanceret logik og uafhængige flows – med REST, MQTT og websockets som bindeled.
