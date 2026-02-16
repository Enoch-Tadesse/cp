import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy

input = input


def solve():
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    for i in range(len(nums) - 2, -1, -1):
        nums[i] += nums[i + 1]
    cand = nums[0]
    nums = sorted(nums[1:], reverse=True)
    print(cand + sum(nums[: k - 1]))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
