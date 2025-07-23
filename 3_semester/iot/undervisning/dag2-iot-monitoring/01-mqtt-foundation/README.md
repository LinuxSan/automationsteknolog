# 🧠 MQTT Foundation – Øvelser med Læringsmål og Refleksion

Disse øvelser hjælper dig med at forstå, konfigurere og anvende MQTT i praksis. Du arbejder både med terminal, Mosquitto broker og Node-RED.

> ⚠️ **Forudsætning:** Du skal have Mosquitto og Mosquitto-clients installeret på din maskine, og brokeren skal køre. Se evt. installationsvejledningen i `3_semester/iot/hardware-og-software/mosquitto-install/`.

---

## 🔧 Del 1 – MQTT med terminal (Mosquitto broker kører allerede)

### 🎯 Læringsmål

* Du forstår forskellen på publisher og subscriber
* Du kan sende og modtage beskeder via terminal
* Du kan bruge forskellige topics aktivt og systematisk

### 1.1 Test basisfunktion: pub/sub

Åbn to terminaler:

**Terminal 1 – Subscriber:**

```bash
mosquitto_sub -h localhost -t test/besked
```

**Terminal 2 – Publisher:**

```bash
mosquitto_pub -h localhost -t test/besked -m "Hej fra terminal"
```

> 🔍 **Overvej:** Hvad sker der, hvis du publicerer før subscriber er startet?

---

### 1.2 Brug flere topics og send værdier

1. Start subscriber på specifik topic:

```bash
mosquitto_sub -h localhost -t "sensor/temp"
```

2. Send forskellige værdier:

```bash
mosquitto_pub -h localhost -t "sensor/temp" -m "21.5"
mosquitto_pub -h localhost -t "sensor/temp" -m "22.1"
```

> 🔎 **Diskutér:** Hvordan kan topic-navngivning bruges til at strukturere større systemer?

---

## 🧰 Del 2 – MQTT i Node-RED med lokal broker

### 🎯 Læringsmål

* Du kan oprette og bruge en MQTT-integration i Node-RED
* Du kan publicere og subscribere mellem Node-RED og terminalen
* Du kan debugge beskeder og forstå flowet af data

### 2.1 Node-RED subscriber

1. Træk en **mqtt in** og en **debug** node ind
2. MQTT in:

   * Server: `localhost`
   * Topic: `sensor/temp`
3. Forbind → deploy
4. I terminal:

```bash
mosquitto_pub -h localhost -t "sensor/temp" -m "23.8"
```

> 🧪 **Se output i debug-vinduet**

---

### 2.2 Node-RED publisher

1. Træk en **inject** og en **mqtt out** node ind
2. mqtt out:

   * Topic: `control/relay1`
3. Forbind inject → mqtt out
4. Tryk på inject

Terminal test:

```bash
mosquitto_sub -h localhost -t "control/relay1"
```

> 🔍 **Tænk:** Hvad skal modtage denne besked i et rigtigt system? En ESP32? Et dashboard?

---

### 🧠 Refleksion

* Hvordan kan pub/sub give fleksibilitet i et system?
* Hvad kan gå galt, hvis du ikke har styr på dine topics?
* Hvordan ville du bruge dette til at bygge et styringssystem?

---

## 📋 Afsluttende opgaver

* Lav et komplet testflow mellem terminal og Node-RED
* Brug mindst 2 forskellige topics og 2 retninger (Node-RED → terminal og omvendt)
* Dokumentér dit flow med screenshots eller forklaring

---

## 🏁 Klar til næste modul?

Når du mestrer pub/sub både i terminal og Node-RED, er du klar til at koble fysiske enheder (ESP32, sensorer, aktuatorer) og bygge IIoT-flows.

