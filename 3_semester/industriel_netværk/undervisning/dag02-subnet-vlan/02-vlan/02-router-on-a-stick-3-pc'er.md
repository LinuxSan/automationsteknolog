# Opgave 1 — To VLAN i GNS3 med isolation

### Formål

* Etablér VLAN10 og VLAN20 med korrekt access og trunk.
* Verificér L2-isolation uden routing.

### Læringsmål

Du kan:

1. Sætte access- og trunkporte i GNS3-switch.
2. Oprette 802.1Q-subinterfaces på Linux-router.
3. Dokumentere at kryds-VLAN ikke virker uden routing.

---

## Topologi

PC1 — SW — R1
PC2 — SW — R1

* PC1 i VLAN10, PC2 i VLAN20.
* SW→R1 er trunk med VLAN 10 og 20.

## Adresseplan

| VLAN | Net        | Router IP  | PC IP      | Maske |
| ---: | ---------- | ---------- | ---------- | ----- |
|   10 | 10.10.10.0 | 10.10.10.1 | 10.10.10.2 | /24   |
|   20 | 10.10.20.0 | 10.10.20.1 | 10.10.20.2 | /24   |

---

## Trin A — Byg i GNS3

* Noder: Ethernet switch, Linux-router (R1), to Linux-PC’er (PC1, PC2).
* Kabler: PC1→SW e1, PC2→SW e2, R1→SW e8.

## Trin B — Switch

* Opret VLAN 10 og 20.
* e1: access VLAN 10.
* e2: access VLAN 20.
* e8: trunk, allowed VLANs 10,20.
* Hvis “dot1q” trunk ikke findes: brug to R1-interfaces og to access-porte.

## Trin C — Router R1

```bash
sysctl -w net.ipv4.ip_forward=0
ip link add link eth0 name eth0.10 type vlan id 10
ip link add link eth0 name eth0.20 type vlan id 20
ip addr add 10.10.10.1/24 dev eth0.10
ip addr add 10.10.20.1/24 dev eth0.20
ip link set eth0.10 up
ip link set eth0.20 up
ip -d link show eth0.10
ip -d link show eth0.20
```

## Trin D — PC1 og PC2

```bash
# PC1 i VLAN10 (access-port)
ip addr flush dev eth0
ip addr add 10.10.10.2/24 dev eth0
ip route replace default via 10.10.10.1
ping -c2 10.10.10.1

# PC2 i VLAN20 (access-port)
ip addr flush dev eth0
ip addr add 10.10.20.2/24 dev eth0
ip route replace default via 10.10.20.1
ping -c2 10.10.20.1
```

## Verificering

* PC1 → 10.10.20.2 skal **fejle** når routing er OFF:

```bash
sysctl -w net.ipv4.ip_forward=0
ping -c3 10.10.20.2
```

* Snif tags på R1:

```bash
tcpdump -ni eth0 'vlan and icmp'
```

## Fejlsøgning

* Forkert access-VLAN på e1/e2 → ARP timeouts.
* Trunk uden VLAN20 → PC2 når ikke 10.10.20.1.
* 8021q mangler i værts-kernel → “Operation not supported”. Indlæs modulet på værten.
* Maske/gateway forkert på PC.

## Videre til Opgave 2

Tænd inter-VLAN routing og test:

```bash
sysctl -w net.ipv4.ip_forward=1
ping -c3 10.10.20.2   # fra PC1
traceroute 10.10.20.2 || tracepath 10.10.20.2
```
