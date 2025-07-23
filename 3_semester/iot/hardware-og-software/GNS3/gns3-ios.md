## 🍏 Installation af GNS3 og GNS3-VM med VMware på macOS

Denne guide hjælper dig med at installere **GNS3** og **GNS3-VM** på **macOS** ved brug af **VMware Fusion**, som er en virtualiseringsløsning til Mac. Denne metode er velegnet til netværksrelaterede simuleringer og giver høj ydeevne med god integration til GNS3 GUI.

---

### 🟢 Trin 1: Forberedelse

1. Sørg for, at du har en moderne Mac med:

   * Min. 8 GB RAM (helst 16 GB eller mere)
   * Virtualisering aktiveret (gælder især Intel-baserede Mac)

2. Opret en gratis konto på: [https://www.gns3.com](https://www.gns3.com)

---

### 🟡 Trin 2: Download nødvendige komponenter

1. GNS3 GUI til macOS:
   [https://www.gns3.com/software/download](https://www.gns3.com/software/download)

2. GNS3 VM (.ova):
   Samme side – vælg seneste version

3. VMware Fusion Player (gratis til ikke-kommerciel brug):
   [https://customerconnect.vmware.com](https://customerconnect.vmware.com)

   * Vælg Fusion Player for macOS (Intel/Apple Silicon afhængig af din Mac)

---

### 🔵 Trin 3: Installer GNS3 GUI

1. Åbn den downloadede `.dmg`-fil
2. Træk GNS3-ikonet til `Applications`
3. Start GNS3 for at sikre, at det åbner korrekt (bekræft adgang til netværk m.m.)

---

### 🟣 Trin 4: Installer og importer GNS3-VM i VMware Fusion

1. Åbn VMware Fusion og vælg `Import...`
2. Vælg `.ova`-filen (`GNS3-VM.ova`)
3. Vælg navn og placering
4. Justér ressourceallokering:

   * CPU: 2+ kerner
   * RAM: min. 4 GB
   * Netværk: NAT eller Bridged (brug NAT, hvis du er i tvivl)
5. Importér og start VM’en for at sikre, at den booter korrekt

---

### ⚙️ Trin 5: Forbind GNS3 GUI med GNS3-VM

1. Start GNS3 GUI
2. Vælg:

   * ✅ "Run appliances in a virtual machine (GNS3 VM)"
3. Gå til `GNS3 > Preferences > GNS3 VM`

   * Enable GNS3 VM ✔️
   * Virtualization engine: `VMware`
   * VM name: skal matche navnet i Fusion (fx `GNS3-VM`)
   * Klik "Test Settings" – status skal være grøn

---

### 🧪 Trin 6: Test integration

1. Start GNS3 GUI og vent på, at GNS3-VM starter i VMware Fusion
2. GUI bør vise "GNS3 VM (connected)"
3. Du kan nu tilføje appliances og starte simuleringer

---

### 📦 Trin 7: Importér en appliance

1. Gå til `File > Import Appliance`
2. Vælg en `.gns3a`-fil (fx Cisco IOS, OpenWRT, VyOS, Docker)
3. Følg guiden og upload evt. `.bin` eller `.img`-filer

---

### 🛑 Tips og administration

* Luk GNS3 GUI → GNS3-VM lukkes automatisk
* Justér CPU/RAM i Fusion hvis GNS3-VM kører langsomt
* Brug NAT netværk hvis du oplever problemer med bridged

---

### 🎯 Klar til brug!

GNS3 og GNS3-VM er nu korrekt installeret og forbundet på din Mac med VMware Fusion. Du kan nu begynde at opbygge avancerede netværk, træne til certificeringer og simulere komplekse setups direkte i macOS. ✅
