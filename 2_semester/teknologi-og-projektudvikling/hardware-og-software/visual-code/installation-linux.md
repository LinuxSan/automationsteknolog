# 🐧 Installation af Visual Studio Code på Linux

Denne guide viser, hvordan du installerer Visual Studio Code og konfigurerer det til Python-udvikling på en Linux-maskine (Ubuntu/Debian-baseret).

---

## 🧰 Forudsætninger

* Linux-distribution (fx Ubuntu 20.04+, Debian 11+)
* Terminaladgang med sudo-rettigheder
* Internetforbindelse

---

## 1️⃣ Tilføj Microsofts repository og GPG-nøgle

Åbn terminalen og kør følgende kommandoer:

```bash
sudo apt update
sudo apt install wget gpg

wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/

sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
```

---

## 2️⃣ Installer VS Code

```bash
sudo apt update
sudo apt install code
```

Dette installerer Visual Studio Code som grafisk applikation.

---

## 3️⃣ Start VS Code

Du kan starte programmet ved at skrive:

```bash
code
```

Eller finde det i din programmenu som “Visual Studio Code”.

---

## 4️⃣ Installer Python (hvis det ikke allerede er installeret)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

Bekræft installation:

```bash
python3 --version
```

---

## 5️⃣ Tilføj Python-understøttelse i VS Code

1. Start VS Code
2. Gå til Extensions (venstre sidebar)
3. Søg efter **Python** og vælg den fra Microsoft
4. Klik på **Install**
5. (Valgfrit) Installer **Pylance** for bedre IntelliSense

---

## 6️⃣ Test din installation

1. Opret en ny mappe og fil:

```bash
mkdir ~/projekter/teknologi
cd ~/projekter/teknologi
code hello.py
```

2. Skriv følgende i `hello.py`:

```python
print("Hej fra Linux og VS Code!")
```

3. Kør filen via terminal:

```bash
python3 hello.py
```

---

## ✅ Klar til brug!

Visual Studio Code og Python er nu installeret på dit Linux-system og klar til databehandling, analyse og programmering.

> Tip: Tilføj Git og konfigurer VS Code til versionsstyring, hvis du arbejder med GitHub.

Kontakt underviser hvis du har problemer undervejs.
