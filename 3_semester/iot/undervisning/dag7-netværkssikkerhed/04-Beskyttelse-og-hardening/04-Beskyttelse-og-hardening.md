# 🧪 Opgaver – Netværkssikkerhed Afsnit 04: Beskyttelse og hardening

Disse øvelser hjælper dig med at arbejde praktisk med beskyttelse af IoT-systemer – både via netværksopsætning og protokolvalg. Opgaverne er enkle og vejledende.

---

## 🟢 Opgave 1 – Identificér usikre forbindelser

**Formål:** Brug Wireshark til at finde trafik uden kryptering.

**Trin-for-trin:**

1. Fang trafik fra en ESP32 eller MQTT-klient, der kommunikerer med en broker
2. Brug filter:

```
mqtt || http || modbus
```

3. Kig på payload:

   * Er den læsbar?
   * Er brugerinfo, sensordata eller kommandoer synlige?

**Svar:**

* Hvilke forbindelser bør erstattes med TLS/DTLS?

---

## 🟠 Opgave 2 – Evaluer adgangssikkerhed

**Formål:** Undersøg dine enheders adgangssikkerhed

**Trin-for-trin:**

1. Tjek en ESP32, Raspberry Pi eller broker
2. Svar på:

   * Er adgangskoden ændret fra standard?
   * Er der nogen services åbne (fx port 80, 1883)?
   * Er der login-logning eller adgangslogs?

**Bonus:** Brug `nmap` til at scanne en IP:

```bash
nmap -p 1-10000 <ip-adresse>
```

---

## 🔵 Opgave 3 – Segmentér med firewall eller VLAN (teoretisk eller GNS3)

**Formål:** Forstå og evt. simulér netværksadskillelse

**Trin-for-trin:**

1. Tegn et netværk med:

   * IoT-enheder i ét segment
   * Admin-enheder i et andet
2. Tænk over:

   * Hvilken trafik bør tillades?
   * Hvordan kan du begrænse uønsket adgang?
3. Hvis muligt: Implementér det i GNS3, MikroTik eller pfSense

---

## 🧠 Refleksion

* Hvad er den største sikkerhedsrisiko i dit netværk lige nu?
* Hvordan kan du sikre, at fremtidige enheder er korrekt konfigureret fra starten?
* Hvilken praksis vil du indføre som standard fremover?

---

📌 Disse øvelser klæder dig på til at opbygge sikrere IoT-miljøer – både i undervisning og virkelige projekter.
