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
    if k == 0:
        print(*[-1] * n)
        return
    k = (n * n + n) // 2 - k

    m = 0
    while k >= m + 1:
        m += 1
        k -= m

    ans = [-2] * m
    all = m * 2 + 1
    ans.append(all - 2 * k)

    ans.extend([1000] * (n - m - 1))
    print(*ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
