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
    nums = list(map(int, input().split()))

    pairs = [(num, i) for i, num in enumerate(nums)]
    pairs.sort(reverse=True)

    rank = [0] * n
    counter = 0
    shift = 0

    seen = set()

    for i in range(n):
        num, j = pairs[i]
        if num in seen:
            shift += 1
            rank[j] = counter
        else:
            counter += 1 + shift
            shift = 0
            rank[j] = counter
            seen.add(num)
    print(*rank)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
