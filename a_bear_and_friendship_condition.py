import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, m = list(map(int, input().split()))
    counts = defaultdict(int)
    parent = {i + 1: i + 1 for i in range(n)}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    for _ in range(m):
        a, b = list(map(int, input().split()))
        counts[a] += 1
        counts[b] += 1
        union(a, b)

    for i in range(1, n + 1):
        find(i)

    members = defaultdict(list)
    for k , v in parent.items():
        members[v].append(k)
    for k , v in members.items():
        for x in v:
            if counts[x] != len(v) - 1:
                print("NO")
                return
    print("YES")



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
