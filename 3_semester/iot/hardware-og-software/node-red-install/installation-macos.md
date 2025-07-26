## 🍏 Installation af Node-RED med Docker Compose (macOS)

Denne guide hjælper dig med at installere **Node-RED** på en Mac ved hjælp af **Docker Compose**. Node-RED er et flow-baseret udviklingsværktøj, særligt anvendt i IoT- og automationsprojekter.

> ⚠️ **Forudsætning:** Docker Desktop og Docker Compose skal være installeret og fungerende på din Mac, før du går i gang.

---

### 🟡 Trin 1: Opret projektmappe

Åbn Terminal og kør:

```bash
mkdir -p ~/node-red && cd ~/node-red
```

---

### 🔵 Trin 2: Opret `docker-compose.yml`

Brug din foretrukne teksteditor (fx `nano` eller Visual Studio Code):

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

Gem og luk filen (Ctrl + O, Enter, Ctrl + X).

---

### 🟣 Trin 3: Start Node-RED med Docker Compose

```bash
docker compose up -d
```

Docker henter Node-RED-image og starter containeren i baggrunden.

---

### 🔶 Trin 4: Åbn Node-RED i browser

Gå til:

```
http://localhost:1880
```

Du burde nu se Node-REDs grafiske floweditor.

---

### 🧹 Trin 5: Administrér din Node-RED container

* Stop:

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

### 🛠️ Ekstra tips

* Data gemmes i `./data`-mappen – den kan du tage backup af.
* Du kan tilføje flere services (fx Mosquitto eller PostgreSQL) i samme `docker-compose.yml`

---

### 🎯 Klar til brug!

Du har nu Node-RED kørende lokalt på din Mac via Docker Compose og kan begynde at bygge IoT-løsninger og automatisering direkte i din browser. ✅
