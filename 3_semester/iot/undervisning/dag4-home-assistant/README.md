# 🏗️ Dag 4 – Home Assistant 01: Installation

Denne lektion hjælper dig med at installere og få adgang til Home Assistant (HA) i et udviklingsmiljø. Home Assistant er en open source smart home-platform, der understøtter tusindvis af enheder, integrationer og automations.

---

## 🎯 Læringsmål

* Du forstår hvad Home Assistant er
* Du kan installere Home Assistant i en container eller som standalone
* Du kan få adgang til og bruge webinterfacet

---

## 🧱 Hvad er Home Assistant?

* Lokal automation-platform for smart home og IoT
* Kører typisk på Raspberry Pi, PC eller i en container
* Har kraftig dashboard (Lovelace UI) og mange integrationer

---

## 🧰 Installationsmuligheder

| Metode            | Beskrivelse                          |
| ----------------- | ------------------------------------ |
| Home Assistant OS | Komplet løsning til Pi, NUC, VM osv. |
| Docker-container  | Hurtig og fleksibel udvikling        |
| Python virtualenv | Avanceret manuel installation        |

For undervisning anbefales **Docker-installation**.

---

## 🐳 Installation via Docker Compose (anbefalet)

1. Sørg for at Docker og Docker Compose er installeret
2. Opret mappe `ha-dev` og fil `docker-compose.yml`:

```yaml
version: '3.7'
services:
  homeassistant:
    container_name: homeassistant
    image: ghcr.io/home-assistant/home-assistant:stable
    volumes:
      - ./config:/config
    environment:
      - TZ=Europe/Copenhagen
    restart: unless-stopped
    network_mode: host  # Linux only
```

> På Windows skal du tilføje port-mapping i stedet for `network_mode: host`:

```yaml
    ports:
      - "8123:8123"
```

3. Start:

```bash
docker compose up -d
```

---

## 🌐 Adgang til Home Assistant

1. Åbn browser og gå til:

```
http://localhost:8123
```

2. Første gang skal du oprette bruger og vælge lokation
3. Du er nu klar til at begynde med integrationer og automations

---

## 🔧 Tips

* Data gemmes i `./config` mappen
* Du kan redigere `configuration.yaml` direkte
* Brug Add-ons kun i Home Assistant OS – ikke Docker

---

## 🧠 Refleksion

* Hvorfor er containerisering nyttigt i undervisningsmiljøer?
* Hvordan ville installation på Raspberry Pi være anderledes?
* Hvad er fordele ved lokal kørsel fremfor cloud-tjenester?

---

📌 Home Assistant giver en stærk og fleksibel platform til smart home og automation – og installationen via Docker er et hurtigt springbræt til udvikling og eksperimentering.
