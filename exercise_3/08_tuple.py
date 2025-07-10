fruits_tuple = ('apple', 'banana', 'pineapple', 'orange')

print(fruits_tuple)
print(fruits_tuple.index('orange'))
print(fruits_tuple[ fruits_tuple.index('pineapple') ])


coord = (48.728650056353025, 9.241895000000559)

latitude = coord[0]
longitude = coord[1]

print()
print("https://maps.google.com/?q=" + str(latitude) + "," + str(longitude) )

# user functions
# len() : measures the length of a tuple.
# count() : returns how many times an element occurs in a tuple.
# index() : finds the position of the first occurrence of an element.