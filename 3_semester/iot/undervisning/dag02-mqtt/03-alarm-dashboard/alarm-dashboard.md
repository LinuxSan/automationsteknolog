# 🛠 Opgaver – Smart Home Alarm Dashboard

Disse opgaver er baseret på teori om alarmklassificering, prioritering, systemtilstande og dashboards. Du lærer at bygge et Node-RED-baseret system, der klassificerer og håndterer alarmer i et smart home.

> 🧠 **Pædagogisk fokus:**
> Du skal ikke blot implementere et system – du skal også forstå, hvorfor alarmer prioriteres, hvordan man reducerer alarm-støj (anti-flapping) og hvordan et dashboard understøtter beslutninger. Refleksionsspørgsmål guider din tænkning.

---

## Del 1 – Temperaturbaseret alarmering

### 🎯 Læringsmål

* Du kan kategorisere temperaturdata som info, advarsel eller kritisk alarm
* Du kan formatere alarmer med passende metadata

### 🔧 Opgave

1. Modtag MQTT-beskeder fra topic `smarthouse/+/temperature`
2. Opret en function node, der:

   * Kategoriserer temperatur som:

     * **Info** (25–30°C)
     * **Warning** (10–25°C og 30–40°C)
     * **Critical** (<10°C eller >40°C)
   * Tilføjer metadata: tid, device-id, type og besked
3. Send beskeder videre til debug og dashboard (tekstnode)

💬 **Refleksion:** Hvilke grænser giver mening i et hjem? Skal de være ens i alle rum?
👥 **Samarbejde:** Byt grænseværdier med en makker – kan I validere hinandens design?

---

## Del 2 – Heartbeat og sensor status

### 🎯 Læringsmål

* Du kan overvåge om sensorer er online
* Du kan sende en alarm, når en sensor bliver tavs

### 🔧 Opgave

1. Modtag `heartbeat/+/status` hver 10. sekund fra ESP32
2. Brug flow memory til at lagre seneste modtagelsestidspunkt
3. Brug en inject + function node der hvert 15. sekund tjekker:

   * Hvis tid > 60 sek siden sidste heartbeat → send critical alarm

💬 **Refleksion:** Hvordan adskiller heartbeat-overvågning sig fra almindelig MQTT-monitorering?
🔍 **Variation:** Lav statusindikator på dashboard (farve eller ikon)

---

## Del 3 – Anti-flapping og hysterese

### 🎯 Læringsmål

* Du kan undgå gentagne alarmer ved værdier tæt på grænsen
* Du kan implementere hysterese og anti-flapping

### 🔧 Opgave

1. Justér temperatur-alarm fra Del 1 med hysterese:

   * Alarm ON: >30°C
   * Alarm OFF: <28°C
2. Gem alarmstatus i context eller flow
3. Brug `rbe` eller `switch` nodes til at forhindre gentagelser

💬 **Refleksion:** Hvilke problemer ville opstå uden hysterese? Hvorfor er det vigtigt i et hjemmemiljø?

---

## Del 4 – Dashboard og visuel prioritering

### 🎯 Læringsmål

* Du kan opsætte visuelle elementer til at vise alarmsystemets tilstand
* Du kan strukturere et dashboard hierarkisk

### 🔧 Opgave

1. Opret et dashboard med:

   * Temperaturmåler (gauge)
   * Alarmstatus (ui\_text)
   * Systemstatus (farvet indikator eller tekst)
2. Farvekod alarmsystemet:

   * Grøn = normal
   * Gul = advarsel
   * Rød = kritisk
3. Test med simulerede temperaturer og manglende heartbeat

💬 **Refleksion:** Hvilke visuelle virkemidler gør det nemt at afkode kritikalitet? Hvad kan blive for meget?

---

## Del 5 – Alarmhistorik og persistering

### 🎯 Læringsmål

* Du kan logge og vise tidligere alarmer
* Du kan begrænse logstørrelse og slette gamle alarmer

### 🔧 Opgave

1. Brug context storage til at gemme alarmer (maks 50 stk)
2. Gem: tidspunkt, type, enhed, besked og status (acknowledged/resolved)
3. Vis seneste 5 alarmer i dashboard (table eller ui\_template)
4. Tilføj en “clear history” knap

💬 **Refleksion:** Hvilke alarmer er vigtige at gemme – og hvor længe?
🔍 **Udvidelse:** Tilføj mulighed for at “acknowledge” alarmer manuelt

---

## Ekstra: Eskalering og integration

> Kun hvis tid og niveau tillader

* Lav logik til at sende email eller push ved kritisk alarm
* Overvej integration med Home Assistant eller ekstern MQTT-broker

---

## Afslutning

📷 **Dokumentation:** Skærmbillede af dashboard og flows med korte noter
✍️ **Opsamling:** Hvad har du lært om alarmklassificering, timing og brugergrænseflader?
🎯 **Del med holdet:** Forklar dit alarmsystem på tavlen eller i breakout-grupper
