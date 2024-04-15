import math

def log_activity(func):
    #
    def wrapper(*args, **kwargs):
        print(f"Entering {func.__name__}")
        try:
            return func(*args, **kwargs)
        finally:
            print(f"Leaving {func.__name__}")
    return wrapper

@log_activity
def isArrayPrimeIter(ary: list, i_size: int) -> bool:
    # Param: an array of integers, size of array as int
    # Post:
    # Return: True if all elements in array are prime, False otherwise
    
    assert isinstance(ary, list)
    assert all(isinstance(x, int) for x in ary)
    assert isinstance(i_size, int)
    
    if i_size == 0: return True
    
    def isNumPrime(num: int) -> bool:
        # Param: receives an integer and determine if it is prime
        # Return: Bool is array is prime
        
        if num <= 1: return False
        if num <= 3: return True # 2 and 3 are prime
        if num % 2 == 0 or num % 3 == 0:
            return False # Eliminate even numbers and multiples of 3
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i+2) == 0:
                return False
            i += 6
        return True
    
    for num in ary:
        if not (isNumPrime(num)):
            print(f"Not a prime array using iteration.")
            return False
    print(f"Array was found to be prime using iteration.")
    return True

if __name__ == "__main__":
    SORT_MAX_SIZE = 8
    