# We define a recursive function for calculating the factorial of a number 'n'.
# In mathematics, the factorial of a number n is the product: n * (n-1) * (n-2) * .... * 1 .
# Exception: the factorial of number 0 is defined as the value 1.
def factorial(n):
    """
        Recursive function to calculate the factorial of a number.
        Attention: n must not be negative!
    """
    if n == 0 or n == 1:  # Base case
        print("Rekursion:  1")
        return 1
    else:
        ergebnis = n * factorial(n-1)  # Recursive step
        print("Rekursion: ", n)
        return ergebnis


#print( factorial(0) )   # output =                  1
#print( factorial(1) )   # output =                  1
#print( factorial(2) )   # output =              2 * 1
#print( factorial(3) )   # output =          3 * 2 * 1
#print( factorial(4) )   # output =      4 * 3 * 2 * 1
print( factorial(5) )   # output =  5 * 4 * 3 * 2 * 1
#print( factorial(-1) )

# Task 1: Modify the function to fix the RecursionError when a negative number is given.
#         Instead of endless recursion, an error message shall be returned by the function.