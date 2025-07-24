# 🧰 Dag 4 – Home Assistant 03: Dashboard Development

I denne lektion lærer du at bygge brugervenlige og informative dashboards i Home Assistant. Dashboardet (Lovelace UI) viser status, sensordata, styring og automatisering af dit smart home-system.

---

## 🎯 Læringsmål

* Forstå opbygningen af Lovelace UI
* Kunne oprette og tilpasse dashboards
* Præsentere sensorer og styre aktuatorer

---

## 🖼 Hvad er Lovelace?

* Frontend system i Home Assistant
* Giver total kontrol over layout og indhold
* Understøtter både GUI-editor og YAML-konfiguration

---

## 🧱 Dashboard-opbygning

* **Views**: faneblade eller sider
* **Cards**: individuelle komponenter (sensorer, knapper, grafer)
* **Entities**: sensorer, switches osv. der vises i kort

> Eksempel: View "Stue" → Card "Temperatur" → Entity `sensor.stue_temperature`

---

## 🎛️ Korttyper (cards)

| Type          | Funktion                            |
| ------------- | ----------------------------------- |
| Entities Card | Liste af sensorer og enheder        |
| Button Card   | Udfører en handling                 |
| Gauge Card    | Viser målinger grafisk              |
| Glance Card   | Kompakt visning med ikoner          |
| History Graph | Viser udvikling over tid            |
| Conditional   | Viser kun noget under visse forhold |

---

## 🧪 Eksempel – Simpelt Temperaturkort

```yaml
views:
  - title: Klima
    path: klima
    cards:
      - type: gauge
        entity: sensor.stue_temperature
        name: Stue Temperatur
        unit: "°C"
        min: 0
        max: 40
```

> Alternativt: opret via GUI → Rediger Dashboard → Tilføj kort

---

## 🖌 Designprincipper

* Farver: signalér status (grøn/gul/rød)
* Hierarki: vigtigst øverst og venstre
* Konsistens: samme rækkefølge og ikoner
* Dynamik: brug `conditional` og `state_color` til feedback

---

## 🧠 Refleksion

* Hvem er målgruppen for dit dashboard (tekniker, bruger, gæst)?
* Hvordan balancerer du information og overskuelighed?
* Hvad ville du vise på et mobilvenligt dashboard?

---

📌 Dashboards i Home Assistant er ikke kun visualisering – de er en integreret del af kontrol, interaktion og formidling af systemets tilstand.
