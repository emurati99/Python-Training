fruits = ["apple", "banana", "cherry"]

print(fruits)

print()
print("first element:  ", fruits[0])
print("second element: ", fruits[1])
print("third element:  ", fruits[2])

print("index of \"apple\":  ", fruits.index("apple"))
print("index of \"banana\": ", fruits.index("banana"))
print("index of \"cherry\": ", fruits.index("cherry"))

print()

fruits.append("strawberry")
print(fruits)
print("index of \"strawberry\": ", fruits.index("strawberry"))

print()

# print all elements with index < 3
print(fruits[:3])

# print all elements with index >= 1
print(fruits[1:])

# print all elements with index >= 1 and index < 3
print(fruits[1:3])



# use functions:
# len() :   returns the length of the list passed to the function.
# count() : returns how many times a value passed as an argument appears in the list.
# sort() :  converts an unsorted list to a sorted list.

print()

fruits.append("cherry")
print (fruits)
print (fruits[3:5].count("cherry"))

print()

fruits2 = fruits[3:5]
fruits2.sort()
print(fruits2)

fruits2.insert(1, "melon")

fruits2[0] = fruits2[1]
print(fruits2)

fruits2.remove("melon")
print(fruits2)
