class Zvieratko:
    def __init__(self,meno):
        self.meno = meno

    def jedz(self, jedlo):
        print(f"{self.meno}: {jedlo} mi chutí!")

#inherit -> dedenie
#dedim od zvieratka jeho metody
class Macka(Zvieratko):
    def urob_zvuk(self):
        print(f"{self.meno}: Mňau!")

    def jedz(self, jedlo):
        super().jedz("šunka")
        print(f"{self.meno}: {jedlo} vypľula!")

#dedim od zvieratka jeho metody
class Pes(Zvieratko):
    def urob_zvuk(self):
        print(f"{self.meno}: Haf!")

macka = Macka("Micka")
pes = Pes("Falko")

#Môžem používať jedz, ktoré som definoval v triede Zvieratko
macka.jedz("Šunka")
macka.urob_zvuk()

#Môžem používať jedz, ktoré som definoval v triede Zvieratko
pes.jedz("Granulka")
pes.urob_zvuk()

#POLYMORFIZMUS
zvieratka = [Macka("Naginy"), Pes("Azor")]

for zvieratko in zvieratka:
    zvieratko.jedz("Granulka")
    zvieratko.urob_zvuk()


#generalizácia