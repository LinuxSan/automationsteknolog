## 🧰 Design for GNS3 Linux Router & CLI-PC Appliance

Dette dokument beskriver design og konfiguration af to enheder til brug i GNS3:

* En **simpel, effektiv Linux-router** med IPv4/IPv6-routing, NAT og VLAN
* En **minimal CLI-baseret Linux-PC**, der kan bruges som klientmaskine i netværksøvelser

---

## 🔌 Linux-router (Debian Minimal)

### ✅ Understøttede funktioner

* VLAN (802.1Q trunk og subinterfaces)
* IPv4 routing og subnetting
* NAT (IPv4 og NAT64)
* IPv6 routing (statisk og radvd)
* DHCPv6 og SLAAC support

### 📦 Base Image

* **OS**: Debian 12 Minimal (CLI-only)
* **Format**: `qcow2`
* **Størrelse**: 2–4 GB disk, 256–512 MB RAM i GNS3

### 🛠️ Installerede pakker (forhåndskonfigureret)

```bash
apt install -y iproute2 ifupdown vlan net-tools iptables nftables isc-dhcp-server \
               radvd wide-dhcpv6-client tayga curl vim tcpdump systemd-resolved
```

> Konfigurationsfiler: `/etc/network/interfaces`, `/etc/sysctl.conf`, `/etc/nftables.conf`, `/etc/radvd.conf`, `/etc/tayga.conf`

### 🔁 Netværksfunktioner (klar til brug)

* IP forwarding (IPv4 og IPv6):

  ```
  net.ipv4.ip_forward=1
  net.ipv6.conf.all.forwarding=1
  ```
* VLAN via `ip link add link eth0 name eth0.10 type vlan id 10`
* Statisk routing med `ip route` og `ip -6 route`
* NAT med iptables og NAT64 via Tayga
* IPv6-routerannouncements med radvd
* DHCPv6 via wide-dhcpv6-server (valgfrit)

### 📁 Filstruktur

* `/etc/network/interfaces`
* `/etc/nftables.conf`
* `/etc/sysctl.conf`
* `/etc/radvd.conf`
* `/etc/tayga.conf`
* `/usr/local/bin/router-boot.sh`

### 🧱 Appliance Definition (gns3a)

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

### 🧪 Brug

Importer appliance, tilføj til projekt, tildel interfaces og konfigurer efter behov.

---

## 🧳 Linux-PC (CLI-klient)

### 🔧 Beskrivelse

En letvægts, uforudkonfigureret Debian CLI-maskine med kun basale værktøjer. Studerende skal selv:

* konfigurere IPv4 og/eller IPv6
* aktivere routing eller pinge enheder

### 📦 Base Image

* Debian 12 Minimal
* Format: `qcow2`
* RAM: 128–256 MB
* Disk: 1–2 GB

### 🛠️ Installerede pakker

```bash
apt install -y iproute2 ifupdown net-tools curl tcpdump wide-dhcpv6-client vim
```

> Ingen netværksinterfaces konfigureret. Ingen IP’er eller routes predefineret.

### 📁 Filstruktur

* Kun standard Debian-miljø
* Ingen aktive services ud over SSH-client, ping, traceroute, curl

### 🧱 Appliance Definition (gns3a)

```json
{
  "name": "linux-pc",
  "category": "host",
  "vendor_name": "Custom",
  "qemu": {
    "ram": 256,
    "adapters": 2,
    "hda_disk_image": "linux-pc.qcow2",
    "platform": "x86_64",
    "qemu_options": ""
  }
}
```

### 🧪 Brug

Bruges som slutbrugerklient. Kan tildeles IP’er manuelt eller via DHCP/NDP. Kan deltage i VLAN og måle forbindelser mod router eller internet.

---

## 📦 Klar til levering?

Jeg kan levere begge appliances som:

* `.qcow2` disk (importerbar)
* `.gns3a` appliance-definition
* Minimal README for installation

Sig til, om du ønsker dem som downloadbar pakke, eller selv vil bygge image fra ISO – jeg guider dig gerne i begge tilfælde.
