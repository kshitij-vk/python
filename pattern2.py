def print_number_pattern(rows):
    """
    Prints a right-angled triangle pattern of numbers.
    """
    # Outer loop handles the number of rows (1 to 4)
    for i in range(1,5):
        for j in range(1, i + 1):
            print (j, end=" ")
        print()
print_number_pattern(int(input("Enter number: ")))