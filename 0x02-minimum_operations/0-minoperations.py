#!/usr/bin/python3
""" define factorail module """


def minOperations(n: int) -> int:
    """function that calculate min operation"""
    temp = n
    divisor: int = 2
    # factor = []
    sum: int = 0
    while n > 1:
        while n % divisor == 0:
            # factor.append(divisor)
            sum += divisor
            n //= divisor
        divisor += 1
    return sum
