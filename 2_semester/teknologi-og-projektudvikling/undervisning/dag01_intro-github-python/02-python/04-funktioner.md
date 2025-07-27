# 🧮 04 – Funktioner i Python

Funktioner er en grundsten i al programmering. De hjælper dig med at genbruge kode, skabe overblik og organisere dine programmer i mindre bidder. I denne guide lærer du at skrive dine egne funktioner og bruge dem effektivt.

---

## 🔧 Indhold

* Hvad er en funktion?
* `def` og `return`
* Parametre og argumenter
* Lokale variabler
* Brug af funktioner i praksis

---

## 📘 1. Hvad er en funktion?

En funktion er en blok af kode, som du kan kalde (starte), når du har brug for den. Det svarer til en maskine med input og output.

---

## 📘 2. Sådan definerer du en funktion

```python
def sig_hej():
    print("Hej med dig!")
```

Du kalder funktionen ved at skrive dens navn efterfulgt af `()`:

```python
sig_hej()
```

---

## 📘 3. Funktion med parametre

```python
def hils(navn):
    print("Hej", navn)

hils("Sara")
hils("Oliver")
```

Parametre er "pladsholdere", og argumenter er de konkrete værdier, du giver med, når du kalder funktionen.

---

## 📘 4. Brug `return` til at sende værdier tilbage

```python
def kvadratet(x):
    return x * x

print(kvadratet(4))  # 16
```

En funktion stopper ved `return` og sender værdien tilbage til det sted, hvor funktionen blev kaldt.

---

## 📘 5. Lokale variabler

Variabler oprettet inde i en funktion findes kun dér:

```python
def beregn_moms(pris):
    moms = pris * 0.25
    return moms

print(beregn_moms(100))
```

Variablen `moms` findes kun inde i funktionen og kan ikke bruges udenfor.

---

## 📘 6. Funktioner og flow

Du kan bruge funktioner til at dele dit program op i trin:

```python
def velkomst():
    print("Velkommen til mit program!")

def hovedmenu():
    print("1. Start")
    print("2. Afslut")

velkomst()
hovedmenu()
```

---

## 🧪 Øvelser

1. Skriv en funktion `sig_farvel()` der printer "Farvel og tak!"
2. Lav en funktion `kvadrat(x)` der returnerer x ganget med sig selv
3. Lav en funktion `omregn_til_euro(dkk)` der returnerer beløbet omregnet med kurs 7,45
4. Skriv en funktion `gennemsnit(liste)` der beregner gennemsnittet af en liste tal
5. Ekstra: Brug input og funktion sammen: spørg brugeren om et tal og vis kvadratet

---

## ✅ Tjekliste

* [ ] Jeg kan definere en funktion med `def`
* [ ] Jeg kan give en funktion parametre
* [ ] Jeg forstår forskellen på `print()` og `return`
* [ ] Jeg har lavet en funktion der returnerer et resultat
* [ ] Jeg har brugt en funktion i et program

---
