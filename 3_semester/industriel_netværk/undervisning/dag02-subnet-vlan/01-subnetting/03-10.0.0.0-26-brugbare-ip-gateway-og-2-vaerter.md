# GNS3 — 2 Linux‑PC’er + 1 Linux‑router med /25‑subnet fra Opgave 1

**Mål:** Brug de **to /25‑subnet** du beregnede i *Opgave 1* til at få PC1↔PC2 til at ping’e via routeren. Ingen firewall. Kun IPv4.

---

## Del A — Skriv dine /25‑resultater ned først

Udfyld med dine tal fra *Opgave 1*.

**Subnet #1**

* Net: `____________________`
* Broadcast: `____________________`
* Første brugbare: `____________________`
* Sidste brugbare: `____________________`

**Subnet #2**

* Net: `____________________`
* Broadcast: `____________________`
* Første brugbare: `____________________`
* Sidste brugbare: `____________________`

> Notation: Brug CIDR `/25` på alle adresser.

---

## Del B — GNS3 step‑by‑step (Linux‑router + 2 Linux‑PC’er)

**Antag** noderne findes: `R1` (Linux‑router), `PC1`, `PC2`. Kablet: `PC1 — R1 — PC2`.

### IP‑plan baseret på dine /25‑subnet

* **LAN A (PC1↔R1‑eth0)** = *Subnet #1*

  * R1‑eth0: vælg **første brugbare** i Subnet #1
  * PC1: vælg **en vilkårlig brugbar** i Subnet #1 (ikke R1‑IP)
* **LAN B (R1‑eth1↔PC2)** = *Subnet #2*

  * R1‑eth1: vælg **første brugbare** i Subnet #2
  * PC2: vælg **en vilkårlig brugbar** i Subnet #2 (ikke R1‑IP)

> Find interfacenavne med `ip -br link` og erstat `eth0/eth1` efter behov.

### 1) Router (R1)

```bash
# Erstat <> med dine konkrete /25‑adresser
ip addr flush dev eth0; ip addr flush dev eth1
ip addr replace <R1_ETH0_IP_I_SUBNET1>/25 dev eth0
ip addr replace <R1_ETH1_IP_I_SUBNET2>/25 dev eth1
ip link set eth0 up; ip link set eth1 up
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
ip addr replace <PC1_IP_I_SUBNET1>/25 dev eth0
ip link set eth0 up
ip route replace default via <R1_ETH0_IP_I_SUBNET1>
```

**Tjek**

```bash
ip -br a; ip r
ping -c2 <R1_ETH0_IP_I_SUBNET1>
```

### 3) PC2

```bash
ip addr flush dev eth0
ip addr replace <PC2_IP_I_SUBNET2>/25 dev eth0
ip link set eth0 up
ip route replace default via <R1_ETH1_IP_I_SUBNET2>
```

**Tjek**

```bash
ip -br a; ip r
ping -c2 <R1_ETH1_IP_I_SUBNET2>
```

### 4) Ende‑til‑ende test

**Fra PC1**

```bash
ping -c3 <PC2_IP_I_SUBNET2>
traceroute <PC2_IP_I_SUBNET2>   # ét hop via R1
```

Valgfrit fra PC2:

```bash
ping -c3 <PC1_IP_I_SUBNET1>
```

---

## Hurtig fejlsøgning

```bash
ip -br link                 # UP på relevante interfaces
ip -br a                    # korrekte /25‑adresser sat
ip r                        # PC’er har default via R1
cat /proc/sys/net/ipv4/ip_forward  # på R1: 1
ip neigh                    # ARP løses ved lokale pings
```

**Typiske fejl**

* Brug af net- eller broadcast‑adresser som host‑IP → vælg brugbare adresser
* Forkert gateway på PC’er → skal være R1‑IP i samme /25
* Forwarding ikke slået til på R1

---

## Aflevering

* Dine to /25‑tabeller fra **Del A** udfyldt.
* Skærmbilleder fra PC1 og PC2: `ip a`, `ip r`, `ping`, `traceroute`.
* Kort note: Hvilket trin løste evt. fejl.
