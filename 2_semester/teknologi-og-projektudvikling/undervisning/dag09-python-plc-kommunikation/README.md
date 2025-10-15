
# Dag 09 – Python ⇄ Siemens S7 med snap7

> Teknologi & Projektudvikling · 2. semester · 5 ECTS
> **Tema:** Dataudveksling og styring via Ethernet mellem Python‑applikation og Siemens S7‑PLC (S7‑1200/1500).

---

## 🔍 Formål

På denne dag lærer du at etablere en **pålidelig TCP/IP‑forbindelse** til en Siemens S7‑PLC, læse og skrive databaser (DB‑områder) samt logge og udstille procesdata i realtid med Python‑biblioteket **snap7**.

---

## 🎯 Læringsmål

Efter dagen kan du

1. Installere og konfigurere Python‑pakken `python‑snap7` på Windows og Linux
2. Forstå PLC‑adressemodeller: DB‑nummer, byte/bit‑offset og datatyper (BOOL, INT, REAL, STRING)
3. Oprette en klientforbindelse (`snap7.client.Client`) og håndtere tilslutningsfejl
4. Læse rå byte‑blokke fra PLC‑data­blokke og pakke dem til Python‑typer via `snap7.util`
5. Skrive værdier tilbage til PLC‑DB’er med korrekt type‑konvertering
6. Opbygge et simpelt logger‑script, der gemmer udvalgte procesvariabler til CSV hvert sekund
7. Dokumentere opsætning, netværks­parametre (IP, rack, slot) og push til GitHub

---

## 🧰 Forudsætninger

| Fra dag | Viden/artefakt                          | Anvendelse i Dag 09            |
| ------: | --------------------------------------- | ------------------------------ |
|   02‑04 | Grundlæggende Python‑miljø & VS Code    | Script‑udvikling & virtual env |
|   06‑08 | Pandas + CSV‑logging                    | Gemme procesdata               |
| PLC‑lab | Adgang til S7‑1200/1500 med TIA‑projekt | Testforbindelse                |

---

## 🗓️ Lektionsplan

| Slot | Tid           | Opgave                                          | Læringsmål | Artefakt             |
| ---- | ------------- | ----------------------------------------------- | ---------- | -------------------- |
| 1    | 08:30 – 09:15 | **Opgave 01 – snap7‑Installation & Smoke‑test** | 1          | `01-installation.md` |
| 2    | 09:15 – 10:30 | **Opgave 02 – PLC‑Connect & Read BOOL/INT**     | 2‑4        | `02-plc-read.md`     |
| 3    | 10:45 – 12:00 | **Opgave 03 – Real‑time Logger til CSV**        | 4‑6        | `03-logger.md`       |
| 4    | 13:00 – 14:15 | **Opgave 04 – Skriv Set‑points til PLC**        | 2‑5        | `04-plc-write.md`    |
| 5    | 14:30 – 15:30 | **Opgave 05 – Mini‑Dashboard (CLI eller Web)**  | 4‑7        | `05-dashboard.md`    |

*(Tidsangivelser kan justeres af underviser efter behov.)*

---

## 📦 Aflevering

* Repo‑struktur:

  ```text
  dag09-snap7/
  ├── 01-installation.md
  ├── 02-plc-read.md
  ├── 03-logger.md
  ├── 04-plc-write.md
  ├── 05-dashboard.md
  ├── src/
  │   ├── connect.py
  │   ├── logger.py
  │   └── write_demo.py
  └── README.md   ← (denne fil)
  ```
* Inkludér `.env.example` med IP, rack, slot – **uden** at committe faktiske adgangsoplysninger.
* Mindst én Pull Request med peer‑review før merge.

---

## ✅ Checkliste

* [ ] `python‑snap7` installeret og import‑test kører
* [ ] Log‑script gemmer CSV med tid, procesværdi, enhed
* [ ] PLC‑setpoint script skriver værdi uden fault bit i TIA
* [ ] README opdateret med netværksopsætning, kørsel & læring
* [ ] Kode følger PEP 8 og fungerer både på Windows og Linux

---

*Tip:* Brug `snap7.util.get_real` / `set_real` for flydende værdier og `snap7.util.get_bool` til bit‑flags. Husk at PLC‑ og Python‑endianness kan være forskellig!\*
