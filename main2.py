
zoznam_prazdny = []
zoznam_cisel = [1,5,8,9,7,15]
zoznam_pismen = ["a""b""c"]
zoznam_mix = ["slovo", 14, 'a', '@', 55]

zoznam_cisel[0] = 9999
print(zoznam_cisel[4])
print(zoznam_pismen)
print(zoznam_mix[-1])

print("----------------")
print(zoznam_cisel)
print(zoznam_mix)
print(zoznam_pismen)

zoznam = list()
print(zoznam)
zoznam_range = list(range(3,7))
print(zoznam_range)
print("----------------")

neorezany_zoznam = list(range(10))
print(neorezany_zoznam)

print(neorezany_zoznam[0:5])
print(neorezany_zoznam[2:8])
print(neorezany_zoznam[1:7:2])
print(neorezany_zoznam[2:9:3])

x = [5,8,1,3,"slovo"]
print(len(x))

zoznam_prvkov = ["jablko","hruska","banan"]

for prvok in zoznam_prvkov:
    print(prvok)

for index in range(len(zoznam_prvkov)):
    print(zoznam_prvkov[index])

myList = [1,5,8,55,500]

myList.append(99)
myList.append(1)
myList.append(0)
print(myList)

hodnota = myList.pop()
print(myList)
print(hodnota)

myList2 = [1,54,7,2,74,-10]
print("minimum", min(myList2))
print("maximum", max(myList2))
print("suma", sum(myList2))

print(myList2)
print(sorted(myList2))


zoznam = list (range(10,0,-1))
for cislo in zoznam:
    print(cislo)


zoznam_ovocia = ["malina","hruska","jablko"]
zoznam_zeleniny = ["paprika","mrkva","kapusta"]
while(True):
    slovo = input("Zadajte názov ľubovolného ovocia alebo zeleniny:")
    if slovo in zoznam_ovocia:
        print("Je to ovocie")
    elif slovo in zoznam_zeleniny:
        print("Je to zelenina")
    else:
        print("Zadal si niečo iné")

suhlas = input("Chceš zadať ďaľšie slovo?")
if suhlas == "ano":
    print("Zadaj iné ľubovolné ovocie alebo zeleninu")
elif suhlas == "nie":
    print("Dobre")
