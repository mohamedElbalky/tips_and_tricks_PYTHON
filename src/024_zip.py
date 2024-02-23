"""
    In Python, zip() is a built-in function that is used to 
    combine two or more iterable objects 
    (like lists, tuples, or strings) into a single iterable. 
    This new iterable, a zip object, 
    generates a series of tuples, 
    where each tuple contains one element from each of the input iterables.

    The general syntax for the zip() function is as follows:

    zip(*iterables)

    Here, iterables is one or more iterable objects you want to combine. 
    If you provide multiple iterables, 
    they must have the same length. 
    The * operator is used to unpack the iterables.
"""

import itertools

names = ["moahmed", "omer", "ali"]

ages = [10, 20, 39]

weights = [1.3, 1.10]

inv = zip(names, ages, weights)
print(list(inv))

# Make sure the input iterables have the same length or
# that you're prepared to handle cases where they don't
# (e.g., by using the zip_longest() function from the itertools module).

inv2 = itertools.zip_longest(names, ages, weights)
# print(list(inv2))

# unzip
names, ages, weights = zip(*inv2)
print(names, ages, weights)




# -----------------------
fruits = ["apple", "banana", "mango"]

colors = ["red", "yellow", "green"]


fruit_colors = dict(zip(fruits, colors))

# print(fruit_colors)
