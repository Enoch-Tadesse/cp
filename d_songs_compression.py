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
    n, m = list(map(int, input().split()))
    nums = []
    total = 0
    for _ in range(n):
        a, b = list(map(int, input().split()))
        nums.append((a, b, a - b))
        total += a
    nums.sort(key=lambda x: (x[2]), reverse=True)

    i = 0
    while total > m and i < n:
        total -= nums[i][2]
        i += 1
    print(i if total <= m else -1)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
