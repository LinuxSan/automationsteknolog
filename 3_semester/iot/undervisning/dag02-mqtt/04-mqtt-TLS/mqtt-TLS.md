# 🐳 MQTT Broker med TLS – Docker Compose

Denne vejledning forklarer, hvordan I opsætter en MQTT-broker (fx Mosquitto) **med TLS** inde i en Docker-container, og hvordan I gør `ca.crt` tilgængelig for andre grupper.

---

## 🧱 Docker Compose struktur

Strukturen for jeres projektmappe kan fx være:

```
node-red-tls/
├── docker-compose.yml
├── mosquitto/
│   ├── config/
│   │   └── mosquitto.conf
│   └── certs/
│       ├── ca.crt
│       ├── server.crt
│       └── server.key
```

---

## 🧾 Eksempel på docker-compose.yml

```yaml
version: '3.8'

services:
  mosquitto:
    image: eclipse-mosquitto
    container_name: mqtt_tls
    ports:
      - "1883:1883"
      - "8883:8883"
    volumes:
      - ./mosquitto/config:/mosquitto/config
      - ./mosquitto/certs:/mosquitto/certs
    restart: unless-stopped
```

---

## ⚙️ Eksempel på mosquitto.conf

```conf
listener 1883
allow_anonymous true

listener 8883
cafile /mosquitto/certs/ca.crt
certfile /mosquitto/certs/server.crt
keyfile /mosquitto/certs/server.key
require_certificate false
```

> Bemærk: Stien `/mosquitto/certs/` svarer til den interne sti i containeren. Mappestrukturen i host skal matche.

---

## 📤 Sådan deler du ca.crt med anden gruppe

### Trin 1: Gør filen synlig

Certifikatet `ca.crt` ligger i jeres `mosquitto/certs/` mappe. For at dele det:

**Metode A – Del mappen**

* Brug netværksdeling (Windows/Ubuntu) til at give læseadgang til `certs/`
* Alternativ: Del via USB, Teams, CryptPad, Git eller skolenetværk

**Metode B – Kopiér ud via container**

```bash
docker cp mqtt_tls:/mosquitto/certs/ca.crt ./ca-out/
```

* Nu ligger `ca.crt` i `./ca-out/` og kan nemt videresendes

---

## 🤝 Gruppe B – Brug af ca.crt i Node-RED

1. Gruppe B modtager `ca.crt` og gemmer den på deres maskine
2. Gå til Node-RED MQTT-broker-konfiguration
3. Aktivér TLS og vælg `ca.crt`
4. Brug IP’en fra Gruppe A og port `8883`
5. Forbind og test

> 💬 Hvis forbindelsen fejler, så dobbelttjek certifikatsti og portnummer.

---

## ✅ Klar til test

* Gruppe A starter deres broker via `docker compose up -d`
* Gruppe B forbinder med `ca.crt` og kan modtage beskeder sikkert

📷 **Dokumentation:** Begge grupper tager skærmbilleder af opsætning og beskedudveksling via TLS.
