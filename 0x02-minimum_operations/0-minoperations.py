#!/usr/bin/python3
""" Contains the implementation of the minimum operations problem"""


def minOperations(n: int) -> int:
    """ task integer as an argument and return the minimum operation needed
        to reach that number of a character using just copy All and paste
        operations
    """
    for i in range(1, n):
        number = n - i
        if not (n % number) and number != 1:
            return int(n / number) + minOperations(number)
    return n
