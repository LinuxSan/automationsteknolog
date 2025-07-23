# 📝 Template Node

Template-noden i Node-RED giver mulighed for at generere nye beskedindhold ved hjælp af Mustache-skabeloner. Dette er et kraftfuldt værktøj til at formatere data, generere dynamisk indhold og transformere beskedstrukturer.

## 🎯 Formål

I denne guide lærer du om template-noden og hvordan du kan:
- Generere dynamisk tekst og HTML ved hjælp af Mustache-skabeloner
- Konstruere velformateret JSON, XML eller andre dataformater
- Inkludere beskeddata i dynamiske skabeloner
- Bruge avanceret logik i dine skabeloner

---

## ⚡ Grundfunktionalitet

Template-noden tager indkommende beskeder og anvender en brugerspecificeret skabelon til at generere et nyt output. Skabelonen kan indeholde:

- Statisk tekst
- Dynamiske pladsholdere med beskedegenskaber
- Betingede udtryk og løkker
- HTML, JSON, XML eller enhver anden tekstbaseret struktur

Standardkonfigurationen placerer resultatet i `msg.payload`, men dette kan ændres.

---

## 🛠️ Konfiguration

![Template Node Configuration](https://nodered.org/docs/user-guide/images/editor-template-node-properties.png)

### Primære indstillinger

- **Name**: Valgfrit navn til noden
- **Template**: Skabelonindholdet der bruger Mustache-syntaks
- **Output as**: Formatering af output (Plain text, parsed JSON, or parsed YAML)
- **Property**: Hvor resultatet skal placeres (standard: `msg.payload`)
- **Template format**: Format til redigering i editoren (Mustache eller Plain text)
- **Output**: Hvordan output håndteres (en enkelt besked eller flere beskeder i et array)

### Mustache grundsyntaks

- `{{variabel}}` - Indsætter værdien af variablen
- `{{{variabel}}}` - Indsætter værdien uden HTML-escaping
- `{{#sektion}}...{{/sektion}}` - Betinget sektion eller løkke
- `{{^sektion}}...{{/sektion}}` - Negeret sektion (vises når sektion ikke eksisterer/er tom)
- `{{.}}` - Henviser til den aktuelle kontekst

---

## 💡 Eksempler

### Eksempel 1: Simpelt tekstformat

```
[Inject] → [Template] → [Debug]
```

Inject-node: Sæt `msg.payload` til et tal og `msg.topic` til "Temperature"

Template-node:
```mustache
Temperaturen er {{payload}}°C.
Emnet er "{{topic}}".
```

Dette erstatter `{{payload}}` og `{{topic}}` med de tilsvarende værdier fra beskeden.

### Eksempel 2: HTML Dashboard

```
[Inject] → [Template] → [Dashboard Template]
```

Inject-node: Inject et objekt med sensordata

Template-node:
```html
<div style="font-family: Arial, sans-serif;">
    <h1>Sensor Dashboard</h1>
    <div class="readings">
        <div class="sensor">
            <h3>Temperatur</h3>
            <p style="color: {{#payload.temp_high}}red{{/payload.temp_high}}{{^payload.temp_high}}green{{/payload.temp_high}}">
                {{payload.temperature}}°C
            </p>
        </div>
        <div class="sensor">
            <h3>Luftfugtighed</h3>
            <p>{{payload.humidity}}%</p>
        </div>
        <div class="sensor">
            <h3>Tidspunkt</h3>
            <p>{{payload.timestamp}}</p>
        </div>
    </div>
</div>
```

Dette genererer et HTML-dashboard med dynamisk farvning baseret på temperaturværdien.

### Eksempel 3: JSON formatering

```
[Inject] → [Template] → [HTTP Response]
```

Template-node:
```json
{
  "device": {
    "id": "{{deviceId}}",
    "name": "{{deviceName}}"
  },
  "readings": [
    {{#payload}}
    {
      "sensor": "{{sensor}}",
      "value": {{value}},
      "unit": "{{unit}}",
      "timestamp": "{{timestamp}}"
    }{{^last}},{{/last}}
    {{/payload}}
  ],
  "status": "{{status}}",
  "generated": "{{now}}"
}
```

Output as: "parsed JSON"

Dette skaber et formateret JSON-objekt fra beskeddata, egnet til API-respons.

---

## 🔄 Avanceret anvendelse

### Løkker over arrays

```
[Inject] → [Template] → [Debug]
```

Inject-node: Injecter `msg.payload` med et array af værdier

Template-node:
```mustache
<ul>
{{#payload}}
    <li>{{.}}</li>
{{/payload}}
</ul>
```

Dette itererer over arrayet og genererer et listeelement for hver værdi.

### Betinget logik

```
[Inject] → [Template] → [Debug]
```

Template-node:
```mustache
{{#payload.temperature}}
    {{#payload.temperature.value}}
        {{! Vi har en temperaturværdi }}
        Temperaturen er {{payload.temperature.value}}°C
        {{#payload.temperature.value.high}}(høj!){{/payload.temperature.value.high}}
        {{#payload.temperature.value.low}}(lav!){{/payload.temperature.value.low}}
    {{/payload.temperature.value}}
    {{^payload.temperature.value}}
        {{! Ingen temperaturværdi }}
        Ingen temperaturdata tilgængelig
    {{/payload.temperature.value}}
{{/payload.temperature}}
{{^payload.temperature}}
    Ingen temperaturinformation fundet
{{/payload.temperature}}
```

Dette demonstrerer avanceret betinget logik og nestedede sektioner.

### Formatering af dato/tid

```
[Inject] → [Template] → [Debug]
```

Template-node med tilpasset dato/tid:
```mustache
Aktuelt tidspunkt: {{new Date().toLocaleTimeString()}}
Formateret dato: {{new Date().toLocaleDateString('da-DK', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}}
```

Dette genererer tilpassede dato- og tidsstrenge.

---

## 🚩 Særlige tilfælde

### Adgang til kontekst

Du kan få adgang til flow og global kontekst:

```mustache
Flow-værdi: {{flow.counterValue}}
Global indstilling: {{global.settings.sensorThreshold}}
```

### Escaping af specialtegn

Brug triple-curly braces `{{{variable}}}` for at undgå HTML-escaping:

```mustache
Escaped HTML: {{htmlContent}}
Unescaped HTML: {{{htmlContent}}}
```

### Brug af hjælpefunktioner

Du kan definere og bruge hjælpefunktioner ved at konfigurere dem i template-noden:

```javascript
// I de avancerede indstillinger for template-noden
const helpers = {
    formatTemperature: function(temp) {
        return parseFloat(temp).toFixed(1) + "°C";
    },
    isHighValue: function(value, threshold) {
        return value > threshold;
    }
};
```

Brug derefter i skabelonen:
```mustache
Formateret temperatur: {{formatTemperature payload.temperature}}
{{#isHighValue payload.humidity 80}}Luftfugtighed er for høj!{{/isHighValue}}
```

### Dynamisk udnyttelse af kontekst-objekter

```mustache
{{#msg}}
  {{#payload}}
    {{#data}}
      {{field1}} - {{field2}}
    {{/data}}
  {{/payload}}
{{/msg}}
```

Dette giver fleksibel adgang til nestedede egenskaber.

---

## 🏋️ Øvelser

### Øvelse 1: Formatering af vejrdata

1. Opret et flow med en inject-node og en template-node
2. Konfigurer inject-node til at injecte følgende objekt:
```json
{
  "location": "København",
  "current": {
    "temperature": 22.5,
    "humidity": 65,
    "conditions": "Delvist skyet",
    "windSpeed": 12
  },
  "forecast": [
    {"day": "Mandag", "high": 24, "low": 14, "conditions": "Solrigt"},
    {"day": "Tirsdag", "high": 22, "low": 15, "conditions": "Regn"},
    {"day": "Onsdag", "high": 19, "low": 13, "conditions": "Skyet"}
  ]
}
```
3. Konfigurer template-node til at generere en velformateret vejrrapport med HTML-formatering

### Øvelse 2: Dynamisk email-generator

1. Opret et flow med inject → template → debug
2. Injecter brugerdata med navn, email og købsinformation
3. Skab en template der genererer en email-bekræftelse med:
   - Personlig hilsen med navnet
   - Liste over købte produkter med priser
   - Total sum
   - Leveringsinformation
   - Forskellige afsnit baseret på betalingsmetode

### Øvelse 3: Dataformateringstransformation

1. Opret et flow med inject → template → debug
2. Injecter rå sensordata fra forskellige sensorer
3. Brug template-noden til at transformere data til et standardiseret format med:
   - Ensartet navngivningskonvention for alle felter
   - Tidsstempel i ISO-format
   - Metadata om datakilde og version
   - Gruppering af relaterede sensordata
   - Output som korrekt formateret JSON

---

## 🔍 Yderligere ressourser

- [Node-RED Documentation - Template Node](https://nodered.org/docs/user-guide/nodes#template)
- [Mustache Template System](https://mustache.github.io/)
- [Handlebars Templates](https://handlebarsjs.com/) (Udvidet Mustache-system)
