import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy

input = input


def solve():
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    cand = nums[-1] - nums[0]
    for i in range(n - 1):
        nums[i] -= nums[i + 1]
    nums.pop()
    nums.sort()
    print(sum(nums[: k - 1]) + cand)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
