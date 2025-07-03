file1= open ('codes/Module 5 - Files, Exceptions and Errors/sample.txt', 'r+')
data = file1.read()
print(data)
write_data = "Hello World"
file1.write(write_data)
print(write_data)
file1.close()