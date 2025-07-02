n = 1 # This n is global
print(n)

def my_function():
        global n # This will take global variable of n
        n = 5 # This n is local to my_function
        print(n) # This will print the local n, which is 5
my_function()

print(n) # This will print the global n, which is 1