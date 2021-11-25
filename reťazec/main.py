retazec = "toto je nejaky retazec"

print(retazec)
for znak in retazec:
    print(znak)
if "o" in retazec:
    print("Retazec obsahuje o")
else:
    print("neobsahuje ")


with open('./subor.txt', encoding='UTF-8'):
    print("ahoj svet", file=subor)










