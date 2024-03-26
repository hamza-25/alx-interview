#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics
"""
import sys
import re


def print_logs(code_dict, size):
    """print format logs
    Args:
        code_dict: dict of status codes
        size: total of the file
    Returns:
        None
    """
    print("File size: {}".format(size))
    for key, value in code_dict.items():
        if value != 0:
            print("{}: {}".format(key, value))


size = 0
counter = 0
code_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0, }

pattern = (
            r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
            r'\[(\d{1,4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}\.\d{1,6})\] '
            r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d{1,4})'
        )

try:
    for line in sys.stdin:
        match = re.search(pattern, line.strip())

        if match:
            counter += 1
            status_code = match.group(3)
            file_size = match.group(4)
            size += int(file_size)

            if status_code in code_dict.keys():
                code_dict[status_code] += 1

            if counter == 10:
                print_logs(code_dict, size)
                counter = 0

finally:
    print_logs(code_dict, size)
