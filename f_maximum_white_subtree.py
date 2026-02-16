from functools import cache
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
    colors = list(map(int, input().split()))
    adj = defaultdict(list)
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)
    val = [-float("inf")] * n

    @cache
    def dfs(curr, par):
        ans = 1 if colors[curr] else -1
        for nei in adj[curr]:
            if nei == par:
                continue
            ans += max(0, dfs(nei, curr))
        val[curr] = max(ans, val[curr])

        return ans

    for i in range(n):
        dfs(i, -1)
    print(*val)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
