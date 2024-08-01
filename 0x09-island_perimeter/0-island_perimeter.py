#!/usr/bin/python3
""" contains island_perimeter function"""


def island_perimeter(grid):
    """takes a grid and compute the perimeter of the land island of it"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                cell_perimeter = 0
                try:
                    if not grid[i][j + 1]:
                        cell_perimeter += 1
                except IndexError:
                    cell_perimeter += 1
                try:
                    if not grid[i][j - 1]:
                        cell_perimeter += 1
                except IndexError:
                    cell_perimeter += 1

                try:
                    if not grid[i + 1][j]:
                        cell_perimeter += 1
                except IndexError:
                    cell_perimeter += 1

                try:
                    if not grid[i - 1][j]:
                        cell_perimeter += 1
                except IndexError:
                    cell_perimeter += 1
                perimeter += cell_perimeter

    return perimeter
