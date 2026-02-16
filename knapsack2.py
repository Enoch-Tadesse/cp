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
    nums = []
    for _ in range(n):
        nums.append(list(map(int, input().split())))
    dp = [float("inf")] * (10**5 + 1) # values are index, min weight is the value
    # find min weight to achieve a specific value
    dp[0] = 0
    for w, v in nums:
        for j in range(len(dp) - 1, v - 1, -1):
            dp[j] = min(dp[j], dp[j -v] + w)
    ans = max(i for i , num in enumerate(dp) if num <= W)

    print(ans)



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
