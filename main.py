start = 100
koniec = 0
while start >= koniec:
    if start == 5:
        start -= 1
        continue
    print(start)
    start -=1

print("------")

start = 10
while start >= koniec:
    if start == 5:
        break
    print(start)
    start -= 1


start = int(input("Zadaj odkial začnem počítať"))
koniec = int(input("Zadaj pokial budem počítať"))
while(start < koniec):
    if(start % 3 == 0):
        print(start, "je nasobok 3ky")
    start += 1

print("---------")
print("---------")
print("---------")


for premenna in range(10):
    print(premenna)



slovo = input ("Zadaj slovo")
samohlasky = "aáeéiíoóuúyý"
spoluhlasky = "dtnlhchkgďťňľžščdžcdzjbmprsvzf"
cisla = "0123456789"
znaky = "?:_,.-)!"
pocet = 0
pocet_samohlasok = 0
pocet_spoluhlasok = 0
pocet_cisel = 0
pocet_znaky = 0


for znak in slovo:
    pocet +=1

    if znak in samohlasky:
        pocet_samohlasok +=1
    if znak in spoluhlasky:
        pocet_spoluhlasok +=1
    if znak in cisla:
        pocet_cisel +=1
    if znak in znaky:
        pocet_znaky +=1

    print(znak)

if pocet_samohlasok > 0:
    print("Slovo obsahuje samohlasky", pocet_samohlasok)
else:
    print("Slovo neobsahuje samohlasky")

if pocet_spoluhlasok > 0:
    print("Slovo obsahuje spoluhlasky", pocet_spoluhlasok)
else:
    print("Slovo neobsahuje spoluhlasky")

if pocet_cisel > 0:
    print("Slovo obsahuje cisla", pocet_cisel)
else:
    print("Slovo neobsahuje cisla")

if pocet_znaky > 0:
    print("Slovo obsahuje znaky", pocet_znaky)
else:
    print("Slovo neobsahuje znaky")





















