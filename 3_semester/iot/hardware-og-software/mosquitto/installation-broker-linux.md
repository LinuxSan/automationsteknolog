# Mosquitto via Docker Compose på Linux

## Krav
- Linux med Docker og `docker compose` (Compose v2).  
- Ingen anden broker på port 1883, eller brug alternativ port.

---

## 0) Compose v2 (hvis mangler)
```bash
docker compose version || {
  sudo mkdir -p /usr/local/lib/docker/cli-plugins
  sudo curl -SL https://github.com/docker/compose/releases/download/v2.27.1/docker-compose-linux-x86_64 \
    -o /usr/local/lib/docker/cli-plugins/docker-compose
  sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
  docker compose version
}
````

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
```

```bash
mkdir -p mosquitto-docker/mosquitto/{config,data,log}
cd mosquitto-docker
```

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

> Hvis du har en systemd-mosquitto kørende, stop den:
> `sudo systemctl stop mosquitto && sudo systemctl disable mosquitto`

---

## 3) Docker Compose (`docker-compose.yml`)

> Fjern `version:`. Den er udfaset.

```yaml
services:
  mosquitto:
    image: eclipse-mosquitto:2
    container_name: mosquitto
    restart: unless-stopped
    # Brug 1883 kun hvis ikke i konflikt. Ellers skift til 1884:1883.
    ports:
      - "1883:1883"
      - "9001:9001"   # valgfri WebSockets
    volumes:
      - ./mosquitto/config:/mosquitto/config
      - ./mosquitto/data:/mosquitto/data
      - ./mosquitto/log:/mosquitto/log
    environment:
      - TZ=Europe/Copenhagen
```

Port-konflikt løsning: brug

```yaml
ports:
  - "1884:1883"
  - "9001:9001"
```

---

## 4) Opret passwordfil med korrekt ejerskab (UID 1883)

```bash
# Luk ned hvis en container kører allerede
docker compose down || true

# Opret passwordfil inde fra billedet som bruger 1883:1883
docker run --rm -u 1883:1883 \
  -v "$(pwd)/mosquitto/config:/mosquitto/config" eclipse-mosquitto:2 \
  mosquitto_passwd -c -b /mosquitto/config/passwordfile user1 'StærkHemmeligKode'

# Sørg for ejerskab på alle mountede mapper
sudo chown -R 1883:1883 mosquitto/config mosquitto/data mosquitto/log
```

Flere brugere senere:

```bash
docker run --rm -u 1883:1883 \
  -v "$(pwd)/mosquitto/config:/mosquitto/config" eclipse-mosquitto:2 \
  mosquitto_passwd -b /mosquitto/config/passwordfile user2 'AndenKode'
```

---

## 5) Start broker og se logs

```bash
docker compose up -d
docker compose logs -f mosquitto
```

---

## 6) Test

Installer klienter (Debian/Ubuntu):

```bash
sudo apt-get update && sudo apt-get install -y mosquitto-clients
```

Subscriber:

```bash
mosquitto_sub -h 127.0.0.1 -p 1883 -t 'test/emne' -u user1 -P 'StærkHemmeligKode' -v
# hvis du brugte 1884: mosquitto_sub -p 1884 ...
```

Publisher:

```bash
mosquitto_pub -h 127.0.0.1 -p 1883 -t 'test/emne' -m 'hej' -u user1 -P 'StærkHemmeligKode'
```

Uden klientinstallation:

```bash
docker exec -it mosquitto sh -c "mosquitto_pub -h 127.0.0.1 -p 1883 -t test/emne -m hej -u user1 -P 'StærkHemmeligKode'"
```

---

## 7) Node-RED

* Kører Node-RED i samme Compose-net: Server `mosquitto`, Port `1883`, WebSockets = off, brug `user1` + password.
* Kører Node-RED på værten: Server `127.0.0.1`, Port `1883` (eller `1884` hvis du mappede sådan).
* Subscriber ser kun nye beskeder. Brug retain hvis ønsket:

```bash
mosquitto_pub -r -t 'test/emne' -m 'persistent' -u user1 -P 'StærkHemmeligKode'
```

---

## 8) TLS (valgfrit)

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ./mosquitto/config/server.key \
  -out   ./mosquitto/config/server.crt \
  -subj "/CN=$(hostname -f)"
```

Tilføj i `mosquitto.conf`:

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

---

## 9) Vedligehold

```bash
docker compose logs -f mosquitto
docker compose pull mosquitto && docker compose up -d
docker compose down
```

---

## 10) Fejl og fix

* **`Unable to open pwfile` / kode 13:** Opret passwordfil som ovenfor og sikr `chown -R 1883:1883`.
* **`Address already in use 1883`:** Stop systemd-mosquitto (`sudo systemctl stop/disable mosquitto`) eller map til `1884:1883`.
* **Ingen forbindelser i log:** Forkert host/port eller forkerte credentials.
* **CRLF i config (skrevet på Windows):** `sudo apt-get install -y dos2unix && dos2unix mosquitto/config/mosquitto.conf`.

Her er en klar “10)”-sektion til din Linux-README.

## 11) Brugere og passwords (tilføj, ændr, slet)

Kør i mappen med `docker-compose.yml`. Filen er `mosquitto/config/passwordfile`.

> Tip: Mosquitto læser først filen ved start. Genindlæs med `docker compose restart mosquitto`.

### Tilføj ny bruger
```bash
docker run --rm -u 1883:1883 \
  -v "$(pwd)/mosquitto/config:/mosquitto/config" eclipse-mosquitto:2 \
  mosquitto_passwd -b /mosquitto/config/passwordfile nybruger 'NyStærkKode'

# sikre ejerskab (hvis nødvendigt)
sudo chown 1883:1883 mosquitto/config/passwordfile
docker compose restart mosquitto
````

### Ændr password for eksisterende bruger

```bash
docker run --rm -u 1883:1883 \
  -v "$(pwd)/mosquitto/config:/mosquitto/config" eclipse-mosquitto:2 \
  mosquitto_passwd -b /mosquitto/config/passwordfile eksisterende 'NyStærkKode'
sudo chown 1883:1883 mosquitto/config/passwordfile
docker compose restart mosquitto
```

### Slet bruger

```bash
docker run --rm -u 1883:1883 \
  -v "$(pwd)/mosquitto/config:/mosquitto/config" eclipse-mosquitto:2 \
  mosquitto_passwd -D /mosquitto/config/passwordfile brugernavn
sudo chown 1883:1883 mosquitto/config/passwordfile
docker compose restart mosquitto
```

### Opret første bruger (hvis filen ikke findes endnu)

```bash
docker run --rm -u 1883:1883 \
  -v "$(pwd)/mosquitto/config:/mosquitto/config" eclipse-mosquitto:2 \
  mosquitto_passwd -c -b /mosquitto/config/passwordfile user1 'StærkHemmeligKode'
sudo chown 1883:1883 mosquitto/config/passwordfile
docker compose restart mosquitto
```

### Verificér

```bash
docker exec -it mosquitto sh -c \
"mosquitto_pub -h 127.0.0.1 -p 1883 -t test/emne -m OK -u user1 -P 'StærkHemmeligKode'"
```

> Bemærk: Brug `-c` kun til at oprette/erstatte hele passwordfilen. Uden `-c` tilføjer/ændrer du enkeltbrugere.
