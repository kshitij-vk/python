
# Add
dictionary = { 'a' : "apple", 'b' : "banana", 'c' : "cherry", 'd' : "date", 'e' : "elderberry" }
print(dictionary)
dictionary['f'] = "fig"
dictionary['g'] = "grape"
print(dictionary)

# Remove
dictionary = { 'a' : "apple", 'b' : "banana", 'c' : "cherry", 'd' : "date", 'e' : "elderberry" }
print(dictionary)
del dictionary['a']
del dictionary['b']
print(dictionary)

# Print Values
dictionary = { 'a' : "apple", 'b' : "banana", 'c' : "cherry", 'd' : "date", 'e' : "elderberry" }
print(dictionary.values())

# Dictionary Functions
dictionary = { 'a' : "apple", 'b' : "banana", 'c' : "cherry", 'd' : "date", 'e' : "elderberry" }
print(dictionary.get('f', 'you mean "f" : "fig?" yeah I forgot to code that part ;)'))  # Returns 'Not Found' if key 'f' does not exist
