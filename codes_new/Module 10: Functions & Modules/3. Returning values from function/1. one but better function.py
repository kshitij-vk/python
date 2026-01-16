def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = even_odd(int(input("Enter a number: ")))
print(result)
