"""
    More than one way to change the position of the item in the List
"""

my_list = ['a', 'b', 'd', 'e', 'f', 'g']
my_val = 'c'

# ----- Using insert(index, item) ------
# my_list.insert(2, my_val)
# print(my_list)


# ----- Using slice notation list[index:inex] = item ----
# my_list[2:2] = my_val
# print(my_list)

# ---- Move the item from position to another ------
my_list = ['a', 'b', 'd', 'e', 'f', 'c']
my_list.insert(2, my_list.pop())
print(my_list)