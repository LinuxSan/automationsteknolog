# 🧪 Opgaver – ESP32 (Client) → Node.js (Modbus TCP Server)

I dette sæt øvelser konfigurerer du ESP32 som Modbus TCP-klient i MicroPython og Node.js som Modbus TCP-server. Formålet er at lære, hvordan man skriver og læser registre fra ESP32 til et brugerstyret system i Node.js.

---

## 🟢 Opgave 1 – Opsæt Modbus TCP-server i Node.js

**Formål:** Kør en simpel Modbus TCP-server i Node.js ved hjælp af `modbus-serial` eller `modbus-tcp`.

**Eksempel (Node.js):**

```js
const ModbusRTU = require('modbus-serial');
const serverTCP = new ModbusRTU.ServerTCP({
  holding: Buffer.alloc(10),
}, {
  host: '0.0.0.0',
  port: 502,
  debug: true,
  unitID: 1,
});

console.log("Modbus TCP-server kører på port 502");
```

**Alternativ:** Brug `jsmodbus` med en TCP-server-implementation.

---

## 🟠 Opgave 2 – ESP32 læser register fra Node.js

**Formål:** ESP32 læser register 0 fra Node.js-serveren

**ESP32-kode:**

```python
from umodbus.tcp import TCPClient

client = TCPClient(host='192.168.1.100', port=502)
value = client.read_holding_registers(address=0, count=1)
print("Modtaget fra server:", value[0])
```

**Udvidelse:**

* Kør læsning hvert 5. sekund og vis i seriel konsol

---

## 🔵 Opgave 3 – ESP32 skriver til Node.js-server

**Formål:** ESP32 sender fx temperaturdata til register 1

**ESP32-kode:**

```python
temp = 248  # 24.8°C
client.write_single_register(address=1, value=temp)
```

**Node.js-server:**

* Log alle `write`-operationer i terminalen
* Vis værdien i konsol eller gem i fil/log

---

## 🧠 Refleksionsspørgsmål

* Hvilke sikkerhedsaspekter bør man overveje ved åbne TCP-porte i Node.js?
* Hvordan valideres input fra ESP32 før det anvendes?
* Hvordan kan man kombinere denne løsning med MQTT, REST eller websockets?
