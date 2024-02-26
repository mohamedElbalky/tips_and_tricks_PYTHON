
inv = {
    "a": 1,
    "b": 2
}

iv = {
    "a": 1,
    "b": 2,
    "c": 3
}

new_one = {
    k: inv.get(k, 0) + iv.get(k, 0) for k in (inv | iv)
}

# new_one = {}

# if len(inv) > len(iv):
# for k in inv:
# new_one[k] = inv.get(k, 0) + iv.get(k, 0)
# else:
# for k in iv:
# new_one[k] = iv.get(k, 0) + inv.get(k, 0)


print(new_one)