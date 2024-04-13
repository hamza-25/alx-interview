#!/usr/bin/python3
"""Module N queens
"""
import sys


def find_solutions(row, column):
    """function that find solution
    """
    solution = [[]]
    for queen in range(row):
        solution = N_palce_queen(queen, column, solution)
    return solution


def N_palce_queen(queen, column, prev_solution):
    """function that place n in place
    """
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """check save place of n
    """
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def n_queens():
    """main function to start logic
    """

    if len(sys.argv) >= 3:
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
    solutions = find_solutions(n, n)
    for array in solutions:
        new_list = []
        for q, x in enumerate(array):
            new_list.append([q, x])
        print(new_list)


if __name__ == '__main__':
    n_queens()
