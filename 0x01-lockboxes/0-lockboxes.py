#!/usr/bin/python3
"""algorithm to check boxes locked"""
# from copy import deepcopy


# def canUnlockAll(boxes):
#     """method that check boxes unlocked"""
#     temp_boxes = deepcopy(boxes)
#     for box in temp_boxes:
#         box.append(False)

#     keys = []
#     temp_boxes[0][-1] = True
#     i = 0
#     while i < len(temp_boxes):
#         if temp_boxes[i][-1]:
#             j = 0
#             while j < len(temp_boxes):
#                 # print(f'start i: {i} j: {j}')
#                 # print(i, j)
#                 if j < len(temp_boxes[i]) - 1:
#                     key = temp_boxes[i][j]
#                     if temp_boxes[key][-1] is False:
#                         temp_boxes[key][-1] = True
#                         keys.append(key)
#                 j += 1
#         i += 1
#     # print(keys)
#     # print(temp_boxes)

#     for index, box in enumerate(temp_boxes):
#         if box[-1]:
#             # print(f'=>{box}')
#             for key in temp_boxes[index]:
#                 if key not in keys:
#                     keys.append(key)
#         if not box[-1]:
#             if index in keys:
#                 box[-1] = True
#     locked = False
#     for index, box in enumerate(temp_boxes):
#         if box[-1]:
#             # print(f'=>{box}')
#             for key in temp_boxes[index]:
#                 if key not in keys:
#                     keys.append(key)
#         if not box[-1]:
#             if index in keys:
#                 box[-1] = True
#             else:
#                 locked = True
#     # print(temp_boxes)
#     # print(keys)
#     if locked:
#         return False
#     return True
def canUnlockAll(boxes):
    """method that check boxes unlocked"""
    index = 0
    unlocked_keys = {}
    for box in boxes:
        if index == 0 or len(box) == 0:
            unlocked_keys[index] = 'always'
        for key in box:
            if key < len(boxes) and key != index:
                unlocked_keys[key] = key
        if len(unlocked_keys) == len(boxes):
            return True
        index += 1
    return False
