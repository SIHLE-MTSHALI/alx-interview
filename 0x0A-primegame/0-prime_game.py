#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
    x (int): The number of rounds.
    nums (list): An array of n for each round.

    Returns:
    str: Name of the player that won the most rounds.
         If the winner cannot be determined, returns None.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_num + 1, i):
                sieve[j] = False

    maria_wins = 0
    for n in nums:
        primes = sum(sieve[2:n+1])
        maria_wins += primes % 2 == 1

    if maria_wins * 2 == x:
        return None
    return "Maria" if maria_wins * 2 > x else "Ben"
