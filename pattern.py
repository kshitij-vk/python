def print_number_pattern(rows):

    # Outer loop handles the number of rows (1 to 4)
    for i in range(1, rows + 1):
        # Inner loop handles the numbers in each row (1 to i)
        for j in range(1, i + 1):
            print(j, end=' ')
        
        # Prints a new line after the inner loop finishes
        print()

# Call the function
print_number_pattern(int(input("Enter number: ")))