"""
    In a for loop in Python, 
    the else block is executed when the loop has exhausted iterating over the sequence. 
    This means that if the loop completes normally 
    (i.e., without encountering a break statement), the else block will be executed.
    
    if the loop breakes out of the loop using the break keyword,  
    then the else block will not be executed.
"""

import random

price = 0

for _ in range(random.randint(5, 15)):
    price += 1
    if price == 10:
        print("Price is 10!")
        break
else:
    print("never got the 10..")

# --------------------------------------
print('---------------------------')

for i in range(5):

    if i == 3:

        print("Found 3")

        break

else:

    print("3 was not found")
