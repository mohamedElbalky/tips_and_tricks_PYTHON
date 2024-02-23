"""
    In Python, if you want to throw away a variable 
    that you no longer need, you can use the _ (underscore) 
    variable name. This is a convention in Python that 
    tells other developers that this variable is 
    intentionally not being used.
"""

name, _, age = ["ali", 2000, 22]
print(name)
print(age)

first, *_, last = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(first)
print(last)

for _ in range(3):
    print('hello momo')