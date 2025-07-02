# Passing Functions as Arguments
# Functions can be passed as arguments to other functions, allowing for higher-order functions.
# Example: Passing functions as arguments
def add(x, y):
    return x + y
def square(z):
    return z * z

result = square(add(6,1))
print(result)  # Output: 49
