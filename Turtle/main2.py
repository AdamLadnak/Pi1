import turtle
import random
from random import randrange, uniform
randrange(-200, 200)

t = turtle.Turtle()


t.penup()
position_x = random.randrange(0, 500)
position_y = random.randrange(0, 700)
t.pendown()

dlzkaA = randrange(0,100)


turtle.setup(500,700)
def trojuholnik(dlzkaA):
    for i in range(3):
        t.forward(dlzkaA)
        t.left(120)

def stvorec(dlzkaA):
    for i in range(4):
        t.forward(dlzkaA)
        t.left(90)


t.penup()
t.setpos(position_x, position_y)
t.pendown()
trojuholnik(dlzkaA)




trojuholnik(dlzkaA)

turtle.exitonclick()