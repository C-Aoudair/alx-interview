#!/usr/bin/python3
""" contains island_perimeter function"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in a 2D grid.

    The grid contains 0s (water) and 1s (land). The perimeter is
    the number of edges that are adjacent to water or
    the grid boundary.

    Args:
        grid (list of list of int): A 2D grid representing the map.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four possible sides
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

    return perimeter
