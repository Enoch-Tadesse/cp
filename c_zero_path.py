import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline

dirs = [(-1, 0), (0, -1)]


def dp(mat, rows, cols, flag):
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                continue
            _max = float("-inf")
            _min = float("inf")
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                _max = max(_max, mat[nr][nc])
                _min = min(_min, mat[nr][nc])
            if flag:
                mat[r][c] += _max
            else:
                mat[r][c] += _min
    return mat[rows - 1][cols - 1]


from copy import deepcopy


def solve():
    rows, cols = list(map(int, input().split()))
    mat = [list(map(int, input().split())) for _ in range(rows)]

    x = deepcopy(mat)
    y = deepcopy(mat)

    if (rows + cols - 1) & 1:
        print("NO")
        return

    _min = dp(x, rows, cols, False)
    _max = dp(y, rows, cols, True)

    if _min == _max == 0:
        print("YES")
        return

    if _max < 0 or _min > 0:
        print("NO")
    else:
        print("YES")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
