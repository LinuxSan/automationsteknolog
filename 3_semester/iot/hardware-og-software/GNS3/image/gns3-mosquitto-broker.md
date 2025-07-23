## 🧰 Design for GNS3 Linux Router, CLI-PC & MQTT-Tank Simulator

Dette dokument beskriver design og konfiguration af tre enheder til brug i GNS3:

* En **simpel Linux-router** med IPv4/IPv6-routing, NAT og VLAN
* En **minimal CLI-baseret Linux-PC** til netværksøvelser
* En **MQTT-broker-maskine** og fremtidig PLC-tank-simulator til IIoT og processtyring

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

### 🛠️ Installerede pakker

```bash
apt install -y iproute2 ifupdown vlan net-tools iptables nftables isc-dhcp-server \
               radvd wide-dhcpv6-client tayga curl vim tcpdump systemd-resolved
```

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

---

## 🧳 Linux-PC (CLI-klient)

### 🔧 Beskrivelse

Letvægts, uforudkonfigureret Debian CLI-maskine. Studerende skal selv:

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

---

## 🧪 MQTT-Broker (Linux-server med brokerfunktion)

### 🧰 Beskrivelse

En Debian-baseret CLI-maskine i GNS3, der fungerer som MQTT-broker til brug i IIoT- og netværksprojekter. Den kan bruges til at:

* hoste en MQTT-broker (Mosquitto)
* teste MQTT-publish/subscribe interaktion
* modtage data fra PLC-simulatorer, sensorer eller scripts

Denne maskine er målrettet undervisningsbrug og opsætning af publish/subscribe-mønstre, og kan nemt udvides med Python, Node-RED eller anden MQTT-klient.

### 📦 Base Image

* **OS**: Debian 12 Minimal (CLI-only)
* **Format**: `qcow2`
* **RAM**: 256–512 MB
* **Disk**: 2–4 GB

### 🛠️ Installerede pakker

```bash
apt install -y mosquitto mosquitto-clients iproute2 ifupdown net-tools curl vim
```

> MQTT-brokeren startes som systemd-service og lytter på port 1883. Ingen adgangskontrol aktiveret som standard (anbefales at aktiveres i produktion).

### 🔧 Funktioner

* Mosquitto MQTT-broker (v2.x)
* CLI-værktøjer (`mosquitto_pub`, `mosquitto_sub`) til test
* Klar til integration med andre GNS3-maskiner (router, klienter, PLC-simulatorer)

### 🧱 Appliance Definition (gns3a)

```json
{
  "name": "linux-mqtt-broker",
  "category": "server",
  "vendor_name": "Custom",
  "qemu": {
    "ram": 512,
    "adapters": 2,
    "hda_disk_image": "linux-mqtt-broker.qcow2",
    "platform": "x86_64",
    "qemu_options": ""
  }
}
```

### 🧰 Beskrivelse

En Debian-baseret GNS3-maskine, der kører en **MQTT-broker (Mosquitto)** og i fremtiden en Python-baseret **PLC-tanksimulator**.

### 📦 Base Image

* Debian 12 Minimal eller Ubuntu Server
* RAM: 256–512 MB
* Disk: 2–4 GB

### 🛠️ Installerede pakker

```bash
apt install -y mosquitto mosquitto-clients python3 python3-pip iproute2 net-tools curl
```

> Python-script til tank-simulator installeres senere via pip med f.eks. `paho-mqtt` og `numpy`

### 🔧 Funktioner (MQTT)

* Mosquitto-broker kører som service
* MQTT-publisher/subscriber-test via CLI
* Klar til integration med PLC-simulator (niveau, flow, ventiler)

### 🧱 Appliance Definition (gns3a)

```json
{
  "name": "mqtt-broker",
  "category": "server",
  "vendor_name": "Custom",
  "qemu": {
    "ram": 512,
    "adapters": 2,
    "hda_disk_image": "mqtt-broker.qcow2",
    "platform": "x86_64",
    "qemu_options": ""
  }
}
```

---

## 📦 Klar til levering?

Jeg kan levere alle tre appliances som:

* `.qcow2` disk (importerbar)
* `.gns3a` appliance-definition
* README til opsætning og test

Sig til, om du ønsker dem som færdige filer eller selv vil bygge image fra ISO – jeg hjælper med begge.
