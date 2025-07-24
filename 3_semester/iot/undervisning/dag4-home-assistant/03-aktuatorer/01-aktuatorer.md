# 🧪 Opgaver – Home Assistant: Aktuatorer

Disse opgaver giver dig praktisk erfaring med opsætning, kontrol og automation af aktuatorer i Home Assistant. Du arbejder med MQTT-discovery, dashboard-interaktion og automatiseret styring.

---

## 🟢 Opgave 1 – Udgiv en aktuator via MQTT Discovery

1. Brug fx Node-RED, MQTT Explorer eller terminal (`mosquitto_pub`)
2. Send følgende konfiguration:

```bash
mosquitto_pub -h localhost -t "homeassistant/switch/lampe/config" -m '{"name": "Loftlampe", "command_topic": "smarthouse/lampe/set", "state_topic": "smarthouse/lampe", "payload_on": "ON", "payload_off": "OFF", "unique_id": "loft_lampe_01"}' -r
```

3. Tjek at Home Assistant viser en ny switch med navnet "Loftlampe"
4. Skift status fra UI og observer MQTT-kommandoer

✅ *Bekræft at kommandoer sendes og state opdateres*

---

## 🔵 Opgave 2 – Brug aktuator i dashboard

1. Gå til dashboardet og redigér visning
2. Tilføj et `Button Card` med handling til `switch.loftlampe`
3. Test funktionen og visuel feedback

✅ *Tilføj også `state_color: true` for farve-feedback*

---

## 🟡 Opgave 3 – Automation: Sluk lys om natten

1. Tilføj følgende automation til `automations.yaml` eller via GUI:

```yaml
automation:
  - alias: "Sluk loftlampe kl 23:00"
    trigger:
      - platform: time
        at: "23:00:00"
    action:
      - service: switch.turn_off
        target:
          entity_id: switch.loftlampe
```

2. Test automationen ved at ændre tidspunktet midlertidigt

✅ *Bekræft at lampen slukkes automatisk*

---

## 🔁 Opgave 4 – Tilføj feedback og status

1. Sørg for at `state_topic` sender korrekt status ("ON" / "OFF")
2. Brug fx Node-RED eller `mosquitto_pub` til at sende:

```bash
mosquitto_pub -h localhost -t "smarthouse/lampe" -m "ON"
```

3. Bekræft at Home Assistant opdaterer status i UI

✅ *Test også om status opdateres ved manuel kommando via broker*

---

## 🧠 Refleksion

* Hvordan kan du verificere at en fysisk aktuator fulgte kommandoen?
* Hvad sker der hvis `state_topic` og `command_topic` ikke stemmer?
* Hvor kunne aktuatorer bruges til sikkerhed, komfort eller energioptimering?

---

📌 Du har nu praktisk erfaring med at integrere aktuatorer i Home Assistant – og at kombinere dem med dashboard, MQTT og automations for styring og kontrol.
