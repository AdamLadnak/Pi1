"""
#trieda Mačka
class Cat:
    #KONŠTRUKTOR -> Vykoná sa vždy keď VYTVÁRAM inštanciu triedy
    def __init__(self, name, vek):
        print("Vytváram objekt mačky")
        self.name = name
        self.vek = vek

    def __str__(self):
        print("Meno mačky je: " + self.name)
        print("Vek mačky je: " + str(self.vek))
        return  " ";

    def zamnaukaj(self):
        print(self.name + " mňau")

    def zjedz(self, food):
        print(self.name + " zjedla/zjedlo " + food)

#vytvorenie inštancie objektu mačka
cat = Cat("Mica", 4)
#cat.meno = "Cica"

#volanie metody
cat.zamnaukaj()
cat.zjedz("rybu")

cat2 = Cat("Murko", 5)
cat2.zamnaukaj()

print(cat2)
"""

class Auto:
    def __init__(self, Značka, rokVyroby, farba, počet_miest_na_sedenie):
        self.znacka = Značka
        self.rok = rokVyroby
        self.color = farba
        self.miesta = počet_miest_na_sedenie
        self.jeNastartované = False

    def __str__(self):
        print("Značka auta: " + self.znacka)
        print("Rok vyroby: " + str(self.rok))
        print("Farba auta: " + self.color)
        print("Počet miest na sedenie: " + str(self.miesta))
        print("Auto je: " + self.nastartuj)
        return "------------";

    def chodDopredu(self):
        print("Auto ide dopredu")

    def zatrub(self):
        print("Trúbi")

    def nastartuj(self):
        print("Auto sa startuje")

    def vypni(self):
        print("Auto sa vyplo")

car = Auto("mercedes", 2012, "biela", 4)
print(car)
car.zatrub()
car.chodDopredu()
car.nastartuj()