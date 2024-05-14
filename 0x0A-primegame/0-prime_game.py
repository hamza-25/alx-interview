#!/usr/bin/python3
"""defined module for game prime number
"""


def isWinner(x, nums):
    """Function that determines the winner of the game."""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    prime_count = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_count[i] = prime_count[i - 1] + primes[i]

    player1_primes = sum(prime_count[num] % 2 == 1 for num in nums)
    if player1_primes * 2 == len(nums):
        return None
    return "Maria" if player1_primes * 2 > len(nums) else "Ben"
