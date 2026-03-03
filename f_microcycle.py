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
    n, k = list(map(int, input().split()))

    par = {i: i for i in range(1, n + 1)}
    adj = defaultdict(set)
    edges = []

    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return True
        par[px] = py
        return False

    for _ in range(k):
        a, b, w = list(map(int, input().split()))
        adj[a].add(b)
        adj[b].add(a)
        edges.append((a, b, w))

    edges.sort(key=lambda x: x[2], reverse=True)
    l, r = 0, 0
    _min = -1
    for a, b, w in edges:
        if union(a, b):
            _min = w
            l, r = a, b

    a, b = l, r
    path = [b]
    visited = set([b])

    def dfs(curr, last):
        if curr == a:
            return True
        for nei in adj[curr]:
            if nei in visited:
                continue
            if nei == last:
                continue
            visited.add(nei)
            if dfs(nei, curr):
                path.append(nei)
                return True
        return False

    dfs(b, a)
    print(_min, len(path))
    print(*path)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
