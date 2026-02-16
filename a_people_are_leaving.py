import sys

sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))
    parent = {i: i for i in range(1, n + 2)}

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if rx > ry:
            parent[ry] = rx
        else:
            parent[rx] = ry

    for _ in range(k):
        t, x = list(map(str, input().split()))
        x = int(x)
        if t == "?":
            ans = find(x)
            print(-1 if ans == n + 1 else ans)
        elif t == "-":
            union(x, x + 1)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
