def print_squares(limit):
    """
    Prints the square of numbers from 1 up to the limit.
    """
    for i in range(1, limit + 1):
        square = i ** 2
        print(f"Number: {i}, Square: {square}")

# Call the function
print_squares(10)