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
    nums = list(map(int, input().split()))
    nums = list((Counter(nums).values()))

    nums.sort()
    n = len(nums)
    total = sum(nums)
    size = len(nums)
    ans = float("inf")

    left = 0
    for i in range(n):
        total -= nums[i]

        delLeft = left
        delRight = total - (size - 1) * nums[i]
        ans = min(ans, delLeft + delRight)

        size -= 1
        left += nums[i]
    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
