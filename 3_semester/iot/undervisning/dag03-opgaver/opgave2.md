# Opgave 2 - MQTT med ESP32 + PIR sensor
I denne opgave skal du opsætte en ESP32 med en PIR bevægelsessensor, som sender data til en MQTT-broker. Du skal bruge MicroPython til at programmere ESP32'en.

## Trin 1: Forberedelse
1. Sørg for, at du har MicroPython firmware installeret på din ESP32.
2. Installer biblioteket, `umqtt.simple`.
3. Tilslut PIR-sensoren til ESP32'en:
   - VCC til 3.3V
   - GND til GND
   - Data til GPIO 14 (du kan vælge en anden pin, men husk at opdatere koden)
## Trin 2: Kode til ESP32
Brug koden fra README til at læse data fra PIR-sensoren og sende den til en MQTT-broker.

- Lav et Node-RED flow, der abonnerer på de relevante MQTT-topics for at modtage bevægelsesdata.
- Visualiser dataene i et dashboard ved hjælp af passende noder (f.eks. text).