# Opgave 3 - MQTT med ESP32 + fan kontrol
I denne opgave skal du opsætte en ESP32, som kan modtage kommandoer via MQTT for at styre en blæser (fan). Du skal bruge MicroPython til at programmere ESP32'en.

## Trin 1: Forberedelse
1. Sørg for, at du har MicroPython firmware installeret på din ESP32.
2. Installer biblioteket, `umqtt.simple`.
3. Tilslut blæseren til ESP32'en:
   - VCC til 3.3V
   - GND til GND
   - Fan til GPIO 18 (du kan vælge en anden pin, men husk at opdatere koden)

## Trin 2: MicroPython kode
- Brug koden fra README til at opsætte MQTT-abonnement og styre blæseren baseret på modtagne beskeder.

- Lav et Node-RED flow, der publicerer kommandoer til MQTT-topics for at tænde og slukke blæseren.
- Test blæserstyringen ved at sende beskeder fra Node-RED og observere blæserens respons.
