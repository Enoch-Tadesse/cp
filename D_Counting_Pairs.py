import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, x, y = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort()
    total = sum(nums)
    l, r = 0, n - 1
    curr = 0
    while l <= r:
        cand = total - (nums[l] + nums[r])
        if cand > y:
            l += 1
        elif cand < x:
            r -= 1
        else:
            # print(nums[l : r + 1])
            # xl = bisect_right(nums, total - nums[r] - x, l, r + 1)
            # xr = bisect_left(nums, total - nums[l] - y, l, r + 1)
            curr += bisect_right(nums, total - nums[r] - x, l, r + 1) - l
            curr += r - bisect_left(nums, total - nums[l] - y, l, r + 1)
            # curr += (xl - l) * (r - xr + 1)
            # print(nums[l : r + 1], curr)
            l, r = l + 1, r - 1
            # l, r = xl, xr
    print(curr)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
