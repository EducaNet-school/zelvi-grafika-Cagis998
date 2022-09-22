import turtle

t = turtle.Turtle()

delka = 0
place1 = 0
place2 = 0

while True:
    t.speed(100)
    t.penup()
    t.goto(place1, place2)
    t.pendown()
    delka += 4
    place1 -= 2
    place2 -= 2
    for i in range(4):
        t.forward(delka)
        t.left(90)

