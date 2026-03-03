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
    n = int(input())
    nums = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        nums.append([a, b, i + 1])
    nums.sort(key=lambda x: (x[1], -x[0]))

    for i in range(1, n):
        l, r, _ = nums[i]
        if l <= nums[i - 1][0]:
            print(nums[i - 1][2])
            return
        nums[i][0] = max(nums[i - 1][1] + 1, l)  # left
        nums[i][1] = max(r, l)  # right
    print(-1)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
