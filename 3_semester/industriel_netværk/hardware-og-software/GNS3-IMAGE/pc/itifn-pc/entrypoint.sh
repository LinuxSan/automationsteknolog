#!/bin/sh
set -eu
IFACES="${IFACES:-eth0}"
[ "${DHCP4:-0}" = "1" ] && for i in $IFACES; do dhclient -4 -v "$i" || true; done
[ "${DHCP6:-0}" = "1" ] && for i in $IFACES; do dhclient -6 -v "$i" || true; done
if [ -n "${IP4:-}" ]; then IF4="$(echo "$IP4"|cut -d@ -f2)"; A4="$(echo "$IP4"|cut -d@ -f1)"; ip link set "$IF4" up; ip addr add "$A4" dev "$IF4"; fi
if [ -n "${IP6:-}" ]; then IF6="$(echo "$IP6"|cut -d@ -f2)"; A6="$(echo "$IP6"|cut -d@ -f1)"; ip link set "$IF6" up; ip -6 addr add "$A6" dev "$IF6"; fi
[ -n "${GW4:-}" ] && ip route replace default via "$(echo "$GW4"|cut -d@ -f1)" dev "$(echo "$GW4"|cut -d@ -f2)"
[ -n "${GW6:-}" ] && ip -6 route replace default via "$(echo "$GW6"|cut -d@ -f1)" dev "$(echo "$GW6"|cut -d@ -f2)"
exec "$@"
