file1 = open("sample.txt", "r+")
print(file1.read())  # Read the content of the file
file1.close()  # Close the file
'''
with open("sample.txt", "w") as file1:
    file1.write("This is a new line.")
'''