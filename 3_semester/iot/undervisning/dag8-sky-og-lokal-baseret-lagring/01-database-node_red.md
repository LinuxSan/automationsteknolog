# 🧪 Opgaver – Dag 8: Firebase og Microsoft SQL (Node-RED Fokus)

Her finder du en række simple, vejledende øvelser som introducerer brugen af Firebase og Microsoft SQL Server i konteksten af IoT – med fokus på Node-RED som forbindelsesled.

---

## 🔥 Firebase

### 🟢 Opgave 1 – Læs data i Node-RED fra Firebase

**Formål:** Visualisere Firebase-data i Node-RED

**Trin:**

1. Opret et Firebase-projekt og find URL + adgangsnøgle
2. Installer `node-red-contrib-firebase` i Node-RED
3. Brug en `firebase in` node til at overvåge fx `"/sensor/temp"`
4. Vis værdierne med en `debug` node eller `ui_chart`

---

### 🟠 Opgave 2 – Skriv data til Firebase fra Node-RED

**Formål:** Sende testdata til Firebase via Node-RED

**Trin:**

1. Tilføj en `inject` node med JSON-data, fx `{ "temp": 24.5 }`
2. Forbind til en `firebase out` node
3. Send data til stien `"/sensor/temp"`
4. Tjek i Firebase Console at værdien opdateres

---

## 🗃 Microsoft SQL Server

### 🟢 Opgave 3 – Indsæt data i SQL fra Node-RED

**Formål:** Gemme sensordata i en struktureret SQL-tabel

**Trin:**

1. Installer `node-red-node-mssql` og forbind til SQL Server
2. Opret en tabel i databasen med fx `timestamp`, `temp`, `humidity`
3. Brug `inject` → `function` → `mssql` flow til at sende `INSERT INTO`-kommandoer
4. Verificér indsættelse i SSMS eller anden databaseklient

---

### 🟠 Opgave 4 – Forespørg og vis SQL-data

**Formål:** Læse og vise data i Node-RED

**Trin:**

1. Brug en `inject` node til at sende en SQL-forespørgsel, fx `SELECT * FROM data`
2. Tilslut til `mssql` node og vis output med `debug` eller `ui_table`
3. Eksperimentér med `ORDER BY` og `LIMIT` for at vise udvalgte rækker

---

## ⚖️ Sammenligning og refleksion

### 🔵 Opgave 5 – Sammenlign Firebase og SQL (fra Node-RED)

**Formål:** Forstå forskelle gennem praktisk integration

**Trin:**

1. Notér dine erfaringer med:

   * Opsætningstid
   * Datastruktur
   * Hastighed
   * Lethed af integration i flows
2. Diskutér: Hvornår giver det mening at bruge den ene fremfor den anden?

---

📌 Alle øvelser kan løses udelukkende i Node-RED – med testdata eller reelle sensorkilder.
