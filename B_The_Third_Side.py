import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

input = input


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    while len(nums) > 1:
        num1 = nums.pop()
        num2 = nums.pop()
        nums.append(num1 + num2 - 1)

    print(*nums)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
