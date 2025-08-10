# 🔁 REST-automation og webhooks i Home Assistant

Denne opgave lærer dig at sende og modtage REST-kald i Home Assistant, så du kan integrere med eksterne systemer og sende styringskommandoer via HTTP.

---

## 🎯 Læringsmål

* Du kan bruge webhook-trigger i Home Assistant
* Du kan sende REST POST-anmodninger til Home Assistant
* Du forstår forskellen mellem `rest_command` og `webhook`-triggers

---

## 📡 Trin 1 – Opret en webhook-trigger i Home Assistant

### 1A: Opsæt webhook via brugerfladen

1. **Åbn Home Assistant**:
   * Log ind på din Home Assistant instance (http://homeassistant.local:8123 eller din IP-adresse)

2. **Naviger til Automations**:
   * Klik på "Configuration" i sidepanelet
   * Vælg "Automations & Scenes"
   * Klik på "Create Automation" eller "+ Add Automation"

3. **Konfigurer en ny automation**:
   * Klik på tandhjulet for at skifte til YAML-redigering (hvis du foretrækker det)
   * Alternativt kan du bruge brugerfladen:
     * **Navn**: Giv automationen navnet "Webhook aktiverer lampe"
     * **Trigger**: Vælg "Webhook" som trigger
     * **Webhook ID**: Indtast "taend_lampe" (undgå æ, ø, å i webhook ID'er for kompatibilitet)
     * **Handling**: Vælg "Call service"
       * **Service**: Vælg "light.toggle"
       * **Target**: Vælg din stuelampe (fx. "light.stue_lampe")
   * Klik på "Save" for at gemme automationen

### 1B: Alternativt - Opsæt webhook via YAML

1. **Find eller opret automations.yaml**:
   * Via File Editor addon eller SSH
   * Typisk i `/config/automations.yaml`

2. **Tilføj følgende YAML-kode**:
   ```yaml
   - id: webhook_toggle_light
     alias: "Webhook aktiverer lampe"
     description: "Tænder eller slukker lampen via webhook"
     trigger:
       - platform: webhook
         webhook_id: taend_lampe
     action:
       - service: light.toggle
         target:
           entity_id: light.stue_lampe
   ```

3. **Gem filen og genindlæs automations**:
   * Gå til Configuration > Server Controls
   * Klik på "RELOAD AUTOMATIONS"

### 1C: Test din webhook

1. **Find din Home Assistant URL**:
   * Hvis du bruger Nabu Casa: `https://[din-id].ui.nabu.casa`
   * Hvis lokal: `http://[din-ip]:8123`

2. **Test med curl fra en terminal**:
   ```bash
   curl -X POST http://[din-ip]:8123/api/webhook/taend_lampe
   ```
   * Hvis du bruger HTTPS eller har adgangskodebeskyttelse uden Nabu Casa, brug:
   ```bash
   curl -X POST -k https://[din-ip]:8123/api/webhook/taend_lampe
   ```

3. **Observér**: Din stuelampe skulle skifte tilstand (tænde hvis den var slukket, eller omvendt)

---

## 🧾 Trin 2 – Opret en rest_command til at sende data ud

### 2A: Tilføj rest_command til configuration.yaml

1. **Åbn configuration.yaml**:
   * Via File Editor addon eller SSH
   * Typisk i `/config/configuration.yaml`

2. **Tilføj rest_command konfiguration**:
   ```yaml
   rest_command:
     send_status_til_node_red:
       url: "http://[NODE_RED_IP]:1880/api/status"
       method: post
       content_type: "application/json"
       payload: '{"status": "alarm_triggered", "timestamp": "{{ now() }}"}'
   ```
   * Erstat `[NODE_RED_IP]` med din Node-RED servers IP-adresse
   * Bemærk: Hvis Node-RED kører på samme maskine, kan du bruge "localhost" eller "127.0.0.1"

3. **Gem filen og genstart Home Assistant**:
   * Gå til Configuration > Server Controls
   * Klik på "CHECK CONFIGURATION"
   * Hvis det er OK, klik på "RESTART"

### 2B: Opret en automation der bruger rest_command

1. **Opret en ny automation via brugerfladen**:
   * Gå til Configuration > Automations & Scenes
   * Klik på "+ Add Automation"

2. **Konfigurer automationen**:
   * **Navn**: "Send alarm status til Node-RED"
   * **Trigger**: Vælg en relevant trigger, f.eks.:
     * Sensor-trigger: Hvis en dørsensor åbnes
     * Numerisk state: Hvis en bevægelsessensor registrerer bevægelse
   * **Handling**: Vælg "Call service"
     * **Service**: Indtast `rest_command.send_status_til_node_red`
   * Klik på "Save"

### 2C: Forbered Node-RED til at modtage data

1. **Åbn Node-RED** i din browser (http://[NODE_RED_IP]:1880)

2. **Opret en HTTP indgang**:
   * Træk en `http in` node til dit workspace
   * Dobbeltklik for at konfigurere:
     * **Method**: POST
     * **URL**: /api/status
     * Klik på "Done"

3. **Tilføj debug output**:
   * Træk en `debug` node til dit workspace
   * Forbind den til `http in` noden

4. **Tilføj HTTP svar**:
   * Træk en `http response` node til dit workspace
   * Forbind den til `http in` noden
   * Konfigurer den til at returnere status 200

5. **Deploy dit flow** ved at klikke på "Deploy" knappen

---

## 🔧 Trin 3 – Simuler ekstern kontrol fra Node-RED til Home Assistant

### 3A: Opret et flow til at styre Home Assistant

1. **Åbn Node-RED** igen, hvis det ikke allerede er åbent

2. **Opret en inject node**:
   * Træk en `inject` node til dit workspace
   * Dobbeltklik for at konfigurere:
     * **Payload**: Vælg "string"
     * Lad indholdet være tomt
     * **Name**: "Tænd/sluk lampe"
     * Klik på "Done"

3. **Tilføj en HTTP request node**:
   * Træk en `http request` node til dit workspace
   * Dobbeltklik for at konfigurere:
     * **Method**: POST
     * **URL**: `http://[HA_IP]:8123/api/webhook/taend_lampe`
     * Erstat `[HA_IP]` med din Home Assistant IP-adresse
     * **Return**: "a parsed JSON object"
     * **Name**: "Kald webhook"
     * Klik på "Done"

4. **Tilføj debug output**:
   * Træk en `debug` node til dit workspace
   * Forbind den til `http request` noden

5. **Forbind noderne**:
   * Forbind `inject` noden til `http request` noden
   * Forbind `http request` noden til `debug` noden

6. **Deploy dit flow** ved at klikke på "Deploy" knappen

### 3B: Test dit flow

1. **Klik på inject-knappen** for at udløse HTTP-kaldet
2. **Observér**:
   * Home Assistant skulle aktivere automationen
   * Din stuelampe skulle skifte tilstand
   * Du kan tjekke Home Assistant logfiler for at bekræfte at webhook blev modtaget

---

## 💡 Udvidelser

### Flere webhook-eksempler

1. **Sluk lampe webhook**:
   * Opret en ny automation med webhook ID "sluk_lampe"
   * Handlingen skal være `light.turn_off` med target `light.stue_lampe`

2. **Start ventilation webhook**:
   * Opret en ny automation med webhook ID "start_ventilation"
   * Handlingen skal være `fan.turn_on` med target for din ventilation

3. **Aktiver scene webhook**:
   * Opret en ny automation med webhook ID "aften_scene"
   * Handlingen skal være `scene.turn_on` med entity_id for din aften-scene

### Send data tilbage til Home Assistant

1. **Opret en REST sensor i Home Assistant**:
   ```yaml
   sensor:
     - platform: rest
       name: node_red_status
       resource: http://[NODE_RED_IP]:1880/api/ha_status
       value_template: "{{ value_json.status }}"
       scan_interval: 30
   ```

2. **Opret et Node-RED endpoint** der returnerer status:
   * Brug en `http in` node med GET på `/api/ha_status`
   * Tilslut en `function` node der returnerer JSON-status
   * Tilslut en `http response` node der svarer med denne status

---

## 🔒 Sikkerhedstiltag

1. **Brug lange, komplekse webhook ID'er** i produktionsmiljøer:
   ```yaml
   webhook_id: a7d2fb5e9c4b8f3d1e6a2c5b9d8f7e3a
   ```

2. **Begræns adgang via netværk**:
   * Placer Home Assistant bag en reverse proxy
   * Brug firewall til at begrænse adgang til port 8123

3. **Tjek inkommende data**:
   * I automations, tilføj en betingelse der validerer indkommende data
   * Brug templates til at sikre at værdier er indenfor acceptable grænser

---

## 🧠 Refleksion

* **Sikkerhed i webhooks**:
  * Webhooks har ingen indbygget autentifikation - hvordan kan du sikre, at de ikke misbruges?
  * Overvej: Lange, tilfældige ID'er, netværksisolation, validering af input

* **Professionelle REST-integrationer**:
  * Hvordan kunne REST POST bruges i en virksomhedsintegration?
  * Overvej: Integration med CRM-systemer, booking-platforme, forretningslogik

* **Fordele ved stateless REST**:
  * Hvorfor er stateless REST-protokollen velegnet til automatisering?
  * Overvej: Fejltolerance, uafhængige systemer, enkel fejlfinding

---

## 📋 Troubleshooting

### Webhook virker ikke:
* Kontroller at Home Assistant er tilgængelig fra det netværk, hvor du sender anmodningen
* Verificer webhook ID - den er case-sensitive
* Tjek Home Assistant logs for fejlmeddelelser

### rest_command fejler:
* Kontroller at URL'en er korrekt
* Sørg for at content_type er konfigureret korrekt
* Tjek om modtageren (fx Node-RED) kører og er tilgængelig

### Ingen respons fra Node-RED:
* Verificer at Node-RED lytter på den korrekte port
* Tjek at HTTP in node er konfigureret med korrekt URL
* Sørg for at flow er deployet

---

📌 Disse øvelser viser, hvordan Home Assistant både kan **modtage kommandoer** og **sende status** via REST – og dermed blive en aktiv deltager i et større IoT-økosystem.