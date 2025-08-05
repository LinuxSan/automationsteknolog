# opgave 1: Caster datatype fra string til int
# Spørg brugeren om deres alder og konverter inputtet til en integer
# og tjek om de er myndige (18 år eller ældre)
alder = int(input("Hvor gammel er du? "))

# opgave 2: Tjek om brugeren er myndig
# Hvis alder er 18 eller mere, print "Du er myndig", ellers print "Du er ikke myndig"
if alder >= 18:
    print("Du er myndig")
else:
    print("Du er ikke myndig")

# opgave 2: Tjek brugerens livsfase
if alder >= 18 and alder < 65:
    print("Voksen under pensionsalderen")
elif alder >= 65:
    print("Pensionist")
else:
    print("Ungdom under myndighedsalderen")

# Opgave 3: For-løkke
for i in range(5):
    print("Tallet er:", i)

# Opgave 4: For-løkke med liste
dyr = ["kat", "hund", "kanin"]
for d in dyr:
    print("Mit dyr er:", d)


# Opgave 5: While-løkke
# Initialiser en variabel x til 0 og brug en while-løkke til at
# tælle op til 5, og print værdien af x i hver iteration
x = 0
while x < 5:
    print("x er", x)
    x += 1

# Opgave 6: Break i en for-løkke
# Brug en for-løkke til at tælle fra 0 til 9 
# og brug break til at stoppe løkken, når i er lig med 4
# (dvs. print ikke 4)
for i in range(10):
    if i == 4:
        break
    print(i)

# Opgave 7: Continue i en for-løkke
# Brug en for-løkke til at tælle fra 0 til 9
# og brug continue til at springe over iterationen, når i er lig med 2
# (dvs. print ikke 2)
for i in range(5):
    if i == 2:
        continue
    print(i)

#1. Lav et program der spørger om et tal og skriver:
#
#   * "Lige" hvis tallet er deleligt med 2
#   * "Ulige" hvis ikke

tal = int(input("Indtast et tal: "))

if tal % 2 == 0:
    print("Lige")
else:
    print("Ulige")

#2. Skriv et program der udskriver tallene fra 1 til 10 ved hjælp af `for`

for i in range(1, 11):
    print(i)

#3. Skriv et program med `while`, der tæller ned fra 5 til 1 og afslutter med "Start!"

x = 5
while x > 0:
    print(x)
    x -= 1
print("Start!")
#4. Lav et program der beder brugeren om et tal indtil de indtaster "0" (brug `while` og `break`)

while True:
    tal = int(input("Indtast et tal (0 for at stoppe): "))
    if tal == 0:
        break
    print("Du indtastede:", tal)
#5. Lav et program der skriver alle tal fra 1 til 20 undtagen dem der er delelige med 3 (brug `continue`)

for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)