import sys
sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline

def far(start, adj):
    level = 0
    q = deque([start])
    visited = set([start])
    ans = -1
    while q:
        level += 1
        for _ in range(len(q)):
            curr = q.popleft()
            ans = curr
            visited.add(curr)
            for nei in adj[curr]:
                if nei not in visited:
                    q.append(nei)
    return ans



def solve():
    n = int(input())
    if n == 1:
        print(1)
        return
    adj = defaultdict(list)

    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        adj[a].append(b)
        adj[b].append(a)

    oppo = far(1, adj)

    dist = [0] * (n + 1)

    visited = set([oppo])
    def dfs(curr, level):
        for nei in adj[curr]:
            if nei in visited:
                continue
            dist[nei] = level
            visited.add(nei)
            dfs(nei, level + 1)
    dfs(oppo, 1)
    _max = max(dist)
    dist[oppo] = _max

    for i in range(1, n + 1):
        print(max(_max, dist[i] + 1))



        


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
