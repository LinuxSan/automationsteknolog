# 🏡 REST-opgave – Brug af eksternt REST API i Home Assistant

I denne opgave skal du integrere data fra et eksternt REST-baseret API direkte i Home Assistant (HA). Du lærer at bruge `rest`-sensorer til at hente data og vise dem i brugergrænsefladen.

---

## 🎯 Læringsmål

* Du kan konfigurere en `rest`-sensor i HA
* Du kan hente og vise data fra et eksternt API
* Du forstår REST i konteksten af Home Assistants automatiseringer og dashboards

---

## 🌦️ Scenarie: Hent vejrdata fra Weatherstack

Du bruger [https://weatherstack.com](https://weatherstack.com) som REST-kilde. Data vises i HA som sensorer.

---

## 🔧 Trin 1 – Få API-nøgle og test endpoint

1. Opret en gratis konto på [https://weatherstack.com](https://weatherstack.com)
2. Find din `access_key` i brugerpanelet
3. Test URL'en i browseren:

```http
http://api.weatherstack.com/current?access_key=DIN_API_NØGLE&query=Copenhagen
```

> Bekræft at du får et JSON-svar med `temperature`, `humidity` og `weather_descriptions`

---

## 🛠 Trin 2 – Tilføj REST-sensor i configuration.yaml

Åbn `configuration.yaml` og tilføj:

```yaml
sensor:
  - platform: rest
    name: Weather Copenhagen
    resource: http://api.weatherstack.com/current?access_key=DIN_API_NØGLE&query=Copenhagen
    value_template: '{{ value_json.current.temperature }}'
    unit_of_measurement: "°C"
    json_attributes:
      - humidity
      - weather_descriptions
```

> Gem og genstart Home Assistant.

---

## 📺 Trin 3 – Vis sensoren i Dashboard

1. Gå til *Lovelace UI* (dit Home Assistant dashboard)
2. Tilføj en *entities card* eller *sensor card*
3. Vælg `sensor.weather_copenhagen`
4. (Valgfrit) Tilføj attributter som sekundær information

---

## 🔁 Ekstra: Automatisering ved vejrskift

1. Lav en automation, der tændes hvis `sensor.weather_copenhagen` er under 0 °C:

```yaml
automation:
  - alias: "Advarsel: Frost i København"
    trigger:
      - platform: numeric_state
        entity_id: sensor.weather_copenhagen
        below: 0
    action:
      - service: persistent_notification.create
        data:
          title: "Frostalarm!"
          message: "Det er koldere end 0 °C i København."
```

---

## 🧠 Refleksion

* Hvad er fordelene ved at bruge REST-data frem for lokale sensorer?
* Hvordan håndterer du fejl – fx tomt svar eller nedetid?
* Hvilke andre REST-baserede tjenester kunne give værdi i et smart home?

---

📌 Denne opgave viser, hvordan REST-integrationer i HA kan give adgang til globale data – og hvordan man bruger dem til både visning og automatisering.
