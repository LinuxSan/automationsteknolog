## 🚀 Installation af Node-RED med Docker Compose (Ubuntu)

Denne guide hjælper dig med at installere **Node-RED** på en Ubuntu-maskine ved hjælp af **Docker Compose**. Node-RED bruges i stigende grad i automations- og IoT-projekter, og Docker gør det nemt at installere og vedligeholde.

> ⚠️ **Forudsætning:** Docker Engine og Docker Compose skal være installeret og konfigureret korrekt på forhånd.

---

### 🟡 Trin 1: Opret projektmappe

```bash
mkdir ~/node-red && cd ~/node-red
```

---

### 🔵 Trin 2: Opret `docker-compose.yml`

Brug din foretrukne teksteditor, f.eks. nano:

```bash
nano docker-compose.yml
```

Indsæt følgende indhold:

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

### 🟣 Trin 3: Start Node-RED med Docker Compose

```bash
docker compose up -d
```

Docker henter Node-RED-billedet og starter containeren i baggrunden.

---

### 🔶 Trin 4: Åbn Node-RED i browser

Gå til:

```
http://localhost:1880
```

Du burde nu se Node-REDs floweditor.

---

### 🧹 Trin 5: Stop og genstart Node-RED

* Stop:

  ```bash
  docker compose stop
  ```
* Start:

  ```bash
  docker compose start
  ```
* Fjern container:

  ```bash
  docker compose down
  ```

---

### 🛠️ Ekstra tip

* Node-RED-data gemmes i `./data` mappen — tag backup herfra efter behov.
* Du kan tilføje flere services i `docker-compose.yml` (f.eks. Mosquitto, InfluxDB).

---

### 🎯 Klar til brug!

Node-RED kører nu på din Ubuntu-maskine via Docker Compose. Du kan begynde at bygge flows, integrere sensorer, og udvikle automatiseringsløsninger med høj fleksibilitet. ✅
