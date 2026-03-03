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


def solve():
    n, k = list(map(int, input().split()))
    grid = [[x for x in input().strip()] for _ in range(n)]

    for r in range(0, n, k):
        temp = []
        for c in range(0, n, k):
            temp.append(grid[r][c])
        print("".join(temp))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
