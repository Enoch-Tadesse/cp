import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def med(nums):
    if len(nums) <= 1:
        return 0

    mid = (len(nums)) // 2
    key = nums[mid]
    ans = 0
    count = 0
    for i in range(mid - 1, -1, -1):
        ans += key - nums[i] - 1 - count
        count += 1
    count = 0
    for i in range(mid + 1, len(nums)):
        ans += -key + nums[i] - 1 - count
        count += 1
    return ans


def solve():
    n = int(input())
    chars = list(x for x in input().strip())
    bees = []
    ace = []
    for i in range(n):
        if chars[i] == "b":
            bees.append(i)
        else:
            ace.append(i)
    print(min(med(bees), med(ace)))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
