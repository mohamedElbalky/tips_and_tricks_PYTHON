"""
    In Python, the match keyword is used in a pattern matching expression. 
It is similar to a switch statement in other programming languages.
"""



x =  10
match x:
    case 10:
        print("10")
    case 20:
        print("20")
    case 30:
        print("30")
    case _:
        print("default")