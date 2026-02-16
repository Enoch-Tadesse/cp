import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    dp = [float("inf")] * n
    dp[0] = 0
    for curr in range(1, n): # 10 ** 5
        for prev in range(max(0, curr - k), curr): # 100
            dp[curr] = min(dp[curr], abs(nums[curr] - nums[prev]) + dp[prev])
            # being at the right place, at the right time, asking the right question
    print(dp[-1])


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
