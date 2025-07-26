# 🛠 Installationsguide – Wireshark (Windows)

Denne guide hjælper dig med at installere Wireshark korrekt på en Windows-computer og teste, at det virker til netværksovervågning.

---

## 💾 Trin 1 – Download Wireshark

1. Gå til den officielle hjemmeside:
   [https://www.wireshark.org/download.html](https://www.wireshark.org/download.html)
2. Klik på **Windows Installer (64-bit)** og download `.exe`-filen

---

## 🔧 Trin 2 – Installer Wireshark

1. Dobbeltklik på den downloadede fil
2. Under installationen:

   * Accepter licensbetingelser
   * **Vælg at installere Npcap**, når du bliver spurgt (vigtigt for at fange trafik)
   * Lad alle standardkomponenter være aktiveret (TShark, USBPcap er valgfri)
   * Aktiver: *Install Npcap in WinPcap API-compatible Mode* (anbefales)
3. Afslut installationen og genstart computeren, hvis du bliver bedt om det

---

## ✅ Trin 3 – Test at Wireshark virker

1. Start Wireshark (brug søgefeltet i Start-menuen)
2. Du skal kunne se en liste over netværksinterfaces (Wi-Fi, Ethernet, etc.)
3. Klik på den aktive forbindelse (fx Wi-Fi)
4. Når pakkefangst starter, skal du se pakker i realtid

### 🔍 Simpel test

1. Start Wireshark og begynd pakkefangst
2. Åbn din browser og gå til fx [https://www.example.com](https://www.example.com)
3. Du bør nu kunne se trafik i Wireshark
4. Stop fangst og brug filteret:

```
ip.addr == 93.184.216.34
```

5. Bekræft at du kan se trafik relateret til websiden

---

📌 Du er nu klar til at bruge Wireshark til netværksanalyse i undervisningsøvelser og sikkerhedstest.
