
plocha = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]
hra_beží = True
víťaz = None
aktuálny_hráč = "X"
def zobraz_plochu():
    print(plocha[0] + " | " + plocha[1] + " | " + plocha[2])
    print(plocha[3] + " | " + plocha[4] + " | " + plocha[5])
    print(plocha[6] + " | " + plocha[7] + " | " + plocha[8])

def hraj_hru():
    zobraz_plochu()
    while hra_beží:
        tvoj_ťah(aktuálny_hráč)

        zisti_či_hra_skončila()

        nasledujúci_hráč()

    if víťaz == "X" or víťaz == "0":
        print(víťaz + " vyhral.")
    elif víťaz == None:
        print("Tie.")

def tvoj_ťah(hráč):
    print("hráč " + hráč + " na rade")
    pozícia = input("Vyber pozíciu od 1 do 9: ")

    platné = False
    while not platné:

        while pozícia not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pozícia = input("Vyber pozíciu od 1 do 9: ")

        pozícia = int(pozícia) - 1

        if plocha[pozícia] == "-":
            platné = True
        else:
            print("Tam nemôžeš ísť. Skús znova.")

    plocha[pozícia] = hráč

    zobraz_plochu()

def zisti_či_hra_skončila():
    zisti_víťaza()
    zisti_remízu()

def zisti_víťaza():

    global víťaz

    riadok_víťaz = skontroluj_riadky()
    stĺpec_víťaz = skontroluj_stĺpce()
    uhlopriečka_víťaz = skontroluj_uhlopriečky()
    if riadok_víťaz:
        víťaz = riadok_víťaz
    elif stĺpec_víťaz:
        víťaz = stĺpec_víťaz
    elif uhlopriečka_víťaz:
        víťaz = uhlopriečka_víťaz
    else:
        víťaz = None
    return


def skontroluj_riadky():
    global hra_beží
    riadok_1 = plocha[0] == plocha[1] ==plocha[2] != "-"
    riadok_2 = plocha[3] == plocha[4] ==plocha[5] != "-"
    riadok_3 = plocha[6] == plocha[7] ==plocha[8] != "-"
    if riadok_1 or riadok_2 or riadok_3:
        hra_beží = False
    if riadok_1:
        return plocha[0]
    elif riadok_2:
        return plocha[3]
    elif riadok_3:
        return plocha[6]
    return

def skontroluj_stĺpce():
    global hra_beží
    stĺpec_1 = plocha[0] == plocha[3] == plocha[6] != "-"
    stĺpec_2 = plocha[1] == plocha[4] == plocha[7] != "-"
    stĺpec_3 = plocha[2] == plocha[5] == plocha[8] != "-"
    if stĺpec_1 or stĺpec_2 or stĺpec_3:
        hra_beží = False
    if stĺpec_1:
        return plocha[0]
    elif stĺpec_2:
        return plocha[1]
    elif stĺpec_3:
        return plocha[2]
    return

def skontroluj_uhlopriečky():
    global hra_beží
    uhlopriečka_1 = plocha[0] == plocha[4] == plocha[8] != "-"
    uhlopriečka_2 = plocha[6] == plocha[4] == plocha[2] != "-"

    if uhlopriečka_1 or uhlopriečka_2:
        hra_beží = False
    if uhlopriečka_1:
        return plocha[0]
    elif uhlopriečka_2:
        return plocha[6]
    return

def zisti_remízu():
    if "-" not in plocha:
        hra_beží = False
    return

def nasledujúci_hráč():
    global aktuálny_hráč
    if aktuálny_hráč == "X":
        aktuálny_hráč = "0"
    elif aktuálny_hráč == "0":
        aktuálny_hráč = "X"
    return


hraj_hru()

