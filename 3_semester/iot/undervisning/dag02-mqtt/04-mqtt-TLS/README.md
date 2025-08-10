# 🔐 README – MQTT med TLS (Transport Layer Security)

Denne fil giver en introduktion til, hvordan MQTT kan sikres med TLS, så data mellem klient og broker ikke kan opsnappes, forfalskes eller manipuleres. Det er relevant i både industrielle netværk og smart home-scenarier med cloud-kommunikation.

---

## 🧠 Hvorfor TLS med MQTT?

MQTT er som standard en ukrypteret protokol (port 1883), hvilket gør den sårbar overfor:

* Man-in-the-middle (MITM) angreb
* Aflytning (sniffing) af credentials og data
* Forfalskede beskeder fra uautoriserede enheder

TLS (Transport Layer Security) løser dette ved at:

* Kryptere forbindelsen
* Muliggøre certificeret godkendelse af klient og server
* Forhindre datamanipulation under transport

---

## 🔧 Portnumre og protokolvalg

| Funktion      | Port |
| ------------- | ---- |
| MQTT uden TLS | 1883 |
| MQTT med TLS  | 8883 |

Broker skal understøtte TLS – fx Mosquitto, HiveMQ eller EMQX.

---

## 🔐 Certifikater og krypteringstyper

TLS anvender X.509-certifikater. De kan være:

* **Selvsignerede** (til testformål)
* **Officielle fra CA** (i produktion, fx Let’s Encrypt)

Filer der typisk bruges:

* `ca.crt`: CA-certifikat
* `server.crt` og `server.key`: Brokerens certifikat og nøgle
* `client.crt` og `client.key`: (valgfrit) Klientens certifikat

---

## 📦 Eksempel: Mosquitto med TLS (lokal test)

1. Generér selvsignerede certifikater (kan gøres med OpenSSL)
2. Rediger `/etc/mosquitto/mosquitto.conf`:

```conf
listener 8883
cafile /etc/mosquitto/certs/ca.crt
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
auth_plugin /etc/mosquitto/passwd
require_certificate false
```

3. Genstart broker:

```bash
sudo systemctl restart mosquitto
```

4. Forbind med klient (mosquitto\_pub/sub):

```bash
mosquitto_sub -h <broker-ip> -p 8883 --cafile ca.crt -t "test/secure"
```

---

## 🔐 TLS i Node-RED

1. Gå til din MQTT-broker-konfiguration i Node-RED
2. Marker “Enable secure (SSL/TLS) connection”
3. Indlæs `ca.crt` og evt. klientcertifikater
4. Sæt port til `8883`

> 💡 TLS virker også med public cloud brokers (fx HiveMQ Cloud, Adafruit IO)

---

## 🛡 Best Practices

* Brug altid TLS over internet
* Sæt adgangskodebeskyttelse på broker og clients
* Roter certifikater årligt
* Log sikkerhedsbrud

---

## 🧪 Test din sikkerhed

* Brug Wireshark til at bekræfte krypteret trafik
* Simuler MITM-angreb i testmiljø (fx med ettercap)
* Brug stærke nøgler (2048-bit RSA eller ECC)

---

## 📚 Læs mere

* [Mosquitto TLS guide (officiel)](https://mosquitto.org/man/mosquitto-tls-7.html)
* [Let’s Encrypt gratis certifikater](https://letsencrypt.org/)
* [Node-RED MQTT Docs](https://nodered.org/docs/user-guide/mqtt/)

---

🔒 *Ved at bruge TLS med MQTT tager du et vigtigt skridt mod sikre og professionelle IoT-installationer.*
