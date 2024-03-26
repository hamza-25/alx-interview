#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics
"""
import sys
import signal
import re


def signal_handler(sig, frame):
    """handler crtl + c"""
    print("File size: {}".format(size))
    for key, value in code_dict.items():
        print("{}: {}".format(key, value))
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

size = 0
code_dict = {'200': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0, }
i = 0
for line in sys.stdin:

    # group1 = '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    # group2 = '\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{1,8})\]'
    # group3 = ' "GET /projects/260 HTTP/1\.1"'
    # group4 = ' (\d{3}) (\d{1,10})'
    # conc_group = group1 + group2 + group3 + group4
    # pattern = r'^' + conc_group
    # print(pattern)
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{1,8})\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d{1,10})'
    match = re.search(pattern, line.strip())

    if match:
        status_code = match.group(3)
        file_size = match.group(4)
        if status_code in code_dict.keys():
            code_dict[status_code] += 1
        size += int(file_size)

    if i == 9:
        print("File size: {}".format(size))
        for key, value in code_dict.items():
            print("{}: {}".format(key, value))
        code_dict = {'200': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0, }
        size = 0
        i = -1

    # if line.strip() == 'exit':
    #     break
    i += 1
