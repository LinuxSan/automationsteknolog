# 🧪 Opgaver – CoAP 04: Client (Home Assistant version)

Denne udgave fokuserer på, hvordan du bruger Home Assistant som klient til at anmode om data fra enheder via CoAP. Vi udnytter RESTful strukturer, template-sensorer og automatisering for at hente og bruge data i et smart home miljø.

---

## 🟢 Opgave 1 – Forstå CoAP i Home Assistant sammenhæng

1. Læs om forskellen mellem HTTP og CoAP (UDP-baseret, lav overhead)
2. Overvej hvorfor CoAP passer godt til sensorbaserede systemer
3. Tænk over hvilken slags data du vil hente fra ESP32

✅ *Du forstår CoAP's relevans i energieffektive smart home-systemer*

---

## 🔵 Opgave 2 – Brug `rest_command` som CoAP gateway (via proxy)

1. Installér en lokal proxy på fx Raspberry Pi, der omdanner HTTP til CoAP (fx coap-http bridge)
2. I Home Assistant `configuration.yaml`:

```yaml
rest_command:
  get_temperature:
    url: "http://localhost:8080/proxy/coap://<ESP32-IP>/temp"
    method: GET
```

3. Brug `script:` eller `automation:` til at kalde kommandoen

✅ *Home Assistant kan indirekte kommunikere med CoAP-enheder*

---

## 🟡 Opgave 3 – Opret sensors med data fra CoAP endpoint

1. Kombiner `rest_command` med `command_line sensor`:

```yaml
sensor:
  - platform: command_line
    name: "Stue Temperatur"
    command: "curl -s http://localhost:8080/proxy/coap://<ESP32-IP>/temp"
    unit_of_measurement: "°C"
    scan_interval: 30
```

2. Tilføj sensoren til dit dashboard og verificér værdien

✅ *Sensor opdateres periodisk og viser live data fra CoAP-serveren*

---

## 🔁 Opgave 4 – Styring via PUT til CoAP endpoint

1. Opret `rest_command` med PUT-metode:

```yaml
rest_command:
  toggle_led:
    url: "http://localhost:8080/proxy/coap://<ESP32-IP>/led"
    method: PUT
    payload: '{"led": "ON"}'
    content_type: 'application/json'
```

2. Tilføj en `script:` i HA til at kalde kommandoen:

```yaml
script:
  tænd_led:
    sequence:
      - service: rest_command.toggle_led
```

3. Vis knap i dashboard med:

```yaml
type: button
name: Tænd LED
tap_action:
  action: call-service
  service: script.tænd_led
```

✅ *Du kan styre LED fra Home Assistant via CoAP (indirekte)*

---

## 🧠 Refleksion

* Hvorfor bruger vi en HTTP-CoAP proxy?
* Kunne man skrive en HA-integration direkte i Python der bruger CoAP?
* Hvordan kan CoAP give dig hurtigere eller mere energieffektive flows end fx MQTT?

---

📌 Home Assistant kan udvides til at bruge CoAP gennem mellemled, hvilket muliggør integration med ultralette IoT-enheder – især nyttigt i energifølsomme og mobile miljøer.
