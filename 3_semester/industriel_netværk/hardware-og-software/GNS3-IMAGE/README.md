# 🚀 Guide: Få **ITiFN PC** og **ITiFN Router** ind i dit GNS3-projekt

> Ingen lokale filer krævet. GNS3 henter images direkte fra Docker Hub:
>
> * `docker.io/sandoe/itifn-pc:1.0`
> * `docker.io/sandoe/itifn-router:1.0`

---

## 🧰 Forudsætninger

* **GNS3 GUI** + **GNS3 VM** aktiveret
  *Hvorfor:* På Windows og macOS kører Docker-noder inde i GNS3 VM. VM’en pull’er selv images fra Docker Hub.
* **Internetadgang i GNS3 VM**
  *Hvorfor:* Uden internet kan VM’en ikke hente images.

Tjek: `Edit → Preferences → GNS3 VM → Enable`.
Tjek også `Edit → Preferences → Docker → Docker preferences → Use the GNS3 VM`.

---

## 🏷️ 1) Opret Docker-templates i GNS3 (én gang)

Templates gør det nemt at genbruge samme image i mange projekter.

### 🖥️ ITiFN PC (generel Linux host)

1. `Edit → Preferences → Docker → Docker containers → New`
2. **Name:** `ITiFN PC`
3. **Image:** `docker.io/sandoe/itifn-pc:1.0`
   *Forklaring:* Public image på Docker Hub. GNS3 VM henter det automatisk.
4. **Number of adapters:** `2`
   *Forklaring:* To NICs rækker til de fleste basisøvelser.
5. **Console type:** `None`
6. **Start command:** `bash`
   *Forklaring:* Du lander i en shell, når du åbner Console.
7. **Run as privileged:** `Off`
   *Forklaring:* PC-noden kræver typisk ikke ekstra kernel-rettigheder.
8. **Finish → Apply**

### 🧩 ITiFN Router (Linux router)

1. `Edit → Preferences → Docker → Docker containers → New`
2. **Name:** `ITiFN Router`
3. **Image:** `docker.io/sandoe/itifn-router:1.0`
4. **Number of adapters:** `4`
   *Forklaring:* Flere interfaces til WAN/LAN/VLAN øvelser.
5. **Console type:** `None`
6. **Start command:** `bash`
7. **Run as privileged:** `On`
   *Forklaring:* Router-imaget bruger net-capabilities og sysctl. Kræver privileged i GNS3.
8. **Finish → Apply**

---

## 🧪 2) Brug templates i et projekt

1. `File → New blank project → OK`
2. Træk **ITiFN PC** og **ITiFN Router** ind fra venstrepanelet under **Docker**.
3. Højreklik hver node → **Start**
4. Højreklik → **Console** for at åbne terminalen i noden.

**Hurtig verifikation i Console**

```bash
uname -a            # viser at du er inde i containeren
ip -br link         # viser interfaces (eth0, eth1, …)
```

På **Router** må `privileged` være slået til, ellers kan enkelte net-funktioner fejle.

---

## 🛠️ Fejlfinding

* ❗**“pull access denied” / “not found”**
  Brug præcis stavning og tag:
  `docker.io/sandoe/itifn-pc:1.0` og `docker.io/sandoe/itifn-router:1.0`.
  Er repo privat, kræver det Docker Hub-login inde i GNS3 VM.

* ❗**GNS3 VM henter ikke image**
  Tjek internet i VM’en:
  `ping -c 3 1.1.1.1` og `ping -c 3 registry-1.docker.io` i VM-konsollen.
  Tjek også at **Docker Engine = Use the GNS3 VM**.

* ❗**Template vises ikke i venstrepanelet**
  Du har kun oprettet den i Preferences. Genåbn projektet eller tryk **Refresh** i venstrepanelet.

* ❗**“repository name must be lowercase”**
  Alle dele af image-navnet skal være små bogstaver.

* ❗**Console åbner, men ingen net-interfaces**
  Start noderne før Console. Tjek `ip -br link`. På Router: bekræft `privileged = On` i templaten.

---

## 🔄 Opdateringer

Når der kommer en ny version, fx `:1.1`:

* Skift **Image** i templaten til `docker.io/sandoe/itifn-pc:1.1` eller `docker.io/sandoe/itifn-router:1.1`.
* Start nye noder fra templaten i dine projekter.

---

## 🧾 Kopi-ark (til hurtig indtastning)

**PC template**

* Name: `ITiFN PC`
* Image: `docker.io/sandoe/itifn-pc:1.0`
* Adapters: `2`
* Console: `None`
* Start command: `bash`
* Privileged: `Off`

**Router template**

* Name: `ITiFN Router`
* Image: `docker.io/sandoe/itifn-router:1.0`
* Adapters: `4`
* Console: `None`
* Start command: `bash`
* Privileged: `On`

---

✅ **Resultat:** De studerende kan nu tilføje både **PC** og **Router** til ethvert GNS3-projekt uden lokale filer. GNS3 VM henter images automatisk fra Docker Hub, og Console giver direkte adgang til bash i hver node.
