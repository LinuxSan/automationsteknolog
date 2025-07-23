
## 🧰 Design for GNS3 Linux Router Appliance

Dette dokument beskriver design og konfiguration af en **simpel, effektiv Linux-router** til brug i GNS3, som understøtter:

* ✅ VLAN (802.1Q trunk og subinterfaces)
* ✅ IPv4 routing og subnetting
* ✅ NAT (IPv4 og NAT64)
* ✅ IPv6 routing (statisk og radvd)
* ✅ DHCPv6 og SLAAC support

Routeren vil være baseret på **Debian Minimal** og anvende QEMU i GNS3.

---

### 📦 Base Image

* **OS**: Debian 12 Minimal (CLI-only)
* **Format**: `qcow2`
* **Størrelse**: 2–4 GB disk, 256–512 MB RAM i GNS3

---

### 🛠️ Installerede pakker (forhåndskonfigureret)

```bash
apt install -y iproute2 ifupdown vlan net-tools iptables nftables isc-dhcp-server \
               radvd wide-dhcpv6-client tayga curl vim tcpdump systemd-resolved
```

> Alle konfigurationsfiler placeres i `/etc/network/interfaces`, `/etc/sysctl.conf`, `/etc/nftables.conf`, `/etc/radvd.conf`, og `/etc/tayga.conf`

---

### 🔁 Netværksfunktioner (klar til brug)

* 🔧 **IP forwarding** (IPv4 og IPv6):

  * Aktiveret i `/etc/sysctl.conf` med:

    ```
    net.ipv4.ip_forward=1
    net.ipv6.conf.all.forwarding=1
    ```

* 🌐 **VLAN subinterfaces**:

  * Konfigureret via `ip link add link eth0 name eth0.10 type vlan id 10`

* 🔁 **Statisk routing**:

  * IPv4: `ip route add ...`
  * IPv6: `ip -6 route add ...`

* 🔄 **NAT (IPv4 og NAT64):**

  * IPv4 NAT: iptables MASQUERADE
  * NAT64: via Tayga (stateless NAT64 for IPv6→IPv4 translation)

* 📡 **radvd** til IPv6 router announcements (SLAAC)

* 📬 **wide-dhcpv6-client/server** til DHCPv6 (valgfrit)

---

### 📁 Filstruktur i appliance

* `/etc/network/interfaces`
* `/etc/nftables.conf`
* `/etc/sysctl.conf`
* `/etc/radvd.conf`
* `/etc/tayga.conf`
* `/usr/local/bin/router-boot.sh` ← eksekveres automatisk

---

### 🧱 GNS3 Appliance Definition (gns3a)

Filen definerer:

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

---

### 🧪 Test og brug

Importer appliance og brug som ethvert andet netværkselement i GNS3:

* Tilføj til projekt
* Tildel interfaces
* Konfigurer IPv4 og IPv6 routing, DHCPv6, NAT og VLAN’er

---

### 🟩 Klar til levering?

Hvis du ønsker det:

* Jeg kan generere:

  * En `.qcow2` disk (du downloader og importerer)
  * En `.gns3a` appliance-definition
  * Et startup-script til både IPv4/IPv6 forwarding og NAT

> Sig til, om du vil have det som en downloadbar pakke, eller om du selv vil bygge image fra ISO – jeg kan guide dig i begge tilfælde.
