# Opgave 1: Find gennemsnittet af en liste
liste = [4, 7, 2, 9, 5]
gennemsnit = sum(liste) / len(liste)
print("Gennemsnit:", gennemsnit)

# Opgave 2: Udskriv alle ord i en tekst på hver sin linje
tekst = input("Skriv en sætning: ")
ord = tekst.split()
for o in ord:
    print(o)
