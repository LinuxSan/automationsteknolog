
# 📘 DAG 8 – Firebase og Microsoft SQL: Cloud- og databasesynkronisering

Denne undervisningsdag fokuserer på to vidt forskellige databaseplatforme – Google Firebase og Microsoft SQL Server. Målet er at give dig en grundlæggende forståelse af, hvordan data fra IoT-enheder kan lagres og tilgås via både skybaserede og lokale databaser.

---

## 🎯 Læringsmål

* Forstå forskellen mellem realtime databaser (Firebase) og relationsdatabaser (SQL)
* Opsætte simple datastrukturer og skrive/læse data
* Koble IoT-data til database via Node-RED, Python eller ESP32
* Overveje fordele og ulemper ved de to tilgange

---

## 🔍 Platformsoverblik

| Funktion        | Firebase                | Microsoft SQL Server      |
| --------------- | ----------------------- | ------------------------- |
| Type            | NoSQL Realtime Database | Relational Database (SQL) |
| Dataformat      | JSON                    | Tabeller og rækker        |
| Adgang          | REST API, SDK           | ODBC, SQL, .NET           |
| Anvendelse      | Hurtig app-integration  | Struktureret dataanalyse  |
| Hosting         | Cloud (Google)          | Lokalt eller Azure        |
| Offline support | Ja                      | Nej                       |

---

## 🧠 Refleksion

* Hvornår vil du bruge Firebase frem for SQL?
* Hvordan påvirker datastrukturen dine forespørgsler?
* Hvad betyder latency og tilgængelighed i valget af database?

---

📌 Du finder øvelser til Firebase og SQL i separate dokumenter – fx:

* `firebase-01-esp32-upload.md`
* `sql-01-node-red-query.md`
* `firebase-vs-sql-case.md`
