
lst = ['a', 'b', 'c', 'd', 'a', 'f', 'a']

# ONE
# new_lst = list(set(lst))  # error in list order

# TWO
# new_lst = []
# for item in lst:
#     if item not in new_lst:
#             new_lst.append(item)

# THREE
new_lst = list(dict.fromkeys(lst).keys())

print(new_lst)