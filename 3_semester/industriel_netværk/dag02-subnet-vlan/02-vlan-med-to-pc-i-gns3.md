# 🟦 VLAN med to PC’er i GNS3

## 📝 Formål

Formålet er at give dig praktisk erfaring med VLAN-segmentering, så du kan se, hvordan VLAN bruges til at opdele netværk – også i virtuelle miljøer.

## 🎯 Kompetencer

- Kan konfigurere VLAN på en (simuleret) Router i GNS3
- Forstår, hvordan VLAN adskiller trafik mellem enheder på samme fysiske netværk
- Kan teste kommunikation mellem PC’er i samme og forskellige VLAN
- Kan dokumentere VLAN-opsætning og resultater

---

## Opgave: Sådan gør du

### 1. Opsætning i GNS3

1. Opret et nyt projekt (fx “VLANtoPC”)
2. Indsæt:
    - **2 x VPCS**
    - **1 x Ethernet Router** (vælg fx “Ethernet Router” eller “Managed Router” hvis tilgængelig)
3. Forbind begge PC’er til Routeren

### 2. Konfigurer VLAN (i GNS3)

- Brug en **Managed Router** (fx GNS3s “Ethernet Router” eller “Cisco IOSv Router” hvis du har licens)
    - Hvis din Router har en web/CLI, opret to VLAN:
      - VLAN 10: Port 1 (PC1)
      - VLAN 20: Port 2 (PC2)
    - Alternativ: Forklar hvordan du ville gøre det på rigtig udstyr, hvis din GNS3-Router ikke understøtter VLAN.

### 3. Tildel IP-adresser (samme subnet)

- Til **VPCS1**:
```

ip 192.168.10.10/24 192.168.10.1

```
- Til **VPCS2**:
```

ip 192.168.10.20/24 192.168.10.1

```

### 4. Test forbindelsen

- På **VPCS1**:
```

ping 192.168.10.20

```
- På **VPCS2**:
```

ping 192.168.10.10

```
- **Skift VLAN:**  
- Sæt begge PC’er i samme VLAN → Test ping (det skal virke)
- Sæt PC’erne i hver sit VLAN → Test ping (det skal fejle)

---

## 📷 Dokumentation

- Tag screenshots af:
  - Netværk i GNS3
  - Router-konfiguration (hvis muligt)
  - Ping-resultater i begge tilfælde (samme vs. forskellige VLAN)

---

## Refleksion

- Hvad observerede du, da PC’erne var i samme VLAN – og i hver sit?
- Hvorfor er VLAN et nyttigt værktøj i industrielle netværk?

---

Når du mestrer VLAN, kan du begynde at bygge sikre og overskuelige netværk til industrien!
