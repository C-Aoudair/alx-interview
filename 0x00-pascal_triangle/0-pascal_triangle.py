#!/usr/bin/python3
""" defines pascal triangle function"""


def pascal_triangle(n):
    """ pascal triangle"""
    if n <= 0:
        return []

    result = []
    for i in range(n):
        row = [1]
        for j in range(1, i + 1):
            try:
                row.append(result[i - 1][j] + result[i - 1][j - 1])
            except IndexError:
                row.append(result[i - 1][j - 1])

        result.append(row)

    return result
