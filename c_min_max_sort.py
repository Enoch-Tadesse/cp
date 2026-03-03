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

    if n == 1:
        print(0)
        return
    q = []
    l, r = 1, n
    while l < r:
        q.append((l, r))
        l += 1
        r -= 1
    q.reverse()

    low, high = -1, n
    ans = 0
    idx = {num: i for i, num in enumerate(nums)}
    for l, r in q:
        la = l + 1
        rb = r - 1
        if not (idx[l] < idx[la] and idx[r] > idx[rb]):
            idx[l] = low
            idx[r] = high
            low -= 1
            high += 1
            ans += 1

    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
