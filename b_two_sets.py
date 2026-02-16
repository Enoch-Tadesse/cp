import sys

sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline


def solve():
    n, a, b = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    par = {i: i for i in range(n + 2)}

    idx = {nums[i]: i for i in range(n)}

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            par[px] = py

    for i, num in enumerate(nums):
        if a - num in idx:
            union(i, idx[a - num])
        else:
            union(i, n)

        if b - num in idx:
            union(i, idx[b - num])
        else:
            union(i, n + 1)

    if find(n) == find(n + 1):
        print("NO")
        return

    ans = [0] * n
    print("YES")

    x = find(n + 1)
    for i in range(0, len(ans)):
        if find(i) == x:
            ans[i] = 0
        else:
            ans[i] = 1
    print(*ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
