# 🐧 Installation af Thonny på Linux (Ubuntu/Debian)

Thonny er en begyndervenlig Python IDE, som er ideel til undervisning. Denne guide dækker installation på Linux-systemer – især Ubuntu eller Debian-baserede distributioner.

---

## 🧰 Forudsætninger

* En Linux-distribution med apt (fx Ubuntu 20.04+, Debian 11+)
* Terminaladgang med sudo-rettigheder

---

## 1️⃣ Installation via terminal (APT)

Åbn terminalen og kør følgende:

```bash
sudo apt update
sudo apt install thonny
```

Dette installerer både Thonny og den nødvendige Python-version.

---

## 2️⃣ Start Thonny

1. Find Thonny i din programmenu og åbn det, eller skriv i terminalen:

```bash
thonny
```

2. Ved første opstart kan du vælge sprog (f.eks. **Dansk** eller **English**)
3. Vælg Python-kørselsmiljø:

   * Brug **standardmiljøet**, medmindre du har installeret andre versioner

---

## 3️⃣ Test din installation

1. Skriv følgende i editorvinduet:

```python
print("Hej fra Thonny på Linux!")
```

2. Tryk `F5` eller klik på den grønne **Run**-knap
3. Se output i konsolvinduet nederst

---

## 🛠 Tips

* Gem din kode med `.py`-endelse: `gem_som.py`
* Brug `Vis > Filer` for at få overblik over dine projektmapper
* Installer ekstra pakker med pip, f.eks.:

```bash
pip3 install pandas matplotlib
```

---

## ✅ Klar til brug!

Thonny er nu installeret og konfigureret til Python-programmering på Linux.

> Spørg underviser ved problemer med installation eller ved brug af pip/moduler.
