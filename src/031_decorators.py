"""
    In Python, a decorator is a function that takes another function as 
an argument and returns a new function. 
The new function has the same behavior as the original function, 
but it can also modify the behavior of the original function.

Decorators are often used to add features to functions, 
such as logging, caching, or authorization. 
They are also used to simplify code by breaking it down into smaller, 
more manageable pieces.
"""



def decorator_func(func):
    def wrapper(*args, **kwargs):
        print(f"Entering {func.__name__}()")
        result = func(*args, **kwargs)
        print(f"Leaving {func.__name__}()")
        return result
    return wrapper



@decorator_func
def add(x, y):
    return x + y

a = add(1,2)
print(a)