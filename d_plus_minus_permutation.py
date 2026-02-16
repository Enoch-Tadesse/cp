import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *

# input = input
input = sys.stdin.readline


def helper(x):
    return (x) * (x + 1) // 2


def get_sum(l, r):
    if l == r:
        return r
    if l > r:
        return 0
    return helper(r) - helper(l - 1)


def solve():
    n, x, y = list(map(int, input().split()))
    dx, dy = n // x, n // y

    overlap = lcm(x, y)
    do = n // overlap
    lower = n - dx + 1
    upper = n

    original = get_sum(lower, upper)
    overcount = get_sum(lower, lower + do - 1)
    original -= overcount

    dy -= do

    overlap = get_sum(1, dy)
    original -= overlap
    print(original)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
