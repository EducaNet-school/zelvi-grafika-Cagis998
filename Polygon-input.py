import turtle

strana = int(input("zadej pocet stran:"))
delka = int(input("Zadej delku strany: "))
uhel = 360/strana

t = turtle.Turtle()


for i in range(strana):
    t.forward(delka)
    t.left(uhel)