#!/usr/bin/python3
""" conatainns makeChange function"""


def makeChange(coins, total):
    """makeChange function"""
    numOfCoins = 0
    while(total):
        status = False
        for coin in reversed(sorted(coins)):
            if coin <= total:
                numOfCoins += 1
                total -= coin
                status = True
                break
        if not status:
            return -1

    return numOfCoins
