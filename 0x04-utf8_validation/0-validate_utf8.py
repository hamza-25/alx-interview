#!/usr/bin/python3
"""Define UTF 8 Module
"""


def validUTF8(data):
    """validate the ASCCI code
    """
    # for num in data:
    #     if num not in range(0, 127):
    #         return False
    # return True
    num_bytes = 0

    for byte in data:
        byte = byte & 0xFF  # Ensure byte is in range 0-255
        if num_bytes == 0:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
