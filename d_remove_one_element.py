import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    groups = []

    l = 0
    ans = 0
    for r in range(1, n):
        if nums[r - 1] < nums[r]:
            continue
        groups.append((l, r - 1))
        ans = max(r - l, ans)
        l = r
    ans = max( n - l, ans)
    groups.append((l, n - 1))

    m = len(groups)
    for i in range(1, m):
        l1, r1 = groups[i - 1]
        l2, r2 = groups[i]


        if r1 - 1 >= l1 and nums[r1 - 1] < nums[l2]:
            ans = max(ans, r2 - l1)

        if l2 + 1 <= r2 and nums[l2 + 1] > nums[r1]:
            ans = max(ans, r2 - l1)


    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
