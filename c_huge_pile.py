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
    n, k = map(int, input().split())

    l = r = n
    cnt = 0

    while r != 1:
        if l <= k <= r:
            print(cnt)
            return
        l //= 2
        r = r // 2 + (r % 2)
        cnt += 1

    if l <= k <= r:
        print(cnt)
    else:
        print(-1)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
