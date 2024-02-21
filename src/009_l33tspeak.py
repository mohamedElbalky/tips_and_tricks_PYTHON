"""
    Making franko app
"""

def l33tspeak(input_text):
    ledger = {
        'a': '4',
        'e': '3',
        'i': '1',
        'k': '|<',
        'l': '7',
        'o': '0',
        'p': '?',
        's': '$',
        't': '7'
    }
    
    output_text = ""
    for  char in input_text:
        if  char.lower() in ledger:
            output_text += ledger[char.lower()]
        else:
            output_text += char
            
    return output_text

# Test the function
print(l33tspeak("Hello, World!"))