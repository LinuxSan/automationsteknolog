# 🐍 01 – Python for Automation: Data fra ESP32

Denne guide introducerer de grundlæggende Python-begreber, du skal bruge for at modtage og behandle data fra hardware som f.eks. en ESP32. Du lærer at skrive simple programmer på en PC, der kan aflæse og reagere på sensordata.

---

## 🔧 Indhold

* **PC'en som HMI/Datalogger**: Brug `print()` og `input()` til at vise status og sende kommandoer.
* **Sensordata**: Variabler og datatyper til at repræsentere målinger.
* **Kodeforståelse**: Kommentarer.
* **Fra PC til System**: Eksekvering af din kode.

---

## 📘 1. Vis status og data med `print()`

På PC'en bruges `print()` til at vise data, du modtager fra din ESP32, eller til at vise systemets status.

```python
print("Systemstatus: Klar. Venter på data fra ESP32...")
print("Modtaget temperatur: 24.5 C")
````

-----

## 📘 2. Send kommandoer med `input()`

Fra PC'en kan du sende simple kommandoer til dit system. `input()` pauser programmet og venter på, at du skriver en kommando i terminalen.

```python
kommando = input("Indtast kommando (start/stop): ")
print("Sender kommandoen:", kommando, "til ESP32.")
```

-----

## 📘 3. Repræsentation af sensordata med variabler

I automation arbejder vi med data fra den virkelige verden. Variabler gemmer disse data, så vi kan behandle dem.

```python
# Eksempler på data fra en ESP32
enheds_id = "ESP32_TEMP_01"  # Tekst (str) til at identificere enheden
temperatur = 24.5            # Decimaltal (float) fra en temperatursensor
tryk_bar = 1.013             # Decimaltal (float) fra en tryksensor
ventil_aaben = True          # Boolesk (bool) for at vise en tilstand (Åben/Lukket)
sensor_vaerdi_raw = 1023     # Heltal (int) direkte fra en Analog-Digital Converter (ADC)
```

**Vigtigt**: Python er dynamisk typet. Du skal ikke definere typen, men det er afgørende, at du ved, hvilken type data du arbejder med (f.eks. kan man ikke lave matematik på en `str`).

-----

## 📘 4. Forklar din kode med kommentarer

Kommentarer er essentielle for at forklare, hvad din kode gør, især når du arbejder med hardware.

```python
# Tjekker om ventilen til kølesystemet er aktiv
if ventil_aaben:
    print("Køling er aktiv.")
```

-----

## 🧪 Øvelse: Simuleret databehandling

Forestil dig, at din ESP32 sender en temperaturmåling som tekst via seriel porten. Din opgave er at lave et Python-program på din PC, der:

1.  **Modtager data**: Spørger brugeren om at indtaste den modtagne temperatur (vi simulerer her, at du modtager data).
2.  **Konverterer data**: `input()` læser alt som tekst (`str`). Du skal konvertere denne tekst til et tal (`float`), så du kan regne med det.
3.  **Behandler og viser data**: Udskriver en formateret sætning med den konverterede temperatur.

**Eksempel på kørsel:**

```text
Indtast modtaget temperatur fra ESP32: 26.8
Temperatur er konverteret til float: 26.8 grader Celsius.
```

**Tip**: Brug `float()` til at konvertere en streng til et decimaltal. F.eks. `tal_som_float = float("26.8")`.

-----

## ✅ Tjekliste

  - [ ] Jeg har brugt `print()` til at vise systemstatus.
  - [ ] Jeg forstår, hvordan variabler kan repræsentere sensordata (`float`, `int`, `bool`).
  - [ ] Jeg har skrevet et program, der bruger `input()` til at simulere modtagelse af data.
  - [ ] Jeg kan konvertere en `str` fra `input()` til en `float` for at kunne behandle dataene.

<!-- end list -->

```
```
