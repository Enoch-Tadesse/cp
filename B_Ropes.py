import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math
from types import prepare_class

input = sys.stdin.readline


def isValid(nums, guess, k):
    counter = 0
    for length in nums:
        counter += int(length / guess)
    return counter >= k


def solve():
    n, k = list(map(int, input().split()))
    error = 10**-6
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    l, r = 0, 10**7
    while l <= r:
        mid = (l + r) / 2
        if isValid(nums, mid, k):
            l = mid + error
        else:
            r = mid - error
    print(r)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
