import sys

sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    par = {i: i for i in range(1, n + 1)}

    edges = []

    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        edges.append((a, b))

    colors = [0] + list(map(int, input().split()))

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(x, y):
        px, py = find(x), find(y)
        if colors[px] != colors[py]:
            return False
        par[px] = py
        return True

    spare = defaultdict(int)
    m = 0
    for a, b in edges:
        if not union(a, b):
            m += 1
            spare[a] += 1
            spare[b] += 1

    for k, v in spare.items():
        if v == m:
            print("YES")
            print(k)
            return

    if len(spare) == 0:
        print("YES")
        print(1)
        return

    print("NO")


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
