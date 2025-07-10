fruits = ["apple", "banana", "orange"]

# list handling with f-strings
print(fruits)
print(f"First fruit: {fruits[0]}")
print(f"All fruits: {', '.join(fruits)}")
print()

    
# Simple conditional formatting
score = 85

print(f"Result: {'Pass' if score >= 70 else 'Fail'}")
print()

# Multiple conditions in data analysis
temperature = 25
print(f"Temperature: {'Hot' if temperature >= 30 else 'Warm' if temperature >= 20 else 'Cool' if temperature >= 10 else 'Cold'}")