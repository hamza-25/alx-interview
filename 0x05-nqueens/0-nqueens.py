#!/usr/bin/python3
"""Module N queens
"""
import sys


def solutions_generate(row, col):
    solution = [[]]
    for queen in range(row):
        solution = place_n_queen(queen, col, solution)
    return solution


def place_n_queen(queen, col, previous_solution):
    safe_position = []
    for array in previous_solution:
        for x in range(col):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, value, array):
    if value in array:
        return (False)
    else:
        return all(abs(array[col] - value) != q - col
                   for col in range(q))


def n_queens():

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        if int(sys.argv[1]) < 4:
            print('N must be at least 4')
            sys.exit(1)
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    n = int(sys.argv[1])

    solutions = solutions_generate(n, n)

    for array in solutions:
        new_arr = []
        for index, value in enumerate(array):
            new_arr.append([index, value])
        print(new_arr)


if __name__ == '__main__':
    n_queens()
