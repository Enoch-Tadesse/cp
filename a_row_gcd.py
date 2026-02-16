import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, m = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort()
    gcd = 0
    for i in range(1, n):
        gcd = math.gcd(nums[i] - nums[i - 1], gcd)
    js = list(map(int, input().split()))
    _min = min(nums)
    for j in js:
        print(math.gcd(gcd, j + _min), end=" ")
    print()


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
