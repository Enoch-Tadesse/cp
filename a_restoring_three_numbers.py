import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    nums = list(map(int, input().split()))
    _max = max(nums)
    nums.remove(_max)
    for num in nums:
        print(_max - num, end=' ')
    print()


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
