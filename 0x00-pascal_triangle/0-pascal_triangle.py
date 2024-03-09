#!/usr/bin/python3
'''Pascal's triangle module.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle.
    '''
    triang = []
    if type(n) is not int or n <= 0:
        return triang
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triang[i - 1][j - 1] + triang[i - 1][j])
        triang.append(line)
    return triang
