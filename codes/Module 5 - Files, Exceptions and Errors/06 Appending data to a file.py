file1 = open("codes/Module 5 - Files, Exceptions and Errors/sample.txt", "w")
file1.write("Hello World")
file1.close()

file1 = open("codes/Module 5 - Files, Exceptions and Errors/sample.txt", "r")
data = file1.read()
print(data)
file1.close()

file1 = open("codes/Module 5 - Files, Exceptions and Errors/sample.txt", "w")
file1.write("Hello Again")
file1.close()

file1 = open("codes/Module 5 - Files, Exceptions and Errors/sample.txt", "r")
data = file1.read()
print(data)
file1.close()