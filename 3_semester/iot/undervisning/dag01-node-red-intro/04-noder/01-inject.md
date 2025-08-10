# 💉 Inject Node

Inject-noden er et af de grundlæggende udgangspunkter for Node-RED flows. Den gør det muligt at manuelt eller automatisk trigge flows ved at sende specificerede beskeder ind i flowet.

## 🎯 Formål

I denne guide lærer du om inject-noden og dens anvendelse til at:
- Starte flows manuelt 
- Sende forskellige datatyper ind i et flow
- Konfigurere periodiske eller planlagte triggers

---

## ⚡ Grundfunktionalitet

Inject-noden kan indsprøjte forskellige typer af data i dit flow:

- **Timestamps**: Dato og klokkeslæt for aktivering
- **Strenge**: Foruddefinerede tekstværdier
- **Tal**: Numeriske værdier
- **Boolske værdier**: true/false
- **JSON objekter**: Strukturerede data
- **Buffer**: Binære data
- **Miljøvariabler**: Værdier fra Node-RED's miljø

Du kan aktivere inject-noden på tre måder:
1. **Manuelt**: Ved at klikke på knappen på selve noden
2. **Periodisk**: Gentag med et fast interval
3. **Planlagt**: På specifikke tidspunkter ved hjælp af cron-udtryk

---

## 🛠️ Konfiguration

### Payload-typer

![Inject Node Configuration](https://nodered.org/docs/user-guide/images/editor-inject-node-properties.png)

- **Timestamp**: Indsætter nuværende dato/tid
- **String**: Tekstværdi (fx "Hello World")
- **Number**: Numerisk værdi (fx 42)
- **Boolean**: true eller false
- **JSON**: Strukturerede data i JSON-format
- **Buffer**: Binært indhold
- **Flow/Global Variable**: Henter værdi fra flow/global context

### Gentag-indstillinger

Du kan konfigurere inject-noden til at aktivere periodisk:

- **None**: Kun manuel aktivering
- **Interval**: Hvert n sekunder/minutter/timer
- **At specific time(s)**: På specifikke tidspunkter med cron-udtryk
- **After startup delay**: n sekunder efter Node-RED opstart

---

## 💡 Eksempler

### Eksempel 1: Basalt timestamp flow

```
[Inject] → [Debug]
```

Konfiguration:
- Payload: timestamp
- Topic: "timestamp"

Dette vil vise det aktuelle tidspunkt i debug-panelet, når du klikker på inject-knappen.

### Eksempel 2: Periodisk numerisk værdi

```
[Inject] → [Function] → [Debug]
```

Konfiguration:
- Payload: number (42)
- Topic: "counter"
- Repeat: interval (hvert 5. sekund)

Function-node:
```javascript
// Tilføj 1 til værdien hver gang
msg.payload = msg.payload + 1;
return msg;
```

Dette vil sende tallet 42, 43, 44, osv. til debug-panelet hvert 5. sekund.

### Eksempel 3: JSON objekt

```
[Inject] → [Debug]
```

Konfiguration:
- Payload: JSON
- Værdi: `{"sensorId": "temp1", "value": 22.5, "unit": "C"}`

Dette vil sende et JSON-objekt der repræsenterer en sensoraflæsning.

---

## 🔄 Avanceret: Multiple Payloads

Du kan også konfigurere inject-noden til at indstille flere egenskaber i en enkelt besked:

1. Indstil først standard payload
2. Klik på "Add property" knappen
3. Angiv egenskabsnavn (f.eks. "topic") og værdi

For eksempel:
- Payload: number (42)
- Property: topic = "temperature"
- Property: unit = "celsius"

Dette vil sende en besked med disse tre egenskaber på én gang.

---

## ⚠️ Begrænsninger

- Inject-noden kan kun starte flows, ikke modtage data fra andre noder
- Cron-planlagte injections kører måske ikke præcis på millisekundet
- Meget hyppige injections (< 100ms) kan påvirke Node-RED's ydeevne

---

## 🏋️ Øvelser

### Øvelse 1: Timestamp med formatering

1. Placer en inject-node konfigureret med timestamp
2. Tilføj en function-node med følgende kode:
   ```javascript
   // Formater tidsstempel pænt
   var date = new Date(msg.payload);
   msg.payload = date.toLocaleTimeString();
   return msg;
   ```
3. Forbind til en debug-node
4. Deploy og test

### Øvelse 2: Gentagende tæller

1. Opret en inject-node der sender 0 som payload hvert 2. sekund
2. Tilføj en function-node der bruger context til at tælle:
   ```javascript
   // Tæl op for hver injektion
   var count = context.get('count') || 0;
   count++;
   context.set('count', count);
   msg.payload = count;
   return msg;
   ```
3. Tilføj en debug-node til at vise resultatet

### Øvelse 3: Daily Report Trigger

1. Opsæt en inject-node til at udløses én gang om dagen kl. 8:00
   - Brug cron-indstillingen: `0 8 * * *`
2. Indstil topic til "daily_report"
3. Indstil payload til en streng: "Generér daglig rapport"
4. Tilslut til en debug-node

---

## 🔍 Yderligere ressourcer

- [Node-RED Documentation - Inject Node](https://nodered.org/docs/user-guide/nodes#inject)
- [Advanced scheduling with Cron syntax](https://crontab.guru/)
- [Working with different data types in Node-RED](https://nodered.org/docs/user-guide/messages)
