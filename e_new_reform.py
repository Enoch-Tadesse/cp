import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
import math

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))
    par = {i: i for i in range(1, n + 1)}
    edges = []

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            par[py] = px
            return True
        return False

    for _ in range(k):
        a, b = list(map(int, input().split()))
        if not union(a, b):
            edges.append((a, b))

    groups = set([find(i) for i in range(1, n + 1)])

    for a, b in edges:
        groups.discard(find(a))
    print(len(groups))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
