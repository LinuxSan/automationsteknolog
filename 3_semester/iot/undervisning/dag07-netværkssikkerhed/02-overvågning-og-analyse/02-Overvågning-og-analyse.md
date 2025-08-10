# 🧪 Opgaver – Netværkssikkerhed Afsnit 02: Overvågning og analyse

Disse opgaver hjælper dig med at bruge Wireshark til at fange og analysere trafik fra IoT-enheder. Øvelserne er vejledende og trin-for-trin, så du kan arbejde i dit eget tempo.

---

## 🟢 Opgave 1 – Fang trafik fra din ESP32

**Formål:** Lær at bruge Wireshark til at overvåge netværkstrafik fra en ESP32.

**Trin-for-trin:**

1. Start Wireshark og vælg din aktive netværksinterface (fx Wi-Fi)
2. Start fangst ved at trykke på "Start capturing packets"
3. Tænd/aktiver din ESP32, som sender fx MQTT-data
4. I Wireshark, anvend dette filter:

```
ip.addr == <ESP32 IP>
```

5. Find en pakke fra ESP32 og åbn den i "Packet Details"
6. Svar på:

   * Hvilken IP har din ESP32?
   * Hvad er destinationens IP og port?

---

## 🟠 Opgave 2 – Find protokoller i klartekst

**Formål:** Identificér kommunikation uden kryptering.

**Trin-for-trin:**

1. Start fangst i Wireshark mens du har fx MQTT, CoAP eller HTTP i gang
2. Brug filter:

```
mqtt || http || coap
```

3. Kig på pakkerne og åbn payload-feltet
4. Svar på:

   * Kan du læse indholdet direkte?
   * Er der brugernavne, sensordata eller kommandoer i klartekst?

---

## 🔵 Opgave 3 – Filtrér efter specifik kommando

**Formål:** Lær at finde bestemte beskeder i trafikken.

**Trin-for-trin:**

1. Brug filteret:

```
frame contains "ON"
```

2. Find en pakke med "ON" som del af payload
3. Svar på:

   * Hvilken protokol blev brugt?
   * Hvilken enhed sendte kommandoen?

> 📌 Dette er nyttigt ved fejlsøgning i fx aktuatorkontrol

---

## 🧠 Refleksion

* Hvor let er det at se ukrypteret data i et åbent netværk?
* Hvilke filtre oplevede du som mest nyttige?
* Hvordan kunne du bruge denne viden til at forbedre sikkerheden i dit system?

---

📌 Du er nu klar til at gå videre til næste afsnit, hvor vi ser på angreb og sårbarheder.
