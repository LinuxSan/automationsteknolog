# 🛡 Netværkssikkerhed – Afsnit 04: Beskyttelse og hardening

I dette afsnit lærer du at beskytte IoT-systemer mod netværksangreb og reducere risikoen for kompromittering. Fokus er på praktiske sikkerhedstiltag såsom netværkssegmentering, adgangskontrol, kryptering og overvågning.

---

## 🔐 Hvad betyder "hardening"?

Hardening betyder at gøre et system mere modstandsdygtigt over for angreb. Det handler om:

* At fjerne unødvendige services
* At sikre konfigurationer
* At begrænse adgangen

> 💡 IoT-enheder bør betragtes som potentielt usikre og adskilles logisk fra administrative systemer

---

## 🧱 Segmentering og adskillelse

Ved at dele netværket op i segmenter kan du begrænse, hvor langt en angriber kan nå.

| Teknik   | Beskrivelse                                    |
| -------- | ---------------------------------------------- |
| VLAN     | Virtuelle LAN til adskilte netværkszoner       |
| Subnet   | IP-baseret adskillelse af enheder              |
| Firewall | Filtrerer trafik mellem netværkszoner          |
| DMZ      | Netværksområde til gæster eller udefra enheder |

---

## 🔑 Adgangskontrol og autorisation

* Brug stærke adgangskoder (ikke admin/admin)
* Begræns hvem der må tilgå hvilke ressourcer
* Brug whitelist eller MAC-adressefiltrering
* Brug login-logning (hvem loggede på og hvornår)

---

## 📦 Kryptering og sikre protokoller

| Protokol | Anbefalet version            | Bemærkninger                   |
| -------- | ---------------------------- | ------------------------------ |
| MQTT     | MQTTS (port 8883 + TLS)      | Brug certifikat eller token    |
| HTTP     | HTTPS                        | Brug Let’s Encrypt ved cloud   |
| CoAP     | CoAPS (DTLS)                 | Understøtter PSK og certifikat |
| SSH      | Anvendes i stedet for Telnet | Krypteret fjernadgang          |

> ⚠️ Undgå klartekst-protokoller – brug TLS/DTLS hvor det er muligt

---

## 🕵️ Overvågning og logning

* Log alle login-forsøg, forbindelser og fejl
* Overvåg netværkstrafik (Wireshark, tcpdump, Zeek)
* Brug intrusion detection (fx Snort eller Suricata)
* Identificér usædvanlige mønstre og forbindelser

---

## ✅ Best practices

* Slå ubrugte services fra (fx webinterface)
* Skift standardindstillinger
* Hold firmware/software opdateret
* Brug fysisk adgangskontrol hvor muligt
* Sørg for backup og gendannelsesplaner

---

📌 Du har nu gennemført grundlaget for netværkssikkerhed i IoT. Brug det du har lært til at evaluere og sikre dine egne systemer – både i test og produktion.
