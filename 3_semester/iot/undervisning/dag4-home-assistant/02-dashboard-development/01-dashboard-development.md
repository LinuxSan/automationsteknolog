# 🧪 Opgaver – Home Assistant: Dashboard Development

Disse opgaver hjælper dig med at opbygge og tilpasse dashboards i Home Assistant ved hjælp af Lovelace UI. Du lærer at visualisere sensorer, kontrollere aktuatorer og præsentere information på en brugervenlig måde.

---

## 🟢 Opgave 1 – Opret nyt dashboard

1. Gå til "Rediger dashboard" i Home Assistant
2. Opret en ny visning (View) med titlen "Klima"
3. Tilføj et `Gauge Card` der viser en temperatur-sensor

   * Entitet: `sensor.stue_temperature`
   * Min: 0, Max: 40, Enhed: °C

✅ *Tjek at visningen vises korrekt i hoved-UI*

---

## 🔵 Opgave 2 – Tilføj flere kort

1. Tilføj et `Entities Card` med mindst 3 sensorer (reelle eller test)
2. Tilføj et `History Graph Card` for en temperatur eller fugtighedssensor
3. Tilføj et `Button Card` der sender en kommando til fx `switch.ventilator`

✅ *Bekræft at hver knap eller sensor fungerer som forventet*

---

## 🟡 Opgave 3 – Design og layout

1. Omdøb visninger og kort for at give mening for brugeren
2. Brug ikoner og farver der indikerer tilstand (grøn/gul/rød)
3. Brug `Conditional Card` til kun at vise advarsler, hvis temp > 30°C

✅ *Tjek hvordan dashboardet ser ud på en mobiltelefon eller tablet*

---

## 🧩 Opgave 4 – Tilføj dynamik og grupper

1. Brug `Glance Card` til hurtigoversigt af 3-4 sensorer
2. Tilføj kort i grupper (fx "Klima", "Lys", "Bevægelse")
3. Gør brug af `state_color: true` hvor muligt

✅ *Organisér indholdet så det er overskueligt og tematisk logisk*

---

## 🧠 Refleksion

* Hvem er din målgruppe – og hvordan påvirker det designvalget?
* Hvilken information er vigtigst i dit smarthome?
* Hvordan kan du vise status, advarsler og kontrol uden forvirring?

---

📌 Lovelace dashboard giver brugeren overblik og kontrol – og det er op til dig at designe et interface, der både informerer og engagerer!
