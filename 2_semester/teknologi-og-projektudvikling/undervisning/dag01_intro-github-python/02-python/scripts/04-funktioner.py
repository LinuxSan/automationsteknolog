# 04 – Funktioner

# Opgave 1: Skriv en funktion der tager to tal og returnerer deres sum
def sum_to_tal(a, b):
    return a + b

print(sum_to_tal(3, 5))

# Opgave 2: Skriv en funktion der tjekker om et tal er lige eller ulige
def er_lige(tal):
    if tal % 2 == 0:
        return "Lige"
    else:
        return "Ulige"

print(er_lige(7))

# Opgave 3: Skriv en funktion der tager en liste og returnerer gennemsnittet
def gennemsnit(liste):
    return sum(liste) / len(liste)

print(gennemsnit([2, 4, 6, 8]))
