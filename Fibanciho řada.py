pocet = int(input("vlož počet čísel? "))

x1, x2 = 0, 1
pocitat = 0

if pocet <= 0:
   print("vlož kladné číslo")
elif pocet == 1:
   print("Fibonaciho řada",pocet,":")
   print(x1)
else:
   print("Fibonaciho řada:")
   while pocitat < pocet:
       print(x1)
       nth = x1 + x2
       x1 = x2
       x2 = nth
       pocitat += 1
