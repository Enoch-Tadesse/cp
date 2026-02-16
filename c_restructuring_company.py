import sys

sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, m = list(map(int, input().split()))
    par = {i: i for i in range(1, n + 1)}

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(x, y):
        px, py = find(x), find(y)
        par[px] = py

    nxt = list(range(n + 2))

    def get_nxt(x):
        if x != nxt[x]:
            nxt[x] = get_nxt(nxt[x])
        return nxt[x]

    def erase(x):
        nxt[x] = x + 1

    for _ in range(m):
        t, l, r = list(map(int, input().split()))
        if t == 1:
            union(l, r)
        elif t == 2:
            x = get_nxt(l)
            while x < r:
                union(x, x + 1)
                erase(x)
                x = get_nxt(l)

        else:
            print("YES" if find(l) == find(r) else "NO")


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
