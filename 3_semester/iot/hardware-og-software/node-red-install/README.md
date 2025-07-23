# 📘 README – Node-RED Installation med Docker Compose

Dette projekt indeholder tre vejledningsfiler, som guider brugeren i installation og opstart af **Node-RED** via **Docker Compose** på forskellige operativsystemer. Hver guide er skræddersyet til platformens tekniske forudsætninger og brugeroplevelse.

## 🗂️ Indhold

### 1. `Node-red Installation Windows`

* Trinvis guide til opsætning af Node-RED med Docker Compose på **Windows 10/11**.
* Indeholder instruktion i:

  * Installation af Docker Desktop
  * Oprettelse af projektmappe og `docker-compose.yml`
  * Opstart og adgang via browser
  * Basal containerstyring (start/stop/down)

### 2. `Node-red Installation Ubuntu`

* Trinvis terminalbaseret guide til **Ubuntu-brugere**.
* Dækker:

  * Installation af Docker og Docker Compose via terminal
  * Tilføjelse af GPG-nøgler og repositories
  * Kørsel og vedligeholdelse af Node-RED container

### 3. `Node-red Installation Mac OS`

* Guide til **macOS-brugere** med Docker Desktop.
* Indeholder:

  * Download og installation af Docker til macOS
  * Terminalkommandoer til opstart af Node-RED
  * Gennemgang af `docker-compose.yml`

## 🧭 Fælles for alle guides

* Anvender den officielle `nodered/node-red` Docker image
* Gør brug af en simpel Docker Compose konfiguration
* Tilpasset begyndere og undervisningsbrug
* Data lagres i en lokal `./data`-mappe for nem backup

## 📦 Forudsætninger

* Grundlæggende kendskab til operativsystemets terminal eller kommandoprompt
* Adgang til internet
* Adgang til systemrettigheder for installation af Docker

## 🎯 Formål

Dette materiale er udviklet til brug i undervisning og selvstudium, hvor man arbejder med **IoT**, **automatisering** og **grafisk programmering** med Node-RED.

Har du behov for ekstra funktionalitet (fx integration med Mosquitto, InfluxDB eller PostgreSQL), kan `docker-compose.yml` udvides efter behov.

---

🛠️ Klar til at køre Node-RED? Vælg din platform og følg guiden.

---

© 2025 – Udarbejdet som del af AAMS / IoT undervisningsmateriale.
