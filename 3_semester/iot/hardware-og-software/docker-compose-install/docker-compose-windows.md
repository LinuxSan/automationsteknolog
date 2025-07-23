## 🪟 Guide: Installation af Docker Compose på Windows 10/11

Docker Compose bruges til at definere og køre multi-container Docker-applikationer. På Windows installeres Docker Compose sammen med Docker Desktop.

---

### 🟢 Trin 1: Download og installer Docker Desktop

1. Gå til den officielle hjemmeside:
   [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

2. Klik på **"Download for Windows (Windows 10/11)"**

3. Kør installationsfilen:

   * Kræver administrator-rettigheder
   * Følg installationsguiden
   * Vælg at aktivere WSL 2 integration (anbefalet)

4. Genstart computeren efter installationen (hvis påkrævet)

---

### 🟡 Trin 2: Verificér installationen af Docker og Docker Compose

1. Åbn **PowerShell** eller **CMD** (som almindelig bruger eller admin)

2. Kør følgende kommandoer:

```bash
docker --version
docker compose version
```

Eksempel på output:

```
Docker version 24.0.5, build abc123
Docker Compose version v2.24.5
```

---

### 🔵 Trin 3: Test Docker Compose virker

1. Opret en mappe:

```bash
mkdir C:\Users\<dit-brugernavn>\docker-test
cd C:\Users\<dit-brugernavn>\docker-test
```

2. Opret en fil med navnet `docker-compose.yml` og indsæt dette indhold:

```yaml
version: "3"
services:
  hello:
    image: hello-world
```

3. Kør Docker Compose:

```bash
docker compose up
```

4. Hvis det virker, ser du beskeden: `Hello from Docker!`

---

### 🛠️ Fejlfinding

* ❌ **"docker: command not found"**: Docker Desktop er ikke korrekt installeret
* ❌ **WSL 2 ikke installeret**: Følg guiden her:
  [https://learn.microsoft.com/windows/wsl/install](https://learn.microsoft.com/windows/wsl/install)
* ❌ **Firewall eller antivirus blokerer**: Tilføj Docker som undtagelse

---

### 📌 Noter

* Docker Compose bruges nu som: `docker compose` (med mellemrum)
* Den gamle version `docker-compose` (med bindestreg) er forældet
* Docker Desktop opdaterer automatisk Compose til nyeste version

---

🎉 Du er nu klar til at bruge Docker Compose på Windows!
