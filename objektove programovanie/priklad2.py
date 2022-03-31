import random

class generator:
    def __init__(self):
        self.pridavne_mena = ["malý", "veľký", "slabý", "silný", "modrý", "červený"]
        self.podstatne_mena = ["lev", "hasič", "učiteľ", "Jano", "lavica", "dom", "kotol"]
        self.predložky = ["s radosťou", "pri strome", "v skrini", "na stole"]
        self.slovesa = ["pribíjal", "spal", "bežal", "varil", ""]

    def generovanie(self):
        print(random.choice(self.pridavne_mena) + " " + random.choice(self.podstatne_mena) + " " + random.choice(self.predložky) + " " + random.choice(self.slovesa) + " " +random.choice(self.podstatne_mena))

generator = generator()
generator.generovanie()







