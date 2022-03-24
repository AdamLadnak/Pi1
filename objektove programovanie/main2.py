class Kalkulacka:
    def __init__(self, cislo1, cislo2):
        self.cislo1 = cislo1
        self.cislo2 = cislo2




    def sucet(self):
        print("Súčet: " + self.cislo1 + self.cislo2)

    def rozdiel(self):
        print("Rozdiel: " + self.cislo1 - self.cislo2)

    def sucin(self):
        print("Súčin: " + self.cislo1 * self.cislo2)

    def podiel(self):
        print("Podiel: " + self.cislo1 // self.cislo2)

cislo1 = int(input(print("Zadaj 1. čislo: ", )))
cislo2 = int(input(print("Zadaj 2. čislo: ", )))

kalkulacka = Kalkulacka()
kalkulacka.sucet()
kalkulacka.rozdiel()
kalkulacka.sucin()
kalkulacka.podiel()
