def even_odd(number):
    if number % 2 == 0:
        print(f"{number} is a Even number!")
    else:
        print(f"{number} is a Odd number!")

result = int(input("Enter a number: "))
even_odd(result)
