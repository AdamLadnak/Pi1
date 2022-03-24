from random import randint
class Kocka:
    def __init__(self, strany):
        self.strany = strany


    def hod_kockou(self, pocet_hodov):
        for i in range(pocet_hodov):
            cislo = randint(1, self.strany)
            print(str(cislo) + " ", end="")



kocka = Kocka(10)
kocka.hod_kockou(3)
print()
kocka2 = Kocka(8)
kocka2.hod_kockou(3)