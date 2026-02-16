import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
import math

# input = input
input = sys.stdin.readline

def atmost(nums, K, max_len):
    if K < 0:
        return 0
    left = 0
    freq = 0
    ans = 0
    for right, val in enumerate(nums):
        freq += val
        while freq > K:
            freq -= nums[left]
            left += 1
        ans += min(right - left + 1, max_len)
    return ans

def solve():
    k = int(input())
    chars = list(int(x) for x in input().strip())
    x, y = atmost(chars, k, float("inf")), atmost(chars, k - 1, float("inf"))

    print(x - y)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
