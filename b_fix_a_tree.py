import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    par = {i: i for i in range(1, n + 1)}


    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        par[px] = py
        return True

    seen = set()

    cnt = 0
    print(*nums)
    bads = set()
    for i in range(n):
        j = i + 1
        num = nums[i]
        if j == num:
            continue
        if j > num:
            j, num = num, j
        if (j, num) in seen:
            continue
        if not union(j, num):
            if j not in bads:
                bads.add(j)
            else:
                bads.add(num)
    print(bads)
    groups = defaultdict(list)
    for i in range(1, n + 1):
        groups[find(i)].append(i)
    if len(groups) <= 0:
        print(cnt)
        print(*nums)
        return
    print(cnt)
    print(*nums)
    rep = []
    for g in groups:
        v = groups[g]
        for ele in v:
            if nums[ele - 1] == ele:
                rep.append(ele - 1)
                break
    cnt += len(rep) - 1
    for i in range(1, len(rep)):
        nums[rep[i]] = rep[0]
    print(cnt)
    print(*nums)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
