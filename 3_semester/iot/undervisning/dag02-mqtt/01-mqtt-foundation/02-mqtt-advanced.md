# 📦 MQTT Avanceret Funktionalitet – QoS, Retain, Last Will

Dette dokument bygger videre på det grundlæggende MQTT-arbejde og introducerer mere avancerede emner, som er vigtige i driftssikre og intelligente IoT-systemer. Du lærer gennem opgaver og refleksion.

> ⚠️ **Forudsætning:** Du har gennemført "MQTT Foundation" og har Mosquitto-broker kørende.

---

## 🔁 Del 1 – QoS (Quality of Service)

### 🎯 Læringsmål

* Du forstår forskellen på QoS 0, 1 og 2
* Du kan teste hvordan QoS påvirker levering og stabilitet

### 1.1 Sammenlign QoS-niveauer

Åbn to terminaler – brug forskellige QoS-værdier:

```bash
mosquitto_sub -t test/qos -q 0
mosquitto_pub -t test/qos -q 0 -m "QoS 0 besked"
```

Skift til:

```bash
mosquitto_sub -t test/qos -q 1
mosquitto_pub -t test/qos -q 1 -m "QoS 1 besked"
```

Og til:

```bash
mosquitto_sub -t test/qos -q 2
mosquitto_pub -t test/qos -q 2 -m "QoS 2 besked"
```

> 🔎 **Refleksion:** Hvornår er det vigtigt at sikre at beskeden bliver leveret præcist én gang?

---

## 📌 Del 2 – Retained Messages

### 🎯 Læringsmål

* Du kan sende retained beskeder og forstå hvordan de bruges

### 2.1 Send en retained besked

```bash
mosquitto_pub -t status/rum1 -r -m "Lys tændt"
```

Subscriber senere:

```bash
mosquitto_sub -t status/rum1
```

> Du burde få beskeden med det samme, selvom du ikke var tilsluttet før.

> 🔍 **Diskutér:** Hvordan adskiller retained fra realtime-pub/sub?

---

## 🕊️ Del 3 – Last Will & Testament (LWT)

### 🎯 Læringsmål

* Du kan konfigurere en klient til at sende en LWT-besked ved uventet afbrydelse

### 3.1 Simuler nedbrud med LWT

Start en klient med LWT:

```bash
mosquitto_sub -t status/plc1 &
mosquitto_pub -t status/plc1 -i plc1 -l --will-topic status/plc1 --will-message "offline" --will-qos 1
```

Afslut processen med `Ctrl+C`, og observer "offline" beskeden i en anden subscriber.

> 🧠 **Refleksion:** Hvorfor er LWT vigtigt i overvågningssystemer og alarmer?

---

## 🧪 Del 4 – Node-RED og avancerede egenskaber

### 🎯 Læringsmål

* Du kan konfigurere QoS og retained i Node-RED MQTT-noder
* Du forstår hvordan Last Will bruges med sensorer eller gateways

### 4.1 Test retained fra Node-RED

1. Brug **inject** → **mqtt out**
2. Sæt retained til "true" og QoS til 1
3. Subscriber via terminal og observer resultat

> 🔧 Du kan også simulere sensorstatus og vise det i Node-RED dashboard

---

## 📝 Afsluttende refleksion

* Hvad er forskellen mellem stabilitet og aktualitet?
* Hvornår giver det mening at bruge QoS 0 vs 2?
* Hvordan kan Last Will forbedre pålidelighed i dit system?

---

📘 Klar til at integrere dine MQTT-kundskaber i virkelige IoT-løsninger!

