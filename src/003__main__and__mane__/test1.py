"""
In Python, __main__ is a built-in name that refers to the current module that is being run. 
When you run a Python script, 
the script is executed as the __main__ module. 
This means that if you have a Python script called my_script.py, 
and you run it using the command python my_script.py, 
then my_script will be the __main__ module.

The __name__ variable is a built-in attribute of every module in Python. 
It contains the name of the module as a string. 
If the module is being run as the __main__ module, 
then __name__ will be set to '__main__'.

if __name__ == "__main__":
    # when  this file is imported by another module, it won't execute anything
    # but if it's run directly, like "python myfile.py", then these lines will execute
    ...
"""

# print(__name__)


def say_hello():
    print("hello world")

if __name__ == "__main__":
    say_hello()
    print("---------------")
