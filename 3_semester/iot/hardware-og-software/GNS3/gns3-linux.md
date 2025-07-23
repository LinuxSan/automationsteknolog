## 🐧 Installation af GNS3 og GNS3-VM med Libvirt (Linux)

Denne guide hjælper dig med at installere **GNS3** og **GNS3-VM** på en Linux-maskine ved hjælp af **QEMU/KVM** og **Libvirt** som virtualiseringsplatform. Denne metode undgår problemer relateret til BitLocker og TPM-nøgler, der ellers gør VMware eller VirtualBox uhensigtsmæssige på visse Linux-installationer.

---

### 🟢 Trin 1: Installer nødvendige pakker (Ubuntu/Debian)

Åbn en terminal og kør:

```bash
sudo apt update
sudo apt install gns3-gui gns3-server qemu-kvm libvirt-daemon-system virt-manager bridge-utils wireshark -y
```

> 💡 Under installationen kan du vælge at tilføje dig selv til `libvirt` og `wireshark` grupperne:

```bash
sudo usermod -aG libvirt $(whoami)
sudo usermod -aG wireshark $(whoami)
```

Genstart eller log ud og ind igen, for at ændringerne træder i kraft.

---

### 🟡 Trin 2: Download og klargør GNS3-VM

1. Gå til [https://www.gns3.com/software/download](https://www.gns3.com/software/download)
2. Download `GNS3-VM.ova` (seneste version)
3. Udpak `.ova` til `.qcow2` og `.vmx` vha. `tar`:

```bash
tar -xvf GNS3-VM.ova
```

4. Du skal bruge `.qcow2` filen (f.eks. `GNS3-VM-disk1.qcow2`)

---

### 🔵 Trin 3: Opret ny virtuel maskine i Virt-Manager

1. Start `virt-manager`
2. Klik `Create new virtual machine`
3. Vælg:

   * **Import existing disk image**
   * Brug `.qcow2` som disk
   * OS-type: `Linux` → `Ubuntu` eller `Generic` (virker fint)
4. Tildel ressourcer:

   * CPU: 2 kerner eller flere
   * RAM: 4096 MB eller mere
5. Netværk:

   * Brug "Bridged adapter" eller "Virtual network: NAT" (afhængigt af din konfiguration)
6. Navngiv VM: `GNS3-VM`
7. Klik "Finish" og boot maskinen

---

### 🟣 Trin 4: Konfigurer GNS3 GUI til Libvirt/QEMU

1. Start **GNS3** GUI
2. Gå til `Edit > Preferences > GNS3 VM`

   * ✅ Enable GNS3 VM
   * ⚙️ Platform: `QEMU`
   * ✅ VM name: `GNS3-VM`
   * Tjek at status viser "connected"
3. Alternativt, tilføj VM'en som en "Remote Server" med IP `127.0.0.1` og port `3080` hvis GUI ikke opdager den automatisk

---

### 🧪 Trin 5: Bekræft integrationen

1. GNS3 GUI skal vise: "GNS3 VM (connected)"
2. Du kan nu importere appliances og køre dem via Libvirt/QEMU

---

### 📦 Trin 6: Tilføj appliances (Cisco IOS, Docker, etc.)

1. Gå til `File > Import Appliance`
2. Vælg `.gns3a`-fil
3. Følg guiden og tilknyt relevante image-filer

---

### 🛑 Afslutning og administration

* Stop GNS3-VM fra Virt-Manager når du lukker GUI
* Brug `virsh` CLI til at styre VM'er, hvis du ikke bruger GUI

---

### 🎯 Klar til brug!

Du har nu GNS3 og GNS3-VM kørende på Linux med Libvirt/QEMU – en hurtig, sikker og TPM/uafhængig løsning. Perfekt til undervisning, certificeringslab og avanceret netværkssimulering. ✅
