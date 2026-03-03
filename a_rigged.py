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
    for _ in range(n):
        nums.append(list(map(int, input().split())))
    first = nums[0][0]
    nums = [nums[i][1] for i in range(0, n) if nums[i][0] >= first]

    mx = nums[0]
    for i in range(1, len(nums)):
        if nums[i] >= mx:
            print(-1)
            return

    print(first)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
