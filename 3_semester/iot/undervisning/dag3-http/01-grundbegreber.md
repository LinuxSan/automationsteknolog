# Trin 1: REST API Grundbegreber for IoT

I dette første modul skal vi forstå principperne bag REST API'er og hvorfor de er vigtige i IoT-systemer. Vi vil lære hvordan vi kan bruge HTTP-protokollen til at sende kommandoer til vores KeyStudio Smart Home Kit.

![REST API Basics](https://cdn.altova.com/images/api_testing_images/rest-api-get-post.png)

## 🎯 I dette trin lærer du

- Hvad REST API'er er, og hvordan de bruges i IoT-systemer
- Forskellen mellem MQTT (telemetri) og REST (kommando)
- De grundlæggende HTTP-metoder: GET, POST, PUT og DELETE
- Hvordan man designer gode API-endpoints for IoT-enheder
- Hvordan Node-RED kan fungere som en API-gateway

## 📡 MQTT vs. REST i IoT

I vores IoT-system bruger vi to hovedtyper af kommunikation:

### MQTT (fra dag 2)
- **Formål**: Telemetri - Enheder sender sensordata
- **Mønster**: Publish-Subscribe
- **Forbindelse**: Vedvarende forbindelse
- **Retning**: Primært enhed → server
- **Eksempel**: Temperatursensor sender regelmæssige målinger

### REST API (i dag)
- **Formål**: Kommando - Server sender instruktioner til enheder
- **Mønster**: Request-Response
- **Forbindelse**: Kortvarig forbindelse pr. request
- **Retning**: Primært server → enhed
- **Eksempel**: Mobilapp sender kommando om at tænde LED

![MQTT vs REST](https://miro.medium.com/v2/resize:fit:1400/1*fYfTvHVErJ4oSMqx9r_DyQ.jpeg)

## 🔄 HTTP-metoder i REST

REST API'er bruger standard HTTP-metoder til forskellige handlinger:

| Metode | Formål | IoT-eksempel |
|--------|--------|--------------|
| GET    | Hent data | Aflæs aktuel temperatur fra sensor |
| POST   | Opret ny ressource | Tilføj en ny planlagt handling |
| PUT    | Opdater eksisterende ressource | Juster servomotorposition |
| DELETE | Fjern ressource | Annuller en planlagt handling |

## 🏗️ Design af IoT API-endpoints

Ved design af API-endpoints for vores KeyStudio Smart Home Kit, følger vi disse principper:

1. **Ressourcebaserede stier**:
   - `/devices/{device_id}/led` - Specifik LED
   - `/rooms/{room_id}/temperature` - Temperatur i et bestemt rum

2. **Konsistente handlinger**:
   - `GET /devices/{device_id}/status` - Hent enhedsstatus
   - `PUT /devices/{device_id}/led` - Opdater LED-tilstand

3. **Meningsfulde status-koder**:
   - `200 OK` - Kommando udført succesfuldt
   - `404 Not Found` - Enhed findes ikke
   - `400 Bad Request` - Forkert kommandoformat

Hvis du ikke allerede har en AWS-konto:
1. Besøg [aws.amazon.com](https://aws.amazon.com)
2. Klik på "Opret en AWS-konto"
3. Følg vejledningen til at oprette en konto (der kræves et betalingskort, men vi holder os inden for det gratis tier)

### 2. Konfigurer AWS IoT Core

1. Log ind på AWS Management Console
2. Søg efter "IoT Core" i søgefeltet
3. Vælg "Get started" for at åbne IoT Core-konsollen
4. Klik på "Connect" og vælg "Connect device"
5. Følg "Get started" guiden:
   - Vælg "Create a single thing"
   - Navngiv din ting (f.eks. "SmartBuilding-Gateway")
   - Vælg "Auto-generate a new certificate"
   - Download alle certifikater og nøgler (device certificate, public key, private key)
   - Download også "Amazon Root CA 1"
   - Klik "Activate" for at aktivere certifikatet
   - Klik "Attach a policy" og opret en ny politik

### 3. Opret IoT Policy

1. Giv din politik et navn (f.eks. "SmartBuilding-Policy")
2. Konfigurer følgende tilladelser:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iot:Connect",
      "Resource": "arn:aws:iot:eu-west-1:ACCOUNT_ID:client/${iot:Connection.Thing.ThingName}"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Publish",
      "Resource": "arn:aws:iot:eu-west-1:ACCOUNT_ID:topic/smartbuilding/*"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Subscribe",
      "Resource": "arn:aws:iot:eu-west-1:ACCOUNT_ID:topicfilter/smartbuilding/*"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Receive",
      "Resource": "arn:aws:iot:eu-west-1:ACCOUNT_ID:topic/smartbuilding/*"
    }
  ]
}
```

3. Erstat "ACCOUNT_ID" med dit AWS-kontonummer
4. Klik på "Create" for at oprette politikken
5. Vedhæft politikken til dit certifikat

## 🔄 Forbind Node-RED til AWS IoT Core

### 1. Installer AWS IoT nodes i Node-RED

1. Åbn Node-RED
2. Åbn hamburger-menuen i øverste højre hjørne
3. Vælg "Manage palette"
4. Gå til "Install" fanen
5. Søg efter "node-red-contrib-aws-iot-hub"
6. Klik "Install"

### 2. Konfigurer AWS IoT i Node-RED

1. Træk en "aws-mqtt in" node til dit flow
2. Dobbeltklik på noden for at konfigurere den
3. Klik på blyantikonet for at tilføje en ny AWS IoT-forbindelse
4. Indtast følgende indstillinger:
   - **Name**: AWS IoT Connection
   - **Region**: eu-west-1 (eller din region)
   - **Host**: Kopier "Endpoint" fra AWS IoT Core konsollen
   - **Access Key & Secret Key**: Lad disse felter være tomme, da vi bruger certifikater
   - **Client ID**: SmartBuilding-Gateway (samme navn som din "thing")
5. Vælg fanebladet "Security"
6. Upload de certifikater og nøgler, du downloadede tidligere
7. Klik "Add" og derefter "Done"

### 3. Opret et bridge-flow fra MQTT til AWS IoT

1. Opret et flow, der forbinder din lokale MQTT-broker til AWS IoT Cloud:
```
[MQTT In] --> [Function] --> [AWS IoT Out]
```

2. Konfigurer MQTT In-noden til at abonnere på `sensor/#`
3. Tilføj en Function-node med denne kode:
```javascript
// Tilføj timestamp og enheds-id
msg.payload = {
    deviceData: msg.payload,
    timestamp: new Date().toISOString(),
    deviceId: msg.topic.split('/')[1]
};

// Omdøb emnet til cloud-format
msg.topic = "smartbuilding/" + msg.topic;

return msg;
```

4. Konfigurer AWS IoT Out-noden til at bruge den AWS IoT-forbindelse, du netop har oprettet

## ✅ Test din Cloud-forbindelse

1. Klik på "Deploy" for at aktivere dit flow
2. Åbn AWS IoT Core-konsollen og naviger til "Test" -> "MQTT test client"
3. Abonner på emnet "smartbuilding/#"
4. Send en testbesked fra en af dine ESP32-enheder eller direkte fra Node-RED
5. Du skulle nu kunne se beskeden dukke op i AWS IoT Test-klienten

## ➡️ Næste skridt

Nu hvor vores IoT-system er forbundet til cloud, kan vi i næste modul fokusere på at implementere robust datalagring i skyen, så vi kan gemme vores sensordata til historisk analyse og rapportering.
