# GNS3 — 2 VLAN på Linux‑router + 2 Linux‑PC’er (router‑on‑a‑stick)

**Mål:** Inter‑VLAN routing. PC1 i VLAN10 kan ping’e PC2 i VLAN20 via Linux‑routerens trunk.

## Topologi (GNS3)

```
PC1 ─┐         ┌─ R1 (Linux‑router)
     ├─(Ethernet switch)─┤
PC2 ─┘         └─ trunk på R1: eth0 (802.1Q)
```

Alle tre noder er koblet til den samme GNS3 Ethernet‑switch. Switchen er “dum” og lader 802.1Q‑tags passere.

## IP‑plan

* **VLAN10 (ID 10)**: 192.168.10.0/24

  * R1: 192.168.10.1/24
  * PC1: 192.168.10.2/24
* **VLAN20 (ID 20)**: 192.168.20.0/24

  * R1: 192.168.20.1/24
  * PC2: 192.168.20.2/24

> Tilpas interface‑navne (`eth0`) hvis dine hedder noget andet.

---

## Trin 0 — Fælles (valgfri oprydning)

På alle noder:

```bash
ip addr flush dev eth0
ip link set eth0 up
```

## Trin 1 — Router (R1): trunk + subinterfaces

```bash
# Opret VLAN‑subinterfaces på trunk‑porten
ip link add link eth0 name eth0.10 type vlan id 10
ip link add link eth0 name eth0.20 type vlan id 20

# Tildel IP’er
ip addr add 192.168.10.1/24 dev eth0.10
ip addr add 192.168.20.1/24 dev eth0.20

# Aktiver
ip link set eth0.10 up
ip link set eth0.20 up

# Routing mellem VLANs
sysctl -w net.ipv4.ip_forward=1
```

Tjek:

```bash
ip -d link show eth0.10
ip -d link show eth0.20
cat /proc/sys/net/ipv4/ip_forward   # 1
```

## Trin 2 — PC1: VLAN10 access via egen NIC

```bash
ip link add link eth0 name eth0.10 type vlan id 10
ip addr add 192.168.10.2/24 dev eth0.10
ip link set eth0.10 up
ip route replace default via 192.168.10.1 dev eth0.10
```

Tjek: `ip -d link show eth0.10`, `ip r`

## Trin 3 — PC2: VLAN20 access via egen NIC

```bash
ip link add link eth0 name eth0.20 type vlan id 20
ip addr add 192.168.20.2/24 dev eth0.20
ip link set eth0.20 up
ip route replace default via 192.168.20.1 dev eth0.20
```

Tjek: `ip -d link show eth0.20`, `ip r`

## Trin 4 — Test

Fra **PC1**:

```bash
ping -c3 192.168.10.1   # gateway VLAN10
ping -c3 192.168.20.1   # gateway VLAN20 via router
ping -c3 192.168.20.2   # PC2 på VLAN20
traceroute 192.168.20.2 # skal gå via R1
```

Valgfrit fra **PC2**: ping 192.168.10.2.

---

## Fejlsøgning (rækkefølge)

```bash
ip -br link                 # interfaces UP
ip -br a                    # korrekte IP’er på subinterfaces
ip -d link show eth0.10     # se VLAN id 10
ip -d link show eth0.20     # se VLAN id 20
cat /proc/sys/net/ipv4/ip_forward
ip neigh
```

**Typiske fejl**

* IP lagt på `eth0` i stedet for `eth0.<vlan>` → flyt til subinterface
* Forkert gateway på PC’erne → brug routerens IP i samme VLAN
* `ip_forward=0` på R1 → slå til

---

## Aflevering

* Skærmbilleder fra alle noder: `ip -d link`, `ip a`, `ip r`
* Ping/traceroute PC1→PC2 bevis
* Kort note: Hvilken fejlsøgning hjalp mest
