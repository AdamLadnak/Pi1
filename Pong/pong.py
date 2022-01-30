import pyglet
import random

from pyglet import gl
from pyglet.window import key

# KONSTANTY OKNA
SIRKA = 1100
VYSKA = 800

# lopta
VELKOST_LOPTY = 20
RYCHLOST = 250  # PIXELY ZA SEKUNDU

# palky
TLSTKA_PALKY = 10
VYSKA_PALKY = 100
RYCHLOST_PALKY = RYCHLOST * 3

# prostredna ciara
CIARA_HRUBKA = 20

# fonT
VELKOST_FONTU = 42
ODSADENIE_TEXTU = 30

# stavove premenne
pozicia_palok = [VYSKA // 2, VYSKA // 2]
pozicia_lopty = [0 + SIRKA // 2, 0 + VYSKA // 2]
rychlost_lopty = [0, 0]
stisknute_klavesy = set()
skore = [0, 0]


# reset lopty na poziciu
def reset():
    pozicia_lopty[0] = SIRKA // 2
    pozicia_lopty[1] = VYSKA // 2

    if random.randint(0, 1):
        rychlost_lopty[0] = RYCHLOST
    else:
        rychlost_lopty[0] = -RYCHLOST

    rychlost_lopty[1] = random.uniform(-1, 1) * RYCHLOST


# vykreslenie lopty
def vykresli_obdlznik(x1, y1, x2, y2):
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(int(x1), int(y1))
    gl.glVertex2f(int(x1), int(y2))
    gl.glVertex2f(int(x2), int(y2))
    gl.glVertex2f(int(x2), int(y1))
    gl.glEnd()


# vykreslenie skore
def nakresli_text(text, x, y, pozice_x):
    napis = pyglet.text.Label(text, font_size=VELKOST_FONTU, x=x, y=y, anchor_x=pozice_x)
    napis.draw()


# stlacenie klaves
def stisk_klavesnice(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.add(('hore', 0))
    if symbol == key.S:
        stisknute_klavesy.add(('dole', 0))
    if symbol == key.UP:
        stisknute_klavesy.add(('hore', 1))
    if symbol == key.DOWN:
        stisknute_klavesy.add(('dole', 1))


# pustenie klaves
def pusti_klavesnice(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.discard(('hore', 0))
    if symbol == key.S:
        stisknute_klavesy.discard(('dole', 0))
    if symbol == key.UP:
        stisknute_klavesy.discard(('hore', 1))
    if symbol == key.DOWN:
        stisknute_klavesy.discard(('dole', 1))


# vykreslenie hracieho pola
def vykresli():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(1, 1, 1)

    # vykresli loptu
    vykresli_obdlznik(
        pozicia_lopty[0] - VELKOST_LOPTY // 2,
        pozicia_lopty[1] - VELKOST_LOPTY // 2,
        pozicia_lopty[0] + VELKOST_LOPTY // 2,
        pozicia_lopty[1] + VELKOST_LOPTY // 2
    )

    # vykresli palky
    for x, y in [(0, pozicia_palok[0]), (SIRKA, pozicia_palok[1])]:
        vykresli_obdlznik(
            x - TLSTKA_PALKY,
            y - VYSKA_PALKY // 2,
            x + TLSTKA_PALKY,
            y + VYSKA_PALKY // 2,
        )

    # vykreslit score
    nakresli_text(str(skore[0], ), x=ODSADENIE_TEXTU, y=VYSKA - ODSADENIE_TEXTU - VELKOST_FONTU, pozice_x="left")
    nakresli_text(str(skore[1], ), x=SIRKA - ODSADENIE_TEXTU, y=VYSKA - ODSADENIE_TEXTU - VELKOST_FONTU, pozice_x="right")

    # poliacia ciara
    for y in range(CIARA_HRUBKA // 2, VYSKA, CIARA_HRUBKA * 2):
        vykresli_obdlznik(
            SIRKA // 2 - 1,
            y,
            SIRKA // 2 + 1,
            y + CIARA_HRUBKA,
        )


# posúva pozíciu pálok a lopty
def posuvanie(dt):
    for cislo_palky in (0, 1):
        if ('hore', cislo_palky) in stisknute_klavesy:
            pozicia_palok[cislo_palky] += RYCHLOST_PALKY * dt
        if ('dole', cislo_palky) in stisknute_klavesy:
            pozicia_palok[cislo_palky] -= RYCHLOST_PALKY * dt

        if pozicia_palok[cislo_palky] < VYSKA_PALKY / 2:
            pozicia_palok[cislo_palky] = VYSKA_PALKY / 2
        if pozicia_palok[cislo_palky] > VYSKA - VYSKA_PALKY / 2:
            pozicia_palok[cislo_palky] = VYSKA - VYSKA_PALKY / 2

        pozicia_lopty[0] += rychlost_lopty[0] * dt
        pozicia_lopty[1] += rychlost_lopty[1] * dt


# obnovuje stav lopty a pridáva skóre
def obnov_stav(dt):
    if pozicia_lopty[1] < VELKOST_LOPTY // 2:
        rychlost_lopty[1] = abs(rychlost_lopty[1])
    if pozicia_lopty[1] > VYSKA - VELKOST_LOPTY // 2:
        rychlost_lopty[1] = -abs(rychlost_lopty[1])

    palka_min = pozicia_lopty[1] - VELKOST_LOPTY / 2 - VYSKA_PALKY / 2
    palka_max = pozicia_lopty[1] + VELKOST_LOPTY / 2 + VYSKA_PALKY / 2

    if pozicia_lopty[0] < TLSTKA_PALKY + VELKOST_LOPTY / 2:
        if palka_min < pozicia_palok[0] < palka_max:
            rychlost_lopty[0] = abs(rychlost_lopty[0])
        else:
            skore[1] += 1
            reset()

    if pozicia_lopty[0] > SIRKA - (TLSTKA_PALKY + VELKOST_LOPTY / 2):
        if palka_min < pozicia_palok[1] < palka_max:
            rychlost_lopty[0] = -abs(rychlost_lopty[0])
        else:
            skore[0] += 1
            reset()


reset()
window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(
    on_draw=vykresli,
    on_key_press=stisk_klavesnice,
    on_key_release=pusti_klavesnice,
)
pyglet.clock.schedule(posuvanie)
pyglet.clock.schedule(obnov_stav)

pyglet.app.run()
