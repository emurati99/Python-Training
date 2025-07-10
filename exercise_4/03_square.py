import math
#from math import sqrt

# Gibt die Quadrate der Zahlen 1 bis 10 aus
# Hinweis: range(start, ende) erzeugt Zahlen: start, start+1, ... ende-1 .
for x in range(1, 11):
    print(x, "*", x, "=", x ** 2)

for x in range(1, 11):
    quadrat = x ** 2
    print("sqrt(", quadrat, ") =", int(math.sqrt(quadrat)))
