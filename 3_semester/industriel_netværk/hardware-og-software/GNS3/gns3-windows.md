## 🛠️ Installation af GNS3 og GNS3-VM med VMware (Windows)

Denne guide hjælper dig med at installere **GNS3** og **GNS3-VM** på en **Windows-maskine** med brug af **VMware Workstation Player**. Dette setup anbefales til performance og avancerede funktioner som QEMU, Docker og L2/L3 netværksvirtualisering.

---

### 🟢 Trin 1: Download nødvendige filer

1. Gå til [https://www.gns3.com/software/download](https://www.gns3.com/software/download)
2. Download:

   * ✅ GNS3 Windows installer (f.eks. `GNS3-2.x.x-all-in-one.exe`)
   * ✅ GNS3-VM til VMware (`GNS3-VM.ova`)

> Du skal have en gratis GNS3-konto for at kunne downloade filerne.

---

### 🟡 Trin 2: Installer VMware Workstation Player

1. Gå til [https://www.vmware.com/products/workstation-player.html](https://www.vmware.com/products/workstation-player.html)
2. Vælg "Download Now" til Windows
3. Installer med standardindstillinger
4. Genstart hvis nødvendigt

> 📝 VMware Workstation Pro virker også, men denne guide tager udgangspunkt i gratisversionen.

---

### 🔵 Trin 3: Installer GNS3 GUI

1. Kør `GNS3-2.x.x-all-in-one.exe`
2. Installér alle standardkomponenter (inkl. Wireshark, Npcap, Dynamips, Solar-PuTTY m.fl.)
3. Accepter firewall-regler og slutinstallation

---

### 🟣 Trin 4: Importer GNS3-VM i VMware

1. Åbn **VMware Workstation Player**
2. Gå til `Player > File > Open...`
3. Vælg den `.ova`-fil du downloadede (GNS3-VM.ova)
4. Vælg navn og placering og klik "Import"
5. Tildel mindst:

   * 2 CPU-kerner
   * 4 GB RAM
   * Netværk: vælg "Bridged" eller "Host-only" (vigtigt for forbindelse til GUI)

---

### ⚙️ Trin 5: Konfigurer GNS3 GUI til at bruge GNS3-VM

1. Start **GNS3 GUI**
2. Vælg:

   * ✅ "Run appliances in a virtual machine (GNS3 VM)"
3. Gå til `Edit > Preferences > GNS3 VM`

   * Enable GNS3 VM: ✔️
   * Virtualization engine: `VMware Workstation`
   * VM name skal matche navnet fra VMware Player
   * Klik "Test Settings" – alt skal blive grønt

---

### 🧪 Trin 6: Bekræft forbindelse

1. Start GNS3 GUI
2. GNS3-VM starter automatisk i VMware
3. Bekræft i GUI at der står "GNS3 VM (connected)"

---

### 📦 Trin 7: Importér appliances

1. Gå til `File > Import Appliance`
2. Vælg en `.gns3a`-fil fra GNS3 Marketplace
3. Følg guiden og angiv de nødvendige image-filer (fx Cisco IOS)

---

### 🧹 Trin 8: Administration og tips

* Luk GNS3 GUI for automatisk at slukke GNS3-VM
* Brug "Tools > Docker support" hvis du har installeret Docker Desktop
* Tjek CPU/RAM-forbrug i VMware og tilpas efter behov

---

### 🎯 Klar til brug!

Du har nu en komplet opsætning med **GNS3 GUI** og **GNS3-VM** kørende på **Windows** med **VMware**. Du er klar til at simulere komplekse netværk med høj stabilitet og ydeevne. ✅
