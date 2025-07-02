def add(a,b):
    print(a+b)
add (11,45)

def add(a,b):
    c = a + b
    return c

result = add(11, 45)
print(result)

def multiply(a, b):
    c = a * b
    return c

result = multiply(11, 45)
print(result)

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    c = a / b
    return c

result = divide(11, 0)
print(result)

result = divide(11, 5)
print(result)