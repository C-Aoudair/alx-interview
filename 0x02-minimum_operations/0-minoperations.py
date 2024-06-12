#!/usr/bin/python3
""" Contains the implementation of the minimum operations problem"""


def minOperations(n: int) -> int:
    """ task integer as an argument and return the minimum operation needed
        to reach that number of a character using just copy All and paste
        operations
    """
    if n == 0 or n == 1 or (type(n) != int and type(n) != float):
        return 0
    return sumOfPrimes(int(n))


def sumOfPrimes(n: int) -> int:
    for number in range(n - 1, 1,  -1):
        if not n % number:
            return int(n / number) + sumOfPrimes(number)
    return n
