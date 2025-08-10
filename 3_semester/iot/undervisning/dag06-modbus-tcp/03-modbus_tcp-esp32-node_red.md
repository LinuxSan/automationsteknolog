# 🧪 Opgaver – ESP32 (MicroPython) → Node-RED

Disse øvelser fokuserer på at sende Modbus TCP-anmodninger fra en ESP32 (klient) til en Node-RED Modbus TCP-server. Øvelserne træner praktisk brug af MicroPython og hvordan man læser/skriver data til industrielle systemer via netværket.

---

## 🟢 Opgave 1 – Opsæt Node-RED som Modbus TCP-server

**Formål:** Konfigurér en Modbus TCP-server i Node-RED, der eksponerer et register, som ESP32 kan læse.

**Materialer:**

* Node-RED med `node-red-contrib-modbus`
* Flow med `modbus-flex-server`

**Trin:**

1. Tilføj `modbus-flex-server` og sæt port til 5020 (for at undgå rootkrav)
2. Tilføj et holding register med værdi 123 (fx adresse 0)
3. Brug `inject`-node til at ændre registerværdien løbende
4. Brug `debug` til at overvåge serveradfærd

---

## 🟠 Opgave 2 – Læs fra ESP32 som Modbus TCP-klient

**Formål:** Konfigurer ESP32 som Modbus TCP-klient, der læser data fra Node-RED-serveren.

**MicroPython-krav:**

* Netværksforbindelse
* Modbus TCP-klientbibliotek (fx `uModbus` eller `modbus_tk`-kompatibel)

**Eksempelkode:**

```python
from umodbus.tcp import TCPClient

client = TCPClient(host='192.168.1.100', port=5020)
value = client.read_holding_registers(address=0, count=1)
print("Læst værdi:", value[0])
```

**Udvidelse:**

* Læs register hvert 10. sekund og send til ESP32’s seriel monitor

---

## 🔵 Opgave 3 – Skriv til Node-RED fra ESP32

**Formål:** Brug ESP32 til at skrive en værdi til Node-RED’s Modbus-server

**ESP32:**

```python
client.write_single_register(address=1, value=555)
```

**Node-RED:**

* Brug `modbus-flex-server` til at håndtere skriveadgang
* Overvåg ændringer i `debug`-output
* Visualisér registrene på dashboard

---

## 🧠 Refleksionsspørgsmål

* Hvordan valideres om ESP32 har sendt korrekte Modbus-rammer?
* Hvilke udfordringer har du oplevet med timing eller netværksstabilitet?
* Hvordan kan du logge eller visualisere Modbus-transaktioner i Node-RED?

> 💡 Bonus: Udvid ESP32 til at læse en lokal sensor (fx temperatur) og skriv den til Node-RED via Modbus TCP.
