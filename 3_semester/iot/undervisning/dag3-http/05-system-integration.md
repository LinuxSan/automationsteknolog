# Trin 5: System Integration & Automatisering

I dette sidste modul skal vi samle alle komponenterne fra vores Smart Building system til en fuldt fungerende, sammenhængende løsning. Vi vil sikre at alle dele spiller sammen og implementere automatisering baseret på vores prædiktive modeller.

## 🎯 I dette trin lærer du

- Hvordan du integrerer alle komponenterne i dit IoT-system
- Hvordan du implementerer automatisering og reaktive handlinger
- Hvordan du sikrer systemets pålidelighed og fejltolerance
- Hvordan du skalerer og vedligeholder din IoT-løsning på lang sigt

## 🔄 End-to-End System Integration

For at opnå et fuldt fungerende system skal vi sikre, at alle komponenterne kommunikerer og fungerer sammen:

### 1. Systemarkitektur oversigt

Lad os gennemgå den komplette systemarkitektur:

```
+-------------+     +-----------+     +---------------+     +----------------+
| ESP32       |---->| Node-RED  |---->| AWS IoT Core  |---->| DynamoDB       |
| Sensorer    | MQTT| Gateway   | REST| Service       |     | Data Storage   |
+-------------+     +-----------+     +---------------+     +----------------+
                         |                                          |
                         v                                          v
                  +-----------+                           +-------------------+
                  | Lokalt    |<--------------------------|  Lambda Functions |
                  | Dashboard |         Predictions       |  (Analytics)      |
                  +-----------+                           +-------------------+
                                                                  |
                                                                  v
                                                          +----------------+
                                                          | S3 / QuickSight|
                                                          | Visualisering  |
                                                          +----------------+
```

### 2. Integration mellem komponenter

For at sikre gnidningsfri integration, skal vi implementere:

1. **Fejlhåndtering** på alle niveauer
2. **Retransmission** af tabte beskeder
3. **Buffering** af data ved forbindelsesproblemer
4. **Logning** for fejlfinding og vedligeholdelse

## 🤖 Automatiseret respons

Nu skal vi implementere automatiserede handlinger baseret på realtidsdata og forudsigelser:

### 1. Opret AWS IoT Rules for automatiske handlinger

Lad os konfigurere regler i AWS IoT Core, der reagerer på bestemte forhold:

```sql
-- Regel for høj temperatur alarm
SELECT 
  temperature, device_id, location
FROM 'smartbuilding/sensor/+'
WHERE temperature > 28
```

Denne regel kan udløse en Lambda-funktion, der sender en alarm via email, SMS eller push-notifikation.

### 2. Prædiktiv HVAC-kontrol med Lambda

Vi kan bruge vores prædiktive model til at styre HVAC-systemet proaktivt:

```python
import boto3
import json
import requests
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Hent device_id og lokation
    device_id = event.get('deviceId')
    location = event.get('location', 'unknown')
    
    # Hent prædiktioner for de næste timer
    predictions = get_temperature_predictions(device_id)
    
    # Analyse af kommende temperaturændringer
    current_temp = predictions[0]['temperature'] if predictions else None
    future_temp = predictions[6]['temperature'] if len(predictions) > 6 else None
    
    if current_temp is None or future_temp is None:
        return {
            'statusCode': 400,
            'body': 'Unable to get valid predictions'
        }
    
    # Beregn temperaturforskel over de næste 6 timer
    temp_change = future_temp - current_temp
    
    # Bestem HVAC-tilstand baseret på forudsigelser
    hvac_action = determine_hvac_action(current_temp, future_temp, temp_change)
    
    # Send kommando til HVAC-systemet via Node-RED
    send_hvac_command(location, hvac_action)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'device': device_id,
            'location': location,
            'currentTemp': current_temp,
            'predictedTemp': future_temp,
            'tempChange': temp_change,
            'action': hvac_action
        })
    }

def get_temperature_predictions(device_id):
    # Kald til vores prediction API
    # Dette kunne være en direkte Lambda invokation eller en API Gateway kald
    # ...
    
def determine_hvac_action(current_temp, future_temp, temp_change):
    # Temperaturgrænser
    comfort_min = 21.0
    comfort_max = 25.0
    
    # Hvis temperatur forventes at stige over komfortzonen
    if future_temp > comfort_max:
        # Jo større stigning, jo tidligere start køling
        if temp_change > 2.0:
            return "COOL_HIGH"
        elif temp_change > 1.0:
            return "COOL_MEDIUM"
        elif future_temp > comfort_max + 1:
            return "COOL_LOW"
    
    # Hvis temperatur forventes at falde under komfortzonen
    elif future_temp < comfort_min:
        # Jo større fald, jo tidligere start opvarmning
        if temp_change < -2.0:
            return "HEAT_HIGH"
        elif temp_change < -1.0:
            return "HEAT_MEDIUM"
        elif future_temp < comfort_min - 1:
            return "HEAT_LOW"
    
    # Hvis temperaturen er i komfortzonen
    else:
        # Hvis vi bevæger os mod yderkanterne af komfortzonen
        if current_temp > comfort_max - 1 and temp_change > 0:
            return "COOL_LOW"
        elif current_temp < comfort_min + 1 and temp_change < 0:
            return "HEAT_LOW"
        else:
            return "OFF"

def send_hvac_command(location, action):
    # Send kommando til Node-RED via MQTT eller HTTP
    node_red_url = "http://your-node-red-server:1880/hvac-control"
    
    payload = {
        'location': location,
        'action': action,
        'timestamp': datetime.utcnow().isoformat()
    }
    
    try:
        response = requests.post(
            node_red_url, 
            json=payload,
            headers={'Content-Type': 'application/json'},
            timeout=5
        )
        return response.status_code == 200
    except Exception as e:
        print(f"Error sending command: {e}")
        return False
```

