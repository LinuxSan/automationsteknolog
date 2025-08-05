# Opgave 1: Udskriv tekst med print()
print("Velkommen til Python!")


# Opgave 2: Læs input fra brugeren
navn = input("Hvad hedder du? ")
print("Hej", navn)


# Opgave 3: Brug af variabler og datatyper
alder = 20               # heltal (int)
pi = 3.14                # decimaltal (float)
er_studerende = True     # boolesk værdi (True/False)
navn = "Anders"          # tekst (str)


# Opgave 4: Kommentarer i Python
print("Kommentarer bliver ikke kørt")
print("En kommentartekst starter med # og bruges til at forklare koden")


# Lav et program, der:
#   Spørger om dit navn og alder
#   Udskriver en sætning med disse oplysninger, fx:
#       Hej Emil, du er 22 år gammel.

navn = input("Hvad hedder du? ")
alder = input("Hvor gammel er du? ")
print(f"Hej %s, du er %d år gammel." % (navn, int(alder)))



