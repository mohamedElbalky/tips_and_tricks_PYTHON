"""
    Making encryption and decryption of the massege by shifing charachers 
"""

import string

# message
input_text = input("Enter  a message: ")

# encryption/dectyption key
key = 5

# encrypt or decrypt
mode = ""
while True:
    mode = input("Choose the model[(1) -> 'encrypt', (2) -> 'decrypt']: ")
    if mode == "1":
        mode = "encrypt"
        break
    elif mode == "2":
        mode = "decrypt"
        break
    else:
        print("Invalid Choise, Please choose (1) or (2)!!")

# ladger
all_letters = string.ascii_lowercase
all_digits = string.digits

ledger = all_letters + " " + all_digits

# output message
output_text = ""

for char in input_text:
    
    # find the index of the character in ledger
    input_index = ledger.find(char)

    # perform encryption/decryption
    if  mode == "encrypt":
        output_index = input_index + key
    if mode == "decrypt":
        output_index = input_index - key
    
    # handle wraparound (overflow left or right)
    if output_index >= len(ledger):
        output_index = output_index - len(ledger)
    elif output_index < 0:
        output_index = output_index + len(ledger)

    # output
    output_text += ledger[output_index]

print(output_text)