### 3. Node-RED Flow til HVAC-kontrol

I Node-RED skal vi implementere et flow, der modtager og eksekverer HVAC-kommandoer:

```json
[
    {
        "id": "hvac-control",
        "type": "http in",
        "name": "HVAC Control API",
        "url": "/hvac-control",
        "method": "post",
        "swaggerDoc": "",
        "x": 140,
        "y": 100,
        "wires": [
            [
                "parse-command"
            ]
        ]
    },
    {
        "id": "parse-command",
        "type": "function",
        "name": "Parse HVAC Command",
        "func": "msg.location = msg.payload.location;\nmsg.action = msg.payload.action;\nreturn msg;",
        "outputs": 1,
        "x": 340,
        "y": 100,
        "wires": [
            [
                "select-device"
            ]
        ]
    },
    {
        "id": "select-device",
        "type": "switch",
        "name": "Select HVAC Device",
        "property": "location",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "room1",
                "vt": "str"
            },
            {
                "t": "eq",
                "v": "room2",
                "vt": "str"
            }
        ],
        "outputs": 2,
        "x": 540,
        "y": 100,
        "wires": [
            [
                "room1-hvac"
            ],
            [
                "room2-hvac"
            ]
        ]
    },
    {
        "id": "room1-hvac",
        "type": "function",
        "name": "Room 1 HVAC Control",
        "func": "// Map action to device-specific command\nconst actionMap = {\n    'COOL_HIGH': {mode: 'cool', fan: 'high', target: 20},\n    'COOL_MEDIUM': {mode: 'cool', fan: 'medium', target: 21},\n    'COOL_LOW': {mode: 'cool', fan: 'low', target: 22},\n    'HEAT_HIGH': {mode: 'heat', fan: 'high', target: 26},\n    'HEAT_MEDIUM': {mode: 'heat', fan: 'medium', target: 25},\n    'HEAT_LOW': {mode: 'heat', fan: 'low', target: 24},\n    'OFF': {mode: 'off', fan: 'off', target: 23}\n};\n\n// Get command for action\nconst cmd = actionMap[msg.action] || actionMap.OFF;\n\n// Prepare MQTT message\nmsg.payload = {\n    device: 'hvac-room1',\n    command: cmd\n};\nmsg.topic = 'control/hvac/room1';\n\nreturn msg;",
        "outputs": 1,
        "x": 750,
        "y": 80,
        "wires": [
            [
                "mqtt-out"
            ]
        ]
    },
    {
        "id": "room2-hvac",
        "type": "function",
        "name": "Room 2 HVAC Control",
        "func": "// Similar logic as Room 1\n// ...",
        "outputs": 1,
        "x": 750,
        "y": 120,
        "wires": [
            [
                "mqtt-out"
            ]
        ]
    },
    {
        "id": "mqtt-out",
        "type": "mqtt out",
        "name": "Send HVAC Command",
        "topic": "",
        "qos": "1",
        "retain": "false",
        "broker": "broker",
        "x": 950,
        "y": 100,
        "wires": []
    },
    {
        "id": "http-response",
        "type": "http response",
        "name": "HTTP Response",
        "statusCode": "200",
        "headers": {},
        "x": 950,
        "y": 160,
        "wires": []
    }
]
```

