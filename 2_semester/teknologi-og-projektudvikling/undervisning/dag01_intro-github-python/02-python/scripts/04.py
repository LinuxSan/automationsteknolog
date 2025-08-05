# Opgave 1: Tæl antallet af vokaler i en tekst
tekst = input("Skriv en tekst: ")
vokaler = "aeiouyæøåAEIOUYÆØÅ"
antal = 0
for bogstav in tekst:
    if bogstav in vokaler:
        antal += 1
print("Antal vokaler:", antal)

# Opgave 2: Udskriv alle tal fra 10 til 1 med while-løkke
x = 10
while x > 0:
    print(x)
    x -= 1
print("Færdig!")
