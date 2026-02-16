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
    a, b = 1, 0

    at = 0
    k = 2
    n -= 1
    while n > 0:
        take = min(n, 2 * k + 1)
        if at:
            a += take
        else:
            b += take
        n -= take
        k += 2
        at ^= 1
    print(a, b)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
