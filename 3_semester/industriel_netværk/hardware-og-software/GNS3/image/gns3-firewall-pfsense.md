# 🛡️ pfSense Firewall i GNS3

Dette dokument fokuserer på opsætning af **pfSense** i GNS3 med særlig vægt på **port-konfiguration** og **ACL-regler** til undervisningsbrug.

## 🔥 Kernefunktioner for netværksundervisning

* ✅ Port-baseret filtrering
* ✅ Access Control Lists (ACL)
* ✅ NAT (Network Address Translation)
* ✅ Stateful firewall
* ✅ Logging og overvågning

---

## 📦 Installation i GNS3

1. Download pfSense ISO fra [pfsense.org/download](https://www.pfsense.org/download/)
   ```bash
   "$BROWSER" https://www.pfsense.org/download/
   ```

2. I GNS3:
   * Opret ny QEMU VM (1GB RAM, 8GB disk)
   * Tildel minimum 2 interfaces (WAN + LAN)
   * Boot fra ISO og gennemfør installationen

---

## 🔒 Port-konfiguration (grundlæggende opgave)

### Sådan tillader du specifikke porte:

1. **Tilgå web interface** (https://LAN-IP, typisk 192.168.1.1)
   * Login: admin / pfsense

2. **Naviger til firewall-regler**:
   * Firewall → Rules → [vælg interface] (f.eks. WAN)
   * Klik "Add" (øverst til højre) for at tilføje en ny regel

3. **Konfigurer regel for at tillade en port**:
   * Action: Pass
   * Interface: WAN
   * Protocol: TCP/UDP (afhængigt af behov)
   * Source: Any (eller specifik IP/netværk for ekstra sikkerhed)
   * Destination: WAN address
   * Destination Port Range: [angiv port] (f.eks. HTTPS = 443)
   * Description: Tillad HTTPS fra internet

4. **Gem og anvend ændringer**
   * Klik "Save"
   * Klik "Apply Changes"

### Praktisk opgave - Åbn for webserver:
```
1. Tillad HTTP (port 80) og HTTPS (port 443) fra WAN til DMZ-webserver
2. Test med klient at forbindelsen er mulig
3. Tjek logs for at bekræfte traffik passerer korrekt
```

---

## 🔐 ACL-konfiguration (Access Control Lists)

ACLs implementeres i pfSense som firewall-regler der læses fra top til bund.

### Trin for at oprette ACL-baseret filtrering:

1. **Plan din sikkerhedspolitik**:
   * Hvilke netværk skal have adgang til hvilke ressourcer?
   * Dokumentér i en tabel før konfiguration

2. **Naviger til firewall-regler**:
   * Firewall → Rules → [vælg interface]
   * Regler anvendes i rækkefølge (top-down)

3. **Opret regler baseret på dit sikkerhedsbehov**:
   * Specifikke regler før generelle
   * Benyt "Default Deny" princippet (tillad kun nødvendig trafik)

### Eksempel på ACL for undervisningsnetværk:

```
LAN (192.168.1.0/24) Interface:
1. Tillad LAN → DMZ webserver (kun HTTP/HTTPS)
2. Tillad LAN → Internet (alle porte)
3. Bloker alt andet

DMZ (10.0.0.0/24) Interface:
1. Tillad DMZ → Internet (kun HTTP/HTTPS for opdateringer)
2. Bloker DMZ → LAN (al trafik)
3. Bloker alt andet

WAN Interface:
1. Tillad WAN → DMZ webserver (kun HTTP/HTTPS)
2. Bloker WAN → LAN (al trafik)
3. Bloker alt andet
```

---

## 🧪 Øvelser til undervisning

### Øvelse 1: Basis port-konfiguration
1. Opsæt pfSense med 3 interfaces (WAN, LAN, DMZ)
2. Tillad HTTP/HTTPS fra WAN til webserver i DMZ
3. Verificér med traceroute og netværkspakke-analyse

### Øvelse 2: ACL mellem segmenter
1. Opret tre netværkssegmenter (Administration, Produktion, Gæster)
2. Implementér følgende politik:
   * Administration → fuld adgang til alle segmenter
   * Produktion → kun adgang til internet og produktionsservere
   * Gæster → kun internet-adgang (blokér internt netværk)

### Øvelse 3: Port-baseret segmentering
1. Konfigurér webserver til at køre på ikke-standard port (f.eks. 8080)
2. Opsæt port forwarding fra standard port til ikke-standard
3. Implementér firewall-regler der begrænser adgang baseret på kilde-IP

---

## 📊 Verificering og fejlfinding

* **Logs**: Diagnostics → Log Files → Firewall
* **States**: Diagnostics → States → Filter på IP/port
* **Packet Capture**: Diagnostics → Packet Capture
  ```
  Vælg interface, angiv filter (f.eks. "port 80"), start capture
  ```

---

## 🔍 Kommandolinjeværktøjer (for avancerede brugere)

Via pfSense shell (option 8 fra konsol):

```bash
# Se aktive forbindelser
pfctl -ss

# Test firewall-regler
pfctl -sr

# Se status på interfaces
ifconfig

# Packet capture (tcpdump)
tcpdump -i em0 -n port 80
```

> **Tip til undervisere:** Vis disse kommandoer via pfSense konsol for at demonstrere sammenhængen mellem GUI og underliggende FreeBSD-system.