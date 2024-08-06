def is_palindrome(x: int) -> bool:
    # Negative numbers are not palindromes
    if x < 0:
        return False

    # Variables to store the original number and the reversed number
    original_x = x
    reversed_x = 0

    while x > 0:
        digit = x % 10  # Get the last digit
        reversed_x = reversed_x * 10 + digit  # Append the digit to the reversed number
        x = x // 10  # Remove the last digit from x
    return original_x == reversed_x


print(is_palindrome(12321))  # True
print(is_palindrome(12345))  # False
print(is_palindrome(-12321))  # False

