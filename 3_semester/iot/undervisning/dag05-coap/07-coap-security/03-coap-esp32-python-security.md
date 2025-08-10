# 🛡 CoAP – Sikkerhedsopgaver med ESP32 (MicroPython) og simpel Python-server

Disse opgaver viser, hvordan en ESP32-enhed kan sende data til en helt enkel Python-server (uden Flask) – med fokus på adgangskontrol og logning. Dette er den mest simple måde at simulere CoAP-lignende kommunikation.

---

## 🔐 Opgave 1 – PSK-validering på ESP32 → Python

**Formål:** Godkend data baseret på en delt nøgle (PSK).

### ESP32 (MicroPython)

```python
import urequests
psk = "sensorkey123"
headers = {"Authorization": psk}
urequests.post("http://<server-ip>:8080", headers=headers, data="23.5")
```

### Simpel Python-server

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        key = self.headers.get('Authorization')
        if key != 'sensorkey123':
            self.send_response(403)
            self.end_headers()
            print("Afvist anmodning fra:", self.client_address)
            return

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        print("Modtaget data:", post_data)

        self.send_response(200)
        self.end_headers()

server = HTTPServer(("", 8080), SimpleHandler)
print("Server kører på port 8080")
server.serve_forever()
```

---

## 📛 Opgave 2 – Hvidliste af enheder med device\_id

**Formål:** Tillad kun bestemte enheder baseret på et `device_id` i payload.

### ESP32 (MicroPython)

```python
urequests.post("http://<server-ip>:8080", headers=headers, data="device_id=esp01&value=21.7")
```

### Python-server (udvidet)

```python
white_list = ["esp01", "esp02"]

# i do_POST:
    fields = post_data.split('&')
    data = dict(f.split('=') for f in fields)
    if data.get('device_id') not in white_list:
        self.send_response(403)
        self.end_headers()
        print("Ugyldig enhed:", data.get('device_id'))
        return
    print(f"{data['device_id']} måler {data['value']}")
```

---

## 🔎 Opgave 3 – Log adgangsforsøg til tekstfil

**Formål:** Gem succes og fejl i en logfil.

### Udvid Python-server:

```python
from datetime import datetime

def log(event, info):
    with open("server_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] {event}: {info}\n")

# kald fx:
log("auth_success", self.client_address[0])
log("auth_fail", self.client_address[0])
```

---

✅ Disse opgaver viser, hvordan du med få linjer kode kan sikre og logge data sendt fra ESP32 til en simpel Python-server – helt uden eksterne biblioteker eller komplekse frameworks.
