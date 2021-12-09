"""
sachovnica = [[" "] * 8 for i in range(8)]
for i in range(len(sachovnica)):
    for j in range(len(sachovnica[i])):
        if i % 2 == 0 and j % 2 == 0:
            sachovnica[i][j] = "█"
        elif i % 2 == 1 and j % 2 == 1:
            sachovnica[i][j] = "█"

for i in sachovnica:
    for j in i:
        print(j, end=' ')
    print()
"""

riadok1 = ["█"," ","█"," ","█"," ","█"," "]
riadok2 = [" ","█"," ","█"," ","█"," ","█"]

def vypisSachovnica(sachovnica):
    for riadok in sachovnica:
        print(riadok)

sachovnica = []

for i in range(4):
    for j in riadok1:
        print(j, end= "")
    print(sep= "")
    for i in riadok2:
        print(i, end= "")
    print("")



