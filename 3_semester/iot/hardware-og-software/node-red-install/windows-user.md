## 🚀 Installation af Node-RED med Docker Compose (Windows)

Denne guide hjælper dig med at installere **Node-RED** på en Windows-maskine ved hjælp af **Docker Compose**. Node-RED er et flow-baseret udviklingsværktøj, særligt anvendt i IoT og automationsprojekter.

> ⚠️ **Forudsætning:** Docker Desktop og Docker Compose skal være installeret og fungerende på din maskine, før du går i gang.

---

### 🟢 Trin 1: Kontroller Docker-installationen

1. Åbn PowerShell eller CMD og tjek at Docker og Compose virker:

   ```bash
   docker --version
   docker compose version
   ```
2. Hvis du får versionsnumre retur, er du klar til næste trin.

---

### 🟡 Trin 2: Opret projektmappe

1. Opret en ny mappe, fx `C:\Users\<bruger>\node-red`
2. Åbn mappen i VS Code eller din terminal

---

### 🔵 Trin 3: Opret `docker-compose.yml`

1. I projektmappen, opret en fil med navnet `docker-compose.yml`
2. Indsæt følgende indhold i filen:

```yaml
version: "3"
services:
  nodered:
    image: nodered/node-red:latest
    container_name: nodered
    ports:
      - "1880:1880"
    volumes:
      - ./data:/data
    restart: unless-stopped
```

---

### 🟣 Trin 4: Start Node-RED med Docker Compose

1. Åbn en terminal i projektmappen (Shift + højreklik → "Åbn PowerShell her")
2. Kør kommandoen:

   ```bash
   docker compose up -d
   ```
3. Første gang vil Docker hente image og oprette containeren

---

### 🔶 Trin 5: Åbn Node-RED i browser

1. Gå til:

   ```
   http://localhost:1880
   ```
2. Du burde nu se Node-REDs visuelle editor

---

### 🧹 Trin 6: Stop og genstart Node-RED

* Stop:

  ```bash
  docker compose stop
  ```
* Start igen:

  ```bash
  docker compose start
  ```
* Fjern containeren helt:

  ```bash
  docker compose down
  ```

---

### 🛠️ Ekstra (valgfrit): Automatisk netværk og volumen-mappe

* Alt data i Node-RED gemmes i `./data`-mappen – denne kan du tage backup af.
* Alle services i `docker-compose.yml` deler et isoleret netværk.

---

### 🎯 Klar til brug!

Du har nu en fuldt fungerende Node-RED-installation via Docker Compose på Windows. Nu kan du begynde at bygge flows, integrere IoT-enheder og udvikle automationsløsninger direkte fra din browser. ✅
