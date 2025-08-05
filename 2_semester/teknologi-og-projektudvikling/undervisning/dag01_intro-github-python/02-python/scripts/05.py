# Opgave 1: Tjek om et tal er primtal
n = int(input("Indtast et tal: "))
if n < 2:
    print("Ikke et primtal")
else:
    primtal = True
    for i in range(2, n):
        if n % i == 0:
            primtal = False
            break
    if primtal:
        print("Primtal")
    else:
        print("Ikke et primtal")

# Opgave 2: Udskriv alle lige tal fra 2 til 20
for i in range(2, 21, 2):
    print(i)
