# 📘 MQTT – Teori og Begreber

Denne sektion forklarer de vigtigste begreber og mekanismer i **MQTT (Message Queuing Telemetry Transport)** – en af de mest anvendte protokoller i IoT.

---

## 🔄 Hvad er MQTT?

MQTT er en letvægts-protokol til **publish/subscribe-kommunikation** over TCP/IP. Den er designet til situationer med:

* Lav båndbredde
* Høj latency
* Ressourcebegrænsede enheder

Det bruges typisk i **IoT-løsninger** til at sende data mellem sensorer, aktuatorer og backend-systemer (fx dashboards, databaser).

---

## 🧭 Publish/Subscribe-modellen

MQTT anvender en **broker** til at formidle beskeder mellem enheder:

* En **publisher** sender beskeder til en **topic**
* En **subscriber** abonnerer på én eller flere topics
* **Broker** sørger for at distribuere beskeder til relevante subscribers

MQTT er **decoupled**: afsendere og modtagere kender ikke hinanden.

Eksempel:

* Publisher: `sensor/temp` → 22.5°C
* Subscriber: `sensor/#` modtager alle under-temaer

---

## 📂 Topics og struktur

Topics er hierarkiske strenge med `/` som separator:

```
sensor/bygning1/rum2/temp
```

Wildcards:

* `+` = én vilkårlig del
* `#` = alle underliggende

Eksempel:

* `sensor/+/rum2/temp` → alle bygninger
* `sensor/#` → alle målinger

---

## 📈 QoS – Quality of Service

MQTT understøtter tre niveauer af leveringssikkerhed:

| Niveau | Navn          | Betydning                        |
| ------ | ------------- | -------------------------------- |
| 0      | At most once  | Ingen bekræftelse (hurtigst)     |
| 1      | At least once | Bekræftelse, kan duplikere       |
| 2      | Exactly once  | Dobbelt håndtryk, ingen duplikat |

QoS vælges af publisher og kan konfigureres i både terminal og Node-RED.

---

## 📌 Retained messages

En **retained** besked gemmes af broker, og **sendes straks til nye subscribers** på en topic.

Eksempel:

* Topic: `status/rum1`
* Payload: `Lys tændt`
* Retained = true

Fordel: seneste status er altid tilgængelig – også for nye forbindelser.

---

## 🕊️ Last Will & Testament (LWT)

En **Last Will** er en besked, som en klient beder brokeren om at sende **hvis forbindelsen pludselig afbrydes**.

Eksempel:

* Will topic: `status/enhed1`
* Will message: `offline`

Det bruges til overvågning, alarmer og systemstatus.

---

## ♻️ Clean Session & Persistent Session

* **Clean session = true**: ingen historik gemmes
* **Clean session = false**: klientens subscriptions og uafleverede beskeder bevares

Persistent sessions er nyttige ved ustabile forbindelser og mobile enheder.

---

## 🔐 Sikkerhed og autentificering

MQTT understøtter:

* Brugernavn + adgangskode
* TLS-kryptering (over port 8883)
* Adgangskontrol pr. topic (ACL)

I undervisningsmiljøer bruges ofte en simpel broker uden adgangskontrol.

---

## 🧠 Opsummering

| Element   | Funktion                               |
| --------- | -------------------------------------- |
| Broker    | Central enhed, der fordeler beskeder   |
| Topic     | Identifikator for beskedkanal          |
| QoS       | Leveringssikkerhed                     |
| Retained  | Gemt seneste besked                    |
| Last Will | Automatisk status ved nedbrud          |
| Pub/Sub   | Uafhængig kommunikation mellem enheder |

MQTT er effektivt, fleksibelt og ideelt til IoT. Gennem praksis lærer du, hvordan man udnytter det i både lokale og cloud-baserede systemer.
