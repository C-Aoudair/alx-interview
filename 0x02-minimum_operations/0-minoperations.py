#!/usr/bin/python3
""" Contains the implementation of the minimum operations problem"""


def minOperations(n: int) -> int:
    """ task integer as an argument and return the minimum operation needed
        to reach that number of a character using just copy All and paste
        operations
        Args:
            n: integer number
        Return:
            the sum of prime factors that represent the number of operations
    """
    if n <= 1:
        return 0

    factors = []
    prime = 2

    while prime ^ 2 <= n:
        while n % prime == 0:
            factors.append(prime)
            n = n / prime
        prime += 1
    if n > 1:
        factors.append(n)

    return int(sum(factors))
