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
    cnts = defaultdict(int)
    for num in nums:
        if num % k == 0:
            continue
        cnts[k - num % k] += 1
    if len(cnts) == 0:
        print(0)
        return

    _max = max(cnts.values())
    _an_max = 0

    for rem, v in cnts.items():
        if v == _max:
            _an_max = max(_an_max, rem)

    print(k * (_max - 1) + _an_max + 1)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
