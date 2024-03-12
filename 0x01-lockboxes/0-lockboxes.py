#!/usr/bin/python3
from copy import deepcopy


def canUnlockAll(boxes):

    temp_boxes = deepcopy(boxes)
    for box in temp_boxes:
        box.append(False)

    keys = []
    temp_boxes[0][-1] = True
    i = 0
    while i < len(temp_boxes):
        if temp_boxes[i][-1]:
            j = 0
            while j < len(temp_boxes):
                # print(f'start i: {i} j: {j}')
                # print(i, j)
                if j < len(temp_boxes[i]) - 1:
                    key = temp_boxes[i][j]
                    if temp_boxes[key][-1] is False:
                        temp_boxes[key][-1] = True
                        keys.append(key)
                j += 1
        i += 1

    locked = False
    for index, box in enumerate(temp_boxes):
        if box[-1]:
            for key in temp_boxes[index]:
                if key not in keys:
                    keys.append(key)
        if not box[-1]:
            if index in keys:
                box[-1] = True
            else:
                locked = True
    # print(temp_boxes)
    # print(keys)
    if locked:
        return False
    return True
