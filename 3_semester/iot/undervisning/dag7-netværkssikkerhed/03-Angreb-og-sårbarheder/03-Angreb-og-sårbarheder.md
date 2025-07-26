# 🧪 Opgaver – Netværkssikkerhed Afsnit 03: Angreb og sårbarheder

Disse opgaver hjælper dig med at forstå og observere typiske netværksangreb i IoT-miljøer. Øvelserne er vejledende og kræver kun basal opsætning i fx Wireshark eller GNS3.

---

## 🟢 Opgave 1 – Identificér sårbarheder

**Formål:** Brug Wireshark til at finde usikkerheder i almindelig trafik.

**Trin-for-trin:**

1. Start Wireshark og fang trafik fra fx en ESP32 der sender til MQTT-broker
2. Brug filter:

```
mqtt || coap || modbus
```

3. Kig i pakkernes indhold – kan du:

   * Se brugernavne, kodeord eller payload?
   * Identificere protokollen og portnummeret?

> 📌 Hvis du kan læse indhold direkte, er det klartekst og sårbart

---

## 🟠 Opgave 2 – Se efter brute force-mønstre

**Formål:** Simulér mange forkerte login-forsøg og se hvad det ligner i netværkstrafik.

**Trin-for-trin:**

1. Brug en MQTT-klient (fx `MQTT.fx`) og forbind gentagne gange med forkert kode
2. Fang trafikken i Wireshark med filter:

```
mqtt
```

3. Læg mærke til:

   * Hvor mange gentagelser vises?
   * Er det muligt at spotte mønstre i IP/port/interval?

---

## 🔵 Opgave 3 – Find "falske" adresser

**Formål:** Brug GNS3 eller dit netværk til at finde ukendte eller "spoofede" enheder

**Trin-for-trin:**

1. Fang netværkstrafik og brug filter:

```
arp
```

2. Kig på MAC/IP-par og se efter:

   * To IP’er med samme MAC?
   * Ændrede MAC’er for kendte IP-adresser?
3. Svar på:

   * Hvad kan dette indikere?
   * Hvorfor er det problematisk?

---

## 🧠 Refleksion

* Hvorfor er det vigtigt at opdage spoofing hurtigt?
* Hvad kan konsekvenserne være af åbne porte og default passwords?
* Hvordan kan du bruge Wireshark og GNS3 til forebyggelse?

---

📌 Husk: Disse øvelser simuleres i et sikkert miljø – du må aldrig angribe rigtige systemer uden tilladelse.