## 🛡️ Systemets robusthed og vedligeholdelse

For at sikre, at vores system er robust og let at vedligeholde, skal vi implementere:

### 1. Overvågning og alarmer

Lad os konfigurere CloudWatch alarmer for at overvåge systemet:

1. **IoT Connection Metrics**: Antal forbundne enheder og beskedgennemløb
2. **Lambda Execution Errors**: Fejl i vores Lambda-funktioner
3. **DynamoDB Throughput**: Overvågning af læse/skrive kapacitet

### 2. Automatisk skalering

For at håndtere varierende belastninger, kan vi konfigurere:

1. **DynamoDB Auto Scaling**: Juster kapacitet baseret på forbrug
2. **Lambda Concurrency**: Konfigurer tilstrækkelig samtidighed for spidsbelastninger

### 3. Backup og disaster recovery

Implementer regelmæssige backups af kritisk data:

```
# CloudFormation snippet for DynamoDB backup
Resources:
  DynamoDBBackup:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: SmartBuilding_Data
      PointInTimeRecoverySpecification:
        PointInTimeRecoveryEnabled: true
```

### 4. Firmware opdateringssystem

For ESP32-enhederne implementerer vi OTA (Over-the-Air) opdateringer:

1. Opret et S3-bucket til firmware-filer
2. Implementer en Node-RED flow, der tjekker for opdateringer
3. Send firmware-opdateringer til enhederne via MQTT

```python
# ESP32 MicroPython OTA update check
import urequests
import machine
import os
import ubinascii

def check_for_updates():
    device_id = ubinascii.hexlify(machine.unique_id()).decode()
    firmware_version = "1.0.0"  # Current version
    
    try:
        r = urequests.get(
            "https://your-api.com/firmware-check",
            params={
                'device_id': device_id,
                'current_version': firmware_version
            }
        )
        
        if r.status_code == 200:
            update_info = r.json()
            
            if update_info.get('update_available', False):
                print("Update available! Downloading...")
                download_and_apply_update(update_info['download_url'])
            else:
                print("No updates available")
                
    except Exception as e:
        print("Error checking for updates:", e)

def download_and_apply_update(url):
    # Implementer sikker download og flash proces
    # ...
```

## 🎬 Demonstration og test

Lad os teste vores komplette system med en end-to-end demonstration:

### 1. Test Case: Temperatursvingninger

1. Simuler en gradvis temperaturstigning i en af rummene
2. Verificér at systemet:
   - Registrerer stigningen i realtidsdashboardet
   - Forudsiger den fremtidige temperaturudvikling
   - Aktiverer kølesystemet på det optimale tidspunkt
   - Holder rumtemperaturen inden for komfortzonen

### 2. Test Case: Fejlhåndtering

1. Simuler en sensorfejl ved at afbryde en af ESP32-enhederne
2. Verificér at systemet:
   - Registrerer den manglende sensor
   - Sender en advarsel til administratoren
   - Fortsætter med at fungere med de tilgængelige sensorer
   - Genopretter forbindelsen når sensoren kommer online igen

## 🏁 Konklusion og næste skridt

Tillykke! Du har nu bygget et komplet Smart Building overvågningssystem med:

1. **Edge enheder** (ESP32) til dataindsamling
2. **MQTT broker** til pålidelig kommunikation
3. **Node-RED gateway** til integration og lokal processering
4. **AWS IoT Core** til sikker cloud-forbindelse
5. **DynamoDB og S3** til robust datalagring
6. **Lambda funktioner** til dataprocessering
7. **Prædiktive modeller** til intelligent forudsigelse
8. **Automatisering** baseret på data og forudsigelser
9. **Dashboard** til visualisering og interaktion

Dette system danner grundlaget for mere avancerede IoT-løsninger og kan udvides med:

- **Flere sensortyper**: CO2, bevægelse, lys, luftkvalitet
- **Video analytics**: Kameraintegration med billedgenkendelse
- **Stemmestyring**: Integration med virtuelle assistenter
- **Mobile apps**: Dedikeret app til fjernbetjening og notifikationer

Du har nu færdighederne til at implementere professionelle IoT-løsninger, der kombinerer edge computing, cloud tjenester, dataanalyse og brugergrænseflader til at løse virkelige problemer.
