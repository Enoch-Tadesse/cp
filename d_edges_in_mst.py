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
    n, k = map(int, input().split())
    edges = []
    for i in range(k):
        a, b, w = map(int, input().split())
        edges.append((w, a - 1, b - 1, i))

    edges.sort()
    ans = ["none"] * k

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            parent[pb] = pa

    r = 0
    while r < k:
        w = edges[r][0]
        same_w = []
        while r < k and edges[r][0] == w:
            same_w.append(edges[r])
            r += 1

        cand = []
        for _, u, v, idx in same_w:
            pu, pv = find(u), find(v)
            if pu == pv:
                ans[idx] = "none"
            else:
                cand.append((pu, pv, idx))

        g = defaultdict(list)
        for u, v, idx in cand:
            g[u].append((v, idx))
            g[v].append((u, idx))

        tin = {}
        low = {}
        timer = [0]
        visited = set()
        is_bridge = set()

        def dfs(u, p_edge):
            visited.add(u)
            tin[u] = low[u] = timer[0]
            timer[0] += 1
            for v, eid in g[u]:
                if eid == p_edge:
                    continue
                if v in visited:
                    low[u] = min(low[u], low[v])
                else:
                    dfs(v, eid)
                    low[u] = min(low[u], low[v])
                    if low[v] > tin[u]:
                        is_bridge.add(eid)

        for u in g:
            if u not in visited:
                dfs(u, -1)

        for u, v, idx in cand:
            if idx in is_bridge:
                ans[idx] = "any"
            else:
                ans[idx] = "at least one"

        for _, u, v, idx in same_w:
            union(u, v)
    for a in ans:
        print(a)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
