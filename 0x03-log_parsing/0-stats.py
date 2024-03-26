#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics
"""
import sys
import re
import signal


def print_logs(code_dict, size):
    """print format logs"""
    print("File size: {}".format(size))
    for key, value in code_dict.items():
        if value != 0:
            print("{}: {}".format(key, value))


def signal_handler(sig, frame):
    """handler crtl + c"""
    print_logs(code_dict, size)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


size = 0
code_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0, }
i = 0

try:
    for line in sys.stdin:

        pattern = (
            r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
            r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{1,6})\] '
            r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d{1,10})'
        )

        match = re.search(pattern, line.strip())

        if match:
            status_code = match.group(3)
            file_size = match.group(4)
            if status_code in code_dict.keys():
                code_dict[status_code] += 1
                size += int(file_size)
        i += 1
        if i == 10:
            print_logs(code_dict, size)
            code_dict = {'200': 0, '401': 0, '403': 0,
                         '404': 0, '405': 0, '500': 0, }
            size = 0
            i = 0
except KeyboardInterrupt:
    print_logs(code_dict, size)
