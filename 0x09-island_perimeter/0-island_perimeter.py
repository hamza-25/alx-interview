#!/usr/bin/python3
"""Define perimeter of the island
"""


def island_perimeter(grid):
    """ returns the perimeter of the island described
    """
    preimeter = 0
    for r_index, row in enumerate(grid):
        for ele_index, element in enumerate(row):
            if element:
                preimeter += 4
                if row[ele_index + 1]:
                    preimeter -= 1
                elif row[ele_index - 1] and row[ele_index - 1] != -1:
                    preimeter -= 1
            if grid[r_index - 1] and r_index != 0:
                if grid[r_index - 1][ele_index]:
                    preimeter -= 1
    return preimeter