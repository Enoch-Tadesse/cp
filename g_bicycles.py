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
    n, m = list(map(int, input().split()))
    adj = defaultdict(list)

    dist = [float("inf")] * (n + 1)

    for _ in range(m):
        a, b, w = list(map(int, input().split()))
        adj[a].append((b, w))
        adj[b].append((a, w))

    nums = list(map(int, input().split()))

    heap = [(0, nums[0], 1)]

    seen = set()

    while heap:
        wei, slow, node = heappop(heap)
        if (node, slow) in seen:
            continue

        seen.add((node, slow))
        for nei, nw in adj[node]:

            _min = min(nums[node - 1], slow)
            new_wei = nw * _min + wei

            if _min <= slow or new_wei < dist[nei]:
                dist[nei] = min(dist[nei], new_wei)
                heappush(heap, (new_wei, _min, nei))

    print(dist[n])


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
