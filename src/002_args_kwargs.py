"""
args and kwargs are special arguments in 
Python that allow you to pass a variable 
number of arguments to a function. 
args stands for "arguments" 
and is a tuple of positional arguments, 
while kwargs stands for "keyword arguments" 
and is a dictionary of keyword arguments.
"""

# ---------- ERROR PART --------
# def average(a, b, c):
#     avg = (a + b + c) / 3
#     print(avg)


# average(1, 2,3)
# average(1, 2)
# average(1)
# ------------------------------


def average(*args):
    avg = sum(args) / len(args)
    print(avg)


average(1, 2, 3)
average(1, 2)
average(1)


# --------------------------------
def my_function(*args, **kwargs):

    print("Positional arguments:", args)

    print("Keyword arguments:", kwargs)


my_function(1, 2, 3, a=4, b=5)
