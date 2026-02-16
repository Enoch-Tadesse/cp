import sys

sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def counter(node, adj, visited):
    visited.add(node)
    for ele in adj[node]:
        if ele not in visited:
            return counter(ele, adj, visited) + 1
    return 1

def solve():
    n = int(input())
    adj = defaultdict(list)
    can = True
    for _ in range(n):
        a, b = list(map(int, input().split()))
        adj[a].append(b)
        adj[b].append(a)
        if a == b or len(adj[a]) > 2 or len(adj[b]) > 2:
            can = False
    if not can:
        print("NO")
        return
    visited = set()
    for i in range(1, n + 1):
        if i in visited:
            continue
        if counter(i , adj, visited) % 2:
            print("NO")
            return
    print("YES")



def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
