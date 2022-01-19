import math

import pyglet

window = pyglet.window.Window(width=1000, height=1000)


def tik(t):
    had.x = had.x + t * 20
    had.y = 20 + 20 * math.sin(had.x / 5)
    # had.rotation = 270


pyglet.clock.schedule_interval(tik, 1 / 30)


def spracuj_text(text):
    had.x = 150


obrazok = pyglet.image.load("snake.png")
had = pyglet.sprite.Sprite(obrazok)


def vykresli():
    window.clear()
    had.draw()


obrazok2 = pyglet.image.load("had2.png")


def zmen(t):
    had.image = obrazok2
    pyglet.clock.schedule_once(zmen_naspat, 3)


def zmen_naspat(t):
    had.image = obrazok
    pyglet.clock.schedule_once(zmen, 3)


pyglet.clock.schedule_once(zmen, 3)


def klik(x, y, tlacitko, mod):
    had.x = x
    had.y = y
    print(x)
    print(y)
    print(tlacitko)
    print(mod)


window.push_handlers(
    on_text=spracuj_text,
    on_draw=vykresli,
    on_mouse_press=klik
)

pyglet.app.run()