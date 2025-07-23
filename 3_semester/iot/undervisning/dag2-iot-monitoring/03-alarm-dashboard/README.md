
# 03 - Smart Home Alarm Dashboard

**Varighed:** 75 minutter  
**Formål:** Forstå alarm systemer og dashboard design for smart home overvågning

## Læringsmål
- Forstå forskellige alarm typer og deres anvendelse
- Kende principper for alarm prioritering og eskalering
- Forstå dashboard design og brugeroplevelse
- Lære fejlfinding og debugging strategier

## Teori: Smart Home Alarm Systemer

### Alarm Kategorisering

**Alarm Typer baseret på Kritikalitet:**
- **🔴 Kritisk (Critical):** Kræver øjeblikkelig handling
  - Sensor komplet offline > 5 minutter
  - Ekstreme temperaturer (< 5°C eller > 40°C indendørs)
  - Sikkerhedsalarmer (røg, brand, indbrud)
  - System total nedbrud

- **🟡 Advarsel (Warning):** Bør undersøges snart
  - Temperatur udenfor komfort zone (< 16°C eller > 28°C)
  - Sensor ustabil (mange fejlmålinger)
  - WiFi signal svagt (< -80 dBm)
  - Unormal energiforbrug

- **🟢 Information (Info):** Bare for information
  - Sensor genstartet
  - Normal system oprydning
  - Scheduled maintenance beskeder
  - Bruger login/logout

### Alarm Prioritering og Eskalering

**Prioriterings Strategi:**
```
1. Sikkerhed (røg, gas, indbrud)
2. System kritisk (total kommunikationssvigt)
3. Komfort kritisk (varme/køl system)
4. Vedligeholdelse (sensor fejl)
5. Information (status opdateringer)
```

**Eskalerings Trin:**
1. **Level 1:** Dashboard notification
2. **Level 2:** Push notification til app
3. **Level 3:** SMS til bruger
4. **Level 4:** Email til backup kontakt
5. **Level 5:** Automatisk systemhandling (fx nød-shutdown)

### Alarm Hysterese og Anti-Flapping

**Problem:** Sensor oscillerer omkring grænseværdi
```
Temperatur: 29.9° → 30.1° → 29.9° → 30.1°
Resultat: Konstant alarm on/off = irriterende
```

**Løsning:** Hysterese (forskellige grænser for on/off)
```
Alarm ON: Temperatur > 30°C
Alarm OFF: Temperatur < 28°C
Resultat: Stabil alarm tilstand
```

**Anti-Flapping Timer:**
- Minimum alarm varighed: 30 sekunder
- Minimum tid mellem samme alarm: 5 minutter
- Grupperet alarmer: Max 1 alarm per kategori per 10 minutter

### Dashboard Design Principper

**Hierarkisk Information Display:**
```
Level 1: Status Overview (Green/Yellow/Red)
├── Level 2: System Categories (Climate, Security, Energy)
│   ├── Level 3: Room Status (Living Room, Kitchen, Bedroom)
│   │   ├── Level 4: Device Details (Temp Sensor, Light Controller)
│   │   │   └── Level 5: Raw Data & Debug Info
```

**Visual Design Guidelines:**
- **Farver:** Grøn=OK, Gul=Advarsel, Rød=Kritisk, Grå=Offline
- **Ikoner:** Intuitive symboler (🌡️ temperatur, 💡 lys, 📶 WiFi)
- **Animationer:** Blinkende for aktive alarmer, statisk for normale
- **Layout:** Vigtigste information øverst og til venstre

### Smart Home Alarm Patterns

**1. Environmental Monitoring Pattern**
```
Sensor → Range Check → Trend Analysis → Alarm Decision
│
├── Normal: 20-25°C → No alarm
├── Warning: 25-30°C → Yellow warning  
└── Critical: >30°C → Red alarm + escalation
```

**2. Connectivity Monitoring Pattern**
```
Heartbeat → Timeout Check → Grace Period → Alarm
│
├── <30 sec: Normal (green status)
├── 30-60 sec: Warning (yellow, might recover)
└── >60 sec: Critical (red, assume offline)
```

**3. System Health Pattern**
```
Multiple Metrics → Weighted Score → Overall Health
│
├── WiFi Signal: 25% weight
├── Response Time: 25% weight  
├── Error Rate: 25% weight
└── Data Quality: 25% weight
```

