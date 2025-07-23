## 🐧 Guide: Installation af Docker Compose på Linux (Ubuntu/Debian)

Docker Compose bruges til at definere og køre multi-container Docker-applikationer. Denne guide viser, hvordan du installerer den nyeste version af Docker Compose som plugin eller standalone.

---

### 🟢 Trin 1: Installer Docker Engine

Først skal Docker være installeret:

```bash
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

Tilføj din bruger til docker-gruppen:

```bash
sudo usermod -aG docker $USER
```

Log ud og ind igen (eller kør `newgrp docker`).

---

### 🟡 Trin 2: Verificér Docker og Compose

Tjek at både Docker og Compose virker:

```bash
docker --version
docker compose version
```

---

### 🔵 Trin 3: Test med Compose

1. Opret en testmappe:

```bash
mkdir ~/docker-compose-test && cd ~/docker-compose-test
```

2. Opret filen `docker-compose.yml`:

```yaml
version: "3"
services:
  hello:
    image: hello-world
```

3. Kør:

```bash
docker compose up
```

Hvis det virker, ser du:

```
Hello from Docker!
```

---

### 🛠️ Alternativ: Installer standalone Docker Compose (V1/V2)

Bruges kun hvis Compose-plugin ikke ønskes:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.5/docker-compose-$(uname -s)-$(uname -m)" \
  -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

Tjek version:

```bash
docker-compose --version
```

> ⚠️ Dette bruges sjældent med nyere Docker. Foretræk plugin (`docker compose`).

---

### 📌 Noter

* `docker compose` (mellemrum) er den moderne metode
* `docker-compose` (bindestreg) er forældet
* Du kan placere `docker-compose.yml` hvor du vil, så længe du befinder dig i mappen

---

🎉 Du har nu installeret Docker Compose på Linux og er klar til at bygge container-baserede applikationer!
