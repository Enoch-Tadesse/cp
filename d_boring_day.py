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
    n, mn, mx = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ans = 0
    curr = 0
    l = 0
    for r in range(n):
        curr += nums[r]
        while curr > mx:
            curr -= nums[l]
            l += 1
        if mn <= curr <= mx:
            ans += 1
            curr = 0
            l = r + 1
    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
