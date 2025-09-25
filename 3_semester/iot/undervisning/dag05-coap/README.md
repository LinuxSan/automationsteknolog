# coapmini (MicroPython)

Lightweight CoAP GET-server til ESP32. Minimal overflade, indbygget discovery (`/.well-known/core`), nul eksterne afhængigheder. Designet til hurtig time-to-value i undervisning.

## Installér biblioteket på enheden

1. Kopiér **`coapmini.py`** til roden af ESP32-filsystemet (samme sted som `main.py`).
2. Verificér at filen ligger der (fil-liste skal vise `coapmini.py`).

> Done. Klar til brug i alle nye projekter.

---

## Quickstart (nyt projekt)

Opret **`main.py`**:

```python
# main.py — minimal demo med coapmini
import urandom
from coapmini import wifi_connect, CoapServer, CF_JSON

# 1) Wi-Fi
SSID = "YOUR_SSID"
PSK  = "YOUR_PASSWORD"
wifi_connect(SSID, PSK, verbose=True)

# 2) Demo-model (random walk)
def rnd(): return urandom.getrandbits(16)/65535
temp, hum = 22.5, 45.0
def dht_sim():
    global temp, hum
    temp += (rnd()-0.5)*0.4
    hum  += (rnd()-0.5)*1.2
    temp = min(max(temp,18.0),30.0)
    hum  = min(max(hum,25.0),70.0)
    return {"sensor":"DHT22(sim)","temperature":round(temp,2),"humidity":round(hum,2),"unit":"C/%"}

# 3) CoAP-server + routing
srv = CoapServer(port=5683, verbose=True, send_404=True)
srv.add("/dht", dht_sim, rt="sensor.temperature", iface="sensor", ct=CF_JSON)
srv.serve_forever("READY → GET /.well-known/core eller /dht")
```

**Forventet konsol-output**

```
Wi-Fi: forbundet <ESP-IP>
CoAP: lytter på udp/5683; routes: /dht
CoAP: discovery via GET /.well-known/core
```

---

## Test fra din computer (samme net)

```bash
# Discovery (CoRE Link Format)
coap-client -m get coap://<ESP-IP>:5683/.well-known/core -A application/link-format

# Data (JSON)
coap-client -m get coap://<ESP-IP>:5683/dht -A application/json
```

Eksempel-output:

```
</dht>;rt="sensor.temperature";if="sensor";ct=50
{"sensor":"DHT22(sim)","temperature":22.1,"humidity":44.8,"unit":"C/%"}
```

Node-RED quick client: `coap request` (GET) → `coap://<ESP-IP>:5683/dht`, og sæt `Accept=application/json`.

---

## API—det du skal bruge, og kun det

```python
from coapmini import wifi_connect, CoapServer, CF_JSON, CF_TEXT, CF_LINK
```

### `wifi_connect(ssid, psk, retries=10, connect_window_ms=7000, verbose=True)`

* Robust STA-connect (radio-reset, backoff, statusprint).
* Returnerer `WLAN` ved success.
* Valgfri – håndtér selv Wi-Fi hvis ønsket.

### `CoapServer(port=5683, bind_ip="0.0.0.0", verbose=True, send_404=True)`

* Starter en UDP/5683 CoAP-server.
* `verbose=True`: logger requests og banner.
* `send_404=True`: ukendte paths svarer 4.04 (ellers stilhed).

### `srv.add(path, handler, rt=None, iface=None, ct=CF_JSON)`

Registrér en ressource (endpoint):

* **path**: URI, fx `"/dht"` ( `"dht"` normaliseres også til `"/dht"` ).
* **handler()**: din **funktions-callback uden argumenter**. Køres på hver GET.

  * Returnér:

    * `dict` → sendes som **JSON** (Content-Format=50)
    * `str` → sendes som **text/plain** (CF=0)
    * `bytes|bytearray` → sendes råt (brug `ct` hvis ikke standard)
    * andre typer → pakkes som `{"value": …}` (JSON)
* **rt**: *resource type* til discovery (fx `"sensor.temperature"`).
* **iface**: *interface description* til discovery (fx `"sensor"`).
* **ct**: *content-format ID* (50=JSON, 0=tekst, 40=link-format). Kan som regel udelades ved `dict`.

**Effekt i discovery** (`/.well-known/core`):

```
</dht>;rt="sensor.temperature";if="sensor";ct=50
```

### `srv.serve_forever(banner=None)`

* Kører den blokkerende serverloop. Understøtter:

  * `GET /.well-known/core` → CoRE Link Format (ID 40)
  * `GET /<path>` → 2.05 Content med din payload

---

## Mønstre der skalerer (copy-paste klar)

### Flere endpoints

```python
srv.add("/temp", lambda: {"temperature": 23.1, "unit":"°C"},
        rt="sensor.temperature", iface="sensor")
srv.add("/hum",  lambda: {"humidity": 46.2, "unit":"%"},
        rt="sensor.humidity",    iface="sensor")
```

### Tekst- og bytes-svar

```python
srv.add("/hello", lambda: "hej verden")              # str → text/plain (ct=0)
srv.add("/raw",   lambda: b"\x01\x02\x03", ct=42)    # bytes → custom CF=42
```

### Minimal (uden metadata og ct)

```python
def ping(): return {"status": "ok"}
srv.add("/ping", ping)   # dict → JSON (ct=50) automatisk
```

---

## Troubleshooting (to-the-point)

* **4.04 Not Found** → Path mismatch. Tjek banneret: `routes: /dht, /temp, …` og brug præcis samme URI.
* **Discovery viser ikke dit endpoint** → Sørg for at `srv.add(...)` kaldes **før** `serve_forever()`.
* **Hotspots** blokerer ofte multicast. Unicast discovery (direkte IP) virker fint.
* **Vil du se runtime-paths** → kør med `verbose=True` (standard), så logger serveren `GET /path fra <ip>`.

---

## One-pager demo (klar til undervisning)

```python
import urandom
from coapmini import wifi_connect, CoapServer, CF_JSON

wifi_connect("YOUR_SSID", "YOUR_PASSWORD")

def rnd(): return urandom.getrandbits(16)/65535
temp, hum = 22.5, 45.0
def dht_sim():
    global temp, hum
    temp += (rnd()-0.5)*0.4
    hum  += (rnd()-0.5)*1.2
    temp = min(max(temp,18.0),30.0)
    hum  = min(max(hum,25.0),70.0)
    return {"sensor":"DHT22(sim)","temperature":round(temp,2),"humidity":round(hum,2),"unit":"C/%"}

srv = CoapServer(port=5683, verbose=True, send_404=True)
srv.add("/dht", dht_sim, rt="sensor.temperature", iface="sensor", ct=CF_JSON)
srv.add("/hello", lambda: "hej verden")
srv.serve_forever("READY → GET /.well-known/core, /dht, /hello")
```

**Test**

```bash
coap-client -m get coap://<ESP-IP>:5683/.well-known/core -A application/link-format
coap-client -m get coap://<ESP-IP>:5683/dht   -A application/json
coap-client -m get coap://<ESP-IP>:5683/hello -A text/plain
```

---

Det her er “low-friction onboarding”: én fil at lægge på enheden, én linje per ressource, og discovery “just works”. Når I er klar til næste sprint, kan vi udvide libbet med **Observe** og **POST/PUT** uden at bryde API’et.
