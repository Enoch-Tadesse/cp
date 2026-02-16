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
    ans = 0
    for i in range(len(nums) - 1):
        ans += abs(nums[i] - nums[i + 1])

    curr = float("inf")
    for i in range(len(nums)):
        if i == 0:
            curr = min(curr, ans - abs(nums[i + 1] - nums[0]))
        elif i == n - 1:
            curr = min(curr, ans - abs(nums[n - 1] - nums[n - 2]))
        else:
            curr = min(
                curr,
                ans - abs(nums[i + 1] - nums[i]) - abs(nums[i] - nums[i - 1]) + abs(nums[i + 1] - nums[i - 1]),
            )

    print(curr)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
