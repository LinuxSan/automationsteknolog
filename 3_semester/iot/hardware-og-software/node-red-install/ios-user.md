## 🚀 Installation af Node-RED med Docker Compose (macOS)

Denne guide hjælper dig med at installere **Node-RED** på en Mac ved hjælp af **Docker Desktop** og **Docker Compose**. Det er en nem og vedligeholdelsesvenlig metode til at afvikle Node-RED lokalt til IoT- og automationsprojekter.

---

### 🍏 Trin 1: Installer Docker Desktop på macOS

1. Gå til [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
2. Vælg "Download for Mac (Apple chip eller Intel chip)"
3. Åbn den downloadede `.dmg`-fil og træk Docker-ikonet over i `Applications`
4. Start Docker Desktop (kan tage lidt tid første gang)
5. Bekræft at Docker kører ved at åbne Terminal og skrive:

   ```bash
   docker --version
   docker compose version
   ```

---

### 📁 Trin 2: Opret projektmappe til Node-RED

Åbn Terminal og kør:

```bash
mkdir ~/node-red
cd ~/node-red
```

---

### 📝 Trin 3: Opret `docker-compose.yml`

Brug `nano`, `vim` eller en teksteditor som VS Code:

```bash
nano docker-compose.yml
```

Indsæt følgende konfiguration:

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

Gem og luk (Ctrl + O, Enter, Ctrl + X).

---

### ▶️ Trin 4: Start Node-RED med Docker Compose

I Terminal, mens du er i mappen `~/node-red`, skriv:

```bash
docker compose up -d
```

Docker vil hente Node-RED billedet og starte containeren.

---

### 🌐 Trin 5: Åbn Node-RED i din browser

Gå til:

```
http://localhost:1880
```

Du burde nu se brugerfladen til Node-RED.

---

### 🔄 Trin 6: Stop og genstart Node-RED

* Stop Node-RED:

  ```bash
  docker compose stop
  ```
* Start igen:

  ```bash
  docker compose start
  ```
* Fjern container:

  ```bash
  docker compose down
  ```

---

### 💡 Ekstra tips

* Alle data gemmes i `./data` – det kan du tage backup af.
* Ønsker du at tilføje fx Mosquitto eller InfluxDB, kan du udvide `docker-compose.yml`.

---

### 🎯 Nu er du klar!

Node-RED kører nu på din Mac via Docker Compose. Du er klar til at opbygge flows, forbinde sensorer og udvikle komplette IoT-løsninger direkte fra din browser. ✅
