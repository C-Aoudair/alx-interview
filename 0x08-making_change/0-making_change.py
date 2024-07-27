#!/usr/bin/python3
""" conatainns makeChange function"""


def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to make the given total.

    Args:
        coins (list of int): A list of coin denominations available.
        total (int): The total amount to be achieved using the coins.

    Returns:
        int: The minimum number of coins needed to make the total.
             Returns -1 if the total cannot be achieved
             with the given denominations.
    """
    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        while total >= coin:
            coin_count += 1
            total -= coin

    return coin_count if total == 0 else -1
