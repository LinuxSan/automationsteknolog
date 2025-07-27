# 🧱 07 – Klasser og objekter i Python

Denne guide introducerer dig til klasser og objekter – grundlæggende begreber i objektorienteret programmering. Klasser gør det muligt at organisere kode i egne datatyper med tilhørende funktioner.

---

## 🔧 Indhold

* Hvad er en klasse?
* Konstruktoren `__init__`
* Instansvariabler og metoder
* Opret og brug objekter
* Flere objekter i praksis

---

## 📘 1. Hvad er en klasse?

En klasse er en skabelon for objekter. Objekter har data (variabler) og funktioner (metoder), som defineres inde i klassen.

```python
class Person:
    def sig_hej(self):
        print("Hej!")

p = Person()
p.sig_hej()
```

---

## 📘 2. Brug af `__init__()`

Konstruktøren `__init__()` bruges til at sætte startværdier:

```python
class Person:
    def __init__(self, navn):
        self.navn = navn

    def sig_hej(self):
        print("Hej, jeg hedder", self.navn)

p1 = Person("Lise")
p1.sig_hej()
```

`self` refererer til det objekt, der kalder metoden.

---

## 📘 3. Flere objekter

Du kan oprette flere objekter fra samme klasse:

```python
person1 = Person("Anders")
person2 = Person("Sara")

person1.sig_hej()
person2.sig_hej()
```

Hver instans har sin egen version af variabler og metoder.

---

## 📘 4. Metoder med beregninger

```python
class Cirkel:
    def __init__(self, radius):
        self.radius = radius

    def areal(self):
        return 3.14 * self.radius ** 2

c = Cirkel(5)
print("Areal:", c.areal())
```

---

## 🧪 Øvelser

1. Lav en klasse `Bil` med attributter `mærke` og `årgang`, og en metode `beskriv()`
2. Opret to `Bil`-objekter og udskriv deres beskrivelse
3. Lav en klasse `Rektangel` med metoden `areal()`
4. Udvid `Person`-klassen med en metode `er_myndig()`
5. Ekstra: Brug en liste til at oprette og vise flere personer

---

## ✅ Tjekliste

* [ ] Jeg kan oprette en klasse og kalde dens metoder
* [ ] Jeg forstår `__init__` og `self`
* [ ] Jeg har lavet funktioner inde i en klasse
* [ ] Jeg har brugt flere objekter i samme program

---
