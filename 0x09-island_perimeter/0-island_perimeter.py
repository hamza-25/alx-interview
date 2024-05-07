#!/usr/bin/python3
"""Define perimeter of the island
"""


def island_perimeter(grid):
    """ returns the perimeter of the island described
    """
    perimeter = 0
    rows_len = len(grid)
    cols_len = len(grid[0])
    for r_index, row in enumerate(grid):
        for ele_index, element in enumerate(row):
            if element:
                perimeter += 4
                if ele_index > 0 and row[ele_index - 1]:
                    perimeter -= 1
                if ele_index < cols_len - 1 and row[ele_index + 1]:
                    perimeter -= 1
                if r_index > 0 and grid[r_index - 1][ele_index]:
                    perimeter -= 1
                if r_index < rows_len - 1 and grid[r_index + 1][ele_index]:
                    perimeter -= 1
    return perimeter
