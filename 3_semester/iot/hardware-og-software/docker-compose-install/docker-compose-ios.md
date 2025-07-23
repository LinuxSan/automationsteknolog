## 🍏 Guide: Installation af Docker Compose på macOS

Docker Compose gør det muligt at definere og køre multi-container Docker-applikationer. På macOS installeres det nemmest gennem Docker Desktop.

---

### 🟢 Trin 1: Installer Docker Desktop

1. Gå til den officielle side:
   [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

2. Vælg "Download for Mac" (Apple Silicon eller Intel)

3. Åbn `.dmg`-filen og træk Docker-ikonet til `Applications`

4. Start Docker Desktop (første opstart kan tage lidt tid)

5. Bekræft installationen:

```bash
docker --version
docker compose version
```

---

### 🟡 Trin 2: Test Docker Compose

1. Åbn **Terminal**
2. Opret en ny mappe og gå ind i den:

```bash
mkdir ~/docker-compose-test && cd ~/docker-compose-test
```

3. Opret en fil `docker-compose.yml`:

```yaml
version: "3"
services:
  hello:
    image: hello-world
```

4. Kør:

```bash
docker compose up
```

5. Hvis det virker, vil du se:

```
Hello from Docker!
```

---

### 🔄 Fejlfinding

* ❌ **Docker starter ikke:** Genstart Mac og prøv igen
* ❌ **"command not found" for Docker:** Kontrollér at Docker Desktop kører
* ❌ **Tilladelser:** Giv Docker tilladelse i Systemindstillinger → Sikkerhed

---

### 📌 Noter

* Docker Compose er integreret i Docker Desktop (v2+)
* Brug `docker compose` med mellemrum – ikke `docker-compose`
* Data gemmes som udgangspunkt i `~/Library/Containers/com.docker.docker/`

---

🎉 Du har nu Docker Compose klar på din Mac og er klar til at opbygge moderne containerbaserede applikationer!
