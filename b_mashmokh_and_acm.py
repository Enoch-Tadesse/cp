import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from functools import lru_cache
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

mod = 10**9 + 7

def solve():
    n, k = list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, len(dp[0])):
        dp[1][i] = 1

    for i in range(1, len(dp) - 1):
        for j in range(1, len(dp[0])):
            l = j
            while l < len(dp[0]):
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][l]) % mod
                l += j
    for d in dp:
        print(d)

    print(sum(dp[-1]) % mod)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
