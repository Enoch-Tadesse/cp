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
    nums = list(map(int, input().split()))
    visited = set()
    i = 0

    while i < n:
        if i in visited:
            i += 1
            continue

        seen = []
        idx = []
        j = i

        while j < n:
            idx.append(j)
            visited.add(j + 1)
            seen.append(nums[j])
            j = j * 2 + 1

        seen.sort()

        for k in range(len(seen) - 1):
            if seen[k] * 2 != seen[k + 1]:
                print("NO")
                return

        for k in range(len(seen)):
            nums[idx[k]] = seen[k]

        i += 1
    print("YES")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
