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
        nums.append((a, b, i + 1))
    nums.sort(key=lambda x: (x[0], -x[1]))

    last = 0
    for i in range(1, n):
        if nums[last][1] >= nums[i][1]:
            print(nums[i][-1], nums[last][-1])
            return
        last = i

    print(-1, -1)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
