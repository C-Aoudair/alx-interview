#!/usr/bin/python3
""" conatainns makeChange function"""


def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to make
    the given total using dynamic programmng.

    Args:
        coins (list of int): A list of coin denominations available.
        total (int): The total amount to be achieved using the coins.

    Returns:
        int: The minimum number of coins needed to make the total.
             Returns -1 if the total cannot be achieved
             with the given denominations.
    """
    if total <= 0:
        return 0

    tabulation = [-1] * (total + 1)
    tabulation[0] = 0

    for index in range(total + 1):
        if tabulation[index] != -1:
            for coin in coins:
                newIndex = index + coin
                if newIndex <= total and (
                    tabulation[newIndex] == -1
                    or tabulation[index] + 1 < tabulation[newIndex]
                ):
                    tabulation[index + coin] = tabulation[index] + 1

    return tabulation[total]
