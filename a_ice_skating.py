import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    pairs = []
    for _ in range(n):
        x, y = list(map(int, input().split()))
        pairs.append((x, y))
    adj = defaultdict(list)
    for i in range(n):
        x1, y1 = pairs[i]
        for j in range(n):
            x2, y2 = pairs[j]
            if i == j:
                continue
            if x1 == x2 or y1 == y2:
                adj[i].append(j)
                adj[j].append(i)
    visited = set()

    def search(curr, par):
        visited.add(curr)
        for nei in adj[curr]:
            if nei == par:
                continue
            if nei in visited:
                continue
            search(nei, curr)
    cnt = 0
    for i in range(n):
        if i not in visited:
            cnt += 1
            search(i, -1)
    print(cnt - 1)


def main():
    t = 1

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
