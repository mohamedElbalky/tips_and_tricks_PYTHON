"""
    The map() function in Python is used to 
    apply a given function to every item of an iterable (like list, tuple etc.) 
    and return a list of the results.
"""

citizens = [('ali', 10), ('omer', 8), ('david', 6)]

def tax(citizen):
    name = citizen[0]
    taxed_balance = citizen[1]*0.93
    return name, taxed_balance

# taxed_citizens = []
# for citizen in citizens:
#     taxed_citizen = tax(citizen)
#     taxed_citizens.append(taxed_citizen)

taxed_citizens = list(map(tax, citizens))

print(taxed_citizens)


# another EX:
numbers = [1, 2, 3, 4, 5]

squares = map(lambda n: n * n, numbers)

print(list(squares))  # Output: [1, 4, 9, 16, 25]