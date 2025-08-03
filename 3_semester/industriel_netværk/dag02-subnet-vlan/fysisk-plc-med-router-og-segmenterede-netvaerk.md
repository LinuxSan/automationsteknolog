# 🟧 Fysisk PLC med router og to segmenterede netværk

## 📝 Formål

Formålet er at lære at segmentere netværk via en router – og koble en fysisk PLC sammen med to forskellige netværkssegmenter.  
Du får erfaring med, hvordan industrielle netværk adskilles og forbindes i praksis – uden brug af managed switch.

## 🎯 Kompetencer

- Kan opbygge et netværk med flere segmenter i GNS3 og fysisk miljø
- Kan tildele og dokumentere IP-adresser og subnet til både virtuelle og fysiske enheder
- Kan konfigurere router til at forbinde flere segmenter/subnets
- Kan teste og dokumentere netværksforbindelse mellem PC’er og PLC
- Kan tegne og forklare et netværksdiagram for en industriel netværksløsning

---

## Opgave: Sådan gør du

### 1. Netværksopbygning

1. **Router (GNS3 eller fysisk):**
    - Brug fx en Cisco-router eller tilsvarende i GNS3 (eller skolens fysiske router hvis muligt)
    - Routeren skal have mindst to interfaces (fx G0/0 og G0/1)
2. **Unmanaged switches:**
    - Brug simple switches til at forbinde flere enheder på hvert netværk (fx GNS3 “Ethernet Switch”)
3. **Fysisk PLC:**
    - Tilslut PLC til en af routerens interfaces (via switch hvis flere enheder på samme subnet)
4. **Virtuelle PC’er (GNS3):**
    - Én PC i hvert subnet (segment)

---

### 2. IP-adresser og subnet

- **Subnet 1 (fx “Produktion”):**
    - PLC: `192.168.10.100/24`
    - PC1: `192.168.10.10/24`
    - Gateway: `192.168.10.1` (routerens interface til dette subnet)
- **Subnet 2 (fx “Service/Admin”):**
    - PC2: `192.168.20.10/24`
    - Gateway: `192.168.20.1` (routerens andet interface)

---

### 3. Router-konfiguration

- **GNS3-router eller fysisk router:**
    - Tildel IP-adresse til begge interfaces:
      - Interface G0/0: `192.168.10.1/24`  *(forbundet til PLC og PC1)*
      - Interface G0/1: `192.168.20.1/24`  *(forbundet til PC2)*
    - Aktiver interface (`no shutdown`)
    - Ingen NAT eller firewall – kun intern routing

---

### 4. Test forbindelsen

- **Fra PC1 til PLC** (samme subnet):  
```

ping 192.168.10.100

```
*(Forventet: Succes)*
- **Fra PC2 til PLC** (på tværs af subnet via router):  
```

ping 192.168.10.100

```
*(Forventet: Succes, hvis routing er sat op korrekt)*

---

### 5. Dokumentation

- Netværksdiagram (tegn i draw.io eller på papir):
  - Router, interfaces/IP, unmanaged switches, PLC, PC1, PC2, subnet-rammer
- Skærmbillede af router-konfiguration (CLI eller GUI)
- Skærmbillede af ping-resultater fra begge PC’er
- Kort tekst: Hvordan hænger det hele sammen?

---

## Refleksion

- Hvorfor er det en fordel at segmentere netværket med router fremfor (kun) switches?
- Hvilke fordele giver det i forhold til sikkerhed og drift i industrien?
- Hvilke problemer kan opstå, hvis netværkssegmenter ikke er ordentligt konfigureret?

---

Når du kan segmentere og forbinde fysiske og virtuelle netværk via router, har du lært en af de vigtigste OT/IT-broer i praksis! 🛠️🌐

**Sig til hvis du ønsker konkret router-konfigurationskode, eller ønsker opgaven tilrettet til specifikt PLC-mærke!**
