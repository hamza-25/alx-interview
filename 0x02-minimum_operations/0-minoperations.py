#!/usr/bin/python3
""" define factorail module """


def minOperations(n):
    """function that calculate min operation"""
    divisor = 2
    sumOfOperation = 0
    while n > 1:
        while n % divisor == 0:
            sumOfOperation += divisor
            n /= divisor
        divisor += 1
    return sumOfOperation
