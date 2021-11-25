slova = []
subory = int(input("Zadaj počet súborov: "))


with open("./basnicka.txt", encoding="utf-8") as subor:
    for riadok in subor:
        slova += riadok.split()

for i in range(subory):
    with open("./"+str(i)+".txt", mode="w", encoding="utf-8") as subor1:
        print(slova[0], file=subor1)

basnicka = len(slova)
x = 0


for i in range(subory):
    if i >= basnicka:
        x = i - basnicka
    open("%s.txt" % i, "w").write(slova[x])

