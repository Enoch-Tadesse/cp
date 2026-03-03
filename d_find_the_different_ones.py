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
    # fuckkkkkkkkkkkkkkkkkkk
    unique = []
    l = 0
    for r in range(n):
        if nums[r] != nums[l]:
            unique.append(l)
            l = r
    unique.append(l)
    q = int(input())

    for _ in range(q):

        l, r = list(map(int, input().split()))
        l -= 1
        r -= 1

        j = bisect_right(unique, l)
        if j == len(unique) or unique[j] > r:
            print(-1, -1)
        else:
            print(l + 1, unique[j] + 1)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
