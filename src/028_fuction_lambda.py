"""
    A lambda function in Python is a small anonymous function that is defined using the lambda keyword, rather than the def keyword. They can take any number of arguments, but can only have one expression. The syntax is as follows:

lambda arguments: expression
"""


def add(x, y):
    return x + y


print(add(1, 2))

print((lambda x, y: x + y)(1, 2))
