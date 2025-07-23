# 🔄 Change Node

Change-noden er et kraftfuldt værktøj til at modificere beskeders indhold uden at skrive JavaScript-kode. Den giver en brugervenlig grænseflade til at ændre, flytte eller slette egenskaber i en besked.

## 🎯 Formål

I denne guide lærer du om change-noden og hvordan du kan:
- Modificere beskedens indhold uden at skrive kode
- Sætte, ændre og slette beskedegenskaber
- Flytte værdier mellem forskellige dele af en besked
- Anvende JSONata-udtryk til avancerede transformationer

---

## ⚡ Grundfunktionalitet

Change-noden tilbyder fire grundlæggende operationer:

1. **Set** - Indstil en egenskab til en specifik værdi
2. **Change** - Find og erstat værdier i en egenskab
3. **Move** - Flyt en værdi fra én egenskab til en anden
4. **Delete** - Fjern en egenskab

Hver change-node kan udføre flere af disse operationer i rækkefølge.

---

## 🛠️ Konfiguration

![Change Node Configuration](https://nodered.org/docs/user-guide/images/editor-change-node-properties.png)

### Operationstyper

- **Set**: `msg.property = value`
- **Change**: `msg.property = msg.property.replace(from, to)`
- **Move**: `msg.target = msg.source; delete msg.source`
- **Delete**: `delete msg.property`

### Værdiindstillinger

For **Set** og **Change** operationer kan du specificere værdien som:
- **String**: En tekststreng (fx "Hello")
- **Number**: En numerisk værdi (fx 42)
- **Boolean**: true eller false
- **JSON**: Et JSON-objekt eller -array
- **Buffer**: Binære data
- **Expression**: Et JSONata-udtryk
- **msg.**: En reference til en anden beskedegenskab
- **flow.**: En reference til en flow-kontekst-variabel
- **global.**: En reference til en global-kontekst-variabel
- **env.**: En reference til en miljøvariabel

---

## 💡 Eksempler

### Eksempel 1: Simpel egenskabsændring

```
[Inject] → [Change] → [Debug]
```

Change-node konfiguration:
- Handling: **Set** `msg.payload` til string `"Hello World"`

Dette vil ændre payload til "Hello World" uanset hvad inject-noden sender.

### Eksempel 2: Tilføje ekstra egenskaber

```
[Inject] → [Change] → [Debug]
```

Change-node konfiguration:
- Handling 1: **Set** `msg.topic` til string `"greeting"`
- Handling 2: **Set** `msg.timestamp` til JSONata-udtryk `$now()`

Dette tilføjer to nye egenskaber til beskeden.

### Eksempel 3: Strukturerede data

```
[Inject] → [Change] → [Debug]
```

Change-node konfiguration:
- Handling: **Set** `msg.payload` til JSON:
  ```json
  {
    "device": "sensor1",
    "readings": {
      "temperature": 22,
      "humidity": 45
    },
    "timestamp": "2023-06-15T14:30:00Z"
  }
  ```

Dette erstatter payload med et JSON-objekt.

### Eksempel 4: Flyt og omdøb egenskaber

```
[Inject] → [Change] → [Debug]
```

Inject: Send et JSON-objekt med temperatur og luftfugtighed

Change-node konfiguration:
- Handling 1: **Move** `msg.payload.temperature` til `msg.temperature`
- Handling 2: **Move** `msg.payload.humidity` til `msg.humidity`
- Handling 3: **Set** `msg.payload` til `msg.temperature`
- Handling 4: **Set** `msg.unit` til string `"celsius"`

Dette reorganiserer beskedstrukturen og tilføjer en enhedsegenskab.

---

## 🔄 Avanceret anvendelse

### Brug af JSONata-udtryk

JSONata er et kraftfuldt udtrykssprogs der lader dig udføre komplekse transformationer. I change-noden kan du bruge JSONata ved at vælge "expression" som værditypen.

**Eksempel: Beregn gennemsnit**

```
[Inject] → [Change] → [Debug]
```

Inject: Send et array af temperaturer: `[22, 24, 19, 21, 23]`

Change-node konfiguration:
- Handling 1: **Set** `msg.average` til JSONata-udtryk `$average(payload)`
- Handling 2: **Set** `msg.max` til JSONata-udtryk `$max(payload)`
- Handling 3: **Set** `msg.min` til JSONata-udtryk `$min(payload)`

Dette beregner gennemsnit, maksimum og minimum af temperaturer.

### Betinget logik med JSONata

Du kan bruge JSONata til betinget logik:

```
[Inject] → [Change] → [Debug]
```

Change-node konfiguration:
- Handling: **Set** `msg.status` til JSONata-udtryk:
  ```
  $msg.payload > 30 ? 'hot' : ($msg.payload < 10 ? 'cold' : 'normal')
  ```

Dette indstiller en status baseret på temperaturværdien.

### Manipulering af arrays og objekter

```
[Inject] → [Change] → [Debug]
```

Inject: Send et array af objekter

Change-node konfiguration:
- Handling: **Set** `msg.processed` til JSONata-udtryk:
  ```
  payload.measurements.{ 
    "time": timestamp,
    "value": value,
    "normalized": (value - $min(payload.measurements.value)) / 
                 ($max(payload.measurements.value) - $min(payload.measurements.value))
  }
  ```

Dette transformerer et datasæt og tilføjer normaliserede værdier.

---

## 🚩 Tips og tricks

### Adgang til dybt indlejrede egenskaber

Du kan bruge punktnotation for at tilgå eller ændre dybt indlejrede egenskaber:

- `msg.payload.readings.temperature`
- `msg.payload.user.profile.preferences.theme`

### Brug af miljøvariabler

Du kan tilgå miljøvariabler med `env.`:

- **Set** `msg.apiKey` til env-egenskab `API_KEY`

### Dynamiske egenskabsnavne

Brug square bracket-notation i JSONata for dynamiske egenskabsnavne:

- **Set** `msg.payload` til JSONata-udtryk `{$msg.fieldName: $msg.fieldValue}`

---

## 🏋️ Øvelser

### Øvelse 1: Dataomstrukturering

1. Opret et flow med inject → change → debug
2. Konfigurer inject til at sende et JSON-objekt:
   ```json
   {
     "sensorData": {
       "t": 22.5,
       "h": 45,
       "p": 1013
     },
     "deviceId": "room1-sensor"
   }
   ```
3. Konfigurer change-noden til at:
   - Flyt `msg.payload.sensorData.t` til `msg.temperature`
   - Flyt `msg.payload.sensorData.h` til `msg.humidity`
   - Flyt `msg.payload.sensorData.p` til `msg.pressure`
   - Flyt `msg.payload.deviceId` til `msg.device`
   - Slet `msg.payload`
   - Sæt `msg.payload` til et nyt objekt med JSONata:
     ```
     {
       "device": $msg.device,
       "readings": {
         "temperature": $msg.temperature,
         "humidity": $msg.humidity,
         "pressure": $msg.pressure
       },
       "timestamp": $now()
     }
     ```

### Øvelse 2: Datavalidering og -berigelse

1. Opret et flow med inject → change → debug
2. Inject sender et simpelt tal (temperatur)
3. Konfigurer change-noden til at:
   - Sæt `msg.original` til `msg.payload`
   - Sæt `msg.valid` til JSONata `$msg.payload >= -40 and $msg.payload <= 60`
   - Sæt `msg.unit` til string "celsius"
   - Sæt `msg.status` til JSONata:
     ```
     $msg.payload > 30 ? 'hot' : 
     $msg.payload < 10 ? 'cold' : 'normal'
     ```
   - Sæt `msg.fahrenheit` til JSONata `($msg.payload * 9/5) + 32`

### Øvelse 3: Multistep transformation

1. Opret et flow med inject → change → debug
2. Inject sender et array af temperaturværdier
3. Konfigurer change-noden med flere trin:
   - Sæt `msg.count` til JSONata `$count(payload)`
   - Sæt `msg.avg` til JSONata `$average(payload)`
   - Sæt `msg.stats` til JSONata:
     ```
     {
       "min": $min(payload),
       "max": $max(payload),
       "range": $max(payload) - $min(payload),
       "variance": $variance(payload)
     }
     ```
   - Sæt `msg.normalized` til JSONata:
     ```
     payload.($-$min(payload))/($max(payload)-$min(payload))
     ```

---

## 🔍 Yderligere ressourcer

- [Node-RED Documentation - Change Node](https://nodered.org/docs/user-guide/nodes#change)
- [JSONata Documentation](https://jsonata.org/)
- [JSONata Exerciser](https://try.jsonata.org/) - Test JSONata-udtryk online
