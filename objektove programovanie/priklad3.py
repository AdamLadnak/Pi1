class auto:
    def __init__(self, SPZ, color):
        self.SPZ = SPZ
        self.color = color


    def zaparkuj(self, garage):
        garage.auta_v_garazi.append("{0} {1}".format(self.SPZ,self.color))

    def vyparkuj(self, garage):
        garage.auta_v_garazi.remove("{0} {1}".format(self.SPZ, self.color))

class garaz:

    auta_v_garazi = []
    def vypis_aut(self):
        if self.auta_v_garazi == []:
            print("Garáž je prázdna")
        else:
            print("V garáži sú autá: {}".format(", ".join(self.auta_v_garazi)))

garaz = garaz()
auto1 = auto("ABC123", "biele")
auto1.zaparkuj(garaz)
auto2 = auto("BCF245", "modré")
auto2.zaparkuj(garaz)
auto3 = auto("MNH987", "zelené")
auto3.zaparkuj(garaz)
auto2.vyparkuj(garaz)
garaz.vypis_aut()