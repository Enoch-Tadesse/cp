import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n - 2):
        if not (nums[i] == nums[i + 1] == nums[i + 2]):
            if nums[i] == nums[i + 1]:
                print(i + 3)
            elif nums[i] == nums[i + 2]:
                print(i + 2)
            else:
                print(i + 1)
            return


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