### Alarm State Management

**State Machine for Alarms:**
```markdown
NORMAL → TRIGGERED → ACKNOWLEDGED → RESOLVED → NORMAL
   │         │            │             │
   │         └── AUTO-CLEAR (hvis problem løst)
   │              │
   └─── SUPPRESSED (midlertidigt slået fra)
```

**State Transitions:**
- **NORMAL → TRIGGERED:** Alarm condition met
- **TRIGGERED → ACKNOWLEDGED:** User sees/acknowledges alarm
- **ACKNOWLEDGED → RESOLVED:** Problem fixed, user confirms
- **TRIGGERED → AUTO-CLEAR:** Problem resolves automatically
- **ANY → SUPPRESSED:** User temporarily disables alarm

### Data Persistence og Historie

**Alarm Logging Strategy:**
```json
{
  "alarm_id": "temp_high_living_room_001",
  "timestamp": "2025-07-23T14:30:00Z",
  "type": "environmental",
  "severity": "warning", 
  "source": "living_room/temperature",
  "message": "Temperature above comfort zone",
  "value": 31.2,
  "threshold": 30.0,
  "acknowledged": false,
  "resolved": false,
  "auto_resolved": false
}
```

**Retention Policies:**
- **Critical alarms:** Keep 1 year
- **Warning alarms:** Keep 3 months  
- **Info alarms:** Keep 1 month
- **Debug logs:** Keep 1 week

### Performance og Skalering

**Real-time Requirements:**
- **Alarm detection:** < 5 sekunder fra sensor til alarm
- **Dashboard update:** < 2 sekunder alarm til visning
- **User response:** < 1 sekund fra klik til action
- **System recovery:** < 30 sekunder efter problem løst

**Scalability Patterns:**
- **Distributed alarming:** Hver sensor evaluerer egne alarmer
- **Centralized correlation:** Central system sammenligner på tværs
- **Event streaming:** MQTT streams til real-time processing
- **Batch processing:** Historisk analyse og trends

### Integration med Smart Home Platforme

**Home Assistant Integration:**
```yaml
# Alarm configuration
automation:
  - alias: "High Temperature Alarm"
    trigger:
      platform: mqtt
      topic: "smarthouse/living_room/temperature"
    condition:
      condition: numeric_state
      entity_id: sensor.living_room_temp
      above: 30
    action:
      service: notify.mobile_app
      data:
        message: "High temperature alert: {{ states('sensor.living_room_temp') }}°C"
```

**OpenHAB Rules:**
```java
rule "Temperature Alarm"
when
    Item Temperature_LivingRoom received update
then
    val temp = Temperature_LivingRoom.state as DecimalType
    if (temp > 30) {
        sendNotification("admin@example.com", "High temperature: " + temp + "°C")
        AlarmStatus.sendCommand("CRITICAL")
    }
end
```

### Mobile og Remote Access

**Push Notification Strategy:**
- **Critical:** Øjeblikkelig push til alle enheder
- **Warning:** Push til primær enhed
- **Info:** Kun dashboard opdatering

**Remote Dashboard Access:**
- **VPN tunnel:** Sikker adgang hjemmefra
- **Cloud proxy:** Managed service (Home Assistant Cloud)
- **Port forwarding:** Direct access (ikke anbefalet for sikkerhed)

### Sikkerhed og Privacy

**Alarm Data Security:**
- **Local processing:** Hold sensitive data lokalt
- **Encrypted transport:** TLS for all remote kommunikation
- **Access control:** Begrænsede brugerrettigheder
- **Audit logging:** Log hvem der har set/behandlet alarmer

**Privacy Considerations:**
- **Data minimization:** Saml kun nødvendige data
- **Retention limits:** Slet gamle data automatisk
- **User consent:** Klar politik for dataanvendelse
- **Export capability:** Brugere kan få deres data

---

**Relaterede emner:**
- [01 - MQTT Foundation](../01-mqtt-foundation/) - Kommunikations grundlag
- [02 - Heartbeat og Plausibility](../02-heartbeat-plausibility/) - System overvågning
- [Dag 3 - Avanceret Monitoring](../../dag3-heartbeat-watchdog/) - Næste niveau
