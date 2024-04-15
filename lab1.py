# Lab 1
# Mikhail Ocampo | 4/15/2024 | https://github.com/mikhailocampo/CIS22C-lab1
# Purpose of the assignment is to create a program that determines if an array of integers is prime using iteration and recursion.

import math

def log_activity(func):
    def wrapper(*args, **kwargs):
        print(f"Entering {func.__name__}")
        try:
            return func(*args, **kwargs)
        finally:
            print(f"Leaving {func.__name__}")
    return wrapper

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

@log_activity
def isArrayPrimeIter(ary: list, i_size: int) -> bool:
    # Algorithm checks if all elements in array are prime using iteration
    # Param: ary - a non-empty array of integers, 
    #        n - size of array as int
    # Post:
    # Return: True or False
    
    assert isinstance(ary, list)
    assert all(isinstance(x, int) for x in ary)
    assert isinstance(i_size, int)
    
    if i_size == 0: return True
    
    for num in ary:
        if not (isNumPrime(num)): return False
    return True

@log_activity
def isArrayPrimeRecur(ary: list, i_size: int) -> bool:
    # Algorithm checks if all elements in array are prime using recursion
    # Param: ary - a non-empty array of integers, 
    #        n - size of array as int
    # Post:
    # Return: True or False
    
    assert isinstance(ary, list)
    assert all(isinstance(x, int) for x in ary)
    assert isinstance(i_size, int)
    
    def isPrimeRecur(dividend: int, divisor = 2):
        if dividend < 2:
            return False
        if divisor > int(math.sqrt(dividend)):
            return True
        if dividend % divisor == 0:
            return False
        return isPrimeRecur(dividend, divisor + 1)
    
    if i_size == 0: return True
    if not isPrimeRecur(ary[i_size - 1]): return False
    
    return isArrayPrimeRecur(ary, i_size - 1)
        
if __name__ == "__main__":
    global SORT_MAX_SIZE
    SORT_MAX_SIZE = 8
    
    print("Please enter your input data on one line only")
    s = input()
    numbers = [int(x) for x in s.split()]
    
    if isArrayPrimeIter(numbers, len(numbers)):
        print("Array was found to be prime using iteration.")  
    else: print("Not a Prime Array using iteration.")  
    
    if isArrayPrimeRecur(numbers, len(numbers)):
        print("Array was found to be prime using recursion.")  
    else: print("Not a Prime Array using recursion.")  
