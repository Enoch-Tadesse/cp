import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
import math

# input = input
input = sys.stdin.readline


def solve():
    n, m, h = map(int, input().split())
    nums = list(map(int, input().split()))

    delta = [0] * n
    id = [0] * n
    counter = 0

    for _ in range(m):
        b, c = list(map(int, input().split()))
        i = b - 1

        if id[i] != counter:
            delta[i] = 0
            id[i] = counter

        new = nums[i] + delta[i] + c

        if new > h:
            counter += 1
        else:
            delta[i] += c

    for i in range(n):
        if id[i] == counter:
            nums[i] += delta[i]

    print(*nums)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
