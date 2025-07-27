# 📚 03 – Lister og Iteration

Denne guide introducerer arbejdet med lister i Python og hvordan du gennemløber dem med løkker. Lister bruges til at gemme flere værdier i én variabel og er en af de vigtigste datastrukturer i Python. De giver dig mulighed for at strukturere og manipulere samlinger af data på en effektiv måde og danner grundlag for mere avancerede datastrukturer og funktioner i programmeringssproget.

---

## 🔧 Indhold

* Opret og brug lister
* Tilføj, fjern og redigér elementer
* Gennemløb med `for`
* Indeks og slicing
* Brug af `len()` og `range()` sammen
* Indlejrede løkker (intro)
* Brug af lister med input og funktioner

---

## 📘 1. Opret en liste

Lister skrives med kantede parenteser. En liste kan indeholde tekst, tal, boolean og mere:

```python
tal = [1, 3, 5, 7, 9]
dyr = ["kat", "hund", "fugl"]
```

Du kan blande typer i en liste, men det er normalt bedst at holde samme type:

```python
blandet = [42, "hej", True]
```

Du kan også starte med en tom liste og tilføje elementer:

```python
frugter = []
frugter.append("æble")
frugter.append("banan")
```

---

## 📘 2. Tilgå og ændr elementer med indeks

Python starter med indeks 0:

```python
dyr = ["kat", "hund", "fugl"]
print(dyr[0])  # kat
print(dyr[2])  # fugl
```

Du kan ændre værdier med tildeling:

```python
dyr[1] = "kanin"
print(dyr)  # ['kat', 'kanin', 'fugl']
```

Brug `len()` til at finde antal elementer:

```python
print(len(dyr))  # 3
```

---

## 📘 3. Brug slicing til at få dele af listen

Slicing giver dig et udsnit af listen baseret på start og slut:

```python
tal = [1, 2, 3, 4, 5, 6]
print(tal[1:4])  # [2, 3, 4]
print(tal[:3])   # [1, 2, 3]
print(tal[3:])   # [4, 5, 6]
```

Du kan også bruge negative indeks:

```python
print(tal[-1])  # 6 (sidste element)
print(tal[-3:-1])  # [4, 5]
```

---

## 📘 4. Gennemløb en liste med `for`

En `for`-løkke kan bruges til at gennemgå alle elementer:

```python
for dyr in ["kat", "hund", "kanin"]:
    print("Mit dyr er:", dyr)
```

Du kan kombinere `range()` og `len()` for at bruge indeks:

```python
tal = [10, 20, 30, 40]
for i in range(len(tal)):
    print("Element", i, "er", tal[i])
```

---

## 📘 5. Ændr lister under iteration

Lister kan opdateres undervejs, men pas på at undgå fejl ved at ændre listen direkte:

```python
navne = ["Anna", "Bo", "Carl"]
for i in range(len(navne)):
    navne[i] = navne[i].upper()
print(navne)  # ['ANNA', 'BO', 'CARL']
```

---

## 📘 6. Indlejrede løkker (liste i liste)

En liste kan indeholde andre lister (2D-lister):

```python
matrix = [[1, 2], [3, 4], [5, 6]]
for række in matrix:
    for værdi i række:
        print(værdi)
```

Indlejrede løkker er nyttige til fx at gennemgå rækker og kolonner i tabeller.

---

## 📘 7. Liste og brugerinput

Du kan opbygge en liste dynamisk med input fra brugeren:

```python
navne = []
for i in range(3):
    navn = input("Indtast navn: ")
    navne.append(navn)

print("Du indtastede:", navne)
```

---

## 🧪 Øvelser

1. Lav en liste med navnene på tre venner og udskriv dem én ad gangen
2. Brug `for` til at udskrive tallene i listen `[2, 4, 6, 8, 10]`
3. Brug slicing til at udskrive de midterste tre tal i `[1, 3, 5, 7, 9]`
4. Lav en liste med fem tal og beregn summen ved hjælp af en `for`-løkke og en variabel til at akkumulere værdierne
5. Ekstra: lav en liste af lister med to rækker tal og brug indlejrede løkker til at udskrive alle værdier
6. Bonus: lav et program, hvor brugeren kan indtaste fem tal, som bliver gemt i en liste og derefter udskrives i omvendt rækkefølge

---

## ✅ Tjekliste

* [ ] Jeg kan oprette og tilgå en liste
* [ ] Jeg forstår hvordan slicing fungerer
* [ ] Jeg kan bruge `for` og `range()` sammen
* [ ] Jeg har arbejdet med indlejrede lister
* [ ] Jeg har brugt lister sammen med input

---
