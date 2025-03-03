'''
example of logical error
    program runs but it doesn't give the expected result
'''

# goal: subtract 2 numbers so there is never a negative number as a result
a = 10
b = 5

if a < b:
    result = a - b
else:
    result = b - a

print(result)
