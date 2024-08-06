def isValid(s):
    stack = []
    mapping = {"}": "{", ")": "(", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif not stack or mapping[char] != stack.pop():
            return False

    return not stack


print(isValid("()"))  # True
print(isValid("([)]"))  # False
print(isValid("{[]}"))  # True

