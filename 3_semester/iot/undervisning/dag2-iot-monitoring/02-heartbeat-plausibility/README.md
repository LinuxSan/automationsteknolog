
# 🛡️ MQTT – Systemovervågning og Datavalidering

Dette dokument fokuserer på pålidelighed og fejlhåndtering i MQTT-baserede IoT-systemer. Det dækker teknikker til at opdage og reagere på:

* Enheder der går offline
* Fejl i datalevering
* Usandsynlige eller ugyldige målinger

---

## ❤️ Heartbeat

Heartbeat er en periodisk besked fra en enhed, fx hvert 10. sekund, som fungerer som "livstegn". Hvis den forsvinder, antages det at enheden er offline eller nede.

**Eksempel:**

* Topic: `heartbeat/esp32_1`
* Payload: `online`
* Interval: hver 10 sek.

**Anvendelser:**

* Visning af tilstedeværelse i dashboards
* Automatisk alarm ved manglende heartbeat

Node-RED kan bruges til at oprette en timeout via `delay` eller `rbe` kombineret med `trigger` node.

---

## ⏱️ Watchdog

En watchdog overvåger systemets aktivitet og reagerer, hvis noget går i stå:

### Typer:

* **Software-watchdog** (i fx Node-RED): hvis en besked ikke ankommer i tide, sendes en alarm
* **Hardware-watchdog** (mikrokontroller): hvis kode ikke svarer, genstartes automatisk

**Eksempel i Node-RED:**

* Brug en `trigger` node sat til at vente 30 sekunder på ny besked
* Udebliver den, sendes besked til fx `alerts/plc_offline`

---

## 🧪 Plausibility Check (Sandsynlighedskontrol)

Plausibility checks bruges til at vurdere om målinger giver mening, fx ud fra:

* Realistiske grænser
* Maksimal ændring per tid
* Tidsmæssig stabilitet

### Eksempler:

| Sensor     | Ugyldig værdi                    |
| ---------- | -------------------------------- |
| Temperatur | 150°C i et kølerum               |
| Tankniveau | Hopper fra 10% til 100% på 1 sek |

### Typiske tjek:

* `value < max` og `value > min`
* Brug `switch`, `rbe` og `deadband` i Node-RED
* Kombinér med logging og alarmer

---

## 🔔 Alarmer og Selvheling

Ved fejl kan et system:

* **Logge fejlen** (fx til fil, MQTT-topic eller database)
* **Sende alarm** (fx e-mail, dashboard, MQTT-message)
* **Genstarte proces/flow** (fx via `exec` eller `function` node i Node-RED)

### MQTT-eksempler:

* `alerts/esp32_1` → "offline detected"
* `status/boiler` → "sensor plausibility error"

Disse kan vises i dashboard eller videresendes til vedligeholdelse.

---

## 🧠 Konklusion

MQTT giver fleksibilitet til at opbygge robuste og selvovervågende systemer.
Ved at kombinere heartbeat, watchdogs og plausibility checks kan man sikre:

* Fejldetektion
* Proaktiv alarmering
* Højere systempålidelighed

Brug dette som grundlag for opgaver med smart home, tankovervågning og IIoT-systemer.
