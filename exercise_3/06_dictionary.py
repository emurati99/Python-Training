oldtimer =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(oldtimer)

print()
print("car brand: ", oldtimer['brand'])
print("car model: ", oldtimer['model'])
print("production year: ", oldtimer['year'])

print()

print(oldtimer.keys())
print(oldtimer.values())

print()

oldtimer["owner"] = "Elijon"
print(oldtimer)

oldtimer["owner"] = "Thorsten"
print(oldtimer)

print()

oldtimer[88] = "value"       # 88 is not an index, but key
oldtimer["88"] = "value2"
print(oldtimer[88])
print(oldtimer["88"])

oldtimer = {}
print(len(oldtimer))
print(type(oldtimer))
