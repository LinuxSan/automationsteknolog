# 07 – Klasser

# Opgave 1: Skriv en simpel klasse for en bil
class Bil:
    def __init__(self, mærke, årgang):
        self.mærke = mærke
        self.årgang = årgang
    def info(self):
        print(f"Bil: {self.mærke}, Årgang: {self.årgang}")

min_bil = Bil("Toyota", 2020)
min_bil.info()

# Opgave 2: Lav en klasse for en person med navn og alder
class Person:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
    def præsentation(self):
        print(f"Hej, jeg hedder {self.navn} og er {self.alder} år.")

p = Person("Emil", 22)
p.præsentation()
