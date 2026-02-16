import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

input = input


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    zeros = nums.count(0)
    ones = nums.count(1)

    if (n - zeros) >= (zeros - 1):
        print(0)
        return
    if 1 not in set(nums) or n - (zeros + ones) > 0:
        print(1)
        return
    print(2)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
