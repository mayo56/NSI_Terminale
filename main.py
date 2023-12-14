import turtle as t
from random import randint

t.penup()
t.goto(0, 0)
t.pendown()

t.setheading(0)
t.hideturtle()
t.speed(1000)
t.color("blue")

t.pensize(1)

# t.forward(100)
# t.left(60)

# t.forward(100)
# t.right(120)

# t.forward(100)
# t.left(60)
# t.forward(100)

color = ["red", "blue", "green"]

def flocon(n, cote):
    if n<=1:
        t.forward(cote)
    else:
        flocon(n - 1, cote/3)
        t.left(60)
        flocon(n - 1, cote/3)
        t.right(120)
        flocon(n - 1, cote/3)
        t.left(60)
        flocon(n - 1, cote/3)


flocon(6,200)
t.right(120)
flocon(6,200)
t.right(120)
flocon(6,200)

t.mainloop()

