import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
from heapq import *
import math

# input = input
input = sys.stdin.readline


def solve():
    n , q , k = list(map(int, input().split()))
    type = list(map(int, input().split()))
    adj = defaultdict(list)
    for _ in range(q):
        a , b = list(map(int, input().split()))
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)
    ans = [0] * k
    visited = set()
    heap = [(0, 0)]
    while heap:
        cost, ele = heappop(heap)
        if ele in visited:
            continue
        ans[type[ele] - 1] = max(cost, ans[type[ele] - 1])
        visited.add(ele)
        for nei in adj[ele]:
            heappush(heap, (cost + 1, nei))
    print(*ans)
        


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
