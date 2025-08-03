# 🌐 Segmentér med subnet og VLAN (GNS3 + fysisk PLC)

## 📝 Formål

Formålet er at lære, hvordan man opdeler et netværk i subnet og VLAN – og ser effekten i både virtuelle og fysiske enheder.  
Du lærer at opsætte VLAN og subnet i GNS3, konfigurere din (fysiske) PLC til at passe ind, og dokumentere hele processen.

## 🎯 Kompetencer

- Kan konfigurere subnet og VLAN i GNS3
- Kan koble virtuel og fysisk udstyr sammen på netværket
- Kan anvende grundlæggende netværksdesign i praksis
- Kan tegne netværksdiagram med både virtuelle og fysiske enheder

---

## Opgave: Sådan gør du

### 1. Opsætning i GNS3

1. Opret et nyt GNS3-projekt (fx “SubnetVLAN-PLC”).
2. Indsæt:
    - Min. **2 x VPCS** (virtuelle PC’er)
    - **1 x Ethernet Switch**
    - Evt. **Ubuntu Docker** eller flere PC’er hvis du ønsker

### 2. Opret subnet

- Vælg fx **192.168.10.0/24** og **192.168.20.0/24** til to subnet
- Tildel én PC i hvert subnet:
    - VPCS1: `ip 192.168.10.10/24 192.168.10.1`
    - VPCS2: `ip 192.168.20.10/24 192.168.20.1`

### 3. Opret VLAN på switchen

- Hvis din GNS3-switch tillader VLAN, opret to VLAN (fx VLAN 10 og VLAN 20)
- Sæt VPCS1 til VLAN 10 og VPCS2 til VLAN 20  
  *(Hvis ikke muligt, beskriv hvordan du ville gøre det på en “rigtig” managed switch)*

### 4. Tilslut fysisk PLC til switchen

- Kobl din fysiske PLC ind i switchen (enten direkte til din PC med “cloud”/bridged interface i GNS3, eller via skolens netværk)
- Sæt PLC’ens IP i ét af subnettene, fx:  
  - PLC: `192.168.10.100` (samme subnet som VPCS1/VLAN10)

### 5. Opdater netværksdiagram

- Tegn et diagram (fx i draw.io eller på papir) med:
    - VPCS1, VPCS2, switch, PLC, VLAN/subnet-mærker
    - Notér IP-adresser og hvilke porte der sidder i hvilket VLAN

---

## 📋 Dokumentation

- Indsæt netværksdiagram (billede eller draw.io/skitse)
- Skriv, hvilke IP-adresser, VLAN og subnet du har brugt
- Beskriv meget kort, hvordan du tilsluttede den fysiske PLC til GNS3-netværket

---

## Refleksion

- Hvorfor bruger man subnet og VLAN i industrielle netværk?
- Hvad er fordelene ved at kunne “holde virtuelle og fysiske” enheder adskilt – eller forbundet?
- Var der noget, der var særligt udfordrende i opsætningen?

---

## Ekstra (hvis tid)

- Prøv at flytte PLC eller en PC fra ét VLAN/subnet til et andet – hvad sker der med kommunikationen?
- Beskriv hvordan VLAN opsættes på en fysisk managed switch (fx Siemens Scalance eller Cisco)

---

Du er nu klar til at teste ping og kommunikation på tværs af dine segmenter! 🚦
