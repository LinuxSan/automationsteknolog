# Mosquitto via Docker Compose på Linux

## Krav
- Linux (Debian/Ubuntu/Fedora/Arch m.fl.)
- Docker + Docker Compose v2 (`docker compose -v`)
- Terminal med adgang til `docker` og `docker compose`

---

## 1) Projektstruktur
```

mosquitto-docker/
├─ docker-compose.yml
└─ mosquitto/
├─ config/
│  └─ mosquitto.conf
├─ data/
└─ log/

````

Opret mapper:
```bash
mkdir -p mosquitto-docker/mosquitto/{config,data,log}
cd mosquitto-docker
````

---

## 2) Konfiguration (`mosquitto/config/mosquitto.conf`)

```conf
persistence true
persistence_location /mosquitto/data/
log_dest stdout

allow_anonymous false
password_file /mosquitto/config/passwordfile

listener 1883
protocol mqtt

# WebSockets (valgfri)
listener 9001
protocol websockets
```

---

## 3) Docker Compose (`docker-compose.yml`)

```yaml
version: "3.9"
services:
  mosquitto:
    image: eclipse-mosquitto:2
    container_name: mosquitto
    restart: unless-stopped
    ports:
      - "1883:1883"   # MQTT
      - "9001:9001"   # WebSockets (valgfri)
    volumes:
      - ./mosquitto/config:/mosquitto/config
      - ./mosquitto/data:/mosquitto/data
      - ./mosquitto/log:/mosquitto/log
    environment:
      - TZ=Europe/Copenhagen
```

---

## 4) Opret bruger(e)

Lav `passwordfile` via containeren (kør i mappen med `docker-compose.yml`):

```bash
docker run --rm -v "$(pwd)/mosquitto/config:/mosquitto/config" eclipse-mosquitto:2 \
  mosquitto_passwd -c -b /mosquitto/config/passwordfile user1 'StærkHemmeligKode'
```

Flere brugere senere:

```bash
docker run --rm -v "$(pwd)/mosquitto/config:/mosquitto/config" eclipse-mosquitto:2 \
  mosquitto_passwd -b /mosquitto/config/passwordfile user2 'AndenKode'
```

---

## 5) Start broker

```bash
docker compose up -d
docker compose logs -f mosquitto
```

Firewall (UFW):

```bash
sudo ufw allow 1883/tcp
sudo ufw allow 9001/tcp
```

Firewall (firewalld):

```bash
sudo firewall-cmd --add-port=1883/tcp --permanent
sudo firewall-cmd --add-port=9001/tcp --permanent
sudo firewall-cmd --reload
```

---

## 6) Test

Installer klienter (Debian/Ubuntu):

```bash
sudo apt-get update && sudo apt-get install -y mosquitto-clients
```

Abonnér:

```bash
mosquitto_sub -h 127.0.0.1 -p 1883 -t 'test/emne' -u user1 -P 'StærkHemmeligKode' -v
```

Publicér (ny terminal):

```bash
mosquitto_pub -h 127.0.0.1 -p 1883 -t 'test/emne' -m 'hej' -u user1 -P 'StærkHemmeligKode'
```

Uden klientinstallation kan du teste i containeren:

```bash
docker exec -it mosquitto sh -c "mosquitto_pub -h 127.0.0.1 -p 1883 -t test/emne -m hej -u user1 -P 'StærkHemmeligKode'"
```

WebSockets: brug en web/GUІ-klient mod `ws://<host>:9001`.

---

## 7) TLS (valgfrit)

Generér selvsigneret cert (demo):

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ./mosquitto/config/server.key \
  -out   ./mosquitto/config/server.crt \
  -subj "/CN=$(hostname -f)"
```

Tilføj til `mosquitto.conf`:

```conf
listener 8883
protocol mqtt
certfile /mosquitto/config/server.crt
keyfile  /mosquitto/config/server.key
```

Genstart:

```bash
docker compose restart mosquitto
```

Test:

```bash
mosquitto_pub -h <host> -p 8883 --cafile ./mosquitto/config/server.crt \
  -t tls/test -m 'sekret' -u user1 -P 'StærkHemmeligKode' --tls-version tlsv1.2
```

---

## 8) Vedligehold

Logs:

```bash
docker compose logs -f mosquitto
```

Backup:

* `mosquitto/config/passwordfile`
* `mosquitto/config/mosquitto.conf`
* `mosquitto/data/` (persistence)

Opgradér:

```bash
docker compose pull mosquitto
docker compose up -d
```

Stop:

```bash
docker compose down
```

---

## 9) Fejl

* Auth-fejl: tjek `passwordfile` og `allow_anonymous false`.
* Port i brug: find proces (`sudo lsof -i :1883`) eller skift port.
* Ingen beskeder: samme topic og credentials på pub/sub.
* WebSockets: bekræft `listener 9001` og portmapping i Compose.
