#!/usr/bin/python3
"""Define UTF 8 Module
"""


def validUTF8(data):
    """validate the ASCCI code
    """
    for num in data:
        if num not in range(0, 128):
            return False
    return True
