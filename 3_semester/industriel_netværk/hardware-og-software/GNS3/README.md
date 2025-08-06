## 🌐 Introduktion til installation af GNS3 og GNS3-VM

**GNS3** (Graphical Network Simulator 3) er et avanceret netværkssimuleringsværktøj, der anvendes af både studerende og professionelle til at bygge, teste og simulere komplekse netværkstopologier. For at få det fulde udbytte af GNS3 anbefales det at bruge **GNS3-VM** – en virtuel maskine, der håndterer tunge processer og giver bedre ydeevne og stabilitet.

Denne introduktion forklarer overordnet:

* Hvad GNS3 og GNS3-VM er
* Hvorfor du bør installere begge
* Hvad du skal bruge før installationen
* Hvad du kan forvente at lære og bruge det til

---

### 🧠 Hvad er GNS3?

* Et gratis og open source grafisk værktøj til netværkssimulering
* Gør det muligt at kombinere **virtuelle enheder (f.eks. Cisco IOS, Juniper, MikroTik)** med **reelle netværkselementer**
* Bruges til **certificeringsforberedelse (CCNA, CCNP, etc.)**, undervisning og testlab

---

### 🖥️ Hvad er GNS3-VM?

* En **Virtual Machine (VM)** der kører GNS3's backend-processer
* Kan bruges med **VMware Workstation/Player**, **VirtualBox** eller **Hyper-V**
* Offloader tunge funktioner fra din host-maskine og sikrer bedre ydeevne
* Kræves til at bruge dynamiske komponenter som **Dynamips, QEMU, IOU, Docker** m.m.

---

### ✅ Hvorfor bruge GNS3-VM?

* Bedre ydeevne og skalerbarhed
* Flere funktioner bliver tilgængelige (Docker, L2/L3 switching, m.m.)
* Mere stabilitet ved simuleringer
* Lettere integration med reelle netværk

---

### 🧰 Hvad skal du bruge før du går i gang?

* **En kraftig maskine (mindst 8 GB RAM anbefales, helst 16+)**
* **Virtualiseringssoftware** (VMware eller VirtualBox anbefales)
* **Download af GNS3 GUI og GNS3-VM** fra [https://www.gns3.com/software/download](https://www.gns3.com/software/download)
* Evt. **Cisco IOS-imagefiler** eller appliance-skabeloner

---

### 📦 Hvad indeholder installationsprocessen typisk?

1. Installation af GNS3 GUI (grafisk brugerflade)
2. Installation og import af GNS3-VM i din virtualiseringsplatform
3. Konfiguration af forbindelsen mellem GNS3 og GNS3-VM
4. Test af forbindelse og netværksenheder

---

### 🎯 Hvad kan du bruge det til bagefter?

* Opsætning og test af netværkstopologier
* Forberedelse til netværkscertificeringer (Cisco, CompTIA, Juniper m.fl.)
* Undervisning og træning i routing, switching, firewall, VPN, m.m.
* Integration med Docker og andre virtuelle platforme

---

📘 I næste trin vil du få en guide til, hvordan du installerer GNS3 GUI og GNS3-VM på netop din platform (Windows/macOS/Linux).

🔗 Husk at oprette en gratis brugerprofil på GNS3.com for at få adgang til download og appliance-marked.
