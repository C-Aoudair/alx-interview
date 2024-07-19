#!/usr/bin/python3
""" Implementation of rotate_2d_matrix function"""


def rotate_2d_matrix(mat):
    """ rotateMatrix function"""
    N = len(mat)
    n = len(mat[0])
    diff = N - n

    if diff < 0:
        while diff < 0:
            mat.append([0 for _ in range(n)])
            diff += 1
        N = n
        rotate(mat)
        for i in range(N):
            mat[i].pop(0)

    elif diff > 0:
        for j in range(N):
            for _ in range(diff):
                mat[j].append(0)
        rotate(mat)
        mat.pop()

    else:
        rotate(mat)


def rotate(mat):
    """ helper function"""
    N = len(mat)
    for x in range(0, int(N / 2)):

        for y in range(x, N - x - 1):

            temp = mat[x][y]
            mat[x][y] = mat[N - 1 - y][x]
            mat[N - 1 - y][x] = mat[N - 1 - x][N - 1 - y]
            mat[N - 1 - x][N - 1 - y] = mat[y][N - 1 - x]
            mat[y][N - 1 - x] = temp
