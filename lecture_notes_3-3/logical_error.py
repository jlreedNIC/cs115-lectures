'''
example of logical error
    program runs but it doesn't give the expected result
'''

# goal: subtract 2 numbers so there is never a negative number as a result
a = 10
b = 5

if a < b:
    print("a is less than b")
    result = b - a
else:
    print("b is less than a")
    result = a - b

print(result)
