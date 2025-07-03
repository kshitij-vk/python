'''
file1= open ('codes/Module 5 - Files, Exceptions and Errors/sample.txt', 'r')
data = file1.read(2)
print(data)
file1.close()
'''

with open('codes/Module 5 - Files, Exceptions and Errors/sample.txt', 'r') as file1:
    data = file1.read()
    print(data)