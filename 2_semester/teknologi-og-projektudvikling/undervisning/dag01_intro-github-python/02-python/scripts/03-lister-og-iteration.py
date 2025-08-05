# 03 – Lister og iteration

# Opgave 1: Udskriv alle elementer i en liste
frugter = ["æble", "banan", "pære", "appelsin"]
for frugt in frugter:
    print(frugt)

# Opgave 2: Find summen af tallene i en liste
liste = [1, 2, 3, 4, 5]
sum_tal = 0
for tal in liste:
    sum_tal += tal
print("Summen er:", sum_tal)

# Opgave 3: Find det største tal i en liste
maks = liste[0]
for tal in liste:
    if tal > maks:
        maks = tal
print("Største tal:", maks)
