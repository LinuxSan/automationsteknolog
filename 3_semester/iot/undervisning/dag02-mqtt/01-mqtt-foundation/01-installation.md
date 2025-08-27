# Windows 10/11

1. Hent og kør installer
   [https://mosquitto.org/download](https://mosquitto.org/download) → vælg `mosquitto-*-install-windows-*.exe`. Vælg “Service” i wizard hvis broker skal køre i baggrunden. ([Eclipse Mosquitto][1], [Cedalo][2])
2. Åbn “Services” og start “Mosquitto Broker”, eller i CMD som admin:

   ```
   sc query mosquitto
   sc start mosquitto
   ```

   (installereren kan sætte den op som service). ([Cedalo][2])
3. Test lokalt i to terminaler:

   ```
   "C:\Program Files\mosquitto\mosquitto_sub.exe" -t test/hello
   "C:\Program Files\mosquitto\mosquitto_pub.exe" -t test/hello -m "hej"
   ```

   Klientsyntaks er som i man-siderne. ([Eclipse Mosquitto][3])
4. Vil du tillade andre maskiner på LAN at forbinde, så lav fx `C:\Program Files\mosquitto\mosquitto.conf` med:

   ```
   listener 1883 0.0.0.0
   allow_anonymous true   # kun til lab
   ```

   Genstart tjenesten. Mosquitto 2.x er som udgangspunkt “local only”, så lytteren skal angives eksplicit. ([Eclipse Mosquitto][4], [Stack Overflow][5])

# macOS (Homebrew)

1. Installer Mosquitto:

   ```
   brew install mosquitto
   ```

   Standard-konfig ligger i `$HOMEBREW_PREFIX/etc/mosquitto/mosquitto.conf`. ([Homebrew Formulae][6])
2. Kør som launchd-service:

   ```
   brew services start mosquitto
   ```

   Alternativt kør i forgrund:

   ```
   mosquitto -c /opt/homebrew/etc/mosquitto/mosquitto.conf
   ```

   (Apple Silicon sti). ([slingacademy.com][7], [brittanyho.com][8])
3. Test i to terminaler:

   ```
   mosquitto_sub -t test/hello
   mosquitto_pub -t test/hello -m "hej"
   ```

   Se man-sider for flere flag. ([Eclipse Mosquitto][9])
4. Åbn for eksterne klienter hvis ønsket, i `.../mosquitto.conf`:

   ```
   listener 1883 0.0.0.0
   allow_anonymous true   # kun til lab
   ```

   Genstart service. macOS-firewall kan kræve tilladelse. ([Eclipse Mosquitto][4], [meshtastic.org][10])

# Ubuntu/Debian

1. Installer broker og klienter:

   ```
   sudo apt update
   sudo apt install mosquitto mosquitto-clients
   ```

   Pakkerne findes i de officielle repoer. ([Eclipse Mosquitto][1], [ubuntuupdates.org][11], [packages.ubuntu.com][12])
2. Aktiver og start service:

   ````
   sudo systemctl enable mosquitto
   sudo systemctl start mosquitto
   sudo systemctl status mosquitto
   ``` :contentReference[oaicite:9]{index=9}  
   ````
3. Test lokalt:

   ````
   mosquitto_sub -t test/hello
   mosquitto_pub -t test/hello -m "hej"
   ``` :contentReference[oaicite:10]{index=10}  
   ````
4. Tillad eksterne klienter ved behov i `/etc/mosquitto/conf.d/local.conf`:

   ```
   listener 1883 0.0.0.0
   allow_anonymous true   # kun til lab
   ```

   Genstart: `sudo systemctl restart mosquitto`. Mosquitto 2.x starter ellers kun på localhost. ([Eclipse Mosquitto][13])

# Hurtig Docker-vej

```
docker run -it -p 1883:1883 eclipse-mosquitto:2.0 mosquitto -c /mosquitto-no-auth.conf
```

Virker uden ekstra filer til lokal test. ([GitHub][14])

# Noter

* `allow_anonymous true` er kun til lab. Brug `password_file`, ACL og evt. TLS i drift. Se `mosquitto.conf` man-siden for valgmuligheder. ([Eclipse Mosquitto][4])
* CLI-værktøjerne `mosquitto_pub` og `mosquitto_sub` følger med og er gode til smoke-tests. ([Eclipse Mosquitto][3])
