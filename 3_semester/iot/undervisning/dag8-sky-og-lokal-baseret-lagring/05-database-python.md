# 🧪 Opgaver – Dag 8: Firebase og Microsoft SQL (Python Fokus)

Disse opgaver introducerer, hvordan du med Python kan kommunikere med både Firebase og Microsoft SQL Server. Alle opgaver er enkle og fokuserer på at sende og læse data.

---

## 🔥 Firebase

### 🟢 Opgave 1 – Skriv data til Firebase med Python

**Formål:** Lære at sende temperaturdata til Firebase

**Trin:**

1. Installer biblioteket `firebase-admin`:

```bash
pip install firebase-admin
```

2. Hent et service account JSON-nøgle fra Firebase Console
3. Eksempel på script:

```python
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://<projekt-id>.firebaseio.com'
})

db.reference('sensor/temp').set(23.7)
```

---

### 🟠 Opgave 2 – Læs data fra Firebase

**Formål:** Udskrive en temperaturværdi fra databasen

**Trin:**

1. Udbyg forrige script med:

```python
temp = db.reference('sensor/temp').get()
print("Temperatur:", temp)
```

---

## 🗃 Microsoft SQL Server

### 🟢 Opgave 3 – Indsæt data i SQL med Python

**Formål:** Gemme måledata i en tabel via Python

**Trin:**

1. Installer bibliotek `pyodbc` eller `pymssql`

```bash
pip install pyodbc
```

2. Eksempel med `pyodbc`:

```python
import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=localhost;DATABASE=iot;'
                      'UID=brugernavn;PWD=kode')

cursor = conn.cursor()
cursor.execute("INSERT INTO data (temp, humidity) VALUES (?, ?)", 24.5, 48)
conn.commit()
print("Data indsat")
```

---

### 🟠 Opgave 4 – Læs data fra SQL og vis i terminal

**Formål:** Udtrække de seneste målinger

**Trin:**

```python
cursor.execute("SELECT TOP 5 * FROM data ORDER BY timestamp DESC")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

---

## ⚖️ Sammenligning og refleksion

### 🔵 Opgave 5 – Evaluer Python-integrationer

**Formål:** Reflektere over forskelle mellem Firebase og SQL

**Trin:**

1. Skriv ned:

   * Hvilket bibliotek var lettest at sætte op?
   * Hvordan adskiller dataformaterne sig?
   * Hvilket setup ville du bruge i et produktionsmiljø – og hvorfor?

---

📌 Du kan løse alle opgaver i én `.py`-fil per platform og eksperimentere videre med udvidelser.
