import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    checker = defaultdict(int)

    for i in range(len(nums)):
        checker[i + 2] = nums[i]

    out = []
    while n in checker:
        out.append(n)
        n = checker[n]
    out.append(1)
    print(*out[::-1])


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
