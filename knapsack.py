import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, W = list(map(int, input().split()))
    dp = [0] * (W + 1)
    nums = []
    for _ in range(n):
        nums.append(list(map(int, input().split())))
    nums.sort()
    for i in range(n):
        w, v = nums[i]
        for j in range(W, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)
    print(max(dp))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
