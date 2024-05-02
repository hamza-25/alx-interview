#!/usr/bin/python3
"""Define module make change
"""


def makeChange(coins, total):
    """determine the fewest number of
    coins needed to meet a given amount total
    """
    # if total <= 0:
    #     return 0

    # dp = [float('inf')] * (total + 1)
    # dp[0] = 0

    # for coin in coins:
    #     for i in range(coin, total + 1):
    #         dp[i] = min(dp[i], dp[i - coin] + 1)

    # if isinstance(dp[total], float):
    #     return -1

    # return dp[total]
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    count_coin = 0
    for i in coins:
        if total % i == 0:
            count_coin += int(total / i)
            return count_coin
        if total - i >= 0:
            if int(total / i) > 1:
                count_coin += int(total / i)
                total = total % i
            else:
                count_coin += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return count_coin
