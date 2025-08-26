# GNS3 — 802.1Q trunk mellem to Linux‑enheder + 2 PC’er (L2‑øvelse)

**Mål:** Byg en **trunk** mellem to Linux‑noder (R1↔R2). PC1 og PC2 er i samme VLAN over trunken. Ingen routing. Kun L2.

## Topologi

```
PC1 ── R1 ──(trunk: eth1)── R2 ── PC2
        ^                     ^
      access                 access
```

Noder findes i GNS3: `R1` og `R2` (Linux), `PC1`, `PC2` (Linux). Direkte links som vist.

## VLAN og IP‑plan

* VLAN10 (ID 10): 192.168.10.0/24  →  PC1 = 192.168.10.2,  PC2 = 192.168.10.3
* VLAN20 (ID 20): bruges i **Del B** til isolations‑test

---

## Del A — Trunk op, PC’er i samme VLAN over trunken

### 1) R1: VLAN‑bevidst bridge + access + trunk

```bash
# Bridge med VLAN‑filtrering
ip link add br0 type bridge vlan_filtering 1
ip link set br0 up
ip link set eth0 up; ip link set eth1 up
ip link set eth0 master br0
ip link set eth1 master br0

# Ryd default VLAN 1 membership (valgfrit for tydelighed)
bridge vlan del dev eth0 vid 1 2>/dev/null || true
bridge vlan del dev eth1 vid 1 2>/dev/null || true

# eth0 = ACCESS i VLAN10 (untagged)
bridge vlan add dev eth0 vid 10 pvid untagged

# eth1 = TRUNK tillader VLAN10 og VLAN20 (tagged)
bridge vlan add dev eth1 vid 10
bridge vlan add dev eth1 vid 20
```

### 2) R2: samme model

```bash
ip link add br0 type bridge vlan_filtering 1
ip link set br0 up
ip link set eth0 up; ip link set eth1 up
ip link set eth0 master br0
ip link set eth1 master br0

bridge vlan del dev eth0 vid 1 2>/dev/null || true
bridge vlan del dev eth1 vid 1 2>/dev/null || true

# eth0 = ACCESS i VLAN10
bridge vlan add dev eth0 vid 10 pvid untagged

# eth1 = TRUNK (vid10,20)
bridge vlan add dev eth1 vid 10
bridge vlan add dev eth1 vid 20
```

### 3) PC1 og PC2: IP i VLAN10 (ingen gateway)

```bash
# PC1
ip addr flush dev eth0
ip addr add 192.168.10.2/24 dev eth0
ip link set eth0 up

# PC2
ip addr flush dev eth0
ip addr add 192.168.10.3/24 dev eth0
ip link set eth0 up
```

### 4) Test

Fra **PC1**

```bash
ping -c3 192.168.10.3
```

Forventet: succes. L2 rammer går PC1→R1(access VLAN10)→R1 trunk tagger→R2 trunk→R2 access VLAN10→PC2.

---

## Del B — Vis isolation mellem VLAN over samme trunk

Skift **PC2** til VLAN20 (nyt subnet) og bekræft at ping fra PC1 fejler.

### 5) R2: gør eth0 til ACCESS i VLAN20

```bash
# Fjern VLAN10 som access
bridge vlan del dev eth0 vid 10
# Sæt VLAN20 som access
bridge vlan add dev eth0 vid 20 pvid untagged
```

### 6) PC2: ny IP i VLAN20

```bash
ip addr flush dev eth0
ip addr add 192.168.20.3/24 dev eth0
ip link set eth0 up
```

### 7) Test igen

Fra **PC1**

```bash
ping -c3 192.168.20.3   # forventet FEJL (VLAN‑isolation)
```

Valgfrit: Tilføj en **PC3** på R1’s access‑port i VLAN20 og bekræft at **PC3↔PC2** virker over samme trunk.

---

## Fejlsøgning

```bash
ip -br link
bridge vlan show                # se pvid/untagged/tagged pr. port
bridge link show                 # medlemskab i br0
ip neigh                         # ARP udfyldes ved trafik
```

**Typiske fejl**

* Access‑port sat med forkert `pvid`/`untagged`
* Trunk mangler et VLAN på én side → føj `bridge vlan add dev eth1 vid <id>`
* IP’er sat i samme /24 men på forskellige VLAN → virker ikke (adskilte L2‑domæner)

---

## Aflevering

* `bridge vlan show` fra begge bro‑noder
* `ip a` fra PC’er
* Ping‑resultater for Del A (succes) og Del B (forventet fejl)
