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
    n, k = list(map(int, input().split()))
    par = {i : i for i in range(n)}

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(x, y ):
        px, py = find(x), find(y)
        if px != py:
            par[px] = py

    og = list(x for x in input().strip())
    target = list(x for x in input().strip())
    

    for i in range(n):
        if i + k < n:
            union(i, i + k)
        if i + k + 1 < n:
            union(i, i + k + 1)
    groups = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    for g, ele in groups.items():
        s = []
        t = []
        for e in ele:
            s.append(og[e])
            t.append(target[e])
        if sorted(s) != sorted(t):
            print("NO")
            return
    print("YES")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
