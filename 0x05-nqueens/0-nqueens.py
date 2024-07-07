#!/usr/bin/python3
""" Contains the solution of N queens problem"""

import sys

args = sys.argv

if len(args) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(args[1])
except Exception as error:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def place_nqueens(n):
    def place(queens, posDiag, negDiag):
        row = len(queens)

        if row == n:
            result.append(queens)
            return None

        for col in range(n):
            if (
                col not in queens
                and row - col not in posDiag
                and row + col not in negDiag
            ):
                place(
                        queens + [col],
                        posDiag + [row - col],
                        negDiag + [row + col]
                    )

    result = []
    place([], [], [])

    return [[[i, j] for i, j in enumerate(sol)] for sol in result]


n = N
solutions = place_nqueens(n)
for solution in solutions:
    print(solution)
