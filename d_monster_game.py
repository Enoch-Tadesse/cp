import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    run = 0
    pre = []

    for x in b:
        run += x
        pre.append(run)

    a.sort(reverse=True)
    ans = 0

    for i, x in enumerate(a):
        left = i + 1

        j = bisect_right(pre, left)

        ans = max(ans, x * j)
    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
