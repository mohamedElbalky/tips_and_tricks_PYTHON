


n = input("Numerator: ")
d = input("Denominator: ")

try:
    ans = int(n) / int(d)
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
except ValueError:
    print("Error! Please enter valid integers for numerator and denominator.")
else:
    print("Devision Operation Result: ", ans)