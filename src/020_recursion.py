"""
    Recursion is a programming technique 
    in which a function calls itself to 
    solve a problem. In Python, 
    you can use recursion to define functions 
    that solve problems by breaking 
    them down into smaller, simpler subproblems.
"""

def foo(x):
    if x == 0:
        return f"The value is {x}."
    return foo(x-1)

a = foo(100)
print(a)