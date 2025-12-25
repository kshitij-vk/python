a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
d = [a, b, c]
# If any number is less than 10, print 'Ok' once; otherwise print the list once
if any(x < 10 for x in d):
    print('Ok')
else:
    print(d)