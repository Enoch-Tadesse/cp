import sys

sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    par = {i: i for i in range(1, n + 1)}
    red = []

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return True
        par[px] = py
        return False

    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        if union(a, b):
            red.append((a, b))
    if not red:
        print(0)
        return

    comps = defaultdict(list)
    for i in range(1, n + 1):
        comps[find(i)].append(i)

    roots = list(comps.keys())
    print(len(roots) - 1)

    for i in range(len(roots) - 1):
        a, b = red[i]
        u = roots[i]
        v = roots[i + 1]
        print(a, b, comps[u][0], comps[v][0])


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
