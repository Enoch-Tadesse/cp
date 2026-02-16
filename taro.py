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
    dp = list(map(int, input().split()))
    for _ in range(1, n):
        nums = list(map(int, input().split()))
        new_dp = [0, 0, 0]
        for j in range(3):
            cand = 0
            for k in range(3):
                if j == k:
                    continue
                cand = max(cand, dp[k])
            new_dp[j] = cand + nums[j]
        dp = new_dp
    print(max(dp))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
