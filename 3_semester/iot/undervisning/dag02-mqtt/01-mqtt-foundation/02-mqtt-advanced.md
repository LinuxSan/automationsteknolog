# 📦 MQTT Avanceret Funktionalitet — QoS, Retain, Last Will

> ⚠️ **Forudsætning:** Mosquitto-broker kører på `localhost:1883`. Klienter installeret:
>
> ```bash
> sudo apt-get update && sudo apt-get install -y mosquitto-clients
> ```

---

## 🔁 Del 1 — QoS (Quality of Service)

🎯 **Mål:** Forstå QoS 0/1/2 og se effekten i praksis.

> Tilføj evt. login: `-u user1 -P 'kode'`

### 1.1 QoS 0 — *best effort*

Terminal A:

```bash
mosquitto_sub -v -t 'test/qos' -q 0
```

Terminal B:

```bash
mosquitto_pub -t 'test/qos' -q 0 -m 'QoS 0 besked'
```

### 1.2 QoS 1 — *mindst én gang*

Terminal A:

```bash
mosquitto_sub -v -t 'test/qos' -q 1
```

Terminal B:

```bash
mosquitto_pub -t 'test/qos' -q 1 -m 'QoS 1 besked'
```

### 1.3 QoS 2 — *præcis én gang*

Terminal A:

```bash
mosquitto_sub -v -t 'test/qos' -q 2
```

Terminal B:

```bash
mosquitto_pub -t 'test/qos' -q 2 -m 'QoS 2 besked'
```

🔎 **Refleksion:** Hvornår kræver du præcis-én-gang (QoS 2) fremfor QoS 1?

---

## 📌 Del 2 — Retained Messages

🎯 **Mål:** Mestre retained til seneste status ved ny tilslutning.

### 2.1 Send retained

```bash
mosquitto_pub -t 'status/rum1' -r -m 'Lys tændt'
```

### 2.2 Abonnér senere og modtag straks

```bash
mosquitto_sub -v -t 'status/rum1'
```

### 2.3 Opdatér retained

```bash
mosquitto_pub -t 'status/rum1' -r -m 'Lys slukket'
```

### 2.4 Slet retained (nul payload)

```bash
mosquitto_pub -t 'status/rum1' -r -n
```

🔍 **Diskussion:** Retained = seneste tilstand. Realtime pub/sub = kun mens man er online.

---

## 🕊️ Del 3 — Last Will & Testament (LWT)

🎯 **Mål:** Udsend “offline” automatisk ved uventet afbrydelse.

### 3.1 Overvåg LWT-topic

Terminal A:

```bash
mosquitto_sub -v -t 'status/plc1'
```

### 3.2 Start klient med Will og birth

Terminal B (holder forbindelsen åben og sætter Will):

```bash
mosquitto_pub -i plc1 \
  --will-topic 'status/plc1' --will-message 'offline' --will-qos 1 --will-retain \
  -t 'status/plc1' -m 'online' -r -l
```

> `-l` = læs linjer fra stdin og hold forbindelsen åben.

### 3.3 Simulér nedbrud

I tredje terminal:

```bash
pkill -9 -f "mosquitto_pub -i plc1"
```

✅ Forvent: `status/plc1 offline` i Terminal A.

> ℹ️ Graceful stop (Ctrl+C i Terminal B) sender **ikke** Will.

🧠 **Refleksion:** Hvorfor er LWT kritisk i overvågning/alarmer?

---

## 🧪 Del 4 — Node-RED: QoS, Retain, Will/Birth

🎯 **Mål:** Brug avancerede egenskaber i Node-RED.

### 4.1 Broker-opsætning

* Samme host: **Server** `127.0.0.1`, **Port** `1883`, **Use WebSockets** off.
* I samme Docker-net som Mosquitto: **Server** `mosquitto`, **Port** `1883`.
* Sæt brugernavn/password hvis krævet. Gem.

### 4.2 Retained + QoS fra Node-RED

1. `inject` → `mqtt out`.
2. Topic `status/rum1`, **QoS = 1**, **Retain = true**.
3. Deploy.
4. Terminal:

   ```bash
   mosquitto_sub -v -t 'status/rum1'
   ```
5. Tryk inject. Stop subscriber. Tryk inject igen. Start subscriber.
   ✅ Forvent retained med det samme.

### 4.3 Will/Birth i brokerconfig

* **Birth**: Topic `status/nodered`, payload `online`, retain on, QoS 1.
* **Will**: Topic `status/nodered`, payload `offline`, retain on, QoS 1.
* Deploy og observer i subscriber.

---

## 🔧 Hurtig fejlfinding

* ❌ Ingen modtagelse: publikér **efter** subscriber er connected eller brug `-r`.
* ❌ `not authorised`: tjek bruger/kode eller midlertidigt `allow_anonymous true`.
* ❌ WebSockets fejler: kræver i Mosquitto:

  ```conf
  listener 9001
  protocol websockets
  ```

  og i Node-RED: **Use WebSockets = on**, port `9001`.
* ❌ Forkert linjeending i `mosquitto.conf`:

  ```bash
  sudo apt-get install -y dos2unix && dos2unix mosquitto.conf
  ```

---

## ✅ Opsummering

* **QoS** styrer leveringssikkerhed (0/1/2).
* **Retain** giver seneste status til nye abonnenter.
* **LWT** giver automatisk “offline” ved uventet disconnect.
* **Node-RED** kan sætte QoS/Retain og Birth/Will centralt i broker-config.
