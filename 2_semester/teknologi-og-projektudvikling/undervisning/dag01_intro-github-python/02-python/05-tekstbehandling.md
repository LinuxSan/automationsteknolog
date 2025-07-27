# 🔤 05 – Tekstbehandling i Python

Tekst (strenge) er en af de mest anvendte datatyper i Python. Denne guide giver dig en introduktion til, hvordan du arbejder med tekst – hvordan du opretter, ændrer, sammenligner og analyserer strenge.

---

## 🔧 Indhold

* Opret og kombiner tekst
* Brug af `len()` og `in`
* Indexering og slicing
* `split()`, `join()` og `replace()`
* Sammenligning og store/små bogstaver

---

## 📘 1. Opret og kombiner tekst

```python
fornavn = "Anna"
efternavn = "Møller"
navn = fornavn + " " + efternavn
print("Hej", navn)
```

Du kan bruge `+` til at kombinere tekst og `*` til at gentage:

```python
print("Ha!" * 3)  # Ha!Ha!Ha!
```

---

## 📘 2. Brug af `len()` og `in`

`len()` fortæller hvor mange tegn der er i en tekst:

```python
tekst = "Programmering"
print(len(tekst))  # 13
```

`in` bruges til at tjekke om en delstreng findes i teksten:

```python
if "gram" in tekst:
    print("Delstrengen findes!")
```

---

## 📘 3. Indexering og slicing

```python
s = "Python"
print(s[0])    # P
print(s[2:5])  # tho
print(s[-1])   # n
```

Du kan bruge slicing til at vende teksten:

```python
print(s[::-1])  # nohtyP
```

---

## 📘 4. `split()`, `join()` og `replace()`

Disse metoder bruges til at analysere og ændre tekst:

```python
sætning = "Hej med dig"
ord = sætning.split()  # ['Hej', 'med', 'dig']

samlet = "-".join(ord)  # Hej-med-dig

ny = sætning.replace("dig", "jer")
print(ny)  # Hej med jer
```

---

## 📘 5. Ændr store og små bogstaver

```python
tekst = "Velkommen"
print(tekst.upper())  # VELKOMMEN
print(tekst.lower())  # velkommen
print(tekst.capitalize())  # Velkommen
```

Du kan bruge disse metoder til at gøre søgning i tekst mere robust:

```python
brugernavn = input("Indtast brugernavn: ").lower()
if brugernavn == "admin":
    print("Adgang givet")
```

---

## 🧪 Øvelser

1. Skriv et program der tager en sætning som input og udskriver antallet af tegn
2. Spørg brugeren om navn og udskriv det bagfra
3. Tag et input og udskift alle mellemrum med underscores
4. Lav et program der tæller hvor mange gange bogstavet "e" optræder i en tekst
5. Ekstra: Tjek om en brugers input indeholder et bestemt ord – fx "python"

---

## ✅ Tjekliste

* [ ] Jeg kan kombinere og analysere tekst
* [ ] Jeg har brugt slicing til at hente dele af en streng
* [ ] Jeg har brugt `split()`, `join()` og `replace()`
* [ ] Jeg forstår hvordan `in` og `len()` bruges på tekst
* [ ] Jeg har brugt `.lower()` og `.upper()` i et program

---
