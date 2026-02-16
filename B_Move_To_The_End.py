# idea is take the last k-1 sum,
# with the remaining k, find the max number you can get,
# go back now add it to your num , pop that from the heap,
# repeat

import sys
from collections import Counter, defaultdict
import heapq
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    _maxs = []
    curr = 0
    for num in nums:
        curr = max(curr, num)
        _maxs.append(curr)

    out = []
    _sum = 0
    for i in range(n - 1, -1, -1):
        out.append(_sum + _maxs[i])
        _sum += nums[i]
    print(*out)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
