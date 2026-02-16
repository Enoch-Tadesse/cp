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
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    bad = defaultdict(int)
    for _ in range(k):
        l, r = list(map(int, input().split()))
        l -= 1
        r -= 1
        if nums[l] > nums[r]:
            bad[l] += 1
        if nums[r] > nums[l]:
            bad[r] += 1
    pairs = [num for i, num in enumerate(nums)]
    pairs.sort()

    ans = [0] * n
    for i in range(n):
        j = bisect_left(pairs, nums[i])
        ans[i] = j - bad[i]
    print(*ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
