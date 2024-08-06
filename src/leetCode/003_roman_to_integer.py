def roman_to_int(s: str) -> int:
    # roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # result = 0
    #
    # i = 0
    #
    # while i < len(s):
    #     if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
    #         result += roman_values[s[i + 1]] - roman_values[s[i]]
    #         i += 2
    #     else:
    #         result += roman_values[s[i]]
    #         i += 1
    #
    # return result

    sum = 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for i, char in enumerate(s):
        sum += roman_dict[char]
        if i > 0:
            if roman_dict[s[i - 1]] < roman_dict[char]:
                sum -= 2 * roman_dict[s[i - 1]]   # x + y = z  ---> y - x = z - 2x
    return sum


print(roman_to_int("LVIII"))
