# 🏡 REST-opgave – Brug af eksternt REST API i Home Assistant

I denne opgave skal du integrere data fra et eksternt REST-baseret API direkte i Home Assistant (HA). Du lærer at bruge `rest`-sensorer til at hente data og vise dem i brugergrænsefladen.

---

## 🎯 Læringsmål

* Du kan konfigurere en `rest`-sensor i HA
* Du kan hente og vise data fra et eksternt API
* Du forstår REST i konteksten af Home Assistants automatiseringer og dashboards

---

## 🔧 Trin 1 – Opret en konto på Weatherstack

1. **Åbn din browser og gå til Weatherstack**:
   * Besøg [https://weatherstack.com](https://weatherstack.com) i din browser
   * Klik på "Sign Up Free" knappen på forsiden

2. **Registrer en ny konto**:
   * Udfyld registreringsformularen med dit navn, e-mail og en adgangskode
   * Vælg den gratis plan (Free Plan)
   * Klik på "Sign Up" for at afslutte registreringen

3. **Find din API-nøgle**:
   * Efter registrering bliver du ført til dit dashboard
   * Din API-nøgle (access_key) vises tydeligt i dashboardet
   * Kopier denne nøgle - du skal bruge den til alle API-kald

---

## 🔧 Trin 2 – Test API'et i browseren

1. **Konstruer din URL med API-nøglen**:
   * Tag den URL-skabelon, der er vist nedenfor
   * Erstat `DIN_API_NØGLE` med den nøgle, du kopierede fra dashboardet
   ```
   http://api.weatherstack.com/current?access_key=DIN_API_NØGLE&query=Copenhagen
   ```

2. **Test i browseren**:
   * Indsæt den komplette URL i din browsers adresselinje
   * Tryk Enter for at udføre API-kaldet

3. **Kontroller JSON-svaret**:
   * Du skulle nu se et JSON-svar der indeholder:
   * `location` med oplysninger om København
   * `current` med aktuelle vejrdata, herunder:
     * `temperature` (temperatur i °C)
     * `humidity` (luftfugtighed i %)
     * `weather_descriptions` (tekstbeskrivelse af vejret)
   * Hvis du ikke ser disse data, kontrollér din API-nøgle og internetforbindelse

---

## 🔧 Trin 3 – Tilføj REST-sensor i Home Assistant

1. **Åbn configuration.yaml**:
   * Find `configuration.yaml` filen i din Home Assistant installation
   * Du kan redigere den via Samba-share, SSH eller File Editor tilføjelsen
   * Åbn den i en teksteditor

2. **Tilføj REST sensor konfiguration**:
   * Indsæt følgende kode i filen (hvis der allerede er en `sensor:` sektion, tilføj kun indholdet):
   ```yaml
   sensor:
     - platform: rest
       name: Weather Copenhagen
       resource: http://api.weatherstack.com/current?access_key=DIN_API_NØGLE&query=Copenhagen
       value_template: '{{ value_json.current.temperature }}'
       unit_of_measurement: "°C"
       scan_interval: 1800  # Opdater hver halve time (for at spare API-kald)
       json_attributes_path: "$.current"
       json_attributes:
         - humidity
         - weather_descriptions
         - weather_icons
         - wind_speed
         - wind_dir
         - pressure
   ```
   * Erstat `DIN_API_NØGLE` med din faktiske API-nøgle

3. **Gem og genstart Home Assistant**:
   * Gem filen
   * Gå til Home Assistant web interface
   * Gå til Konfiguration > Server Controls
   * Klik på "Check Configuration" knappen for at kontrollere syntaksen
   * Hvis konfigurationen er gyldig, klik på "Restart" knappen

---

## 🔧 Trin 4 – Verificer at sensoren fungerer

1. **Tjek Developer Tools**:
   * Gå til Home Assistant web interface
   * Vælg "Developer Tools" fra sidepanelet
   * Vælg "States" fanebladet
   * Søg efter "weather" i filterfeltet
   * Find `sensor.weather_copenhagen` og tjek at den viser en temperaturværdi

2. **Tjek attributter**:
   * Klik på `sensor.weather_copenhagen` i listen
   * Se på "Attributes" sektionen 
   * Bekræft at du kan se attributter som humidity, weather_descriptions osv.

---

## 🔧 Trin 5 – Opret template sensorer for attributter

1. **Tilføj template sensorer** til configuration.yaml:
   * Tilføj følgende kode for at oprette separate sensorer for hver attribut:
   ```yaml
   # Template sensorer for vejrattributter
   template:
     - sensor:
         - name: "Copenhagen Weather Description"
           state: "{{ state_attr('sensor.weather_copenhagen', 'weather_descriptions')[0] }}"
           icon: mdi:text
         
         - name: "Copenhagen Humidity"
           state: "{{ state_attr('sensor.weather_copenhagen', 'humidity') }}"
           unit_of_measurement: "%"
           icon: mdi:water-percent
           
         - name: "Copenhagen Wind Speed"
           state: "{{ state_attr('sensor.weather_copenhagen', 'wind_speed') }}"
           unit_of_measurement: "km/h"
           icon: mdi:weather-windy
   ```

2. **Gem og genstart Home Assistant** igen, som beskrevet tidligere.

---

## 🔧 Trin 6 – Opret et vejr-dashboard

1. **Gå til Lovelace UI**:
   * Åbn Home Assistant
   * Klik på de tre prikker i øverste højre hjørne
   * Vælg "Edit Dashboard"

2. **Tilføj et nyt kort**:
   * Klik på "+" knappen for at tilføje et nyt kort
   * Vælg "Entities" kortet

3. **Konfigurer kortet**:
   * Giv kortet en titel, f.eks. "København Vejr"
   * Tilføj følgende enheder:
     * `sensor.weather_copenhagen` (temperatur)
     * `sensor.copenhagen_humidity`
     * `sensor.copenhagen_weather_description`
     * `sensor.copenhagen_wind_speed`
   * Klik på "Save" for at gemme kortet

4. **Tilføj et glance-kort** (valgfrit):
   * Tilføj endnu et kort, vælg "Glance" typen
   * Tilføj de samme sensorer som ovenfor
   * Dette giver en mere kompakt visning med ikoner

---

## 🔧 Trin 7 – Opret en frostalarm-automatisering

1. **Gå til Automations**:
   * Gå til Konfiguration > Automations & Scenes
   * Klik på "+ Add Automation"

2. **Konfigurer automatiseringen**:
   * **Navn**: "Advarsel: Frost i København"
   * **Trigger**:
     * Vælg "Numeric State" som trigger type
     * Vælg `sensor.weather_copenhagen` som entitet
     * Sæt "Below" til 0
   * **Action**:
     * Vælg "Call Service" som action type
     * Vælg `persistent_notification.create` som service
     * Tilføj følgende service data:
       ```yaml
       title: "Frostalarm!"
       message: "Det er koldere end 0 °C i København nu ({{ states('sensor.weather_copenhagen') }} °C)."
       ```

3. **Gem automatiseringen** ved at klikke på "Save".

---

## 🔧 Trin 8 – Test og fejlfinding

1. **Test sensoren**:
   * Overvåg sensorværdierne på dit dashboard
   * Bemærk at data kun opdateres i henhold til `scan_interval` (30 minutter i vores konfiguration)

2. **Fejlfinding**:
   * Hvis sensoren viser `unknown` eller `unavailable`:
     * Tjek din API-nøgle igen
     * Tjek Home Assistant logs for eventuelle fejlmeddelelser
     * Verificer at Home Assistant har internetadgang
     * Prøv at reducere `scan_interval` midlertidigt for hurtigere opdateringer under test

3. **API begrænsninger**:
   * Bemærk at den gratis plan på Weatherstack har begrænsninger:
     * 1000 kald pr. måned
     * Kun HTTP (ikke HTTPS) i den gratis plan
     * Begrænset adgang til historiske data

---

## 🧠 Refleksion

* Hvad er fordelene ved at bruge REST-data frem for lokale sensorer?
  * Overvej: global dækning, data du ikke selv kan måle, professionel datakvalitet.

* Hvordan håndterer du fejl – fx tomt svar eller nedetid?
  * Overvej: template sensorer med standardværdier, notification ved fejl, automatisk genstart.

* Hvilke andre REST-baserede tjenester kunne give værdi i et smart home?
  * Overvej: solenergidata, luftkvalitet, trafikinformation, valutakurser, nyhedsoverskrifter.

---

📌 Denne opgave viser, hvordan REST-integrationer i HA kan give adgang til globale data – og hvordan man bruger dem til både visning og automatisering.