fruits = ["apple", "banana", "cherry"]

# print array elements
for f in fruits:
    print(f)
    print(fruits.index(f))

print()

# print array elements with their index
for i, f in enumerate(fruits):
    print(str(i) + ") " + f)

# modify array?
for i, f in enumerate(fruits):
    if f == "banana":
        fruits[i] = "mango"

print()

# print modified array
for fruit in fruits:
    print(fruit)

