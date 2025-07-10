fruit_set1 = {"apple", "banana", "cherry"}
fruit_set2 = set()

print("fruit_set1: " + str(fruit_set1))
print("fruit_set2: " + str(fruit_set2))

new_fruit = "banana"
fruit_set1.add(new_fruit)
fruit_set2.add(new_fruit)

print()
print("fruit_set1: " + str(fruit_set1))
print("fruit_set2: " + str(fruit_set2))

fruit_set1.remove(new_fruit)
fruit_set2.remove(new_fruit)

print()
print("fruit_set1: " + str(fruit_set1))
print("fruit_set2: " + str(fruit_set2))

