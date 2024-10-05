#!/usr/bin/python3
"""
pascal triangle module
"""


def pascal_triangle(n):
    """Pascal Triangle Algorithm"""
    if n <= 0:
        return []
    lists = [[1]]
    for row in range(1, n):
        col = [0 for _ in range(row + 1)]
        for index in range(row):
            col[index] += lists[row - 1][index]
            col[index + 1] += lists[row - 1][index]
        lists.append(col)
    return lists
