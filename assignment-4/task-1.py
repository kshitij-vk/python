try:
    file1= open ('codes/Module 5 - Files, Exceptions and Errors/sample.txt', 'r')
    data = file1.readlines(1)
    data1 = file1.readlines(2)
except FileNotFoundError:
    print(f"Error: The file 'sample.txt' was not found.")
finally:
    print("Line 1:", data[0].strip())
    print("Line 2:", data1[0].strip())
    file1.close()