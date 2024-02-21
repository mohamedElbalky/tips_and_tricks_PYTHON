"""
    Using negative rounding to round numbers in int part
    32 ---> 30 with -1
    32 ---> 00 with -2
"""

num = 14.22
rounded_num = str(round(num, -2))
print(rounded_num)

num = 15.22
rounded_num = str(round(num, -1))
print(rounded_num)

num = 16.22
rounded_num = str(round(num, -1))
print(rounded_num)