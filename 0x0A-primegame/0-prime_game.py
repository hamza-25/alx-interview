#!/usr/bin/python3
"""defined module for game prime number
"""


# def is_prime_number(num):
#     """check the number is prime or not
#     Return boolean
#     """
#     if num == 0:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True


# def multiple_of_num(num):
#     """Generate a list of multiples of num."""
#     multi_nums = []
#     i = 2
#     while True:
#         result = num * i
#         if result > 10000:
#             break
#         multi_nums.append(result)
#         i += 1
#     return multi_nums


# def isWinner(x, nums):
#     """Determine the winner of the game."""
#     if not nums or x < 1:
#         return None
#     round = 1
#     ben_win = 0
#     maria_win = 0
#     for index, num in enumerate(nums):
#         if round > x:
#             break
#         if is_prime_number(num):
#             multiples = multiple_of_num(num)
#             for i in range(len(nums)):
#                 if nums[i] in multiples:
#                     nums[i] = 0
#             if (index % 2) == 0:
#                 ben_win += 1
#             else:
#                 maria_win += 1
#         round += 1
#     if maria_win == ben_win:
#         return None
#     elif maria_win > ben_win:
#         return "Maria"
#     else:
#         return "Ben"

# def isWinner(x, nums):
#     """function that checks for the winner"""
#     if not nums or x < 1:
#         return None
#     max_num = max(nums)

#     my_filter = [True for _ in range(max(max_num + 1, 2))]
#     for i in range(2, int(pow(max_num, 0.5)) + 1):
#         if not my_filter[i]:
#             continue
#         for j in range(i * i, max_num + 1, i):
#             my_filter[j] = False
#     my_filter[0] = my_filter[1] = False
#     y = 0
#     for i in range(len(my_filter)):
#         if my_filter[i]:
#             y += 1
#         my_filter[i] = y
#     player1 = 0
#     for x in nums:
#         player1 += my_filter[x] % 2 == 1
#     if player1 * 2 == len(nums):
#         return None
#     if player1 * 2 > len(nums):
#         return "Maria"
#     return "Ben"

def isWinner(x, nums):
    """Function that determines the winner of the game."""
    if not nums or x < 1:
        return None

    # Sieve of Eratosthenes to mark prime numbers
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Count the number of primes for each number up to max_num
    prime_count = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_count[i] = prime_count[i - 1] + primes[i]

    # Determine the winner based on prime counts
    player1_primes = sum(prime_count[num] % 2 == 1 for num in nums)
    if player1_primes * 2 == len(nums):
        return None
    return "Maria" if player1_primes * 2 > len(nums) else "Ben"
