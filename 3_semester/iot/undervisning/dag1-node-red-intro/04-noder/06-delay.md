# ⏱️ Delay Node

Delay-noden i Node-RED giver mulighed for at introducere tidsforsinkelser i dit flow, rate-limiting beskeder eller implementere simple time-out funktionaliteter. Dette er en central node for tidsstyring af beskeder.

## 🎯 Formål

I denne guide lærer du om delay-noden og hvordan du kan:
- Forsinke beskeder i et specificeret tidsrum
- Rate-begrænse beskeder for at undgå overbelastning
- Droppe beskeder ved for høj frekvens
- Samle flere beskeder i batches

---

## ⚡ Grundfunktionalitet

Delay-noden tilbyder fire primære funktioner:

1. **Delay each message**: Forsinker hver enkelt besked med et specificeret tidsrum
2. **Limit rate to**: Begrænser antallet af beskeder der kan passere pr. tidsenhed
3. **Throttle messages**: Kun lader seneste besked passere efter en venteperiode
4. **Queue messages and output at fixed interval**: Samler beskeder og sender dem videre med faste intervaller

---

## 🛠️ Konfiguration

### Forsinkelse (Delay Each Message)

![Delay Node Configuration](https://nodered.org/docs/user-guide/images/node-red-delay-node.png)

- **For** - Tidsperioden beskeder skal forsinkes (millisekunder, sekunder, minutter, timer)
- **Random delay** - Forsink med et tilfældigt tidsrum op til det angivne maksimum
- **Dynamic delay** - Brug en beskedegenskab til at bestemme forsinkelsen

### Rate Begrænsning (Limit Rate)

- **To** - Antallet af beskeder der tillades pr. tidsrum (f.eks. 1 besked pr. sekund)
- **Drop intermediate messages** - Mellem-beskeder droppes (kun de tilladte antal videreføres)
- **Queue intermediate messages** - Mellem-beskeder køes og sendes med den tilladte rate

### Throttling

- **To 1 message per** - Venter på at der ikke er flere indkomne beskeder i et givent tidsrum, før den videresender den seneste besked
- **Reset timeout if new message arrives** - Nulstiller ventetiden når der kommer en ny besked

### Fast Interval

- **Send at fixed interval** - Sender beskeder videre med fast interval uanset inputraten
- **Timed interval** - Vælg tidsinterval mellem outputs
- **Send concatenated array** - Sender alle beskeder som ét array
- **Send each message individually** - Sender beskederne enkeltvis med det angivne interval

---

## 💡 Eksempler

### Eksempel 1: Simpel forsinkelse

```
[Inject] → [Delay] → [Debug]
```

Delay-node konfiguration:
- Action: "Delay each message"
- For: "2 seconds"

Dette forsinkelser hver besked med 2 sekunder, hvilket er nyttigt for at simulere netværksforsinkelse eller give enheder tid til at reagere.

### Eksempel 2: Rate begrænsning af API-kald

```
[Inject] → [HTTP Request] → [Delay] → [Debug]
```

Delay-node konfiguration:
- Action: "Limit rate to"
- To: "1 message per 5 seconds"
- Drop intermediate messages: unchecked (queue them instead)

Dette sikrer, at API-kald ikke overstiger en frekvens på 1 kald hver 5. sekund, og køer yderligere forespørgsler.

### Eksempel 3: Debounce sensor input

```
[MQTT In] → [Delay] → [Debug]
```

Delay-node konfiguration:
- Action: "Throttle messages"
- To: "1 message per 500 milliseconds"
- Reset timeout if new message arrives: checked

Dette filtrerer hurtigt skiftende sensorværdier og lader kun den seneste værdi passere efter en stabil periode på 500 ms.

### Eksempel 4: Batch-behandling

```
[Inject] → [Delay] → [Debug]
```

Delay-node konfiguration:
- Action: "Queue messages and output at fixed interval"
- Send: "Every 5 seconds"
- Send as concatenated array: checked

Dette samler beskeder over 5 sekunder og sender dem som et enkelt array for batch-behandling.

---

## 🔄 Avanceret anvendelse

### Dynamisk forsinkelse

Du kan bruge en dynamisk forsinkelse baseret på en beskedegenskab:

```
[Inject] → [Function] → [Delay] → [Debug]
```

Function-node:
```javascript
msg.delay = Math.floor(Math.random() * 5000); // Random delay up to 5 seconds
return msg;
```

Delay-node konfiguration:
- Action: "Delay each message"
- For: "msg.delay milliseconds"

Dette giver dynamiske forsinkelser baseret på beskedindhold.

### Implementering af retry-mekanisme

```
[HTTP Request] → [Switch] → [Delay] → [Change] → [HTTP Request]
```

Switch-node: Check for fejlkode (status != 200)
Change-node: Sæt `msg.retry_count = (msg.retry_count || 0) + 1`
Delay-node konfiguration:
- Action: "Delay each message"
- For: "2^msg.retry_count seconds" (eksponentiel backoff)

Dette giver eksponentiel backoff for fejlede HTTP-requests.

### Dag/nat timing

```
[Inject] → [Function] → [Delay] → [Debug]
```

Function-node:
```javascript
const hour = new Date().getHours();
// Længere forsinkelse om natten, kortere om dagen
msg.delayTime = (hour >= 22 || hour <= 6) ? 60000 : 10000;
return msg;
```

Delay-node konfiguration:
- Action: "Delay each message"
- For: "msg.delayTime milliseconds"

Dette giver forskellige forsinkelser baseret på tidspunkt på dagen.

---

## 🚩 Særlige tilfælde

### Håndtering af msg.delay

Når du bruger dynamisk forsinkelse, husk at:
- `msg.delay` skal være et tal i millisekunder
- Negative værdier behandles som 0 (ingen forsinkelse)

### Rate-limit vs. Throttle

- **Rate-limit**: Jævn fordeling af beskeder over tid, med potentielt kø
- **Throttle**: Filtrerer burst af aktivitet til én besked, ignorerer mellemliggende beskeder

### Memory begrænsning

Vær opmærksom på:
- Store batches kan forbruge betydelig hukommelse
- Lange køer ved rate-limiting kan også bruge meget hukommelse
- Ved systemgenstart mistes køede beskeder

### Flow/global kontekst

Delay-noden gemmer ikke sit interne tilstand i flow eller global kontekst, så ved genstart af Node-RED:
- Alle ventende forsinkede beskeder går tabt
- Køede beskeder ved rate-limiting går tabt
- Batches nulstilles

---

## 🏋️ Øvelser

### Øvelse 1: Implementer en simpel trafiklys-sekvens

1. Opret et flow med en inject-node (trigger) og tre debug-noder (rød, gul, grøn)
2. Tilføj delay-noder mellem inject og debug-noderne
3. Konfigurer delayene til følgende sekvens:
   - Rød: Ingen forsinkelse
   - Gul: 2 sekunders forsinkelse efter rød
   - Grøn: 4 sekunders forsinkelse efter rød
4. Tilføj yderligere delay-noder for at skifte tilbage (grøn → gul → rød)

### Øvelse 2: Rate-limit dashboard-opdateringer

1. Opret et flow med et MQTT-input, en delay-node og en dashboard gauge
2. Konfigurer delay-noden til at:
   - Begrænse opdateringer til 1 pr. sekund
   - Køe mellemliggende beskeder
3. Test med hurtige MQTT-beskeder og observer dashboard-opdateringsraten

### Øvelse 3: Debounce med betinget output

1. Opret et flow med inject → delay → function → debug
2. Konfigurer delay-noden til throttle-mode (1 besked pr. 2 sekunder)
3. I function-noden, tilføj logik der sammenligner den aktuelle værdi med den forrige:
```javascript
// Gem sidste værdi i flow-kontekst
const lastVal = flow.get('lastValue') || 0;
const currentVal = msg.payload;

// Hvis værdien er uændret, afbryd flow
if (currentVal === lastVal) {
    return null;
}

// Gem den nye værdi og send beskeden videre
flow.set('lastValue', currentVal);
return msg;
```
4. Dette skaber et debounced output der kun sender beskeder når værdien faktisk ændrer sig

---

## 🔍 Yderligere ressourcer

- [Node-RED Documentation - Delay Node](https://nodered.org/docs/user-guide/nodes#delay)
- [Understanding Rate Limiting in APIs](https://nordicapis.com/everything-you-need-to-know-about-api-rate-limiting/)
- [Debounce and Throttle Concepts](https://css-tricks.com/debouncing-throttling-explained-examples/)
