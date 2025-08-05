# 05 – Tekstbehandling

# Opgave 1: Tæl antallet af vokaler i en tekst
tekst = input("Skriv en tekst: ")
vokaler = "aeiouyæøåAEIOUYÆØÅ"
antal = 0
for bogstav in tekst:
    if bogstav in vokaler:
        antal += 1
print("Antal vokaler:", antal)

# Opgave 2: Udskriv alle ord i en tekst på hver sin linje
tekst = input("Skriv en sætning: ")
ord = tekst.split()
for o in ord:
    print(o)
