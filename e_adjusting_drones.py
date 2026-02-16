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
    nums = list(map(int, input().split()))

    size = [0] * (2 * n + 2)
    for num in nums:
        size[num] += 1

    cnt = 0
    for i in range(2 * n + 1):
        if size[i] > k:
            size[i + 1] += size[i] - 1
            size[i] = 1
            cnt += 1

    last = size[-1]
    cnt += max(0, last - k)
    print(cnt)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
