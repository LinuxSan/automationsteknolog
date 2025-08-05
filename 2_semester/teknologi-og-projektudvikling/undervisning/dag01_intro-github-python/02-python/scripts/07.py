# Opgave 1: Tæl hvor mange gange et bogstav optræder i en tekst
tekst = input("Skriv en tekst: ")
bogstav = input("Hvilket bogstav vil du tælle? ")
antal = 0
for b in tekst:
    if b == bogstav:
        antal += 1
print(f"Bogstavet '{bogstav}' optræder {antal} gange.")

# Opgave 2: Udskriv alle tal fra 1 til 100, men spring over dem der slutter på 7
for i in range(1, 101):
    if str(i)[-1] == "7":
        continue
    print(i)
