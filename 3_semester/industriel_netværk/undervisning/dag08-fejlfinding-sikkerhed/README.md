# 🛡️ Dag 08 – Fejlfinding & Netværkssikkerhed

Velkommen til dag 8 af Industrielt Netværk!

> I dag får du trænet fejlfinding på industrielle netværk – og lærer, hvordan man beskytter OT-udstyr mod angreb og fejl. Vi arbejder især i GNS3, men bruger også dokumentation og cases.

---

## 🎯 Læringsmål for dagen

- Forstå grundprincipper i OT-netværkssikkerhed (fx firewall, segmentering, ACL)
- Udføre fejlfinding på netværk (ping, traceroute, fysisk/logisk analyse)
- Identificere og håndtere almindelige fejlsituationer (IP-konflikt, forkert VLAN, gateway-problemer)
- Dokumentere fejl og løsninger systematisk

---

## 📚 Dagens indhold

- **Mini-forelæsning:**  
  - Netværkssikkerhed: Hvorfor er OT mere sårbart end IT?
  - Firewalls, access control, fysisk adskillelse
  - Fejlfinding: Metoder og værktøjer i praksis (ping, traceroute, netværksdiagrammer)
- **Cases og hands-on i GNS3:**  
  - Lav bevidste fejl (forkert subnet, dobbelte IP’er, defekt kabel, fejl i VLAN)
  - Konfigurér og test firewall/regler og adgangskontrol
  - Dokumentér fejl og løsning

---

## 🛠️ Opgaver

| #   | Titel                       | Type      | Aflevering           |
|-----|-----------------------------|-----------|----------------------|
| 1   | Fejlfinding i GNS3          | Individuel/gruppe | `.md` + screenshots/diagrammer |
| 2   | Firewall & ACL konfiguration| Individuel/gruppe | `.md` + config/skærmbilleder  |
| 3   | Dokumentér fejl og løsning  | Individuel | `.md` (skema)        |

Dokumentér alt i en undermappe med dit navn (eller gruppe) under `dag08-fejlfinding-sikkerhed`.

---

## 💾 Ressourcer

- [OT-netværkssikkerhed: Intro (pdf, dansk)](https://www.industriensnetvaerk.dk/wp-content/uploads/2021/01/Industrielt-netvaerk-og-sikkerhed.pdf)
- [GNS3: Simulering af firewalls](https://gns3.com/tech/firewall-simulation)
- [Ping & Traceroute – Hurtig guide](https://www.cloudflare.com/learning/network-layer/what-is-ping/)

---

## 📝 Afleveringsguide

1. Opret mappe: `dag08-ditnavn` eller `dag08-gruppeX`
2. Løs alle opgaver, dokumentér fejl og løsninger med tekst og screenshots
3. Lav evt. en oversigt (tabel/skema) over fejltyper og hvordan de blev fundet/løst
4. Push til GitHub senest før næste undervisningsgang

> Husk: Jo bedre du dokumenterer dine fejl og løsninger, desto nemmere er det for andre (og dig selv!) at forstå netværket.

---

## ❓ FAQ

- **Må vi arbejde i grupper?**  
  Ja – men alle skal bidrage til dokumentation.
- **Hvordan viser jeg en firewall-konfiguration?**  
  Brug screenshots fra GNS3, kopier konfigurationskode, eller upload et billede af dit setup.
- **Hvad gør jeg hvis jeg ikke kan finde en fejl?**  
  Beskriv hvordan du ledte, og hvad du forsøgte. Spørg underviser eller gruppen.

---

Held og lykke med fejlfinding og sikkerhed – det er her du lærer at redde produktionen! 🦺🔐
