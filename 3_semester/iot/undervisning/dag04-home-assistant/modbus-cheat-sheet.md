# Komplet Guide til Læsning af Modbus-TCP i Home Assistant

Denne guide viser dig, hvordan du konfigurerer Home Assistant til at læse data fra de fire primære Modbus-områder. Princippet er det samme for dem alle: Du definerer én central forbindelse (en "hub") til din Modbus-enhed og tilføjer derefter de forskellige sensorer.

De to vigtigste parametre, du kommer til at ændre, er:
1.  **Platformen:** `binary_sensors` for On/Off-værdier og `sensors` for talværdier.
2.  **`input_type`**: Fortæller Home Assistant, hvilket Modbus-område den skal læse fra.

## Grundlæggende Opsætning (Din Hub)
Al din konfiguration vil leve i `configuration.yaml`-filen og starte med en "hub"-definition som denne. Alle eksemplerne nedenfor forudsætter, at du har denne base.

```yaml
modbus:
  - name: "min_modbus_enhed"
    type: tcp
    host: 192.168.1.102 # IP-adressen på din Modbus-enhed
    port: 502
    # Herunder tilføjer vi de forskellige sensorer...
```

---
## Metode 1: Læsning af Coils (Digitale On/Off-værdier) 🔌

**Hvad er det?** Tænk på en "Coil" som en relæ-udgang eller en digital on/off-værdi, du kan læse (og skrive til). Den er enten `true` (On) eller `false` (Off).
**Bruges til:** At aflæse status på en kontakt, et relæ eller en lampe.
**Home Assistant Entitet:** `binary_sensor`

### YAML Konfiguration
Tilføj en `binary_sensors:` sektion under din hub.

```yaml
    binary_sensors:
      - name: "Status Relæ 1"
        unique_id: status_relae_1_modbus
        slave: 1
        address: 0 # Adressen på den coil du vil læse (f.eks. 00001)
        input_type: coil
        device_class: power # Giver et passende ikon, f.eks. et lyn
```
**Forklaring:**
* **`binary_sensors:`**: Angiver, at de følgende enheder er binære (kun on/off).
* **`address: 0`**: Adressen på den coil, du vil aflæse.
* **`input_type: coil`**: Dette er den **vigtige** linje, der fortæller Home Assistant, at den skal læse fra Coil-området.

---
## Metode 2: Læsning af Discrete Inputs (Digitale Læse-Værdier)

**Hvad er det?** Tænk på en "Discrete Input" som en digital indgang – en status, der kun kan aflæses. Den er enten `true` (On) eller `false` (Off).
**Bruges til:** At aflæse status på en dørkontakt, en alarm-input eller en anden ren status-indikator.
**Home Assistant Entitet:** `binary_sensor`

### YAML Konfiguration
Denne tilføjes også under `binary_sensors:` sektionen.

```yaml
    binary_sensors:
      - name: "Status Dørkontakt"
        unique_id: status_doerkontakt_modbus
        slave: 1
        address: 1 # Adressen på den discrete input du vil læse (f.eks. 10002)
        input_type: discrete_input
        device_class: door # Giver et dør-ikon
```
**Forklaring:**
* **`input_type: discrete_input`**: Fortæller Home Assistant, at den skal læse fra Discrete Input-området.

---
## Metode 3: Læsning af Holding Registers (Analoge Læse/Skrive-Værdier) 🔢

**Hvad er det?** Tænk på et "Holding Register" som en analog værdi (et tal), der både kan læses og ændres.
**Bruges til:** Temperatur-setpunkter, hastighedsregulering, konfigurationsværdier. Dette er den mest almindelige registertype.
**Home Assistant Entitet:** `sensor`

### YAML Konfiguration
Tilføj en `sensors:` sektion under din hub.

```yaml
    sensors:
      - name: "Stuetemperatur"
        unique_id: stuetemperatur_modbus
        slave: 1
        address: 100 # Adressen på det holding register du vil læse (f.eks. 40101)
        input_type: holding
        # Dataformatering
        scale: 0.1
        precision: 1
        # Integration med HA
        unit_of_measurement: "°C"
        device_class: temperature
        state_class: measurement
```
**Forklaring:**
* **`sensors:`**: Angiver, at de følgende enheder er sensorer, der viser en numerisk værdi.
* **`input_type: holding`**: Fortæller Home Assistant, at den skal læse fra Holding Register-området.

---
## Metode 4: Læsning af Input Registers (Analoge Læse-Værdier)

**Hvad er det?** Tænk på et "Input Register" som en analog værdi (et tal), der kun kan aflæses.
**Bruges til:** Faktiske målinger fra udstyr, f.eks. den aktuelle temperatur, et energiforbrug eller et flow-meter.
**Home Assistant Entitet:** `sensor`

### YAML Konfiguration
Denne tilføjes også under `sensors:` sektionen.

```yaml
    sensors:
      - name: "Energiforbrug"
        unique_id: energiforbrug_modbus
        slave: 1
        address: 101 # Adressen på det input register du vil læse (f.eks. 30102)
        input_type: input
        # Dataformatering
        scale: 0.01
        precision: 2
        # Integration med HA
        unit_of_measurement: "kWh"
        device_class: energy
        state_class: total_increasing
```
**Forklaring:**
* **`input_type: input`**: Fortæller Home Assistant, at den skal læse fra Input Register-området.

---
## Samlet Konfigurations-Eksempel
Her er, hvordan din `configuration.yaml` kunne se ud med alle fire typer samlet under den samme hub.

```yaml
modbus:
  - name: "min_modbus_enhed"
    type: tcp
    host: 192.168.1.102
    port: 502
    
    binary_sensors:
      - name: "Status Relæ 1"
        unique_id: status_relae_1_modbus
        slave: 1
        address: 0
        input_type: coil
        device_class: power
        
      - name: "Status Dørkontakt"
        unique_id: status_doerkontakt_modbus
        slave: 1
        address: 1
        input_type: discrete_input
        device_class: door
        
    sensors:
      - name: "Stuetemperatur"
        unique_id: stuetemperatur_modbus
        slave: 1
        address: 100
        input_type: holding
        scale: 0.1
        precision: 1
        unit_of_measurement: "°C"
        device_class: temperature
        state_class: measurement

      - name: "Energiforbrug"
        unique_id: energiforbrug_modbus
        slave: 1
        address: 101
        input_type: input
        scale: 0.01
        precision: 2
        unit_of_measurement: "kWh"
        device_class: energy
        state_class: total_increasing
```

---
## Opsummeringstabel

| Modbus Type | Formål | HA Entitet | `input_type` Værdi | Eksempel Register |
| :--- |:---|:---|:---|:---|
| **Coil** | Digital On/Off (Læs/Skriv) | `binary_sensor` | `coil` | `00001` |
| **Discrete Input** | Digital On/Off (Kun Læse) | `binary_sensor` | `discrete_input` | `10001` |
| **Holding Register**| Analog Værdi (Læs/Skriv) | `sensor` | `holding` | `40001` |
| **Input Register** | Analog Værdi (Kun Læse) | `sensor` | `input` | `30001` |

Det vigtigste er altid at have dokumentationen for din Modbus-enhed ved hånden, så du ved præcis, hvilken adresse og `input_type` du skal bruge til de data, du vil have fat i.
