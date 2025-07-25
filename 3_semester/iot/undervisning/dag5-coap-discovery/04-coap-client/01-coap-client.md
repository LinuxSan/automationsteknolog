# 🧪 Opgaver – CoAP 04: Client

Disse opgaver guider dig i at oprette og teste en CoAP-klient, enten i Python eller med ESP32. Du lærer at sende forespørgsler og fortolke svar fra en CoAP-server.

---

## 🟢 Opgave 1 – Python-klient GET-anmodning

1. Installer `aiocoap`:

```bash
pip install aiocoap
```

2. Opret script med denne funktion:

```python
from aiocoap import *
import asyncio

async def main():
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri='coap://<ESP32-IP>/temp')
    response = await protocol.request(request).response
    print('Result:', response.payload.decode())

asyncio.run(main())
```

3. Udskift `<ESP32-IP>` med den rigtige adresse og test

✅ *Resultatet vises i terminalen*

---

## 🔵 Opgave 2 – ESP32 som klient

1. Brug `CoAP-simple-library` i Arduino IDE
2. I `loop()` send fx hver 10. sekund:

```cpp
coap.get(IPAddress(192,168,1,50), 5683, "status");
```

3. Overvåg `Serial Monitor` for svar

✅ *ESP32 skal modtage svar og udskrive det*

---

## 🟡 Opgave 3 – PUT med JSON payload

1. I Python:

```python
payload = b'{"led": "ON"}'
request = Message(code=PUT, uri='coap://<IP>/led', payload=payload)
```

2. ESP32 eller server skal modtage JSON og tænde LED
3. Bekræft at CoAP-server svarer korrekt

✅ *CoAP-klienten kontrollerer aktuator vha. RESTful PUT*

---

## 🔁 Opgave 4 – Fejl og timeout-test

1. Sluk CoAP-serveren midlertidigt
2. Send GET fra klient og observer:

   * Timeout?
   * Exception?
   * Retry?
3. Tilføj logik til at håndtere manglende svar

✅ *Klienten håndterer netværksfejl robust*

---

## 🧠 Refleksion

* Hvordan adskiller en CoAP-klient sig fra en HTTP-klient?
* Hvad kræver det at skalere en klient til mange endpoints?
* Skal en klient gemme tidligere svar lokalt? Hvorfor/hvorfor ikke?

---

📌 CoAP-klienter er essentielle komponenter i RESTful IoT-systemer – og du har nu lært at bygge, teste og tilpasse dem til virkelige netværk.
