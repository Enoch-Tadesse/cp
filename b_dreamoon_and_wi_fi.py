import sys

sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline


def solve():
    og = list(x for x in input().strip())
    res = og.count("+") - og.count("-")

    got = list(x for x in input().strip())

    success = 0

    def dp(i, curr):
        nonlocal success, res
        if i == len(got):
            success += curr == res
            return
        if got[i] == "+":
            dp(i + 1, curr + 1)
        elif got[i] == "-":
            dp(i + 1, curr - 1)
        else:
            dp(i + 1, curr - 1)
            dp(i + 1, curr + 1)

    dp(0, 0)
    ways = pow(2, got.count("?"))
    if ways == 0:
        print(1 if success else 0)
    else:
        print(success / ways)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
