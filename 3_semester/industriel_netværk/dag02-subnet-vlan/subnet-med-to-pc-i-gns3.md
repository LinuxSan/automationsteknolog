# 🖧 Subnetting med to PC’er i GNS3

## 📝 Formål

Formålet er at lære at dele et netværk op i subnet og forstå, hvordan adressering påvirker kommunikation mellem to enheder.

## 🎯 Kompetencer

- Kan opbygge et simpelt netværk i GNS3
- Kan tildele IP-adresser i forskellige subnet
- Kan forudsige og teste, om to PC’er kan kommunikere på tværs af subnet
- Kan dokumentere og reflektere over netværksopsætning

---

## Opgave: Sådan gør du

### 1. Opsætning i GNS3

1. Opret et nyt GNS3-projekt (fx “SubnetToPC”)
2. Indsæt:
    - **2 x VPCS** (Virtual PC)
    - **1 x Ethernet Switch**
3. Forbind begge PC’er til switchen

### 2. Tildel IP-adresser i forskellige subnet

- Til **VPCS1**:
```

ip 192.168.10.10/24 192.168.10.1

```
- Til **VPCS2**:
```

ip 192.168.20.10/24 192.168.20.1

```
*(Her er de i hvert sit subnet: .10.0/24 og .20.0/24)*

### 3. Test forbindelsen

- På **VPCS1**:
```

ping 192.168.20.10

```
- På **VPCS2**:
```

ping 192.168.10.10

```
- **Spørgsmål:** Kan PC’erne nå hinanden?  
- Forklar hvorfor/hvorfor ikke.

---

## 📷 Dokumentation

- Tag screenshot af:
  - Dit netværk i GNS3
  - Ping-forsøg fra begge PC’er

---

## Refleksion

- Hvad skete der, da du pingede mellem subnettene?
- Hvorfor er subnetting vigtigt i industrielt netværk?

---

Når du forstår subnetting, er du klar til at koble flere segmenter sammen senere!

**Sig til hvis du vil have næste trin (samme subnet, derefter router/gateway, så VLAN, osv.)!**
