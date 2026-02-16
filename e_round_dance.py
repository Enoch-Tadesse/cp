import sys

sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

# ---------- Union-Find / Disjoint Set Union ----------
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])  # Path compression
        return self.par[node]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # Already connected
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.par[ry] = rx
        else:
            self.par[rx] = ry
            self.rank[ry] += 1
        return True


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums = [num - 1 for num in nums]

    par = {i: i for i in range(n)}

    spare = {i: 2 for i in range(n)}
    seen = set()

    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(x, y):
        px, py = find(x), find(y)
        par[px] = py

    for a, b in enumerate(nums):
        if a > b:
            a, b = b, a
        if (a, b) in seen:
            continue
        seen.add((a, b))
        spare[a] -= 1
        spare[b] -= 1
        union(a, b)

    groups = defaultdict(list)
    left = defaultdict(int)

    for i in range(n):
        groups[find(i)].append(i)

    worst = len(groups)

    has, dont = 0, 0
    comp = []

    for g in groups:
        for ele in groups[g]:
            left[g] += spare[ele]
        if left[g] > 0:
            comp.append(left[g])
            has += 1
        else:
            dont += 1
    comp.sort(reverse=True)
    j = 1
    gs = 1
    if len(comp) == 0:
        print(worst, worst)
        return
    else:
        for r in range(len(comp)):
            if j == len(comp):
                break
            while comp[r] > 0 and j < len(comp):
                comp[r] -= 1
                comp[j] -= 1
                j += 1
            if r == j:
                j += 1
                gs += 1
    print(gs + dont, worst)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
