Her er et **cheat sheet** som du kan lægge direkte ind i opgaven (eller som separat fil), med **helt konkrete trin-for-trin-vejledninger** for både GNS3, Docker-images, IP-adressering og ping – uden at forudsætte Linux-erfaring.

---

```markdown
# 💡 Cheat sheet: Kom godt i gang med GNS3-netværk, IP-adresser og ping

## 1. Start GNS3 og opret et simpelt netværk

### A. Opret projekt
- Åbn GNS3
- Klik på **File → New blank project**
- Giv projektet et navn (fx “MitFørsteNetværk”)

### B. Tilføj noder (PC’er og switch)
- Klik på **Browse all devices** (eller “End devices”)
- Træk **2 x VPCS** (Virtual PC) ind på arbejdsområdet
- Træk en **Switch** ind (fx “Ethernet switch”)

### C. Forbind enhederne
- Vælg “Add a link” (lyn-ikon eller tryk på kabel-ikon)
- Klik på PC1 → Switch → PC2 → Switch
- Hver PC skal forbindes til switchets porte (fx port 1 og 2)

---

## 2. Indsæt og brug Docker images (fx Alpine Linux)

### A. Tilføj Docker-support til GNS3
- Vælg **Browse all devices** > **Docker Containers**
- Højreklik og vælg “New template” > “Pull a docker image”
- Søg fx på `alpine` (let Linux) eller `ubuntu`
- Følg anvisninger og træk den nye docker-node ind på arbejdsområdet

### B. Forbind Docker-node til netværk
- Forbind docker-containeren til switchen (på samme måde som PC’er)
- Start alle noder (tryk på den grønne “Play”-knap)

---

## 3. Tildel IP-adresser til VPCS (Virtual PC)

1. **Dobbeltklik** på PC1-ikonet for at åbne konsollen.
2. Skriv (fx til PC1):  
```

ip 192.168.1.10/24 192.168.1.1

```
- (Her tildeles IP 192.168.1.10, subnet 255.255.255.0, gateway 192.168.1.1 – gateway kan udelades for nu)
3. Skriv til PC2:  
```

ip 192.168.1.20/24 192.168.1.1

```

---

## 4. Tildel IP-adresser til Docker containers (Alpine/Ubuntu)

1. **Dobbeltklik** på docker-containeren for at åbne terminalen.
2. Skriv:  
```

ifconfig eth0 192.168.1.30 netmask 255.255.255.0 up

```
(eller på Ubuntu:  
```

ip addr add 192.168.1.30/24 dev eth0
ip link set eth0 up

```
)

---

## 5. Test netværksforbindelsen (ping)

- I **VPCS**-konsollen, skriv:  
```

ping 192.168.1.20

```
(Test fra PC1 → PC2)

- I **Docker** (alpine/ubuntu), skriv:  
```

ping 192.168.1.10

```
- **Hvis du får “Request timed out” eller ingen svar:**
- Tjek at begge enheder har korrekte IP-adresser og er på samme subnet
- Tjek at du har startet alle noder

---

## 6. Ekstra: Hvad sker der hvis…

- ...begge PC’er får samme IP?  
→ Ping fejler (IP-konflikt) – kun én svarer, eller netværket fejler.
- ...de er på forskellige subnet (fx .10 og .130)?  
→ Ping fejler – uden router/gateway kan de ikke “se” hinanden.

---

## 7. Screenshots

- **Windows/Mac:**  
- Windows: PrtScn eller “Snipping Tool”
- Mac: Shift+Cmd+4
- Gem dine screenshots og indsæt dem i din `.md`-fil sådan:  
```

![Mit netværk](mit-billede.png)

```

---

## 8. Hvis du sidder fast…

- Spørg en klassekammerat eller underviser – og skriv ned, hvad du forsøgte!
- Du kan altid “genstarte” en node eller slette forbindelsen og lave den igen.

---

**Denne cheat sheet må gerne gemmes, printes eller udvides med egne erfaringer!**
```

---
