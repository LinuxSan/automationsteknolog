# 🧪 Opgaver – CoAP 01: Grundbegreber

Disse opgaver introducerer dig til brugen af CoAP i praksis. Du tester hvordan klient og server kommunikerer, og reflekterer over fordele og ulemper ved protokollen i forhold til fx HTTP og MQTT.

---

## 🟢 Opgave 1 – Send en CoAP GET-anmodning

1. Installer CoAP-klientværktøj (fx [Copper](https://addons.mozilla.org/en-US/firefox/addon/copper-coap/) til Firefox eller `aiocoap` i terminalen)
2. Find IP på en testserver (eller start en lokal med fx `aiocoap-proxy`)
3. Send GET-anmodning:

```bash
aiocoap-client coap://localhost/temp
```

4. Observer svaret (fx temperaturværdi)

✅ *Forbindelsen etableres, og svar returneres korrekt*

---

## 🔵 Opgave 2 – Sammenlign CoAP og HTTP

1. Brug Postman eller `curl` til at anmode om HTTP-data fra en REST-server
2. Sammenlign med CoAP-anmodning:

   * Hvilken bruger flest ressourcer (trafik, tid)?
   * Hvilken håndterer fejl bedst?
3. Notér forskelle i protokol, port, pakkeformat og respons

✅ *Beskriv fordele og ulemper ved hver metode*

---

## 🟡 Opgave 3 – Observer UDP-adfærd

1. Brug Wireshark til at sniffe trafik mens du laver CoAP GET
2. Identificér UDP-pakker, port 5683
3. Tjek retransmission og CON/ACK-forløb (bekræftede pakker)

✅ *Få indsigt i hvor lidt overhead CoAP bruger i forhold til HTTP*

---

## 🔁 Opgave 4 – Anvend NON vs CON pakker

1. Brug CoAP-klient til at sende NON-request (ikke bekræftet)
2. Gentag med CON-request (bekræftet)
3. Fjern forbindelsen midt i CON og observer retransmission

✅ *Diskutér: Hvornår bør man bruge NON? Hvornår er CON nødvendigt?*

---

## 🧠 Refleksion

* Hvordan adskiller CoAP sig fra MQTT og HTTP?
* Hvilke typer IoT-enheder er CoAP særligt velegnet til?
* Hvordan håndterer CoAP netværksfejl og begrænsninger?

---

📌 Du har nu testet CoAP’s grundlæggende funktioner, og kan vurdere dets egnethed til forskellige IoT-scenarier.
