# Mosquitto via Docker Compose på Windows

## Krav
- Windows 10/11
- Docker Desktop (WSL2 backend)
- PowerShell

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
```powershell
mkdir mosquitto-docker\mosquitto\config, mosquitto-docker\mosquitto\data, mosquitto-docker\mosquitto\log
cd mosquitto-docker
````

---

## 2) Konfiguration (`mosquitto\config\mosquitto.conf`)

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
      - "1883:1883"
      - "9001:9001"
    volumes:
      - ./mosquitto/config:/mosquitto/config
      - ./mosquitto/data:/mosquitto/data
      - ./mosquitto/log:/mosquitto/log
    environment:
      - TZ=Europe/Copenhagen
```

---

## 4) Opret bruger(e)

Lav `passwordfile` via containeren og bind mount. Kør i mappen med `docker-compose.yml`:

```powershell
$pwdPath = (Get-Location).Path
docker run --rm -v "$pwdPath\mosquitto\config:/mosquitto/config" eclipse-mosquitto:2 `
  mosquitto_passwd -c -b /mosquitto/config/passwordfile user1 "StærkHemmeligKode"
```

Flere brugere senere:

```powershell
docker run --rm -v "$pwdPath\mosquitto\config:/mosquitto/config" eclipse-mosquitto:2 `
  mosquitto_passwd -b /mosquitto/config/passwordfile user2 "AndenKode"
```

---

## 5) Start broker

```powershell
docker compose up -d
docker compose logs -f mosquitto
```

Åbn Windows Firewall-porte:

```powershell
netsh advfirewall firewall add rule name="Mosquitto MQTT 1883" dir=in action=allow protocol=TCP localport=1883
netsh advfirewall firewall add rule name="Mosquitto WS 9001"   dir=in action=allow protocol=TCP localport=9001
```

---

## 6) Test uden ekstra installation

Kør klienter inde i containeren.

```powershell
docker exec -it mosquitto sh
# inde i containeren:
mosquitto_sub -h 127.0.0.1 -p 1883 -t test/emne -u user1 -P "StærkHemmeligKode" -v
# i en anden PowerShell:
docker exec -it mosquitto sh -c "mosquitto_pub -h 127.0.0.1 -p 1883 -t test/emne -m hej -u user1 -P 'StærkHemmeligKode'"
```

WebSockets test fra valgfri GUI-klient der kan bruge `ws://<din-host>:9001`.

---

## 7) TLS (valgfrit)

```powershell
openssl req -x509 -nodes -days 365 -newkey rsa:2048 `
  -keyout .\mosquitto\config\server.key `
  -out .\mosquitto\config\server.crt `
  -subj "/CN=$(hostname)"
```

Tilføj til `mosquitto.conf`:

```conf
listener 8883
protocol mqtt
certfile /mosquitto/config/server.crt
keyfile  /mosquitto/config/server.key
```

Genstart:

```powershell
docker compose restart mosquitto
```

---

## 8) Vedligehold

Logs:

```powershell
docker compose logs -f mosquitto
```

Backup: `mosquitto/config/passwordfile`, `mosquitto/config/mosquitto.conf`, mappen `mosquitto/data/`.

Opgradér:

```powershell
docker compose pull mosquitto
docker compose up -d
```

Stop:

```powershell
docker compose down
```

---

## 9) Fejl

* Auth-fejl: tjek `passwordfile` og `allow_anonymous false`.
* Port bruges: find proces eller ændr port.
* Ingen beskeder: brug samme topic og credentials.
* WebSockets virker ikke: bekræft `listener 9001` og portmapping.
