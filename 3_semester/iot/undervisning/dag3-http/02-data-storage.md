# Trin 2: IoT Data Storage i Skyen

Nu hvor vi har forbundet vores Smart Building system til AWS IoT Core, skal vi implementere en løsning til at gemme og organisere vores sensordata, så vi kan få adgang til historiske data og bruge dem til analyse.

## 🎯 I dette trin lærer du

- Hvordan du designer en datamodel til IoT-sensordata
- Hvordan du bruger AWS-tjenester til at gemme IoT-data
- Hvordan du implementerer databehandling og filtreringsregler
- Hvordan du opsætter automatisk arkivering af historiske data

## 💾 Datalagring for IoT-systemer

IoT-systemer genererer ofte store mængder tidsserie-data, der kræver særlig håndtering:

1. **Høj skrivehastighed**: Mange enheder sender data samtidigt
2. **Tidsserie-format**: Data er knyttet til specifikke tidspunkter
3. **Varierende struktur**: Forskellige enheder sender forskellige datatyper
4. **Skaleringsbehov**: Datamængden vokser kontinuerligt

For vores Smart Building projekt vil vi bruge to AWS-tjenester:
- **DynamoDB**: En NoSQL-database til aktuelle data og hurtig adgang
- **S3**: Objektlagring til arkivering af historiske data

## 📊 Design af datamodel

For vores Smart Building system vil vi bruge denne datamodel i DynamoDB:

### Primær tabel (SmartBuilding_Data)
- **Partition Key**: `device_id` (identifikator for sensoren)
- **Sort Key**: `timestamp` (ISO 8601 format)
- **Attributter**:
  - `temperature`: Numerisk værdi
  - `humidity`: Numerisk værdi
  - `light`: Numerisk værdi (hvis tilgængelig)
  - `motion`: Boolean (hvis tilgængelig)
  - `battery`: Batteriniveau i procent
  - `location`: Bygning/rum identifikator
  - `status`: Enhedsstatus

## 🔧 Opsætning af AWS DynamoDB

### 1. Opret en DynamoDB tabel

1. Gå til AWS Management Console
2. Søg efter "DynamoDB" og vælg tjenesten
3. Klik på "Create table"
4. Konfigurer tabellen:
   - **Table name**: SmartBuilding_Data
   - **Partition key**: device_id (String)
   - **Sort key**: timestamp (String)
   - **Table settings**: Brug standardindstillinger
5. Klik på "Create table"

### 2. Opret en IAM-rolle til IoT Rules

1. Gå til "IAM" i AWS Management Console
2. Vælg "Roles" og klik på "Create role"
3. Vælg "IoT" som trusted entity
4. Søg efter og vedhæft disse politikker:
   - AmazonDynamoDBFullAccess
   - AmazonS3FullAccess
5. Navngiv rollen "IoT_to_DynamoDB_Role"
6. Klik på "Create role"

## ⚡ Opsætning af AWS IoT Rules

Nu skal vi konfigurere en AWS IoT Rule, der automatisk gemmer indkommende data i DynamoDB:

1. Gå til AWS IoT Core-konsollen
2. Vælg "Act" og klik på "Rules"
3. Klik på "Create" for at oprette en ny regel
4. Navngiv reglen "SaveToDynamoDB"
5. Skriv følgende SQL-forespørgsel:
```sql
SELECT 
  topic(2) as device_id,
  timestamp() as timestamp,
  payload.deviceData.temperature as temperature,
  payload.deviceData.humidity as humidity,
  payload.deviceData.light as light,
  payload.deviceData.battery as battery,
  payload.deviceData.location as location
FROM 'smartbuilding/sensor/+'
```

6. Klik på "Add action"
7. Vælg "Split message into multiple columns of a DynamoDB table"
8. Vælg "SmartBuilding_Data" tabellen
9. Sæt "Hash key value" til `${device_id}`
10. Sæt "Range key value" til `${timestamp}`
11. Vælg "IoT_to_DynamoDB_Role" som IAM-rolle
12. Klik på "Add action" og "Create rule"

## 🗄️ Arkivering til S3

For langtidslagring vil vi konfigurere automatisk arkivering til S3:

1. Opret en S3 bucket:
   - Gå til S3 i AWS Console
   - Klik på "Create bucket"
   - Navngiv din bucket (f.eks. "smartbuilding-data-archive")
   - Vælg en region (samme som dine andre ressourcer)
   - Behold standardindstillingerne og klik "Create bucket"

2. Opret en ny IoT Rule for arkivering:
   - Navngiv reglen "ArchiveToS3"
   - Brug denne SQL-forespørgsel:
   ```sql
   SELECT * FROM 'smartbuilding/sensor/+'
   ```
   - Tilføj en action: "Store message in Amazon S3"
   - Vælg din S3 bucket
   - Sæt key til: `${topic()}/${timestamp()}.json`
   - Vælg "IoT_to_DynamoDB_Role" som IAM-rolle
   - Klik på "Add action" og "Create rule"

## 🔍 Data Access API

Nu opretter vi en simpel API til at hente data. Vi vil bruge AWS API Gateway og Lambda:

1. Opret en Lambda-funktion:
```javascript
const AWS = require('aws-sdk');
const dynamo = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
    const deviceId = event.pathParameters.deviceId;
    const startTime = event.queryStringParameters?.startTime || 
                     new Date(Date.now() - 24*60*60*1000).toISOString();
    const endTime = event.queryStringParameters?.endTime || 
                   new Date().toISOString();
    
    const params = {
        TableName: 'SmartBuilding_Data',
        KeyConditionExpression: 'device_id = :deviceId AND #ts BETWEEN :startTime AND :endTime',
        ExpressionAttributeNames: {
            '#ts': 'timestamp'
        },
        ExpressionAttributeValues: {
            ':deviceId': deviceId,
            ':startTime': startTime,
            ':endTime': endTime
        }
    };
    
    try {
        const result = await dynamo.query(params).promise();
        return {
            statusCode: 200,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify(result.Items)
        };
    } catch (error) {
        return {
            statusCode: 500,
            body: JSON.stringify(error)
        };
    }
};
```

2. Konfigurer API Gateway for at eksponere denne funktion som en REST API endpoint.

## ✅ Test datalagring og -adgang

For at teste vores datalagring:

1. Send testdata fra en ESP32 eller Node-RED til vores MQTT-broker
2. Bekræft at data når AWS IoT Core ved at bruge MQTT Test Client
3. Kontroller DynamoDB-tabellen for at bekræfte at data bliver gemt
4. Tjek S3-bucket for at verificere arkiveringen
5. Test API'et ved at hente data for en specifik enhed

## ➡️ Næste skridt

Nu hvor vi har implementeret robust datalagring for vores Smart Building sensordata, er vi klar til at gå videre til det næste modul, hvor vi vil skabe avancerede visualiseringer og dashboards for at få indsigt i vores data.
