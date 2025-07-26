# 🧪 Opgaver – Dag 8: Firebase og Microsoft SQL (Node.js Fokus)

Disse opgaver guider dig i, hvordan du med Node.js kan kommunikere med både Firebase og Microsoft SQL Server. Opgaverne er simple og fokuserer på grundlæggende læsning og skrivning af data.

---

## 🔥 Firebase

### 🟢 Opgave 1 – Skriv data til Firebase med Node.js

**Formål:** Lære at sende data til Firebase Realtime Database

**Trin:**

1. Opret et Firebase-projekt og aktiver Realtime Database
2. Installer Firebase SDK i Node.js-projekt:

```bash
npm install firebase
```

3. Skriv et script der sender temperaturdata:

```js
const { initializeApp } = require('firebase/app');
const { getDatabase, ref, set } = require('firebase/database');

const firebaseConfig = {
  databaseURL: "https://<projekt-id>.firebaseio.com"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

set(ref(db, 'sensor/temp'), 23.7);
```

---

### 🟠 Opgave 2 – Læs data fra Firebase

**Formål:** Hente og udskrive realtime data

**Trin:**

1. Udbyg dit script fra Opgave 1:

```js
const { onValue } = require('firebase/database');

const tempRef = ref(db, 'sensor/temp');
onValue(tempRef, (snapshot) => {
  console.log('Temperatur:', snapshot.val());
});
```

2. Test at det opdateres når du ændrer værdien i konsollen

---

## 🗃 Microsoft SQL Server

### 🟢 Opgave 3 – Indsæt data i SQL med Node.js

**Formål:** Lære at sende data til en SQL-database

**Trin:**

1. Installer `mssql`-pakken:

```bash
npm install mssql
```

2. Opret forbindelse og indsæt data:

```js
const sql = require('mssql');

const config = {
  user: 'brugernavn',
  password: 'kode',
  server: 'localhost',
  database: 'iot',
  options: {
    trustServerCertificate: true
  }
};

async function insertData() {
  try {
    await sql.connect(config);
    await sql.query(`INSERT INTO data (temp, humidity) VALUES (24.5, 48)`);
    console.log('Indsat i database');
  } catch (err) {
    console.error(err);
  }
}

insertData();
```

---

### 🟠 Opgave 4 – Læs data fra SQL og vis i konsol

**Formål:** Læse sensordata og udskrive det

**Trin:**

1. Udvid forrige script:

```js
async function fetchData() {
  try {
    await sql.connect(config);
    const result = await sql.query(`SELECT TOP 5 * FROM data ORDER BY timestamp DESC`);
    console.log(result.recordset);
  } catch (err) {
    console.error(err);
  }
}

fetchData();
```

---

## ⚖️ Sammenligning og refleksion

### 🔵 Opgave 5 – Sammenlign integrationer

**Formål:** Forstå forskelle i udviklingsoplevelse

**Trin:**

1. Reflektér over:

   * Hvor hurtigt kom du i gang?
   * Hvilken database føltes mest fleksibel?
   * Hvilken API var lettest at forstå?
2. Vælg hvilken du vil bruge til et fremtidigt IoT-projekt – og hvorfor

---

📌 Du kan løse alle opgaver direkte i et enkelt Node.js-script per database.
