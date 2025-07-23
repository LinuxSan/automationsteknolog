## 🚀 Installation af Node-RED med Docker Compose (Ubuntu)

Denne guide hjælper dig med at installere **Node-RED** på en Ubuntu-maskine ved hjælp af **Docker Compose**. Node-RED bruges i stigende grad i automations- og IoT-projekter, og Docker gør det nemt at installere og vedligeholde.

---

### 🟢 Trin 1: Installer Docker og Docker Compose

Åbn en terminal og kør følgende kommandoer:

```bash
# Opdater systemet
sudo apt update && sudo apt upgrade -y

# Installer nødvendige pakker
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Tilføj Dockers GPG-nøgle og repository
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Installer Docker og Docker Compose plugin
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Aktiver og start Docker
sudo systemctl enable docker
sudo systemctl start docker

# Gør det muligt at bruge Docker uden sudo (kræver genstart)
sudo usermod -aG docker $USER
```

🔁 Log ud og ind igen, eller genstart din maskine for at ændringen træder i kraft.

---

### 🟡 Trin 2: Opret projektmappe

```bash
mkdir ~/node-red && cd ~/node-red
```

---

### 🔵 Trin 3: Opret `docker-compose.yml`

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

### 🟣 Trin 4: Start Node-RED med Docker Compose

```bash
docker compose up -d
```

Docker henter Node-RED-billedet og starter containeren i baggrunden.

---

### 🔶 Trin 5: Åbn Node-RED i browser

Gå til:

```
http://localhost:1880
```

Du burde nu se Node-REDs floweditor.

---

### 🧹 Trin 6: Stop og genstart Node-RED

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
