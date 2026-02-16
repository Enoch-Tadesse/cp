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
    final = list(map(int, input().split()))
    fav = list(map(int, input().split()))

    par = {i: i for i in range(1, n + 1)}

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        par[px] = py
        return True

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if abs(i - j) == fav[i]:
                union(i + 1, j + 1)
    for i in range(1, n + 1):
        if find(i) != find(final[i - 1]):
            print("NO")
            return
    print("YES")


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
