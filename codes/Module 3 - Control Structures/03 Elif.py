number1 = int(input("Enter first number: "))
opeator= input("Enter operator (+, -, *, /): ")
number2= int(input("Enter second number: "))
if opeator == "+":
    result = number1 + number2
elif opeator == "-":
    result = number1 - number2
elif opeator == "*":
    result = number1 * number2
elif opeator == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print("Result:", result)