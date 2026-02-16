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
    edges = []
    e2 = []
    for _ in range(m):
        a, b, w = list(map(int, input().split()))
        edges.append((a, b, w))
        e2.append((a, b , w))

    edges.sort(key=lambda x: x[-1])

    parent = {i: i for i in range(1, n + 1)}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px
            return True
        return False

    span = set()
    curr = 0
    adj = defaultdict(list)
    for a, b, w in edges:
        if union(a, b):
            adj[a].append((b, w))
            adj[b].append((a, w))

            curr += w
            span.add((a, b))
    # for s in span:
    #     print(s)
    edges = e2
    print(*span)
    for a, b , w in edges:
        extra = dict()
        if (a, b) in span:
            print(curr)
            continue
        ans = -1
        for x, y in adj[a]:
            extra[x] = y
        for x, y in adj[b]:
            if x in extra:
                ans = max(ans, extra[x], y)
        print(curr - ans + w)




def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
