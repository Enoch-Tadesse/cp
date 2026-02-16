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
    if nums[0] == 0:
        print(-1)
    else:
        curr = nums[0]
        i = 1
        while i < len(nums) and  nums[i] == 0:
            curr *= 10
            i += 1
        next = 0
        while i < len(nums):
            next *= 10
            next += nums[i]
            i += 1
        if (next > curr):
            print(curr, next)
        else:
            print(-1)

    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
