#!/usr/bin/python3
# """Module N queens
# """
# from sys import argv


# def is_safe(board, row, col, N):
#     """function that check safe place to place Q
#     """
#     for i in range(col):
#         if board[row][i] == 1:
#             return False

#     for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False

#     for i, j in zip(range(row, N, 1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False

#     return True


# def solve_n_queens(board, col, N):
#     """function that use recursion to check all possibility
#     """
#     if col >= N:
#         return True

#     for i in range(N):
#         if is_safe(board, i, col, N):
#             board[i][col] = 1
#             if solve_n_queens(board, col + 1, N):
#                 return True
#             board[i][col] = 0

#     return False


# def print_solution(board, N):
#     """function that print solution
#     """
#     new_list1 = []
#     new_list2 = []
#     count = 0
#     for i in range(N):
#         count = 0
#         for j in range(N):
#             if board[i][j] == 1:
#                 new_list1.append([i, j])
#                 new_list2.append([count, i])
#             count += 1
#     print(new_list2)
#     print(new_list1)


# def n_queens(N):
#     """main function that start logic
#     """

#     if len(argv) >= 3:
#         print('Usage: nqueens N')
#         exit(1)

#     try:
#         if int(argv[1]) < 4:
#             print('N must be at least 4')
#             exit(1)
#     except ValueError:
#         print('N must be a number')
#         exit(1)

#     board = [[0] * N for _ in range(N)]
#     if not solve_n_queens(board, 0, N):
#         print("Solution does not exist")
#         return False

#     print_solution(board, N)
#     return True

# if __name__ == '__main__':
#     n_queens(int(argv[1]))
import sys


def generate_solutions(row, column):
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():

    n = init()
    # generate all solutions
    solutions = generate_solutions(n, n)
    # print solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
