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
    nums = []
    eles = []
    for i in range(n):
        con = list(map(int, input().split()))[1:]
        nums.extend(con)
        eles.append(con)

    nums.sort()
    nxt = dict()

    for i in range(len(nums) - 1):
        nxt[nums[i]] = nums[i + 1]
    nxt[nums[-1]] = -1
    cnt = 0

    for e in eles:
        for i in range(len(e) - 1):
            if nxt[e[i]] != e[i + 1]:
                cnt += 1
    print(cnt, n + cnt - 1)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
