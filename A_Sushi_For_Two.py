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
    coll = list()
    curr, i = 1, 0
    while i < len(nums):
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            curr += 1
            i += 1
        coll.append(curr)
        i += 1
        curr = 1
    ans = float("-inf")
    for i in range(1, len(coll)):
        ans = max(ans, min(coll[i], coll[i - 1]))
    print(ans * 2)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
