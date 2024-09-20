#!/usr/bin/python3
"""
Module for making change using the fewest number of coins
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total

    Args:
    coins (list of int): List of coin denominations
    total (int): The target total to make change for

    Returns:
    int: Fewest number of coins needed to meet total, or -1 if not possible
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
        if total == 0:
            return count

    return -1
