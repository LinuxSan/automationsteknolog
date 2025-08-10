# ⚙️ Dag 4 – Home Assistant 04: Aktuatorer

I denne lektion arbejder vi med aktuatorer i Home Assistant – altså enheder du kan styre (fx lys, relæer, kontakter). Du lærer at konfigurere og kontrollere dem via UI, MQTT og automations.

---

## 🎯 Læringsmål

* Forstå hvad en aktuator er i HA
* Opsætte og teste styring via dashboard og automations
* Forstå MQTT-kontrol af aktuatorer

---

## 🔌 Hvad er en aktuator?

En aktuator er en enhed, der kan ændre tilstand efter en kommando:

* Tænd/sluk lys
* Aktivér relæ
* Lås dør
* Skift farve/intensitet på LED

I HA vises de typisk som `switch`, `light`, `lock`, `cover`, `fan` osv.

---

## 🔁 Dataflow for styring

1. Bruger klikker UI-knap eller automation aktiveres
2. Home Assistant sender kommando via fx MQTT, Zigbee, REST
3. Enhed reagerer og bekræfter status
4. Status vises i dashboard

---

## 🧪 Eksempel: MQTT-switch discovery

```json
Topic: homeassistant/switch/lampe/config
Payload:
{
  "name": "Loftlampe",
  "command_topic": "smarthouse/lampe/set",
  "state_topic": "smarthouse/lampe",
  "payload_on": "ON",
  "payload_off": "OFF",
  "unique_id": "loft_lampe_01"
}
```

> Når payload er sendt og enheden svarer, vises en kontakt i HA

---

## 🕹 UI-styring

* Brug `button card` eller `entities` card
* `light.turn_on`, `switch.turn_off`, `cover.open_cover`, osv.
* Kombinér med automation (fx tænd lys ved bevægelse)

---

## ⚙️ Automation eksempel

```yaml
automation:
  - alias: "Sluk lys kl 23"
    trigger:
      - platform: time
        at: "23:00:00"
    action:
      - service: switch.turn_off
        target:
          entity_id: switch.loftlampe
```

---

## 🧠 Refleksion

* Hvordan sikrer du, at status og fysisk tilstand matcher?
* Hvad er forskellen på at sende kommando og modtage status?
* Hvilke typer aktuatorer bruger du i dit projekt?

---

📌 Aktuatorer gør Home Assistant til en aktiv platform – ikke kun observerende, men styrende og reaktiv.
