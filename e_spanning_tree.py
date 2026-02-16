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
    # ---------- Union-Find / Disjoint Set Union ----------
    class UnionFind:
        def __init__(self, n):
            self.par = list(range(n))
            self.rank = [0] * n

        def find(self, node):
            if self.par[node] != node:
                self.par[node] = self.find(self.par[node])  # Path compression
            return self.par[node]

        def union(self, x, y):
            rx, ry = self.find(x), self.find(y)
            if rx == ry:
                return False  # Already connected
            if self.rank[rx] < self.rank[ry]:
                self.par[rx] = ry
            elif self.rank[rx] > self.rank[ry]:
                self.par[ry] = rx
            else:
                self.par[rx] = ry
                self.rank[ry] += 1
            return True

    n, k = list(map(int, input().split()))

    qs = []
    u = UnionFind(n)

    for _ in range(k):
        qs.append(list(map(int, input().split())))
    qs.sort(key=lambda x: x[2])
    ans = 0
    for a, b, w in qs:
        if u.union(a - 1, b - 1):
            ans += w
    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
