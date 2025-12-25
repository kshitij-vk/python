'''
l = ['Mike', 10.1, 1900, 'python']
l.append('java')  # Append 'java' to the end of the list
print(l)

l = ['Mike', 10.1, 1900, 'python']
l.extend(['c++', '1550'])  # Extend the list with multiple elements
print(l)

l = ['Mike', 10.1, 1900, 'python']
l.remove('python')  # Remove the first occurrence of 'python' from the list
print(l)

l = ['Mike', 10.1, 1900, 'python']
del l[0:3]  # Delete the elements at index 0, 1, and 2
print(l)
'''
l = ['Mike', 10.1, 1900, 'python']
l.clear()  # Clear all elements from the list
print(l)