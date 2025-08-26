# GNS3 — 3 VLAN på Linux‑router + 3 Linux‑PC’er (router‑on‑a‑stick)

**Mål:** Inter‑VLAN routing mellem tre VLAN. PC1 (VLAN10) kan ping’e PC2 (VLAN20) og PC3 (VLAN30) via Linux‑routerens trunk.

## Topologi (GNS3)

```
PC1 ─┐         ┌─ R1 (Linux‑router)
PC2 ─┼─ Switch ┤  trunk: eth0 (802.1Q)
PC3 ─┘         └─────────────────────
```

Switch’en er VLAN‑uvidende i GNS3 og lader 802.1Q‑tags passere.

## IP‑plan

* **VLAN10 (ID 10)**: 192.168.10.0/24  →  R1 = 192.168.10.1,  PC1 = 192.168.10.2
* **VLAN20 (ID 20)**: 192.168.20.0/24  →  R1 = 192.168.20.1,  PC2 = 192.168.20.2
* **VLAN30 (ID 30)**: 192.168.30.0/24  →  R1 = 192.168.30.1,  PC3 = 192.168.30.2

> Tilpas interface‑navne hvis dine ikke hedder `eth0`.

---

## Trin 0 — Oprydning (alle noder)

```bash
ip addr flush dev eth0
ip link set eth0 up
```

## Trin 1 — Router (R1): trunk + tre subinterfaces

```bash
# Opret VLAN‑subinterfaces
ip link add link eth0 name eth0.10 type vlan id 10
ip link add link eth0 name eth0.20 type vlan id 20
ip link add link eth0 name eth0.30 type vlan id 30

# Tildel IP’er
ip addr add 192.168.10.1/24 dev eth0.10
ip addr add 192.168.20.1/24 dev eth0.20
ip addr add 192.168.30.1/24 dev eth0.30

# Aktivér
ip link set eth0.10 up
ip link set eth0.20 up
ip link set eth0.30 up

# Slå routing til
sysctl -w net.ipv4.ip_forward=1
```

Tjek:

```bash
ip -d link show eth0.10
ip -d link show eth0.20
ip -d link show eth0.30
cat /proc/sys/net/ipv4/ip_forward   # 1
```

## Trin 2 — PC1 (VLAN10)

```bash
ip link add link eth0 name eth0.10 type vlan id 10
ip addr add 192.168.10.2/24 dev eth0.10
ip link set eth0.10 up
ip route replace default via 192.168.10.1 dev eth0.10
```

## Trin 3 — PC2 (VLAN20)

```bash
ip link add link eth0 name eth0.20 type vlan id 20
ip addr add 192.168.20.2/24 dev eth0.20
ip link set eth0.20 up
ip route replace default via 192.168.20.1 dev eth0.20
```

## Trin 4 — PC3 (VLAN30)

```bash
ip link add link eth0 name eth0.30 type vlan id 30
ip addr add 192.168.30.2/24 dev eth0.30
ip link set eth0.30 up
ip route replace default via 192.168.30.1 dev eth0.30
```

## Trin 5 — Test

Fra **PC1**:

```bash
ping -c2 192.168.10.1   # egen gateway
ping -c2 192.168.20.1   # anden SVI
ping -c2 192.168.30.1   # tredje SVI
ping -c3 192.168.20.2   # PC2
ping -c3 192.168.30.2   # PC3
traceroute 192.168.30.2 # via R1
```

Gentag valgfrit fra PC2/PC3.

---

## Fejlsøgning

```bash
ip -br link                 # UP?
ip -br a                    # korrekte IP’er på eth0.{10,20,30}
ip -d link show eth0.10     # VLAN id = 10
ip -d link show eth0.20     # VLAN id = 20
ip -d link show eth0.30     # VLAN id = 30
cat /proc/sys/net/ipv4/ip_forward
ip neigh
```

**Typiske fejl**

* IP lagt på `eth0` i stedet for `eth0.<vlan>`
* Forkert default‑route på PC’er
* `ip_forward=0` på R1

---

## Aflevering

* `ip -d link`, `ip a`, `ip r` fra alle tre PC’er og R1
* Ping/traceroute PC1→PC2 og PC1→PC3
* Kort note om evt. fejl og fix
