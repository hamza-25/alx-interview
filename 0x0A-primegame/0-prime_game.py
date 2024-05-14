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
#             # print(round % 2)
#             if (index % 2) == 0:
#                 ben_win += 1
#             else:
#                 maria_win += 1
#             # print('{}: Maria{} Ben {}'.format(index, maria_win, ben_win))
#         # else:
#         #     if (round % 2) == 0:
#         #         return 'Ben'
#         #     else:
#         #         return 'Maria'
#         round += 1
#     if maria_win == ben_win:
#         return None
#     elif maria_win > ben_win:
#         return "Maria"
#     else:
#         return "Ben"

def is_prime_number(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determine the winner of the game."""
    maria_win = 0
    ben_win = 0

    for n in nums:
        if n == 1 or not is_prime_number(n):
            continue  # Skip non-prime numbers

        # Calculate the winner based on the starting player
        if n % 2 == 0:  # Ben's turn
            ben_win += 1
        else:  # Maria's turn
            maria_win += 1

    # Determine the overall winner
    if maria_win == ben_win:
        return None
    elif maria_win > ben_win:
        return "Maria"
    else:
        return "Ben"
