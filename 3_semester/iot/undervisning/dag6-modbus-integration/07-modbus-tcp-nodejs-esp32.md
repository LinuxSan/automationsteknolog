# 🧪 Opgaver – Node.js (Client) → ESP32 (Modbus TCP Server)

Disse øvelser fokuserer på, hvordan du kan bruge Node.js som Modbus TCP-klient til at læse og skrive data til en ESP32, der kører som server med MicroPython. Du lærer at opsætte ESP32 med registrene og bruge Node.js til at kommunikere med den.

---

## 🟢 Opgave 1 – ESP32 som Modbus TCP-server

**Formål:** Kør en MicroPython-baseret Modbus TCP-server på ESP32 med to holding registers:

* Adresse 0: LED-styring (0 = slukket, 1 = tændt)
* Adresse 1: Temperatur (fx 235 = 23.5°C)

**Eksempel:**

```python
from umodbus.tcp import TCPServer

registers = {0: 0, 1: 235}  # LED + Temperatur

def on_write(address, value):
    print(f"Skrevet: adresse {address}, værdi {value}")
    if address == 0:
        # Tænd/sluk LED logik
        pass

server = TCPServer(regs=registers, on_write=on_write)
server.start(ip='0.0.0.0', port=502)
```

---

## 🟠 Opgave 2 – Læs register fra Node.js

**Formål:** Brug Node.js med `jsmodbus` til at læse temperatur fra register 1

**Node.js:**

```js
const Modbus = require('jsmodbus');
const net = require('net');

const socket = new net.Socket();
const client = new Modbus.client.TCP(socket);
const options = { host: '192.168.1.50', port: 502 };

socket.connect(options);

socket.on('connect', function () {
  client.readHoldingRegisters(1, 1)
    .then(response => {
      const value = response.response._body.valuesAsArray[0];
      console.log('Temperatur:', value / 10);
    })
    .catch(console.error);
});
```

---

## 🔵 Opgave 3 – Skriv værdi fra Node.js til ESP32

**Formål:** Skriv til register 0 for at styre LED-status

**Node.js:**

```js
client.writeSingleRegister(0, 1)  // Tænd LED
  .then(() => console.log('Skrev 1 til adresse 0'))
  .catch(console.error);
```

ESP32 vil logge handlingen og evt. udføre fysisk handling

---

## 🧠 Refleksionsspørgsmål

* Hvordan validerer du at ESP32 reagerer korrekt på Modbus-skriv?
* Hvordan kan du simulere fejlsituationer (forkert adresse, netværksfejl)?
* Hvordan skalerer denne løsning sammenlignet med HTTP eller MQTT?
