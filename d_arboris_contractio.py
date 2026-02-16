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
    deg = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a , b = list(map(int, input().split()))
        adj[a].append(b)
        adj[b].append(a)
        deg[a] += 1
        deg[b] += 1
    if n <= 3:
        print(0)
        return
    c1 = sum(x == 1 for x in deg)
    mx = max(sum(deg[x] == 1 for x in adj[v]) for v in range(n))
    print(c1 - mx)



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
