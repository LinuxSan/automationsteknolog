# 🛠 Installationsguide – Wireshark (Linux)

Denne guide beskriver, hvordan du installerer og konfigurerer Wireshark korrekt på en Linux-distribution (Ubuntu/Debian-baseret), samt tester at netværksovervågning virker.

---

## 🐧 Trin 1 – Installer Wireshark via terminalen

Åbn en terminal og kør følgende kommandoer:

```bash
sudo apt update
sudo apt install wireshark
```

Under installationen bliver du spurgt:

> "Should non-superusers be able to capture packets?"
> Vælg **Ja**, så du ikke skal køre Wireshark som root.

---

## 👤 Trin 2 – Giv bruger adgang

Tilføj din bruger til `wireshark`-gruppen:

```bash
sudo usermod -aG wireshark $USER
```

> Log ud og log ind igen for at ændringerne træder i kraft.

---

## ✅ Trin 3 – Test installationen

1. Åbn Wireshark fra programmenu eller ved at skrive `wireshark` i terminalen
2. Du bør kunne se en liste over netværksinterfaces (fx `eth0`, `wlan0`, `enpXsY`)
3. Start pakkefangst ved at klikke på din aktive netværksforbindelse

---

## 🔍 Simpel test

1. Start fangst på dit aktive interface
2. Åbn din browser og besøg [https://www.example.com](https://www.example.com)
3. Stop fangsten og brug filter:

```wireshark
http
```

4. Du bør kunne se HTTP(S)-trafik og IP-adresser i listen

---

📌 Wireshark er nu klar til brug til netværksanalyse, IoT-inspektion og sikkerhedsøvelser.
