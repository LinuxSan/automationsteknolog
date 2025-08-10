# 🧪 Opgaver – CoAP 04: Client (Python version)

Denne udgave viser, hvordan du bruger Python som CoAP-klient ved hjælp af biblioteket `aiocoap`. Du lærer at sende GET- og PUT-anmodninger, håndtere svar og teste robustheden i CoAP-kommunikationen.

---

## 🟢 Opgave 1 – Installér og test `aiocoap`

1. Opret et virtuelt miljø (valgfrit, men anbefalet):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Installer `aiocoap`:

```bash
pip install aiocoap
```

3. Bekræft installationen:

```bash
python -c "import aiocoap; print('aiocoap klar')"
```

✅ *Python-miljø er klar til brug med aiocoap*

---

## 🔵 Opgave 2 – Send GET-anmodning

1. Opret en fil `get_temp.py`:

```python
from aiocoap import *
import asyncio

async def main():
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri='coap://<ESP32-IP>/temp')
    try:
        response = await protocol.request(request).response
        print('Svar:', response.payload.decode())
    except Exception as e:
        print('Fejl:', e)

asyncio.run(main())
```

2. Udskift `<ESP32-IP>` med IP-adressen på din CoAP-server
3. Kør scriptet:

```bash
python get_temp.py
```

✅ *Du ser temperatur-data returneret fra ESP32 i terminalen*

---

## 🟡 Opgave 3 – Send PUT-anmodning med JSON

1. Opret fil `put_led.py`:

```python
from aiocoap import *
import asyncio

async def main():
    protocol = await Context.create_client_context()
    payload = b'{"led": "ON"}'
    request = Message(code=PUT, uri='coap://<ESP32-IP>/led', payload=payload)
    try:
        response = await protocol.request(request).response
        print('Svar:', response.payload.decode())
    except Exception as e:
        print('Fejl:', e)

asyncio.run(main())
```

2. Kør scriptet med ESP32 aktiveret

✅ *LED tændes og ESP32 returnerer bekræftelse som svar*

---

## 🔁 Opgave 4 – Timeout og fejl

1. Afbryd netværket eller sluk ESP32
2. Kør GET- eller PUT-script og observer fejl
3. Tilføj fejlhåndtering og logging for at gøre systemet mere robust

✅ *Programmet fejler ikke, men rapporterer klart at der ikke kom svar*

---

## 🧠 Refleksion

* Hvordan håndterer Python retries og timeouts i UDP-baserede protokoller?
* Kunne du udvide klienten til at parse JSON og udtrække værdier?
* Hvad ville være næste skridt for at logge eller videresende CoAP-data til en database eller MQTT?

---

📌 Python med `aiocoap` gør det nemt at udvikle fleksible og scriptbare CoAP-klienter, særligt nyttigt i undervisning, datalogi og testautomatisering.
