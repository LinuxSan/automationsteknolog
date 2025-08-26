# GNS3 — 4 Linux‑PC’er + 1 Linux‑router med /26‑subnet fra Opgave 2

**Mål:** Brug dine **fire /26‑subnet** fra *Opgave 2* til at få PC1↔PC2↔PC3↔PC4 til at ping’e via én Linux‑router. Ingen firewall. Kun IPv4.

---

## Del A — Notér dine /26‑resultater først

Udfyld fra *Opgave 2*.

**Subnet #1**
Net: `____________________` · Broadcast: `____________________`   
Første brugbare: `____________________` · Sidste brugbare: `____________________`

**Subnet #2**
Net: `____________________` · Broadcast: `____________________`   
Første brugbare: `____________________` · Sidste brugbare: `____________________`

**Subnet #3**
Net: `____________________` · Broadcast: `____________________`   
Første brugbare: `____________________` · Sidste brugbare: `____________________`

**Subnet #4**
Net: `____________________` · Broadcast: `____________________`   
Første brugbare: `____________________` · Sidste brugbare: `____________________`

> Brug altid `/26` notation.

---

## Del B — GNS3 step‑by‑step (Linux‑router + 4 Linux‑PC’er)

**Antag** noderne allerede findes: `R1` (Linux‑router), `PC1`, `PC2`, `PC3`, `PC4`.
**Kabling:** `PC1—R1:eth0`, `PC2—R1:eth1`, `PC3—R1:eth2`, `PC4—R1:eth3`.

### IP‑plan (map dine subnet)

* **LAN1** = *Subnet #1*:  PC1 ↔ R1‑eth0
  R1‑eth0 = **første brugbare** i Subnet #1.
  PC1 = **en anden brugbar** i Subnet #1.
* **LAN2** = *Subnet #2*:  PC2 ↔ R1‑eth1
  R1‑eth1 = **første brugbare** i Subnet #2.
  PC2 = **en anden brugbar** i Subnet #2.
* **LAN3** = *Subnet #3*:  PC3 ↔ R1‑eth2
  R1‑eth2 = **første brugbare** i Subnet #3.
  PC3 = **en anden brugbar** i Subnet #3.
* **LAN4** = *Subnet #4*:  PC4 ↔ R1‑eth3
  R1‑eth3 = **første brugbare** i Subnet #4.
  PC4 = **en anden brugbar** i Subnet #4.

> Find rigtige interfacenavne med `ip -br link` og erstat `eth0..eth3` efter behov.

### 1) Router (R1)

```bash
# Erstat <> med dine konkrete /26‑adresser
ip addr flush dev eth0; ip addr flush dev eth1; ip addr flush dev eth2; ip addr flush dev eth3
ip addr replace <R1_ETH0_IP_I_SUBNET1>/26 dev eth0
ip addr replace <R1_ETH1_IP_I_SUBNET2>/26 dev eth1
ip addr replace <R1_ETH2_IP_I_SUBNET3>/26 dev eth2
ip addr replace <R1_ETH3_IP_I_SUBNET4>/26 dev eth3
ip link set eth0 up; ip link set eth1 up; ip link set eth2 up; ip link set eth3 up
sysctl -w net.ipv4.ip_forward=1
```

**Tjek**

```bash
ip -br a
cat /proc/sys/net/ipv4/ip_forward   # skal være 1
```

### 2) PC1

```bash
ip addr flush dev eth0
ip addr replace <PC1_IP_I_SUBNET1>/26 dev eth0
ip link set eth0 up
ip route replace default via <R1_ETH0_IP_I_SUBNET1>
```

### 3) PC2

```bash
ip addr flush dev eth0
ip addr replace <PC2_IP_I_SUBNET2>/26 dev eth0
ip link set eth0 up
ip route replace default via <R1_ETH1_IP_I_SUBNET2>
```

### 4) PC3

```bash
ip addr flush dev eth0
ip addr replace <PC3_IP_I_SUBNET3>/26 dev eth0
ip link set eth0 up
ip route replace default via <R1_ETH2_IP_I_SUBNET3>
```

### 5) PC4

```bash
ip addr flush dev eth0
ip addr replace <PC4_IP_I_SUBNET4>/26 dev eth0
ip link set eth0 up
ip route replace default via <R1_ETH3_IP_I_SUBNET4>
```

### 6) Ende‑til‑ende tests

**Fra PC1**

```bash
ping -c2 <PC2_IP_I_SUBNET2>
ping -c2 <PC3_IP_I_SUBNET3>
ping -c2 <PC4_IP_I_SUBNET4>
traceroute <PC4_IP_I_SUBNET4>   # ét hop via R1
```

Valgfrit: gentag fra de andre PC’er.

---

## Hurtig fejlsøgning

```bash
ip -br link                 # UP på relevante interfaces
ip -br a                    # korrekte /26‑adresser sat
ip r                        # hver PC har default via sin R1‑IP
cat /proc/sys/net/ipv4/ip_forward  # R1: 1
ip neigh                    # ARP entries opstår ved lokale pings
```

**Typiske fejl**

* Brug af net/broadcast som host‑IP → vælg brugbare adresser
* Forkert gateway på en PC → skal være R1‑IP i samme /26
* Forwarding ikke slået til på R1

---

## Aflevering

* Udfyldt **Del A** for alle fire /26.
* Skærmbilleder fra alle PC’er: `ip a`, `ip r`, `ping` til mindst to andre PC’er, `traceroute` til én PC i et andet subnet.
* Kort note: Hvilken kontrol fandt og fjernede en fejl?

> Hvis din Linux‑router kun har 2 interfaces: brug to ekstra NICs eller erstat med VLAN‑subinterfaces (ud over pensum, valgfrit).
