import sys

# sys.setrecursionlimit(10**6)
from collections import *
from heapq import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    h = []

    total = 0

    for num in nums:
        heappush(h, num)
        total += num

        if total < 0:
            total -= heappop(h)

    print(len(h))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
