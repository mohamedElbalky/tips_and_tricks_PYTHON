"""
    return the number index of the even numbers
"""

def my_func(my_input):

    return [x for x, y in enumerate(my_input) if y % 2 == 0]


my_input = [2, 3, 643, 65, 56]

print(my_func(my_input))