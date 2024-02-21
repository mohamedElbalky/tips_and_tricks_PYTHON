"""
    Flatten lists to one list
"""
names1 = ['A', 'B']
names2 = ['C', 'D']
names3 = ['E', 'F']

# names = names1 + names2 + names3

names = [*names1, *names2, *names3]
print(names)