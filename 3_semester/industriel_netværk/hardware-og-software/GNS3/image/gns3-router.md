# Design og Konfiguration af GNS3 Linux Router Appliance

Dette dokument beskriver design, konfiguration og import af en Linux-router appliance til brug i GNS3. Routeren understøtter VLAN, IPv4/IPv6 routing, NAT, og DHCPv6/SLAAC og er baseret på Debian Minimal.

---

## 🧰 **Design**

Routeren er designet til at være enkel og effektiv med følgende funktioner:

- **VLAN Support**: 802.1Q trunking og subinterfaces.
- **IPv4 Routing**: Statisk routing og subnetting.
- **NAT**: IPv4 NAT og NAT64.
- **IPv6 Routing**: Statisk routing og SLAAC via `radvd`.
- **DHCPv6**: Support for DHCPv6 og SLAAC.

---

## 📦 **Base Image**

### **Specifikationer**
- **OS**: Debian 12 Minimal (CLI-only).
- **Format**: `qcow2` eller Docker-image.
- **Ressourcer i GNS3**: 
  - Disk: 2–4 GB (qcow2) eller Docker-container.
  - RAM: 256–512 MB.

---

## 🛠️ **Installerede Pakker**

Installér følgende pakker i routeren:
```bash
apt install -y iproute2 ifupdown vlan net-tools iptables nftables isc-dhcp-server \
               radvd wide-dhcpv6-client tayga curl vim tcpdump systemd-resolved
```

### **Konfigurationsfiler**
Alle nødvendige konfigurationsfiler placeres i følgende mapper:
- `/etc/network/interfaces`
- `/etc/sysctl.conf`
- `/etc/nftables.conf`
- `/etc/radvd.conf`
- `/etc/tayga.conf`

---

## 🔁 **Netværksfunktioner**

### **IP Forwarding**
Aktiver IP forwarding for IPv4 og IPv6 i `/etc/sysctl.conf`:
```plaintext
net.ipv4.ip_forward=1
net.ipv6.conf.all.forwarding=1
```

### **VLAN Subinterfaces**
Opsæt VLAN subinterfaces med følgende kommando:
```bash
ip link add link eth0 name eth0.10 type vlan id 10
```

### **Statisk Routing**
- **IPv4**:
  ```bash
  ip route add <destination> via <gateway>
  ```
- **IPv6**:
  ```bash
  ip -6 route add <destination> via <gateway>
  ```

### **NAT**
- **IPv4 NAT**:
  Brug iptables med `MASQUERADE`:
  ```bash
  iptables -t nat -A POSTROUTING -o <interface> -j MASQUERADE
  ```
- **NAT64**:
  Konfigurer Tayga til stateless NAT64:
  - Konfigurationen placeres i `/etc/tayga.conf`.

### **IPv6 Router Announcements**
Brug `radvd` til SLAAC:
- Konfigurationsfil: `/etc/radvd.conf`.

### **DHCPv6**
Opsæt DHCPv6 med `wide-dhcpv6-client/server` (valgfrit).

---

## 📁 **Filstruktur**

Routerens konfiguration er organiseret som følger:
- `/etc/network/interfaces`
- `/etc/nftables.conf`
- `/etc/sysctl.conf`
- `/etc/radvd.conf`
- `/etc/tayga.conf`
- `/usr/local/bin/router-boot.sh` ← eksekveres automatisk ved opstart.

---

## 🧱 **GNS3 Appliance Definition**

### **QEMU Appliance**
Opret en GNS3 appliance-definition i JSON-format:
```json
{
  "name": "linux-router",
  "category": "router",
  "vendor_name": "Custom",
  "qemu": {
    "ram": 512,
    "adapters": 4,
    "hda_disk_image": "linux-router.qcow2",
    "platform": "x86_64",
    "qemu_options": ""
  }
}
```

### **Docker Appliance**
Hvis du bruger Docker, skal du definere appliance i GNS3 Preferences:
1. Gå til **Edit → Preferences → Docker Containers**.
2. Klik på **New** og udfyld følgende:
   - **Name**: `Linux Router`.
   - **Image**: `linux-router`.
   - **Number of Adapters**: 4.
   - **RAM**: 256–512 MB.

---

## 🧪 **Import og Brug**

### **Import i GNS3**
1. **QEMU Method**:
   - Importér `.qcow2` diskbilledet via **File → Import Appliance**.
   - Vælg `linux-router.gns3a` filen og følg guiden.
   
2. **Docker Method**:
   - Følg guiden i **Docker Appliance**-sektionen ovenfor.

### **Opsætning i Projekt**
1. Træk routeren ind i arbejdsområdet.
2. Forbind den til andre enheder som switches, routere eller VPC'er.
3. Konfigurer og test netværksfunktionerne som NAT, VLAN, IPv4/IPv6 routing, osv.

---

## 🟩 **Klar til Levering?**

Jeg kan levere følgende:
1. **En .qcow2 disk**: Klar til at importere i GNS3.
2. **En .gns3a appliance-definition**.
3. **Et startup-script**: Automatisk aktiverer IPv4/IPv6 forwarding og NAT.

**Alternativt**, hvis du ønsker at bygge image fra ISO eller Dockerfile:
- Jeg kan guide dig i processen.

Lad mig vide, hvad du har brug for! 😊
