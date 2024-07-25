#!/usr/bin/python3
""" conatainns makeChange function"""


def makeChange(coins, total):
    """makeChange function"""
    if total == 0:
        return 0

    for coin in reversed(sorted(coins)):
        if coin <= total:
            numOfCoins = makeChange(coins, total - coin)
            if numOfCoins == -1:
                return -1
            return numOfCoins + 1

    return -1
