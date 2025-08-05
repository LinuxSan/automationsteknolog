# 06 – Fejlfinding og debug

# Opgave 1: Find og ret fejl i koden
# (Eksempel på en typisk fejl)
for i in range(5):
    print("Tallet er:", i)

# Opgave 2: Brug print til at debugge
x = 10
print("Før while:", x)
while x > 0:
    print("I løkken:", x)
    x -= 1
print("Efter while:", x)
