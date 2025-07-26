# 🛠 Installationsguide – Wireshark (macOS)

Denne guide hjælper dig med at installere og konfigurere Wireshark korrekt på en Mac-computer, samt verificere at den kan overvåge netværkstrafik.

> ⚠️ Wireshark er **ikke** tilgængelig som app til iOS (iPhone/iPad), men kan installeres på macOS.

---

## 🍏 Trin 1 – Download og installer Wireshark

1. Gå til den officielle hjemmeside:
   [https://www.wireshark.org/download.html](https://www.wireshark.org/download.html)
2. Vælg **macOS 64-bit Intel** eller **Apple Silicon (ARM64)** afhængigt af din Mac
3. Download `.dmg`-filen og åbn den
4. Træk **Wireshark** over i **Programmer**-mappen

---

## 🔧 Trin 2 – Tilladelser til netværksadgang

1. Kør installationspakken `Install ChmodBPF.pkg` inde i `.dmg`-vinduet
2. Følg installationsvejledningen og godkend med din administratoradgangskode
3. Dette giver Wireshark tilladelse til at læse netværksinterfaces

---

## ✅ Trin 3 – Test at Wireshark virker

1. Åbn **Wireshark** fra Launchpad eller Programmer
2. Du skal kunne se en liste over netværksinterfaces som `en0` (Wi-Fi), `en1`, `lo0` osv.
3. Vælg dit aktive interface og tryk **Start** for at begynde at fange pakker

---

## 🔍 Simpel test

1. Start fangst på fx `en0`
2. Åbn en browser og gå til [https://www.example.com](https://www.example.com)
3. Stop fangsten og filtrér med:

```wireshark
ip.addr == 93.184.216.34
```

4. Bekræft at du kan se trafik til/fra websiden

---

📌 Du er nu klar til at bruge Wireshark til netværksovervågning og IoT-analyse på macOS.
