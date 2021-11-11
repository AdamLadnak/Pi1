import turtle



t = turtle.Turtle()
def obdlznik():
    for i in range(2):
        t.forward(40)
        t.left(90)
        t.forward(20)
        t.left(90)

obdlznik()

t.penup()
t.left(90)
t.forward(60)
t.right(90)
t.pendown()

def schody():
    for i in range(6):
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.right(90)

schody()

t.penup()
t.forward(60)
t.pendown()

def stvorec():
    for i in range(4):
        t.forward(50)
        t.left(90)


stvorec()
t.left(20)
stvorec()
t.left(20)
stvorec()


turtle.exitonclick()


