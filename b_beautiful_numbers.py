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
    nums = list(int(x) for x in input().strip())

    if len(nums) == 1:
        print(0)
        return

    curr = nums[0]
    nums = nums[1:]
    nums.sort()
    i = 0
    while i < len(nums) and curr + nums[i] <= 9:
        curr += nums[i]
        i += 1
    print(len(nums) - i)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
