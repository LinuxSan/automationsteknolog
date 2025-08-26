# Lab: 2 Linux‑PC’er + 1 Linux‑router (statisk routing) — Minimal

> **Mål**: Få PC1 og PC2 til at pinge hinanden via en simpel Linux‑router. Ingen firewall. Kun IPv4.

## Topologi og IP‑plan

```
PC1 ──(eth0)── Router ──(eth1)── PC2
```

| Enhed  | Interface | IP/Mask         | Gateway      |
| ------ | --------- | --------------- | ------------ |
| PC1    | eth0      | 192.168.10.2/24 | 192.168.10.1 |
| Router | eth0      | 192.168.10.1/24 | —            |
| Router | eth1      | 192.168.20.1/24 | —            |
| PC2    | eth0      | 192.168.20.2/24 | 192.168.20.1 |

## Kommandoer (midlertidig lab‑opsætning)

Tilpas `ethX` til dine interface‑navne.

### PC1

```bash
ip addr replace 192.168.10.2/24 dev eth0
ip link set eth0 up
ip route replace default via 192.168.10.1
```

### Router

```bash
ip addr replace 192.168.10.1/24 dev eth0
ip addr replace 192.168.20.1/24 dev eth1
ip link set eth0 up; ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1
```

### PC2

```bash
ip addr replace 192.168.20.2/24 dev eth0
ip link set eth0 up
ip route replace default via 192.168.20.1
```

## Verifikation

```bash
# fra PC1
ping -c3 192.168.10.1   # router eth0
ping -c3 192.168.20.1   # router eth1
ping -c3 192.168.20.2   # PC2
traceroute 192.168.20.2
```

Hvis det fejler, tjek i rækkefølge:

```bash
ip -br link           # interfaces skal være UP
ip -br a              # korrekte adresser
ip r                  # PC1/PC2 skal have default via router
cat /proc/sys/net/ipv4/ip_forward  # på router: 1
```

## Aflevering (kort)

* Skærmbillede af `ip a` og `ip r` på alle tre maskiner
* Ping og traceroute fra PC1 til PC2

> Bonus (valgfrit): Gem opsætningen permanent med netplan eller systemd‑networkd. Ikke et krav i denne opgave.
