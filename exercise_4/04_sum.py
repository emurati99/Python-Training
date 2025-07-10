# Gibt die Summe der Zahlen 1 bis 5 aus
summe = 0
bereich = range(1, 6)
for x in bereich:
    summe_akt = summe
    summe += x
    print("Aktuelle Summe: ", summe_akt, " addiere:", x, " kumulierte Summe:", summe)

print()
print("Die Summe der Zahlen ", min(bereich), "bis", max(bereich), " ergibt: ", summe)