#!/usr/bin/python3
"""Define perimeter of the island
"""


# def island_perimeter(grid):
#     """ returns the perimeter of the island described
#     """
#     preimeter = 0
#     for r_index, row in enumerate(grid):
#         for ele_index, element in enumerate(row):
#             if element:
#                 preimeter += 4
#                 if row[ele_index + 1]:
#                     preimeter -= 1
#                 elif row[ele_index - 1] and row[ele_index - 1] != -1:
#                     preimeter -= 1
#             if grid[r_index - 1] and r_index != 0:
#                 if grid[r_index - 1][ele_index]:
#                     preimeter -= 1
#     return preimeter
def island_perimeter(grid):
    """ returns the perimeter of the island described
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    for r_index, row in enumerate(grid):
        for ele_index, element in enumerate(row):
            if element == 1:  # Check if it's land
                perimeter += 4
                # Check left neighbor
                if ele_index > 0 and row[ele_index - 1] == 1:
                    perimeter -= 1
                # Check right neighbor
                if ele_index < cols - 1 and row[ele_index + 1] == 1:
                    perimeter -= 1
                # Check top neighbor
                if r_index > 0 and grid[r_index - 1][ele_index] == 1:
                    perimeter -= 1
                # Check bottom neighbor
                if r_index < rows - 1 and grid[r_index + 1][ele_index] == 1:
                    perimeter -= 1
    return perimeter
