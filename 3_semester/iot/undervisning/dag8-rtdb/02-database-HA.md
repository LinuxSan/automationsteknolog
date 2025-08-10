# 🧪 Opgaver – Dag 8: Firebase og Microsoft SQL (Home Assistant Fokus)

Disse opgaver guider dig i, hvordan du integrerer Firebase og Microsoft SQL med Home Assistant (HA) til opsamling og visning af IoT-data. Øvelserne er simple og fokuserer på opsætning og brug af eksisterende integrationer og scripts.

---

## 🔥 Firebase

### 🟢 Opgave 1 – Læs data fra Firebase i Home Assistant

**Formål:** Læse temperaturdata gemt i Firebase og vise dem i HA.

**Trin:**

1. Opret et Firebase-projekt og tilføj en realtime database
2. Brug en ekstern REST API-integration i Home Assistant (fx via `rest` sensor):

```yaml
sensor:
  - platform: rest
    name: "Firebase Temperatur"
    resource: https://<firebase-url>/sensor/temp.json
    value_template: "{{ value }}"
    scan_interval: 60
```

3. Genstart HA og tilføj sensoren til dit dashboard

---

### 🟠 Opgave 2 – Skriv data til Firebase fra Home Assistant

**Formål:** Sende data fra HA til Firebase (fx automation eller knaptryk)

**Trin:**

1. Brug `rest_command` integration i `configuration.yaml`:

```yaml
rest_command:
  upload_temp:
    url: "https://<firebase-url>/sensor/temp.json"
    method: PUT
    payload: "{{ states('sensor.indoor_temperature') }}"
    content_type: 'application/json'
```

2. Kald `rest_command.upload_temp` fra en automation eller knap i UI

---

## 🗃 Microsoft SQL Server

### 🟢 Opgave 3 – Indsæt HA-data i SQL med Node-RED eller mellemserver

**Formål:** Send data fra Home Assistant til en Microsoft SQL Server via HTTP og mellemlag

**Trin:**

1. I HA: brug webhook, automation eller REST til at sende data til en mellemserver (fx Node-RED)
2. På mellemserver: brug et script der indsætter i SQL med INSERT INTO
3. Alternativt: brug `command_line` integration til at køre Python-script lokalt

---

### 🟠 Opgave 4 – Vis SQL-data i Home Assistant

**Formål:** Træk data fra SQL-database og vis dem som sensor i HA

**Trin:**

1. Brug `command_line` sensor til at køre et Python-script som forespørger SQL:

```yaml
sensor:
  - platform: command_line
    name: "SQL Temperatur"
    command: "python3 /config/scripts/read_sql_temp.py"
    scan_interval: 120
```

2. I script: brug `pyodbc` eller `pymssql` til at lave SELECT og udskrive én værdi
3. Vis sensoren i dashboard

---

## ⚖️ Sammenligning og refleksion

### 🔵 Opgave 5 – Overvej integrationsvalg i Home Assistant

**Formål:** Reflekter over integrationer, vedligehold og latency

**Trin:**

1. Lav en tabel over dine to integrationer:

   * Tilgængelighed
   * Sværhedsgrad
   * Overvågning/mulighed for fejl
2. Svar på:

   * Hvilken metode vil du bruge i produktion?
   * Er der forskel på realtid og stabilitet?

---

📌 Øvelserne er lavet, så du kan arbejde med eksisterende HA-funktioner uden at bygge fuld backend – men kan udvides efter behov.
