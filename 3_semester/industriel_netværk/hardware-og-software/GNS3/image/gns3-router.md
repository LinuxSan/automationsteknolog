# 🧭 ITiFN Router (Docker) — Trin-for-trin (med emojis)

## 🔧 0) Variabler

```bash
export USERNAME="DIT_DOCKERHUB_BRUGERNAVN"     # fx acmeorg
export REPO="docker.io/${USERNAME}"
export BASE_TAG="${REPO}/itifn-base:1.0"
export ROUTER_TAG="${REPO}/itifn-router:1.0"

export BASEDIR="/home/aso/code/AAMS/Teknolog/03-semester/01-netværk/gns3/router"
mkdir -p "$BASEDIR/itifn/itifn-base" "$BASEDIR/itifn/itifn-router"
cd "$BASEDIR"
```

## 📦 1) Base-image (Alpine)

`itifn/itifn-base/Dockerfile`

```dockerfile
FROM alpine:3.20
LABEL maintainer="Anders Sandø Østergaard <aso@aams.dk>"
RUN apk add --no-cache bash iproute2 iputils busybox-extras ethtool \
    dhclient python3 perl tcpdump ca-certificates tini
ENTRYPOINT ["/sbin/tini","--"]
CMD ["bash"]
```

🛠️ Byg:

```bash
docker build -t "$BASE_TAG" itifn/itifn-base
```

## 🧱 2) Router-image

`itifn/itifn-router/Dockerfile`

```dockerfile
ARG BASE
FROM ${BASE}
LABEL maintainer="Anders Sandø Østergaard <aso@aams.dk>"
COPY entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh
ENTRYPOINT ["/sbin/tini","--","/bin/entrypoint.sh"]
CMD ["bash"]
```

`itifn/itifn-router/entrypoint.sh`

```sh
#!/bin/sh
set -eu
IFACES="${IFACES:-all default lo eth0}"
for iface in $IFACES; do
  sysctl -w "net.ipv6.conf.${iface}.autoconf=0" >/dev/null || true
  sysctl -w "net.ipv6.conf.${iface}.dad_transmits=0" >/dev/null || true
  sysctl -w "net.ipv6.conf.${iface}.accept_ra=0" >/dev/null || true
  sysctl -w "net.ipv6.conf.${iface}.router_solicitations=0" >/dev/null || true
done
[ "${IPV4_FORWARD:-0}" = "1" ] && sysctl -w net.ipv4.ip_forward=1 >/dev/null || true
[ "${IPV6_FORWARD:-0}" = "1" ] && sysctl -w net.ipv6.conf.all.forwarding=1 >/dev/null || true
exec "$@"
```

🚀 Byg:

```bash
docker build --build-arg BASE="$BASE_TAG" -t "$ROUTER_TAG" itifn/itifn-router
```

## ☁️ 3) Publicér (til GNS3-VM/remote)

```bash
docker login -u "$USERNAME"
docker push "$BASE_TAG"
docker push "$ROUTER_TAG"
```

💾 Alternativ uden Hub: `docker save | gzip` → `scp` → `docker load` på serveren.

## 🖱️ 4) GNS3-GUI template

1. **Edit → Preferences → Docker → Docker containers → New**
2. **Name**: `ITiFN Router`
3. **Image**: `"$ROUTER_TAG"`
4. **Adapters**: `4`
5. **Console type**: `None`
6. **Run as privileged**: **On**
7. **Environment**:

   * `IFACES=all default lo eth0`
   * `IPV4_FORWARD=1`
   * `IPV6_FORWARD=1`
8. **OK → Apply**

Brug: Træk noden ind, start, højreklik → **Console** (`bash`).

## 🌐 5) Hurtige net-kommandoer

```bash
# aktiver interface
ip link set eth1 up

# IPv4
ip addr add 192.168.0.15/24 dev eth0

# IPv6
ip -6 addr add 2001:db8:1::1/64 dev eth1

# default routes
ip route replace default via 192.168.0.1 dev eth0
ip -6 route replace default via 2001:db8::1 dev eth0
```

### 🧩 VLAN

```bash
ip link add link eth1 name eth1.10 type vlan id 10
ip link set eth1 up; ip link set eth1.10 up
ip addr add 10.10.10.1/24 dev eth1.10
ip -6 addr add 2001:db8:10::1/64 dev eth1.10
```

### ✅ Tjek

```bash
ip addr show
ip route; ip -6 route
ping -c 2 8.8.8.8
ping -6 -c 2 2001:4860:4860::8888
```

## 🧩 6) Enkel “persistens” via Environment (valgfrit)

Tilføj i `entrypoint.sh` før `exec "$@"`:

```sh
[ -n "${IP4_ETH1:-}" ] && { ip link set eth1 up; ip addr add "$IP4_ETH1" dev eth1; }
[ -n "${IP6_ETH1:-}" ] && { ip link set eth1 up; ip -6 addr add "$IP6_ETH1" dev eth1; }
[ -n "${GW4:-}" ]      && ip route replace default via "$GW4" dev eth0
[ -n "${GW6:-}" ]      && ip -6 route replace default via "$GW6" dev eth0
```

🌱 Sæt i template → **Environment**:

```
IP4_ETH1=192.168.10.1/24
IP6_ETH1=2001:db8:10::1/64
GW4=192.168.0.1
GW6=2001:db8::1
```

## 🛠️ 7) Fejlfinding

* 🔒 **Pull-fejl**: Brug præcist image-tag. Test `docker pull "$ROUTER_TAG"` på GNS3-server.
* 🧷 **Sysctl virker ikke**: Template skal være **privileged**.
* 🧭 **Ingen rute**: Sæt gateway eller IP i samme subnet. `ip route` viser sandheden.
* 🖥️ **Console**: `None` for Docker-noder.

## 📦 8) (Valgfrit) `.gns3a`-skabelon

Erstat `IMAGE_TAG_HERE` med `"$ROUTER_TAG"`.

```json
{
  "name": "ITiFN Router (Docker)",
  "category": "router",
  "vendor_name": "Custom",
  "registry_version": 8,
  "status": "stable",
  "description": "Alpine router. IPv6 RA disabled. Bash shell.",
  "maintainer": "Anders Sandø Østergaard <aso@aams.dk>",
  "settings": [
    {
      "default": true,
      "template_type": "docker",
      "template_properties": {
        "image": "IMAGE_TAG_HERE",
        "adapters": 4,
        "console_type": "none",
        "privileged": true,
        "environment": [
          "IFACES=all default lo eth0",
          "IPV4_FORWARD=1",
          "IPV6_FORWARD=1"
        ],
        "category": "router"
      }
    }
  ]
}
```
