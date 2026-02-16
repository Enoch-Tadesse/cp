import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline


def bfs(source, adj, reds):
    q = deque([source])
    n, f = -1, -1
    level = 0
    visited = set()
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            visited.add(curr)
            if curr in reds:
                if level > f:
                    n = curr
                    f = level
            for nei in adj[curr]:
                if nei in visited:
                    continue
                q.append(nei)
        level += 1

    return n, f


def solve():
    n, k = list(map(int, input().split()))
    reds = list(map(int, input().split()))
    adj = defaultdict(list)
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        adj[a].append(b)
        adj[b].append(a)
    if len(reds) <= 1:
        print(0)
        return

    x, _ = bfs(reds[0], adj, set(reds))
    _, y2 = bfs(x, adj, set(reds))
    y2 += 1
    print(y2 // 2)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
