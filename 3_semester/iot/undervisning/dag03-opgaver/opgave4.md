# Opgave 4 - Sammensætning af opgaverne
I denne opgave skal du kombinere de tidligere opgaver ved at opsætte en ESP32, der både læser data fra en DHT11 temperatursensor og en PIR bevægelsessensor. Dataene skal sendes til en MQTT-broker, og du skal bruge Node-RED til at visualisere dataene i et dashboard.

## Trin 1: Forberedelse
1. Sørg for, at du har MicroPython firmware installeret på din ESP32.
2. Installer biblioteket, `umqtt.simple`.
3. Tilslut DHT11 sensoren til ESP32'en:
   - VCC til 3.3V
   - GND til GND
   - Data til GPIO 4 (du kan vælge en anden pin, men husk at opdatere koden)
4. Tilslut PIR-sensoren til ESP32'en:
   - VCC til 3.3V
   - GND til GND
   - Data til GPIO 14 (du kan vælge en anden pin, men husk at opdatere koden)
5. Tilslut blæseren til ESP32'en:
   - VCC til 3.3V
   - GND til GND
   - Fan til GPIO 18 (du kan vælge en anden pin, men husk at opdatere koden)

## Trin 2: MicroPython kode
- Brug koden fra README til at opsætte MQTT-abonnement og sende data fra både DHT11 og PIR sensorerne.
- Lav et Node-RED flow, der visualiserer dataene i et dashboard.
- Test systemet ved at observere dataene fra begge sensorer i Node-RED dashboardet.
- Implementer blæserstyring baseret på dht11 temperaturdata via MQTT.
