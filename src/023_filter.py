"""
    The filter() function in Python is used to 
    filter the items of an iterable
    (like list, tuple etc.) based on a given function. 
    It returns a new iterator with the items for which 
    the given function returns True.
"""

nums = range(1, 1_000)


"""
    Prime numbers are positive integers greater 
    than 1 that have no positive integer divisors 
    other than 1 and themselves. The first few prime 
    numbers are 2, 3, 5, 7, 11, and so on.
"""


def is_prime(n):
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        """even numbers"""
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
        
    return True


primes = list(filter(is_prime, nums))
print(primes)



