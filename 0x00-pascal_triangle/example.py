#!/usr/bin/python3
def pascal(n):
    if type(n) is not int or n <= 0:
        return []
    pascal = [[1,],]
    for i in range(n - 1):
        new_arr = [1,]
        for j in range(i):
            if j + 1 < len(pascal[i]):
                    new_arr.append(pascal[i][j] + pascal[i][j + 1]) 
        new_arr.append(1)
        pascal.append(new_arr)
    return pascal