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
    if n == 1:
        print(0)
        return
    dp = [0, abs(nums[1] - nums[0])]
    for i in range(2, n):
        prev2, prev1 = abs(nums[i] - nums[i - 2]), abs(nums[i] - nums[i - 1])
        dp.append(min(prev2 + dp[i - 2], prev1 + dp[i - 1]))
    print(dp[-1])


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
