# 🌐 Netværkssikkerhed – Ekstra modul: Analyse og risikovurdering af Modbus TCP

Dette modul fokuserer på netværksanalyse af Modbus TCP – en almindeligt anvendt protokol i industriel automation. Du lærer, hvordan du identificerer og analyserer Modbus-trafik med Wireshark, og hvorfor protokollen er særlig sårbar uden yderligere sikkerhedslag.

---

## 📦 Hvad er Modbus TCP?

Modbus TCP er en simpel master/slave-protokol, der kører over TCP (typisk port 502). Den bruges til at læse og skrive data i registre på industrielle enheder som motorstyringer, målere og I/O-moduler.

Eksempel:

```
Læse holding register 0x0001 på slave 1
```

Modbus TCP indeholder ikke nogen form for kryptering eller autentificering.

---

## 🔍 Analyse med Wireshark

1. Start en Modbus TCP-server (fx ESP32, simulator eller PLC)
2. Brug en klient (fx Node-RED, pymodbus eller ModScan) til at sende forespørgsler
3. Start Wireshark og vælg aktiv netværksinterface
4. Brug filter:

```wireshark
tcp.port == 502
```

### Undersøg i Wireshark:

* Function Code (fx 0x03 = Read Holding Register)
* Adresse og antal registre
* Payload (typisk integer, float, bit-array)

> 💡 Wireshark kan fortolke Modbus TCP automatisk og vise læsbare felter

---

## ⚠️ Sikkerhedsproblemer

| Risiko                | Forklaring                             |
| --------------------- | -------------------------------------- |
| Klartekst-data        | Alle værdier er direkte læsbare        |
| Ingen autentificering | Alle kan sende forespørgsler           |
| Ingen adgangskontrol  | Enhver klient kan læse/skrive registre |
| Ingen kryptering      | Kan nemt opsnappes og manipuleres      |

Modbus TCP er velegnet i lukkede netværk, men kræver ekstra beskyttelse i IoT-sammenhæng.

---

## 🔐 Beskyttelse og afhjælpning

Modbus TCP kan sikres ved at placere det bag:

* VPN eller krypteret tunnel (WireGuard, OpenVPN)
* Gateway der oversætter til fx MQTT over TLS
* Firewall der begrænser adgang til port 502
* Netværkssegmentering (kun lokale adgangspunkter)

> 🚫 Det er sjældent muligt at tilføje TLS direkte til Modbus TCP – det håndteres i netværkslaget

---

## 🧪 Opgaver

### 🟢 Opgave 1 – Fang Modbus TCP-trafik

1. Start en klient der læser et register fra en Modbus TCP-server
2. Fang trafikken i Wireshark og filtrér med `tcp.port == 502`
3. Dokumentér:

   * IP-adresser
   * Function Code
   * Registeradresse
   * Payload (fx værdi læst)

### 🟠 Opgave 2 – Manipuler eller gensend (kun i testnetværk)

1. Brug en Modbus test-klient til at sende en "write register"-anmodning
2. Fang pakken og observer hvordan payload er opbygget
3. Diskutér:

   * Hvad kunne en angriber ændre her?
   * Hvilke skader kunne det medføre?

### 🔵 Opgave 3 – Beskyttelsesrefleksion

1. Tegn et netværk med en Modbus TCP-enhed
2. Tilføj komponenter som:

   * Firewall
   * VPN-server
   * Gateway (Modbus → MQTT)
3. Skriv hvordan hver komponent beskytter trafikken

---

📌 Modbus TCP er udbredt men sårbar – især i åbne netværk. Forståelse af dets begrænsninger er afgørende for at kunne beskytte industrielle IoT-løsninger effektivt.
