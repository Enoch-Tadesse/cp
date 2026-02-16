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


def can(nums, k):
    n = len(nums)
    par = {(nums[i], i): (nums[i], i) for i in range(n)}
    compare = sorted(nums)

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(x, y):
        px, py = par[x], par[y]
        if px == py:
            return
        par[py] = px

    seen = [False] * n

    for i in range(n):
        if seen[i]:
            break
        seen[i] = True
        for j in range(i + k, n):
            union((nums[i], i), (nums[j], j))
            seen[j] = True
    cnt = defaultdict(lambda: defaultdict(int))
    for i, num in enumerate(nums):
        val, j = find((num, i))
        cnt[val][j] += 1


def atmost(nums, target):
    left = 0
    sums = 0
    count = 0

    for right in range(len(nums)):
        sums += nums[right]
        while sums > target:
            sums -= nums[left]
            left += 1
        count += right - left + 1
    return count


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    if nums == sorted(nums):
        print(-1)
        return
    l = 1
    r = n
    while l <= r:
        mid = (l + r) // 2
        if can(nums, mid):
            l = mid + 1
        else:
            r = mid - 1
    print(r)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
