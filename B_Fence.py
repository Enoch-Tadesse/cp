import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

input = input


def solve():
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    curr = 0
    out = -1
    res = float("inf")

    for r in range(n):
        if r + 1 < k:
            curr += nums[r]
            continue
        curr += nums[r]
        if curr < res:
            res = curr
            out = r - k + 1
        curr -= nums[r - k + 1]
    print(out + 1)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
