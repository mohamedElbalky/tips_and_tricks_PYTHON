"""
    In Python, the ^ operator is used to perform 
    the bitwise XOR (exclusive or) 
    operation on two numbers. 
    The XOR operation compares 
    the corresponding bits of two numbers and 
    returns 1 if the bits are different and 0 if the bits are the same.
"""

x = 5  # 0101 in binary

y = 3  # 0011 in binary

# ---->  0110 <---  '^' gives this result

result = x ^ y


print(result)  # 0110 in binary, which is 6 in decimal

# ------------------------------
print(bin(10))  # 0b1010
print(bin(10)[2:])  # 1010
print(format(10,'08b')) # 00001010