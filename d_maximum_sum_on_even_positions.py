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
    nums = list(map(int, input().split()))
    base = sum(nums[i] for i in range(0, n, 2))

    a = []
    for i in range(0, n - 1, 2):
        a.append(nums[i + 1] - nums[i])

    b = []
    for i in range(1, n - 1, 2):
        b.append(nums[i] - nums[i + 1])

    def kadane(array):
        best = 0
        curr = 0

        for num in array:
            curr = max(num, curr + num)
            best = max(best, curr)
        return best

    ans = base + max(kadane(a), kadane(b))
    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
