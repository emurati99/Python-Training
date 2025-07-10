for i in range(1, 11):
	print('Ich darf meinen Lehrer nicht mit Eiern bewerfen.')

print()

for i in range(1, 11):
	print('Diese Schleife wird nach 5 Durchläufen verlassen.')
	if i == 5:
		break

print()

for i in range(1, 11):
	print("Schleifeniteration: ", i) 
	if i > 5:
		continue
	print('Diese Schleife wird 10 mal durchlaufen, doch die Ausgabe erfolgt nur 5 mal.')

print()

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	print("Schleifeniteration: ", i)
	if i > 5:
		continue
	print('Diese Schleife wird 10 mal durchlaufen, doch die Ausgabe erfolgt nur 5 mal.')
