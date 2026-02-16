import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    counter = 0
    l = 0
    adder = 0
    for r in range(n):
        cand = adder + nums[r]
        if cand >= (r + 1):
            counter += r - l + 1
            continue
        while l <= r and nums[r] + adder < r + 1:
            adder += 1
            l += 1
        counter += (r - l + 1)
    print(counter)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
