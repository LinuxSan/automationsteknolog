# 🌐 Netværkssikkerhed – Ekstra modul: Analyse og sikring af MQTT-trafik

Dette ekstra modul fokuserer på praktisk analyse og beskyttelse af MQTT-trafik i IoT-systemer. Du lærer, hvordan MQTT ser ud i Wireshark, hvordan ukrypteret kommunikation kan opsnappes, og hvordan du beskytter trafikken med TLS.

---

## 🔍 Del 1 – Analyse af ukrypteret MQTT

MQTT er en populær publish/subscribe-protokol i IoT, som typisk kører over TCP port 1883 – ofte uden kryptering.

### Eksempel på klartekst-analyse:

1. Start en MQTT-klient (fx ESP32 eller MQTT.fx) og forbind til en broker uden TLS
2. Start Wireshark og vælg din netværksinterface
3. Brug filter:

```wireshark
mqtt
```

4. Find en MQTT CONNECT eller PUBLISH-pakke og undersøg:

   * Brugernavn og kodeord (i CONNECT)
   * Topic og payload (i PUBLISH)

> 💡 Mange MQTT-brokere tillader ukrypteret login og dataoverførsel – let at aflæse med Wireshark

---

## 🔐 Del 2 – Beskyttelse med TLS (MQTTS)

TLS (Transport Layer Security) kan beskytte MQTT ved at kryptere forbindelsen. Det bruges typisk over port 8883.

### Effekten af TLS:

Når TLS er aktiv:

* Wireshark ser forbindelsen som "TLS" eller "Encrypted Application Data"
* Brugernavn, kodeord, topic og payload er ikke læsbare

> 🛑 TLS kræver både broker og klient med certifikatsupport

---

## 📘 Sammenligning: Ukrypteret vs. sikret MQTT

| Funktion               | MQTT (1883)     | MQTTS (8883 + TLS)     |
| ---------------------- | --------------- | ---------------------- |
| Læsbar payload         | Ja              | Nej                    |
| Brugernavn/kodeord     | Ja              | Nej                    |
| Risiko for MITM        | Høj             | Lav                    |
| Kan angriber abonnere? | Ja (ingen auth) | Ikke uden certifikater |

---

## 🧪 Opgaver

### 🟢 Opgave 1 – Opsnap en MQTT-pakke

1. Start en MQTT-klient og broker uden TLS
2. Start Wireshark og fang trafik
3. Brug filter: `mqtt`
4. Dokumentér:

   * Topic
   * Payload
   * Brugernavn/kodeord (hvis relevant)

### 🟠 Opgave 2 – Aktivér TLS (MQTTS)

1. Opsæt en MQTT-broker med TLS (fx Mosquitto med certifikat)
2. Brug klient med TLS-understøttelse (fx MQTT.fx, ESP32, Python)
3. Fang trafikken i Wireshark og filtrér med:

```wireshark
tcp.port == 8883
```

4. Besvar:

   * Er payload synlig?
   * Hvordan ved du, at TLS er aktiv?

### 🔵 Opgave 3 – Sammenlign

1. Sammenlign to forbindelser: én via port 1883, én via 8883
2. Notér forskelle i:

   * Læsbarhed
   * Protokol-identifikation
   * Sikkerhed

---

📌 Dette modul hjælper dig med at forstå hvorfor MQTT-sikkerhed er vigtig og hvordan Wireshark kan bruges til både at identificere sårbarheder og verificere beskyttelse.
