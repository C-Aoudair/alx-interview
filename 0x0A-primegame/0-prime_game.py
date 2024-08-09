#!/usr/bin/python3
""" Defines isWinner function the solution of prime game problem"""


def isWinner(x, nums):
    """ isWinner function"""
    Maria = 0
    Ben = 0
    
    for n in nums:
        rounds_number = 1
        while rounds_number <= x:
            primes = [True for _ in range(n + 1)]

            p = 2
            Maria_turn = True
            while(p * p <= n):
                if (primes[p]):
                    for i in range(p*p, n + 1, p):
                        primes[i] = False
                    Maria_turn = not Maria_turn

                    p += 1

            if (Maria_turn):
                Ben += 1
            else:
                Maria += 1
            
            rounds_number += 1

    if Maria > Ben:
        return "Maria"
    if Maria < Ben:
        return "Ben"
    return None
