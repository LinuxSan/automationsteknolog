# 🔀 Switch Node

Switch-noden fungerer som en betinget router i Node-RED. Den evaluerer beskedens indhold mod et eller flere vilkår og dirigerer beskeden til forskellige outputs baseret på resultaterne.

## 🎯 Formål

I denne guide lærer du om switch-noden og hvordan du kan:
- Implementere betinget logik uden at skrive JavaScript-kode
- Route beskeder til forskellige dele af dit flow baseret på indholdet
- Opsætte forskellige sammenligningstyper og operatorer
- Anvende avancerede filtreringsmønstre med regulære udtryk og JSONata

---

## ⚡ Grundfunktionalitet

Switch-noden evaluerer en specifik egenskab i en besked (typisk `msg.payload`) mod et sæt definerede regler. For hver regel, der er opfyldt, sendes beskeden til det tilsvarende output. Noden kan konfigureres til at:

- Sende til første matchende output og derefter stoppe
- Sende til alle outputs hvor reglerne er opfyldt
- Sende til outputs baseret på forskellige egenskaber i beskeden

---

## 🛠️ Konfiguration

![Switch Node Configuration](https://nodered.org/docs/user-guide/images/editor-switch-node-properties.png)

### Egenskab at evaluere

Du angiver først hvilken beskedegenskab du vil teste, fx:
- `msg.payload` (standard)
- `msg.topic`
- `msg.temperature`
- Eller enhver anden valid egenskabssti

### Operatorer

Switch-noden tilbyder mange sammenligningsoperatorer:

- **==**: Er lig med
- **!=**: Er ikke lig med
- **<**: Mindre end
- **<=**: Mindre end eller lig med
- **>**: Større end
- **>=**: Større end eller lig med
- **is between**: Mellem to værdier (inklusiv)
- **contains**: Indeholder en understreng eller et element
- **matches regex**: Matcher et regulært udtryk
- **is valid JSONata**: Evaluerer et JSONata-udtryk til true

### Outputs

- **Checking all rules** (standard): Sender beskeden til alle outputs hvor reglen er opfyldt
- **Stopping after first match**: Sender kun til det første matchende output

---

## 💡 Eksempler

### Eksempel 1: Temperaturzoner

```
[Inject] → [Switch] → [Debug 1, Debug 2, Debug 3]
```

Switch-node konfiguration:
- Egenskab: `msg.payload` (temperatur)
- Regel 1 (til output 1): `payload < 18` (koldt)
- Regel 2 (til output 2): `payload >= 18 && payload <= 25` (behageligt)
- Regel 3 (til output 3): `payload > 25` (varmt)

Dette router temperaturværdier til forskellige outputs baseret på værdiområder.

### Eksempel 2: Fejlfiltrering

```
[MQTT In] → [Switch] → [Debug 1, Debug 2]
```

Switch-node konfiguration:
- Egenskab: `msg.payload.status`
- Regel 1 (til output 1): `== "ok"` (normale beskeder)
- Regel 2 (til output 2): `!= "ok"` (fejlbeskeder)

Dette separerer normale driftsmeddelelser fra fejlrapporter.

### Eksempel 3: Topic-baseret routing

```
[MQTT In] → [Switch] → [Debug 1, Debug 2, Debug 3]
```

Switch-node konfiguration:
- Egenskab: `msg.topic`
- Regel 1 (til output 1): `contains "temperature"`
- Regel 2 (til output 2): `contains "humidity"`
- Regel 3 (til output 3): `contains "pressure"`

Dette dirigerer beskeder til forskellige outputs baseret på deres emne.

---

## 🔄 Avanceret anvendelse

### Regexp routing

Regulære udtryk giver kraftfuld mønstergenkendelse:

```
[Inject] → [Switch] → [Debug 1, Debug 2]
```

Switch-node konfiguration:
- Egenskab: `msg.payload`
- Regel 1: `matches regexp ^[A-Z][0-9]{3}$` (matcher formatet: et stort bogstav efterfulgt af 3 cifre)
- Regel 2: `!matches regexp ^[A-Z][0-9]{3}$` (matcher ikke formatet)

Dette kan bruges til at validere formater som produkt-ID'er, serienumre, osv.

### JSONata betingelser

JSONata giver mulighed for komplekse betingede udtryk:

```
[Inject] → [Switch] → [Debug 1, Debug 2, Debug 3]
```

Switch-node konfiguration:
- Egenskab: (JSONata udtryk vælges direkte)
- Regel 1: `$count(payload.readings) > 5` (mere end 5 målinger)
- Regel 2: `$average(payload.readings) > 50` (gennemsnit over 50)
- Regel 3: `$max(payload.readings) - $min(payload.readings) > 20` (range større end 20)

Dette lader dig udføre komplekse dataanalyser og betingelser.

### Multiple egenskaber

Du kan teste forskellige egenskaber med hver regel:

```
[Inject] → [Switch] → [Debug 1, Debug 2, Debug 3]
```

Switch-node konfiguration:
- Regel 1: `msg.payload.temperature > 30` (høj temperatur)
- Regel 2: `msg.payload.humidity > 80` (høj luftfugtighed)
- Regel 3: `msg.payload.battery < 20` (lavt batteri)

Dette lader dig reagere på forskellige betingelser fra samme besked.

---

## 🚩 Særlige tilfælde

### Håndtering af null/undefined

Når du tester værdier, er det vigtigt at være opmærksom på null/undefined:

- Brug operatoren `is null` til at tjekke for null-værdier
- Brug operatoren `is undefined` til at tjekke for udefinerede egenskaber

### Typekonvertering

Switch-noden forsøger at udføre type-konvertering ved sammenligning:
- Sammenligning mellem streng "42" og tal 42 vil evaluere som lig
- For streng typesammenligning, brug JSONata-udtryk

### Otherwise output

Tilføj en "otherwise" regel som den sidste regel for at fange beskeder, der ikke matcher nogen anden regel:

- Klik på '+add' knappen
- Vælg 'otherwise' (vil altid være sand)

---

## 🏋️ Øvelser

### Øvelse 1: Datavalidering

1. Opret et flow med inject → switch → 3 debug-noder
2. Konfigurer inject til at sende forskellige JSON-objekter
3. Konfigurer switch-noden til at:
   - Output 1: Gyldige beskeder med alle påkrævede felter  
     `is valid JSONata: payload.id && payload.value`
   - Output 2: Mangelfulde beskeder, men med id  
     `is valid JSONata: payload.id && !payload.value`
   - Output 3: Ugyldige beskeder uden id  
     `otherwise`

### Øvelse 2: Temperaturalarm med hysterese

1. Opret et flow med inject → switch → 3 debug-noder
2. Konfigurer switch-noden med JSONata-udtryk der implementerer hysterese:
   - Output 1 (normal): `$flowContext("lastState") != "normal" && payload > 18 && payload < 26`  
     Sæt også flow-konteksten: `$flowContext("lastState", "normal")`
   - Output 2 (for koldt): `$flowContext("lastState") != "cold" && payload <= 16`  
     Sæt også flow-konteksten: `$flowContext("lastState", "cold")`
   - Output 3 (for varmt): `$flowContext("lastState") != "hot" && payload >= 28`  
     Sæt også flow-konteksten: `$flowContext("lastState", "hot")`

### Øvelse 3: Multi-kriterier filtering

1. Opret et flow der analyserer sensormålinger
2. Konfigurer switch-noden til at route beskeder baseret på flere kriterier:
   - Output 1: Kritisk høj temperatur OG lav luftfugtighed  
     `msg.payload.temperature > 30 && msg.payload.humidity < 20`
   - Output 2: Temperatur stigende hurtigt  
     `msg.payload.temperature - msg.payload.lastTemperature > 5`
   - Output 3: Unormal sensoropførsel  
     `isNaN(msg.payload.temperature) || msg.payload.temperature < -40 || msg.payload.temperature > 100`
   - Output 4: Normal drift  
     `otherwise`

---

## 🔍 Yderligere ressourcer

- [Node-RED Documentation - Switch Node](https://nodered.org/docs/user-guide/nodes#switch)
- [Regular Expression Tester](https://regex101.com/)
- [JSONata Documentation](https://jsonata.org/)
