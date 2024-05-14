#!/usr/bin/python3
"""defined module for game prime number
"""


def is_prime_number(num):
    """check the number is prime or not
    Return boolean
    """
    if num == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def multiple_of_num(num):
    """Generate a list of multiples of num."""
    multi_nums = []
    i = 2
    while True:
        result = num * i
        if result > 10000:
            break
        multi_nums.append(result)
        i += 1
    return multi_nums


def isWinner(x, nums):
    """Determine the winner of the game."""
    # round = 1
    # is_maria_turn = False
    # for num in nums:
    #     if round > x:
    #         break
    #     if is_prime_number(num):
    #         multiples = multiple_of_num(num)
    #         for i in range(len(nums)):
    #             if nums[i] in multiples:
    #                 nums[i] = 0
    #         if is_maria_turn:
    #             return "Maria"
    #         else:
    #             return "Ben"
    #     is_maria_turn = not is_maria_turn
    #     round += 1
    # return None
    maria_wins = 0
    ben_wins = 0
    for i in range(x):
        num = nums[i]
        maria_turn = (i % 2 == 0)

        # Find primes and mark their multiples
        for j in range(2, num + 1):
            if is_prime_number(j):
                for k in range(j, num + 1, j):
                    if nums[i] == 0:  # Skip marked multiples
                        continue
                    if k % j == 0:
                        nums[i] = 0  # Mark as multiple

        if maria_turn:
            maria_wins += 1 if sum(nums) > 0 else 0
        else:
            ben_wins += 1 if sum(nums) > 0 else 0

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
