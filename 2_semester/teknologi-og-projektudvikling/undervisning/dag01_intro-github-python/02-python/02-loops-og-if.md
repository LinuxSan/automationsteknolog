# 🔁 02 – Loops og If-Else

Denne guide introducerer dig til kontrolstrukturer i Python: `if`, `else`, `elif`, `for` og `while`. Du lærer at styre flowet i dine programmer og udføre gentagelser. Det er fundamentalt i al programmering at kunne styre, hvornår og hvor mange gange en kode skal køres, og hvordan programmet reagerer på forskellige inputs.

---

## 🔧 Indhold

* `if`, `else`, `elif`
* Betingelser og logiske operatorer
* `for`-løkker
* `while`-løkker
* Brug af `break` og `continue`

---

## 📘 1. Betinget logik med `if`

Med `if`-udsagn kan du få Python til at træffe beslutninger baseret på data.

```python
alder = int(input("Hvor gammel er du? "))

if alder >= 18:
    print("Du er myndig")
else:
    print("Du er ikke myndig")
```

> Bemærk: Vi bruger `int()` til at konvertere input fra tekst til tal, så vi kan sammenligne det numerisk.

Du kan også udvide logikken med `elif` (else if):

```python
if alder < 13:
    print("Barn")
elif alder < 18:
    print("Teenager")
else:
    print("Voksen")
```

Du kan bruge så mange `elif`-blokke, du vil. Programmet kører kun den første betingelse, der er sand.

---

## 📘 2. Sammenlignings- og logiske operatorer

| Operator | Betydning        |
| -------- | ---------------- |
| `==`     | er lig med       |
| `!=`     | er ikke lig med  |
| `>`      | større end       |
| `<`      | mindre end       |
| `>=`     | større eller lig |
| `<=`     | mindre eller lig |

Du kan kombinere betingelser med `and`, `or` og `not`:

```python
if alder >= 18 and alder < 65:
    print("Voksen under pensionsalderen")
```

---

## 📘 3. `for`-løkker

En `for`-løkke bruges til at gentage noget et bestemt antal gange.

```python
for i in range(5):
    print("Tallet er:", i)
```

Dette skriver tallene 0 til 4. Funktionen `range(start, stop)` kan bruges til at kontrollere rækken:

```python
for i in range(1, 6):
    print("Nu skriver vi:", i)
```

Du kan også bruge `for` til at gå gennem lister:

```python
dyr = ["kat", "hund", "kanin"]
for d in dyr:
    print("Mit dyr er:", d)
```

---

## 📘 4. `while`-løkker

`while`-løkker gentager noget så længe en betingelse er sand:

```python
x = 0
while x < 5:
    print("x er", x)
    x += 1
```

Du skal selv huske at ændre variablerne inde i løkken, ellers kører programmet i uendelighed.

---

## 📘 5. Styring af løkker med `break` og `continue`

`break` stopper løkken med det samme:

```python
for i in range(10):
    if i == 4:
        break
    print(i)
```

`continue` springer til næste iteration:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 🧪 Øvelser

1. Lav et program der spørger om et tal og skriver:

   * "Lige" hvis tallet er deleligt med 2
   * "Ulige" hvis ikke

2. Skriv et program der udskriver tallene fra 1 til 10 ved hjælp af `for`

3. Skriv et program med `while`, der tæller ned fra 5 til 1 og afslutter med "Start!"

4. Lav et program der beder brugeren om et tal indtil de indtaster "0" (brug `while` og `break`)

5. Lav et program der skriver alle tal fra 1 til 20 undtagen dem der er delelige med 3 (brug `continue`)

---

## ✅ Tjekliste

* [ ] Jeg forstår forskellen på `if`, `elif` og `else`
* [ ] Jeg kan skrive betingelser med `==`, `>`, `!=` osv.
* [ ] Jeg har skrevet både `for` og `while`-løkker
* [ ] Jeg har brugt `break` og `continue` korrekt

---
