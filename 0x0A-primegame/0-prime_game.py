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

def isWinner(x, nums):
    """function that checks for the winner"""
    if not nums or x < 1:
        return None
    max_num = max(nums)

    my_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            my_filter[j] = False
    my_filter[0] = my_filter[1] = False
    y = 0
    for i in range(len(my_filter)):
        if my_filter[i]:
            y += 1
        my_filter[i] = y
    player1 = 0
    for x in nums:
        player1 += my_filter[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
