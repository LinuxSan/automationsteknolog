# 🔁 REST-automation og webhooks i Home Assistant

Denne opfølgende opgave lærer dig at sende og modtage REST-kald i Home Assistant, så du kan integrere med eksterne systemer og sende styringskommandoer via HTTP.

---

## 🎯 Læringsmål

* Du kan bruge webhook-trigger i Home Assistant
* Du kan sende REST POST-anmodninger til Home Assistant
* Du forstår forskellen mellem `rest_command` og `webhook`-triggers

---

## 📡 Trin 1 – Lav en webhook-trigger i Home Assistant

1. Gå til din `automations.yaml` eller brugerflade
2. Opret en automation med webhook-trigger:

```yaml
automation:
  - alias: "Webhook aktiverer lampe"
    trigger:
      - platform: webhook
        webhook_id: tænd_lampe
    action:
      - service: light.toggle
        target:
          entity_id: light.stue_lampe
```

3. Genstart Home Assistant
4. Test webhook fra terminal:

```bash
curl -X POST https://<DIN_HA_IP>:8123/api/webhook/tænd_lampe
```

> Hvis du ser lyset skifte tilstand, virker din REST trigger.

---

## 🧾 Trin 2 – Brug `rest_command` til at sende data ud

1. I `configuration.yaml`, tilføj:

```yaml
rest_command:
  send_status_til_node_red:
    url: "http://<NODE_RED_IP>:1880/api/status"
    method: post
    headers:
      Content-Type: application/json
    payload: '{"status": "alarm_triggered", "timestamp": "{{ now() }}"}'
```

2. Lav en automation som kalder `rest_command.send_status_til_node_red` når en alarm aktiveres.

---

## 🔧 Trin 3 – Simuler ekstern kontrol fra Node-RED

1. Lav en inject-node i Node-RED
2. Tilslut en `http request` node:

   * Method: POST
   * URL: `http://<HA_IP>:8123/api/webhook/tænd_lampe`
3. Test og se om Home Assistant reagerer

---

## 💡 Udvidelser

* Lav flere webhooks: fx `sluk_lampe`, `start_ventilation`, `aktiver_scene`
* Send status tilbage til Home Assistant som REST sensor
* Brug IFTTT eller GitHub Actions til at kalde din webhook

---

## 🧠 Refleksion

* Hvordan kan du sikre at en webhook ikke misbruges?
* Hvad ville REST POST bruges til i en professionel integration?
* Hvorfor er stateless REST et godt valg til automatisering?

---

📌 Disse øvelser viser, hvordan Home Assistant både kan **modtage kommandoer** og **sende status** via REST – og dermed blive en aktiv deltager i et større IoT-økosystem.
