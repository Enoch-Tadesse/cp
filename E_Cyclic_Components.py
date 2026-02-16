import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def traverse(i, visited, adj):
    stack = [i]
    status = len(adj[i]) == 2
    while stack:
        curr = stack.pop()
        for nei in adj[curr]:
            if nei in visited:
                continue
            status &= len(adj[nei]) == 2
            visited.add(nei)
            stack.append(nei)
    return status


def solve():
    n, e = list(map(int, input().split()))
    adj = defaultdict(list)
    for _ in range(e):
        e1, e2 = list(map(int, input().split()))
        adj[e1].append(e2)
        adj[e2].append(e1)
    counter = 0
    visited = set()
    for i in range(1, n + 1):
        if i not in visited:
            visited.add(i)
            status = traverse(i, visited, adj)
            if status:
                counter += 1
    print(counter)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
