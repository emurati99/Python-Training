def add(a, b):
    return a + b

# use integers as parameters
print( add(1, 1))

# use variables
a = 2
b = 7
sum = add(a, b)
print(sum)

# nested use of a function
print( add( add(1, 2), add(3, 4)) )

print( add("Hello", ", World!"))

joined_array = add( ["Hello"] ,  add( [", World!"], ["- How are you?"] ) )
print( joined_array )
print( "\n".join(joined_array))
