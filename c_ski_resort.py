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
    n, k, q = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ans = 0
    l = 0
    for r in range(n):
        if nums[r] > q:
            l = r + 1
            continue
        if r - l + 1 >= k:
            ans += r - l + 1 - k + 1
    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
