"""
    making custom sort by using key in sorted function
"""

chars = ['A', 'C', 'B']
# chars.sort()

rarity = {
    'A': 1,
    'B': 2,
    'C': 3
}

# sorted_chasr = sorted(chars, key=rarity.__getitem__)
sorted_chasr = sorted(chars, key=lambda  x: rarity[x])
print(sorted_chasr) 

print(rarity.__getitem__("A"))
