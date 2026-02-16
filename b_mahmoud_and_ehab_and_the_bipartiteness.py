import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    adj = defaultdict(list)
    for _ in range(n - 1):
        a , b = list(map(int, input().split()))
        adj[a].append(b)
        adj[b].append(a)
    colors = [-1] * (n + 1)
    colors[0] = 1
    def dfs(curr, par):
        if colors[curr] != -1:
            return
        colors[curr] = 1 - colors[par]
        for nei in adj[curr]:
            dfs(nei, curr)
    dfs(1, 0)
    zeros = colors.count(0)
    ones = n - zeros
    print(ones * zeros - (n - 1))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
