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


def solve():
    n = int(input())
    adj = defaultdict(list)
    ind = [0] * n
    for i in range(n):
        nums = list(map(int, input().split()))
        ind[i] = nums[0]
        for j in range(1, len(nums)):
            adj[nums[j] - 1].append(i)
    for _ , v in adj.items():
        v.sort()
    q = deque([i for i in range(n) if ind[i] == 0])
    ans = 0
    visited = set()

    print("0-0-0-0-0-0-0-0-0-0-0-0")
    print(len(q))

    while q:
        ans += 1
        k = len(q)
        i = 0
        run = 0
        poppy = []
        while i < k:
            run += 1
            curr = q.popleft()
            poppy.append(curr)
            visited.add(curr)
            for nei in adj[curr]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    print(curr, nei)
                    q.append(nei)
                    if (curr < nei):
                        print(curr, nei, "here")
                    k += (nei > curr)
                    if nei > curr:
                        print("here")
            i += 1
        # print(f"{i=} {k=} {q=} {run=} {poppy=}")
    if len(visited) != n:
        print(-1)
    else:
        print(ans)

        


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
