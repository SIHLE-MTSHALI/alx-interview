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

    # Initialize an array to store minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through all amounts from 1 to total
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
