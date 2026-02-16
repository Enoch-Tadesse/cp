import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *

# input = input
input = sys.stdin.readline


def find(left, right, nums):
    turn = 0
    got = 0
    for num in nums:
        if num == left:
            if not turn:
                turn ^= 1
                got += 1
        elif num == right:
            if turn:
                turn ^= 1
                got += 1
    return got - turn


def solve():
    nums = list(int(x) for x in input().strip())
    n = len(nums)

    counts = Counter(nums)

    best = max(counts.values())

    for i in range(10):
        for j in range(10):
            if i == j:
                continue
            x = find(i, j, nums)
            best = max(best, x)
    print(n - best)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
