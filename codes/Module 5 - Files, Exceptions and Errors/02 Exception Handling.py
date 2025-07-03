try:
    a = 5
    b = 0
    print(a / b)
except ZeroDivisionError:
    print(f"Division by zero not allowed!")
finally:
    print("This block always executes.")