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
    nc = n
    aw, ab, bw, bb = 0, 0, 0, 0
    wd = 0
    aw += 1
    n -= 1

    at = 0
    k = 2
    while n - (2 * k + 1) >= 0:
        take = 2 * k + 1
        if at:
            if wd:
                aw += (take + 1) // 2
                ab += (take) // 2
            else:
                ab += ((take + 1)) // 2
                aw += (take) // 2
        else:
            if wd:
                bw += (take + 1) // 2
                bb += (take) // 2
            else:
                bb += (take + 1) // 2
                bw += (take) // 2
        n -= take
        k += 2
        wd ^= 1
        at ^= 1
    curr = nc - n + 1
    for i in range(curr, nc + 1):
        if at:
            aw += i & 1
            ab += i & 1 == 0
        else:
            bw += i & 1
            bb += i & 1 == 0

    print(aw, ab, bw, bb)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
