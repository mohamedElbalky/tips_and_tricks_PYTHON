import string
import random

# all_letters = string.ascii_letters
# all_digits = string.digits
# all_punctuation = string.punctuation
# print(all_punctuation)

# generate all letters and digits and punctuation  combinations
all_printable = string.printable

# print(all_printable)


# input
length = input("Enter the length of password: ")

try:
    int(length) # if it is not possible to convert into integer then ValueError will be raised
except  ValueError:
    print("You must enter a Number")
else:
    password = ""
    for _ in range(int(length)):
        password = "".join([password, random.choice(all_printable)])

    # output
    print(password)