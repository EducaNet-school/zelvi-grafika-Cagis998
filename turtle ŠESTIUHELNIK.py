import turtle

t = turtle.Turtle()

def sestiuhelnik():
   for i in range(6):
      t.forward(100)
      t.left(60)

def vypln():
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)

sestiuhelnik()
for i in range(5):
    vypln()
    t.left(120)