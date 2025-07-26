# 🌐 Netværkssikkerhed – Ekstra modul: Analyse og sikring af HTTP REST-trafik

Dette modul fokuserer på, hvordan HTTP REST-baseret kommunikation analyseres og sikres i IoT-sammenhæng. Du lærer at identificere REST-kald i Wireshark, se hvordan data sendes i klartekst – og hvordan du sikrer det med HTTPS.

---

## 🔍 Del 1 – Analyse af ukrypteret HTTP

HTTP bruges ofte i REST-API’er til at kommunikere med sensorer, gateways eller cloud-tjenester. Det foregår typisk via TCP port 80 – uden kryptering.

### Eksempel på HTTP REST:

```http
GET /api/temp HTTP/1.1
Host: 192.168.1.50
```

Eller:

```http
POST /api/led HTTP/1.1
Host: 192.168.1.50
Content-Type: application/json

{"state": "on"}
```

### Analyse med Wireshark:

1. Start Wireshark og vælg din netværksinterface
2. Brug filter:

```wireshark
http
```

3. Find en GET eller POST-request og klik på den
4. Undersøg:

   * URL og metode (GET, POST...)
   * Headers (Host, Content-Type)
   * Payload (JSON eller tekst)

> 💡 Data kan aflæses direkte – både URI, parametre og body

---

## 🔐 Del 2 – Beskyttelse med HTTPS

HTTPS er HTTP med TLS (Transport Layer Security). Det krypterer hele forbindelsen, herunder URL-parametre og body.

### Effekt i Wireshark:

1. Forbindelse vises som "TLS" i stedet for "HTTP"
2. Du kan se handshake, men **ikke** payload eller headers
3. Brug filter:

```wireshark
tcp.port == 443
```

> 🛡️ HTTPS kræver certifikat på serveren – fx med Let’s Encrypt, self-signed eller cloud-løsning

---

## 📘 Sammenligning: HTTP vs. HTTPS

| Funktion              | HTTP (port 80) | HTTPS (port 443) |
| --------------------- | -------------- | ---------------- |
| URI og headers synlig | Ja             | Nej              |
| Body/payload synlig   | Ja             | Nej              |
| Risiko for MITM       | Høj            | Lav              |
| Krav om certifikat    | Nej            | Ja               |

---

## 🧪 Opgaver

### 🟢 Opgave 1 – Opsnap en HTTP REST-request

1. Brug fx Postman eller ESP32 til at sende HTTP-request til en lokal API
2. Start Wireshark og filtrér med `http`
3. Dokumentér:

   * URL og metode
   * Headers
   * Payload

### 🟠 Opgave 2 – Skift til HTTPS

1. Konfigurer en HTTPS-server (fx med Python Flask + certifikat)
2. Gentag samme request via `https://...`
3. Fang trafik i Wireshark med:

```wireshark
tcp.port == 443
```

4. Besvar:

   * Er nogen dele læsbare?
   * Hvordan bekræfter du, at TLS er aktivt?

### 🔵 Opgave 3 – Sammenlign

1. Sammenlign en HTTP-request og en HTTPS-request
2. Notér:

   * Læsbarhed af URI og data
   * Visning i Wireshark (HTTP vs. TLS)
   * Sikkerhedsforskel i praksis

---

📌 Brug dette modul til at forstå hvorfor REST-API’er skal køre over HTTPS – især i netværk med IoT-enheder, hvor adgang kan være bred og datatyper følsomme.
